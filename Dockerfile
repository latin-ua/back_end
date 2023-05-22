FROM docker.io/python:3.10-alpine
ADD ./src/ua_latin.py /ua_latin.py
ADD ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ENTRYPOINT python3 /ua_latin.py