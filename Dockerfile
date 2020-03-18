FROM python:3.7.5-slim-buster

WORKDIR /app

COPY . .

RUN apt update && \
    apt install -y gcc libxml2-dev libxmlsec1-dev libz-dev && \
    pip install -U pip -r requirements.txt && \
    rm -rf /root/.cache/pip /var/lib/apt/lists/*

CMD [ "python" ]
