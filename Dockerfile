FROM python:3.11.3-buster 

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /code

COPY requirements.txt /code/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./core /code

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
