FROM nginx
ARG namespace
MAINTAINER CyberArk

RUN apt-get update && \
    apt-get install -y python3

#---copy summon into image---#
COPY summon /usr/local/bin/summon
COPY summon-conjur /usr/local/lib/summon-conjur

#---copy secrets.yml into image---#
COPY secrets.yml /etc/secrets.yml
COPY app.py /etc/app.py

RUN chmod +x /usr/local/bin/summon
RUN chmod +x /usr/local/lib/summon-conjur

#---override entrypoint to wrap command with summon---#
ENTRYPOINT ["summon", "--provider", "/usr/local/lib/summon-conjur", "-f", "/etc/secrets.yml", "python3", "/etc/app.py"]