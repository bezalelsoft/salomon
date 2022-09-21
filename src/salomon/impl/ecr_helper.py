from typing import List, Dict
import boto3, base64, re


def build_docker_auths_from_ecr(images: List[str], boto3_session: boto3.session.Session) -> List[Dict[str, str]]:
    """
    Get AWS auths for ECR from list of images
    :param images:
    :param boto3_session:
    :return:
    """
    ecr_client = boto3_session.client('ecr')

    docker_auths = {}
    for image in images:
        if 'dkr.ecr.' in image:
            registry, registryId = get_docker_registry_from_image(image)
            if registry not in docker_auths.keys():
                response = ecr_client.get_authorization_token(registryIds=[registryId])
                user_pass = base64.b64decode(response['authorizationData'][0]['authorizationToken']).decode('utf-8')
                user, passwd = user_pass.split(':', 2)
                docker_auths[registry] = {
                    "username": user,
                    "password": passwd
                }
    return docker_auths


def get_docker_registry_from_image(image: str):
    m = re.findall("^(([0-9]{12})\\.dkr\\.ecr.*\\.amazonaws\\.com)/.*$", image)
    registry = m[0][0]
    registryId = m[0][1]

    return registry, registryId
