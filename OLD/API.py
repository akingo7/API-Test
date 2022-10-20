import pytest
import requests
import yaml
import json


apis_filename = "url.yaml"

def api_urls(yaml_file):
    api_file = yaml.safe_load(open(yaml_file, "r"))
    api_urls = []
    for api in api_file["apis"]:
        url = api.get("url")
        for path in api.get("paths"):
            api_url = str(url) + str(path)
            print(api_url)

            api_urls.append(api_url)
    return api_urls


@pytest.mark.parametrize("url", api_urls(apis_filename))
def test_status_code(url):
    print("Running test on the URL: " + url)
    response = requests.get(url)
    assert response.status_code == 200