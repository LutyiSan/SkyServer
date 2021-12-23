FROM   python:latest

ADD    /pyserver/

RUN    pip3 install -r /pyserver/requirements.txt

#CMD    python3 server.py
