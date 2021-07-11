import requests

endpoint = "https://pixe.la/v1/users"
my_para = {
    'token': "hsagsns23jsh",
    "username": "k-krishna11",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=endpoint,json=my_para)

graph_para = {
    "id":"graph11",
    "name":"Cycling",
    "unit":"km",
    "type": "float",
    "color":"shibafu"
}
graph_endpoint = f"{endpoint}/k-krishna11/graphs"

headers={
    "X-USER-TOKEN" : "hsagsns23jsh"
}

#response = requests.post(url=graph_endpoint, json=graph_para,headers = headers)

graph1_endpoint = f"{graph_endpoint}/graph11"

grap1_para ={
    "date":"20210711",
    "quantity":"10"
}

response = requests.post(url=graph1_endpoint,headers=headers,json=grap1_para)
print(response.text)
