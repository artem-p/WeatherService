import json


def get(secret_key):
    secret_file = '../secrets.json'
    with open(secret_file) as f:
        secrets = json.load(f)

    return str(secrets[secret_key])
