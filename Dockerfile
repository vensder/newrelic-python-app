FROM python:3.7.2-alpine3.9

WORKDIR /usr/src/app/

COPY . /usr/src/app

RUN pip install -r /usr/src/app/requirements.txt

EXPOSE 8080

# CMD ["python","-u","application.py"]
CMD ["newrelic-admin","run-program","application.py"]