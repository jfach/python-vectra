import json
import requests

class Vectra:

    headers = {'Content-Type': 'application/json'}

    def __init__(self, ip_address, username, password):
        #self.ip_address = ip_address
        self.url = "https://" + ip_address + "/api/{0}"
        self.auth = (username, password)

    def settings(self):
        req_url = self.url.format("settings")
        req = requests.get(url=req_url,
                           auth=self.auth,
                           headers=self.headers, 
                           verify=False)
        return json.loads(req.content)

    def rules(self):
        req_url = self.url.format("rules")
        req = requests.get(url=req_url,
                           auth=self.auth,
                           headers=self.headers,
                           verify=False)
        return json.loads(req.content)

    def detections(self,
                   fields=None,
                   page=None,
                   page_size=None,
                   ordering=None,
                   min_id=None,
                   max_id=None,
                   state=None,
                   type_vname=None,
                   category=None,
                   source=None,
                   t_score=None,
                   t_score_gte=None,
                   c_score=None,
                   c_score_gte=None,
                   last_timestamp=None,
                   host_id=None,
                   tags=None,
                   destination=None,
                   proto=None,
                   dst_port=None,
                   inbound_ip=None,
                   inbound_proto=None,
                   inbound_port=None,
                   inbound_dns=None,
                   outbound_ip=None,
                   outbound_proto=None,
                   outbound_port=None,
                   outbound_dns=None,
                   dns_ip=None,
                   dns_request=None,
                   resp_code=None,
                   resp=None):
        parameters = {}
        req_url = self.url.format("detections")
        if fields:
            parameters['fields'] = fields
        if page:
            parameters['page'] = page
        if page_size:
            parameters['page_size'] = page_size
        if ordering:
            parameters['ordering'] = ordering
        if min_id:
            parameters['min_id'] = min_id
        if max_id:
            parameters['max_id'] = max_id
        if state:
            parameters['state'] = state
        if type_vname:
            parameters['type_vname'] = type_vname
        if category:
            parameters['category'] = category
        if source:
            parameters['source'] = source
        if t_score:
            parameters['t_score'] = t_score
        if t_score_gte:
            parameters['t_score_gte'] = t_score_gte
        if c_score:
            parameters['c_score'] = c_score
        if c_score_gte:
            parameters['c_score_gte'] = c_score_gte
        if last_timestamp:
            parameters['last_timestamp'] = last_timestamp
        if host_id:
            parameters['host_id'] = host_id
        if tags:
            parameters['tags'] = tags
        if destination:
            parameters['destination'] = destination
        if proto:
            parameters['proto'] = proto
        if dst_port:
            parameters['dst_port'] = dst_port
        if inbound_ip:
            parameters['inbound_ip'] = inbound_ip
        if inbound_proto:
            parameters['inbound_proto'] = inbound_proto
        if inbound_port:
            parameters['inbound_port'] = inbound_port
        if inbound_dns:
            parameters['inbound_dns'] = inbound_dns
        if outbound_ip:
            parameters['outbound_ip'] = outbound_ip
        if outbound_proto:
            parameters['outbound_proto'] = outbound_proto
        if outbound_port:
            parameters['outbound_port'] = outbound_port
        if outbound_dns:
            parameters['outbound_dns'] = outbound_dns
        if dns_ip:
            parameters['dns_ip'] = dns_ip
        if dns_request:
            parameters['dns_request'] = dns_request
        if resp_code:
            parameters['resp_code'] = resp_code
        if resp:
            parameters['resp'] = resp
   
        req = requests.get(url=req_url,
                           auth=self.auth,
                           headers=self.headers,
                           params=parameters, 
                           verify=False)
        return json.loads(req.content)

    def hosts(self,
              fields=None,
              page=None,
              page_size=None,
              ordering=None,
              name=None,
              state=None,
              last_source=None,
              t_score=None,
              t_score_gte=None,
              c_score=None,
              c_score_gte=None,
              last_timestamp=None,
              tags=None,
              key_asset=None):
        parameters = {}
        req_url = self.url.format("hosts")
        if fields:
            parameters['fields'] = fields
        if page:
            parameters['page'] = page
        if page_size:
            parameters['page_size'] = page_size
        if ordering:
            parameters['ordering'] = ordering
        if name:
            parameters['name'] = name
        if state:
            parameters['state'] = state
        if last_source:
            parameters['last_source'] = last_source
        if t_score:
            parameters['t_score'] = t_score
        if t_score_gte:
            parameters['t_score_gte'] = t_score_gte
        if c_score:
            parameters['c_score'] = c_score
        if c_score_gte:
            parameters['c_score_gte'] = c_score_gte
        if last_timestamp:
            parameters['last_timestamp'] = last_timestamp
        if tags:
            parameters['tags'] = tags
        if key_asset:
            parameters['key_asset'] = key_asset
  
        req = requests.get(url=req_url,
                           auth=self.auth,
                           headers=self.headers,
                           params=parameters,
                           verify=False)
        return json.loads(req.content)

    def health(self, headend_luid=None):
        if headend_luid:
            req_url = self.url.format("health/" + headend_luid)
        else:
            req_url = self.url.format("health")
        req = requests.get(url=req_url,
                          auth=self.auth,
                          headers=self.headers,
                          verify=False)
        return json.loads(req.content)

    def sensors(self):
        req_url = self.url.format("sensors")
        req = requests.get(url=req_url,
                           auth=self.auth,
                           headers=self.headers,
                           verify=False)
        return json.loads(req.content)

   def traffic(self, headend_luid=None):
	if headend_luid:
	    req_url = self.url.format("health/" + headend_luid + "/traffic")
	else:
	    req_url = self.url.format("health/traffic")
	req = requests.get(url=req_url,
                           auth=self.auth,
                           headers=self.headers,
                           verify=False)
	return json.loads(req.content)

