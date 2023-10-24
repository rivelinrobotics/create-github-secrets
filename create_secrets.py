import base64
import sys
from typing import Dict, Tuple

import requests
from nacl import encoding, public


def parse_secrets(secrets: str) -> Dict[str, str]:
    """Parses secrets of the form `k1=v1 k2=v2 ...` to a dict."""
    return dict(secret.split("=", maxsplit=1) for secret in secrets.split())


def github_headers(token: str) -> Dict[str, str]:
    """Returns the headers required to authenticate with the GitHub API."""
    return {
        "Accept": "application/vnd.github+json",
        "Authorization": f"token {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def get_public_key(environment_url: str, token: str) -> Tuple[str, bytes]:
    """Returns the public key and its ID for an Environment."""
    public_key_url = f"{environment_url}/secrets/public-key"
    response = requests.get(url=public_key_url, headers=github_headers(token))
    key = response.json()["key"].encode("utf-8")
    return response.json()["key_id"], key


def encrypt_secret(secret: str, public_key: bytes) -> str:
    """Encrypts a secret using the public key."""
    nacl_key = public.PublicKey(public_key, encoding.Base64Encoder())
    sealed_box = public.SealedBox(nacl_key)
    encrypted_value = sealed_box.encrypt(secret.encode("utf-8"))
    return base64.b64encode(encrypted_value).decode("utf-8")


def create_secret(
    base_url: str, token: str, public_key_id: str, secret_name: str, secret_value: bytes
) -> None:
    """Creates a Secret in an Environment."""
    secret_url = f"{base_url}/secrets/{secret_name}"
    payload = {"encrypted_value": secret_value, "key_id": public_key_id}
    requests.put(url=secret_url, headers=github_headers(token), json=payload)


if __name__ == "__main__":
    repository, environment, token, secrets = sys.argv[1:]
    base_url = "https://api.github.com"
    environment_url = f"{base_url}/repositories/{repository}/environments/{environment}"
    public_key_id, public_key = get_public_key(environment_url, token)
    for secret_name, secret_value in parse_secrets(secrets).items():
        encrypted_secret = encrypt_secret(secret_value, public_key)
        create_secret(
            environment_url, token, public_key_id, secret_name, encrypted_secret
        )
