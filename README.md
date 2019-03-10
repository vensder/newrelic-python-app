# Python Web Application With New Relic Monitoring

```docker build -t myapp .```

```sh
docker run -d --rm \
	-p 0.0.0.0:80:8080 \
	-e PYTHONUNBUFFERED=1 \
	-e NEW_RELIC_CONFIG_FILE=newrelic.ini \
	-e NEW_RELIC_LICENSE_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
	myapp
```


```sudo NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program app.py```

