FROM python:3.10-alpine
#FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN \
apk add --no-cache bash && \
apk add --no-cache postgresql-libs && \
apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

RUN python3 -m pip install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "/bin/bash", "entrypoint.sh" ]

#ENTRYPOINT [ "python3", "app.py" ]
#ENV FLASK_APP=app.py
#ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]




