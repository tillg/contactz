from datetime import datetime
import json
import logging
import requests
from typing import Literal

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

BASE_URL = "http://localhost:3000/"
VALID_TYPES = ["PROFILE", "CONTACTINFO", "CONNECTIONS"]


def persist_resource(type: Literal[tuple(VALID_TYPES)], data: str):  # type: ignore
    if type not in VALID_TYPES:
        raise ValueError(f"Invalid type: {type}. Expected one of: {VALID_TYPES}")

    persist_data = {"as_of": datetime.now().isoformat(), "data": data}

    # Ensure we got a json string
    try:
        json_data = json.dumps(persist_data)
    except (TypeError, ValueError) as e:
        logger.error(f"write_resourse: Invalid JSON data: {e}")
        raise Exception(f"Invalid JSON data: {e}")

    url = f"{BASE_URL}{type}"
    response = requests.post(
        url, json=json.loads(json_data), headers={"Connection": "close"}
    )
    logger.info(f"persist_resource {response.status_code=}")

    # 200: OK, 201: Created
    if response.status_code not in (200, 201):
        response_dict = {
            "status_code": response.status_code,
            "url": response.url,
            "headers": dict(response.headers),
            "body": response.text,
        }
        logger.error(
            "persist_resource: Response received:\n%s",
            json.dumps(response_dict, indent=4),
        )
        raise Exception(f"persist_resource {response.status_code=}")


def get_thing(type, id):
    url = f"{BASE_URL}{type}/{id}"
    response = requests.get(url)
    response_json = response.json()
    logger.info(response_json)
    return response_json
