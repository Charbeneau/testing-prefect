from common import encode_string, semver_str_to_int
from prefect import flow, task, get_run_logger
from datetime import datetime
from pprint import pprint


@task
def encode_task(d):
    logger = get_run_logger()
    logger.info("Creating masked_ip from ip.")
    d["masked_ip"] = encode_string(d["ip"])
    del d["ip"]
    logger.info("Creating masked_device_id from device_id.")
    d["masked_device_id"] = encode_string(d["device_id"])
    del d["device_id"]
    return d


@task
def str_to_int_task(d):
    logger = get_run_logger()
    logger.info("Making app_version an int.")
    d["app_version"] = semver_str_to_int(d["app_version"])
    return d


@task
def create_date_task(d):
    logger = get_run_logger()
    logger.info("Creating create_date an int.")
    d["create_date"] = datetime.now()
    return d


@flow
def dictionaries_flow(d):
    d = encode_task(d)
    d = str_to_int_task(d)
    d = create_date_task(d)
    return d


if __name__ == "__main__":
    d = {
        "user_id": "424cdd21-063a-43a7-b91b-7ca1a833afae",
        "app_version": "2.3.0",
        "device_type": "android",
        "ip": "199.172.111.135",
        "locale": "RU",
        "device_id": "593-47-5928",
    }
    d = dictionaries_flow(d)
    pprint(d)
