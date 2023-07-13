FROM docker.io/python:3.10-alpine
ADD ./src/ua_latin.py /ua_latin.py
ADD ./requirements.txt /requirements.txt
ADD ./newrelic.ini /newrelic.ini

RUN pip install -r /requirements.txt

RUN pip install newrelic==8.8.1

ENV NEW_RELIC_CONFIG_FILE=/newrelic.ini

ENTRYPOINT newrelic-admin run-program python3 /ua_latin.py