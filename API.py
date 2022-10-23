import pytest
import requests
import yaml
from config import *



apis_filename = "url.yaml"

def get_api_urls():
    try:
        api_file = yaml.safe_load(open(apis_filename, "r"))
    except:
        print(f'error reading file {apis_filename}')
    else:
        print(f'loaded {apis_filename} file\n')

    api_urls = []

    for api in api_file["apis"]:
        url = str(api.get("url"))

        for path_details in api.get("paths"):
            path = str(path_details.get("path"))

            if path_details.get("auth") == "Special":
                auth = auths.get("Special")
            elif path_details.get("auth") == "Basic":
                auth = auths.get("Basic")
            elif path_details.get("auth") == "No":
                auth = auths.get("No")
            # else:
            #     print("invalid auth value for auth" + url + path)
            requests = path_details.get("requests")
            api_urls_load = {
                "url": url + path,
                "auth": auth,
                "requests": requests
            }
            api_urls.append(api_urls_load)

    return api_urls

def api_request(url_dets):
    responses = []
    for url_det in url_dets:
        for req in url_det["requests"]:
            print("request type: " + req + "\n")
            if req == "POST":
                print("Running test on the URL: " + url_det["url"])
                response = requests.post(url_det["url"], data=url_det["auth"])
                print("Status Code: " + str(response.status_code))

            elif req == "GET":
                print("Running test on the URL: " + url_det["url"])
                response = requests.get(url_det["url"], data=url_det["auth"])

            elif req == "DELETE":
                print("Running test on the URL: " + url_det["url"])
                response = requests.delete(url_det["url"], data=url_det["auth"])

            elif req == "PUT":
                print("Running test on the URL: " + url_det["url"])
                response = requests.put(url_det["url"], data=url_det["auth"])
            else:
                print("invalid request")
            print("response" + response.text + "\n")
            responses.append({
                "url": url_det["url"],
                "response": response.text,
                "status_code": response.status_code
            })

    return responses



@pytest.mark.parametrize("url", api_request(get_api_urls()))
def test_api_status_code(url):
    assert url["status_code"] == 200