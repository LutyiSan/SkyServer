FROM   python:latest

ADD    /pyserver/

ADD    apt install python3-pip

RUN    pip3 install -r /pyserver/requirements.txt

CMD    python3 /pyserver/server.py
