FROM python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./core  /app

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]

# Step1 -> build image : docker build -t django . 
# Step2 -> run image :  docker run -p 8000:8000 django 