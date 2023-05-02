FROM python

WORKDIR /maktab-app

COPY requirements.txt /maktab-app/

RUN pip install -r requirements.txt

COPY ./core  /maktab-app

CMD ["python","manage.py","runserver"]