release: python manage.py migrate --noinput
web: gunicorn symfoni.wsgi:application --log-file -
