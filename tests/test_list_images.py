from unittest import TestCase
import json, re, os, sys, datetime, boto3
from salomon import *


def test_list_images():
    dir = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir}/config_list.json", "r") as fp:
        cfg = json.load(fp)

    images = list_docker_images_in_model_package(**cfg)
    print(json.dumps(images, indent=2))


if __name__ == "__main__":
    test_list_images()

