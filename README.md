# panto
a pantomim online game


how to run 

. venv/bin/activate

gunicorn main:app --worker-class gevent -w 1 --bind 0.0.0.0:8000
