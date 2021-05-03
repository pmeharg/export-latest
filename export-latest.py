#!/usr/bin/env python

import requests
import json
import os
import pprint

# modify repo to correspond to the desired repository
repo='repository=npm-group-proxy'
urlbase = "http://localhost:8081/service/rest/v1/components?"
url = "http://localhost:8081/service/rest/v1/components?" + repo

payload={}
headers = {
  'accept': 'application/json'
}

# for testing, load one component in the dictionary.  Use the following for actual use
components = {}

i = 1
while i:
  if i == 1:
    response = requests.request("GET", url, headers=headers, data=payload)
  else:
    url = urlbase +  "continuationToken=" + r['continuationToken'] +"&" + repo
    response = requests.request("GET", url, headers=headers, data=payload)

  r = response.json()
  i = r['continuationToken']
  for item in r['items']: 
    name = item['name']
    version = item['version']
    downloadUrl = item['assets'][0]['downloadUrl']
    id = item['id']
    value = components.get(name)
    if  value == None:
      components[name] = (version, downloadUrl, id)
    else:
      if value[0] < version :
        components[name] = (version, downloadUrl, id)
      # else:
        # do nothing to the version.

for item in components:
  print("wget ", components[item][1])

  