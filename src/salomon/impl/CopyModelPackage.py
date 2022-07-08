import boto3, os
from pprint import pprint
from .s3_helper import parse_s3_url


def copy_model_package(source_arn: str, dst_account_id: str, dst_name: str, dst_group_name: str, dst_s3_path: str, dst_ecr: str):
    sm = boto3.client('sagemaker')
    src_model_package = sm.describe_model_package(ModelPackageName=source_arn)

    dst_model_package, files_to_copy, docker_images_to_copy = rebuild_model_package(src_model_package, dst_account_id, dst_name, dst_group_name, dst_s3_path, dst_ecr)
    pprint(dst_model_package)
    pprint(files_to_copy)

    copy_files(files_to_copy)

    response = sm.create_model_package(**dst_model_package)
    pprint(response)

    pass


def rebuild_model_package(src_model_package: dict, dst_account_id: str, dst_name: str, dst_group_name: str, dst_s3_path: str, dst_ecr: str):
    dont_copy_keys = [
        'ModelPackageName', 'ModelPackageGroupName',
        'ModelPackageVersion', 'ModelPackageArn', 'CreationTime', 'ModelPackageStatus', 'ModelPackageStatusDetails',
        'CreatedBy', 'LastModifiedTime', 'LastModifiedBy', 'ApprovalDescription', 'ResponseMetadata']

    dst_model_package = {}
    for k, v in src_model_package.items():
        if k not in dont_copy_keys:
            dst_model_package[k] = v

    # dst_model_package['Tags'] = []
    # dst_model_package['ModelPackageName'] = dst_name
    dst_model_package['ModelPackageGroupName'] = dst_group_name

    files_to_copy = []
    docker_images_to_copy = []
    for container in dst_model_package.get("InferenceSpecification").get("Containers"):
        # copy docker image
        p: tuple = prepare_docker_urls(container.get("Image"), dst_ecr)
        docker_images_to_copy.append(p)

        del container["ImageDigest"]

        # copy files
        p: tuple = prepare_file_paths(container.get("ModelDataUrl"), dst_s3_path)
        container["ModelDataUrl"] = p[1]
        files_to_copy.append(p)

        if type(container.get("Environment")) is dict:
            for var_name, var_value in container["Environment"].items():
                if var_value.startswith("s3://"):
                    p: tuple = prepare_file_paths(var_value, dst_s3_path)
                    container["Environment"][var_name] = p[1]
                    files_to_copy.append(p)
    return dst_model_package, files_to_copy, docker_images_to_copy


def prepare_file_paths(src: str, dst_s3_path: str):
    filename = os.path.basename(src)
    dst = join_uri(dst_s3_path, filename)
    return src, dst


def join_uri(path: str, filename: str) -> str:
    if path.endswith("/") or path == "":
        return f"{path}{filename}"
    else:
        return f"{path}/{filename}"


def prepare_docker_urls(src_image: str, dst_ecr: str):
    return (src_image, src_image)


def copy_files(files_to_copy: list):
    s3 = boto3.resource('s3')
    for src, dst in files_to_copy:
        src_tuple = parse_s3_url(src)
        dst_tuple = parse_s3_url(dst)
        copy_source = {
            'Bucket': src_tuple[0],
            'Key': src_tuple[1]
        }
        print(f"Copying from {src} to {dst}")
        s3.meta.client.copy(copy_source, dst_tuple[0], dst_tuple[1])
