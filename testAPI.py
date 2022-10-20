import requests
import json


data = {
    "code": "JVw1Ntjj55VbO3cDfX8ZCMw0B9lcl9YPSSuGQ2/dqssgQeH3HhoF2A=="
}


url = "https://giftapi.hydrafacialnation.com/gift-card-usage/list/v2"

try:
    response = requests.get(url, data=data)
except:
    print("Error: " + response.text)
else:
    if response.status_code == 200:
        texts = json.loads(response.text)
        print(texts["token"])
    else:
        print("Status code not equal to 200\n")
        print("Error: " + response.text)
        print("Status Code: " + str(response.status_code) )



# data = {
#     "email": "eve.gb@reqres.in",
#     "password": "pistol"
# }
# try:
#     response = requests.post("https://reqres.in/api/register", data=data)
# except:
#     print("error")
# else:
#     if response.status_code == 200:
#         texts = json.loads(response.text)
#         print(texts["token"])
#     else:
#         print("Status code not equal to 200")