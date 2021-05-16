pip install gunicorn 
gunicorn -w 4 -b localhost:5000 run:app