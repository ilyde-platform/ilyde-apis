#!/usr/bin/env bash

# starting flask (default)
if [ $1 = 'flask' ]; then
	# run flask with gunicorn
    gunicorn --bind 0.0.0.0:8080 --worker-class=gevent -t 300 apis_server:app --access-logfile '-'  --error-logfile '-'
fi

#override command
exec "$@"
