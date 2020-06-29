web: gunicorn note_api.wsgi:application --log-file - --log-level debug
web: python manage.py runserver 0.0.0.0:$PORT
web2: daphne note_api.asgi:channel_layer --port $PORT --bind 0.0.0.0
worker: python manage.py runworker
web3:    bin/start-pgbouncer bundle exec unicorn -p $PORT -c ./config/unicorn.rb -E $RACK_ENV
worker2: bundle exec rake worker