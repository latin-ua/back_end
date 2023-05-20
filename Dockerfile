FROM docker.io/python:3.10-alpine
ADD ./test.py /test.py
ADD ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ENTRYPOINT python3 /test.py