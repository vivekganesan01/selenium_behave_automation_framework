import os
from docker import APIClient
from docker.utils import kwargs_from_env

kwargs = kwargs_from_env()
#kwargs['tls'].assert_hostname = False
client = APIClient(**kwargs)

containers = client.containers()

seleniums = [c for c in containers if c['Image'] == 'selenium/standalone-chrome:latest']
s = [s['Ports'][0]['IP'] + ':' + str(s['Ports'][0]['PublicPort']) for s in seleniums]
print(s)
