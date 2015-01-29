#!/usr/bin/python
from docker import Client
import json

dockerCli = Client(base_url='unix://var/run/docker.sock')

# For every virtual host defined
listHosts={}

# Append this new host
	
listHosts["nuclyuswww"] = []
	
listHosts["nuclyuswww"].append(json.loads('{"ID":"7e92fa5ae63db7ddc922bc0b34205bafdfaa30e707fe58ab6d7830a384423535","Addresses":[{"IP":"172.17.0.73","Port":"443","HostPort":"","Proto":"tcp"},{"IP":"172.17.0.73","Port":"80","HostPort":"","Proto":"tcp"}],"Gateway":"172.17.42.1","Name":"grave_bell","Image":{"Registry":"","Repository":"nuclyus_www_10","Tag":"3"},"Env":{"NGINX_VERSION":"1.7.9-1~wheezy","PATH":"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin","VIRTUAL_HOST":"nuclyuswww"}}'))

# Do the real stuff
for hostName, dockerHost in listHosts.iteritems():
	
	maxTagAsInt = -1;
	maxTagAsString = "";
	
	for container in dockerHost:
	
		if not 'Image' in container or not 'Tag' in container["Image"] or len(container['Image']['Tag']) == 0:
			print "nogta"
			break;
	
		try:
			tagAsInt = int(container['Image']['Tag'])
		except:
			print "Error while retrieving container tag for %s. Tag is: %s" % hostName, container['Image']['Tag']
			break;
			
		if container['Image']['Tag'] and int(container['Image']['Tag']) and tagAsInt > maxTagAsInt:
			maxTagAsInt = tagAsInt
			maxTagAsString = container['Image']['Tag']
	
	if maxTagAsInt > -1:
		for hostName, dockerHost in listHosts.iteritems():
			for container in dockerHost:
				if 'Image' in container and 'Tag' in container["Image"] and container['Image']['Tag'] != maxTagAsString:
					print "stopped! %s" % container['ID']
					dockerCli.stop(container['ID'], 60*60)