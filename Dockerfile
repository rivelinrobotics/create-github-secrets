FROM python:3.12-slim
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
COPY create_secrets.py /tmp/create_secrets.py
ENTRYPOINT [ "python3", "/tmp/create_secrets.py" ]