FROM python:3.9-slim
ADD . /codes/api
WORKDIR /codes/api
RUN pip install -r requirements.txt
CMD python manage.py
