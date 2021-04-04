FROM python:3.6-slim

WORKDIR /app

RUN apt update && \
    apt install -y build-essential \
    libcairo2 libpango-1.0-0 libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 libffi-dev shared-mime-info libxml2-dev libxmlsec1-dev \
    libz-dev

COPY requirements.txt .

RUN pip install -U pip -r requirements.txt && \
    apt purge -y build-essential && \
    rm -rf /root/.cache/pip /var/lib/apt/lists/*

COPY . .

CMD [ "python" ]
