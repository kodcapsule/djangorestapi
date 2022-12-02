import requests


def getRequest(url):
    endpoint = requests.get(url, params={'data': 1224}, json={
                            'myname': 'this is my name'})
    return endpoint.content
