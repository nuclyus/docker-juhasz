FROM jwilder/docker-gen
MAINTAINER Lysander Vogelzang <lysander@nuclyus.nl>

# Install necessary packages. We don't need the latest version of Docker

RUN apt-get update
RUN apt-get install -y --force-yes wget python python-pip python-dev libssl-dev libffi-dev bash apt-transport-https

RUN sh -c "echo deb https://get.docker.com/ubuntu docker main > /etc/apt/sources.list.d/docker.list"
RUN apt-get update
RUN apt-get install lxc-docker -y --force-yes

# Install dockerPy
RUN pip install docker-py

ADD juhasz.tmpl /var/juhasz/

ENTRYPOINT ["/usr/local/bin/docker-gen"]


# This command should be executed outside of the container
# TODO: Use supervisor/cron instead of the interval parameter
#command: docker-gen -interval 10 -watch -notify "python /tmp/juhasz_containers.py" /var/juhasz/juhasz.tmpl /tmp/juhasz.py