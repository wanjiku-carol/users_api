FROM python:3.8.7-slim-buster

WORKDIR /app

COPY requirements.txt /app

RUN python -m venv venv

RUN pip install --no-cache-dir --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

RUN ["chmod", "+x", "entrypoint.sh"]

ENTRYPOINT ["sh", "entrypoint.sh"]


