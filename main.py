

import requests
from requests.auth import HTTPBasicAuth
from downloadnexus import downjar


components_list = []


#res1 = requests.get('http://127.0.0.1:8081/service/rest/v1/repositories' ,auth=HTTPBasicAuth('admin', 'che1199Z'))
result = requests.get("http://127.0.0.1:8081/service/rest/v1/components?repository=maven-snapshots" ,auth=HTTPBasicAuth('admin', 'che1199Z'))

t = result.json()
components_list = t["items"]
downjar(components_list)





