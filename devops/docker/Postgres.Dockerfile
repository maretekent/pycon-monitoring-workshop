FROM postgres:9.5

MAINTAINER Urandu Bildad


RUN apt-get update
RUN apt-get install -y zlib1g-dev uuid-dev libmnl-dev gcc make autoconf autoconf-archive autogen automake pkg-config curl
RUN apt-get install -y python python-yaml python-mysqldb python-psycopg2 nodejs lm-sensors netcat git
RUN git clone https://github.com/netdata/netdata.git --depth=1 ~/netdata
RUN cd ~/netdata && ./netdata-installer.sh --dont-wait --dont-start-it

COPY ./devops/netdata/stream.conf /etc/netdata/stream.conf
COPY ./devops/netdata/postgres.conf /etc/netdata/python.d/postgres.conf

RUN chmod 775 /etc/netdata/stream.conf
RUN chmod 775 /etc/netdata/python.d/postgres.conf