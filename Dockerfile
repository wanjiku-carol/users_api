FROM python:3.8.7-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN python -m venv venv

RUN pip install --no-cache-dir --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
