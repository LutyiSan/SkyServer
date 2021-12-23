FROM   python:latest

ADD    /pyserver/

RUN    pip3 install -r /pyserver/requirments.txt

#CMD    python3 server.py
