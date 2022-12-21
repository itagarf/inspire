#FROM python:3.10-alpine
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD python app.py

#CMD [ "/bin/bash", "entrypoint.sh" ]

#ENTRYPOINT [ "python", "app.py" ]
#ENV FLASK_APP=app.py
#ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]




