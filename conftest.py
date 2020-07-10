"""Fixture definitions"""
import yaml
import pytest


@pytest.fixture(scope="session")
def url_under_test():
    """
    A session scoped fixture to read in the url-under-test from a config.yaml file
    :return: str object with fully qualified URL
    """
    with open("config.yaml") as config:
        test_config = yaml.safe_load(config)
        return test_config.get("urls").get("google")
