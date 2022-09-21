from unittest import TestCase
import json, re, os, sys, datetime, boto3, base64, logging
from salomon import *


def test_copy_sample_model_package(config_file: str):
    with open(config_file, "r") as fp:
        cfg = json.load(fp)

    copy_params = cfg.get("copy_params")

    try:
        model_package_group = copy_params.get("dst_group_name")
        sm = boto3.client("sagemaker")
        response = sm.create_model_package_group(ModelPackageGroupName=model_package_group)
        print(json.dumps(response, indent=2))
    except Exception as e:
        print(f"Exception adding package group: {e}")

    src_session = session_from_role(cfg.get("src_role_arn"))
    dst_session = session_from_role(cfg.get("dst_role_arn"))

    # get docker auth
    images = list_docker_images_in_model_package(model_package_arn=copy_params.get("source_arn"), session=src_session)
    src_docker_auths = build_docker_auths_from_ecr(images, src_session)

    dst_docker_auth = None
    if 'dkr.ecr.' in copy_params.get("dst_ecr"):
        dst_docker_auth = list(build_docker_auths_from_ecr([copy_params.get("dst_ecr")], dst_session).values())[0]

    print()
    print()
    print(f"src_docker_auths: {src_docker_auths}")
    print()
    print()
    print(f"dst_docker_auth: {dst_docker_auth}")
    print()
    print()

    copy_model_package(src_session=src_session, dst_session=dst_session,
                       src_docker_auths=src_docker_auths, dst_docker_auth=dst_docker_auth,
                       **copy_params)


def session_from_role(
        role_arn: str, session_name="assumed-role",
        session: boto3.session.Session = boto3.session.Session()
) -> boto3.session.Session:
    if role_arn is None:
        return boto3.session.Session()
    sts = session.client('sts')
    response = sts.assume_role(RoleArn=role_arn, RoleSessionName=session_name)
    return boto3.session.Session(
        aws_access_key_id=response["Credentials"]["AccessKeyId"],
        aws_secret_access_key=response["Credentials"]["SecretAccessKey"],
        aws_session_token=response["Credentials"]["SessionToken"],
    )


if __name__ == "__main__":
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    logger = logging.getLogger("salomon.impl.CopyModelPackage")
    logger.setLevel(logging.DEBUG)
    test_copy_sample_model_package(sys.argv[1])

