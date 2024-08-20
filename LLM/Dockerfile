FROM python:3.11.9-slim-bookworm

RUN apt-get update --quiet \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends --quiet \
    gnupg \
    libodbc1 \
    unixodbc \
    unixodbc-dev \
    git \
    libgl1 \
    curl \
    build-essential \
    software-properties-common \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt
COPY . /app

EXPOSE 80

CMD ["gunicorn", "app.app:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:80", "--timeout", "200", "--keep-alive", "5", "--log-level", "info"]