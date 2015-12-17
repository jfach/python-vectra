import requests

class Vectra:

    headers = {'Content-Type': 'application/json'}

    def __init__(self, ip_address, username, password):
        #self.ip_address = ip_address
        self.url = "https://" + ip_address + "/api/{0}"
        self.auth = (username, password)

    def settings(self):
        parameters = {}
        req_url = self.url.format("settings")
        req = requests.get(url=req_url,
                           auth=self.auth,
                           headers=self.headers, 
                           verify=False)
        return req

    def rules(self):
        parameters = {}
        req_url = self.url.format("rules")
        req = requests.get(url=req_url, auth=self.auth, headers=self.headers, verify=False)
        return req

    def detections(self, host=None):
        parameters = {}
        req_url = self.url.format("detections")
        if host:
            parameters["source"] = host
        req = requests.get(url=req_url,
                           auth=self.auth,
                           headers=self.headers,
                           params=parameters, 
                           verify=False)
        return req

    def hosts(self):
        parameters = {}
        req_url = self.url.format("hosts")
        req = requests.get(url=req_url, auth=self.auth, headers=self.headers, verify=False)
        return req

    def sensors(self):
        parameters = {}
        req_url = self.url.format("sensors")
        req = requests.get(url=req_url, auth=self.auth, headers=self.headers, verify=False)
        return req