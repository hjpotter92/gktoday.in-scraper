FROM python:3.7.5-slim-buster

WORKDIR /app

COPY . .

# python3-dev python3-pip python3-setuptools python3-wheel python3-cffi \

RUN apt update && \
    apt install -y build-essential \
    libcairo2 libpango-1.0-0 libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 libffi-dev shared-mime-info libxml2-dev libxmlsec1-dev \
    libz-dev && \
    pip install -U pip -r requirements.txt && \
    apt purge -y build-essential && \
    rm -rf /root/.cache/pip /var/lib/apt/lists/*

CMD [ "python" ]
