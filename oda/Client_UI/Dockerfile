FROM python:3.8-slim-buster

WORKDIR /client

COPY requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5001

ENTRYPOINT [ "python3", "client.py" ]
#ENV FLASK_APP=client.py
#ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]


