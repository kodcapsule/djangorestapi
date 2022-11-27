import requests


def getRequest(url):
    endpoint = requests.get(url)
    return endpoint.text
