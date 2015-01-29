#!/usr/bin/python
from docker import Client
import json

dockerCli = Client(base_url='unix://var/run/docker.sock')

# For every virtual host defined
i = 0
hosts=[]
hosts.append(0)
hosts[0] = []

hosts[0].append(json.loads ('{"ID":"3f6934ff4ac6f290ff7b2f5c5692e05f368fea667a3faa6f99c21c1a27891acc","Addresses":[{"IP":"172.17.0.69","Port":"443","HostPort":"","Proto":"tcp"},{"IP":"172.17.0.69","Port":"80","HostPort":"","Proto":"tcp"}],"Gateway":"172.17.42.1","Name":"loving_torvalds","Image":{"Registry":"","Repository":"nuclyus_www_10","Tag":"1"},"Env":{"NGINX_VERSION":"1.7.9-1~wheezy","PATH":"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin","VIRTUAL_HOST":"nuclyuswww"}}'))
hosts[0].append(json.loads ('{"ID":"b3f6934ff4ac6f290ff7b2f5c5692e05f368fea667a3faa6f99c21c1a27891acc","Addresses":[{"IP":"172.17.0.69","Port":"443","HostPort":"","Proto":"tcp"},{"IP":"172.17.0.69","Port":"80","HostPort":"","Proto":"tcp"}],"Gateway":"172.17.42.1","Name":"loving_torvalds","Image":{"Registry":"","Repository":"nuclyus_www_10","Tag":"2"},"Env":{"NGINX_VERSION":"1.7.9-1~wheezy","PATH":"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin","VIRTUAL_HOST":"nuclyuswww"}}'))

# Do the real stuff
for dockerHost in hosts:
    
	maxTagAsInt = -1;
	maxTagAsString = "";
	
	for container in dockerHost:

		print container
	
		tagAsInt = int(container['Image']['Tag'])
	
		if container['Image']['Tag'] and int(container['Image']['Tag']) and tagAsInt > maxTagAsInt:
			maxTagAsInt = tagAsInt
			maxTagAsString = container['Image']['Tag']
	
	if maxTagAsInt > -1:
		for dockerHost in hosts:
			for container in dockerHost:
				if container['Image']['Tag'] and container['Image']['Tag'] != maxTagAsString:
					print "stopped! %s" % container['ID']
					dockerCli.stop(container['ID'], 60*60)
				else:
					print "not stopped"