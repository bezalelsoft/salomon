from unittest import TestCase
import json, re, os, sys, datetime, boto3
from salomon import *


def test_copy_sample_model_package():
    dir = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir}/config_copy_model_between_accounts.json", "r") as fp:
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

    copy_model_package(src_session=src_session, dst_session=dst_session, **copy_params)


def session_from_role(
        role_arn: str, session_name="assumed-role",
        session: boto3.session.Session = boto3.session.Session()
) -> boto3.session.Session:
    sts = session.client('sts')
    response = sts.assume_role(RoleArn=role_arn, RoleSessionName=session_name)
    return boto3.session.Session(
        aws_access_key_id=response["Credentials"]["AccessKeyId"],
        aws_secret_access_key=response["Credentials"]["SecretAccessKey"],
        aws_session_token=response["Credentials"]["SessionToken"],
    )


if __name__ == "__main__":
    test_copy_sample_model_package()

