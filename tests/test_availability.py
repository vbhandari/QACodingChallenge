"""
Module with test cases to verify availability of URL endpoint
"""
import pytest
import requests


@pytest.mark.timeout(30)
def test_google_is_available(url_under_test):
    """
    Test case to verify availability of https://www.google.com
    Test will pass when response code is 2XX or 3XX
    Test will fail when response code is 4XX or 5XX
    Test will fail when the site does not respond within 30 seconds.
    The defined timeout also prevents the test suite from hanging until the underlying requests library times out

    :param url_under_test: session fixture from conftest.py
    :return: None
    """
    try:
        with requests.get(url_under_test) as response:
            assert 200 <= response.status_code < 400
    except requests.exceptions.HTTPError:
        assert False, "HTTP Error thrown"
    except requests.exceptions.RequestException:
        assert False, "Requests GET call failed"
