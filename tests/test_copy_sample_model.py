from unittest import TestCase
import json, re, os, sys, datetime, boto3
from salomon import *



def test_copy_sample_model_package():
    dir = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir}/config.json", "r") as fp:
        cfg = json.load(fp)

    try:
        model_package_group = cfg.get("dst_group_name")
        sm = boto3.client("sagemaker")
        response = sm.create_model_package_group(ModelPackageGroupName=model_package_group)
        print(json.dumps(response, indent=2))
    except Exception as e:
        print(f"Exception adding package group: {e}")

    copy_model_package(**cfg)


if __name__ == "__main__":
    test_copy_sample_model_package()

