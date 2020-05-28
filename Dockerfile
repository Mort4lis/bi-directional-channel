FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1

RUN apk --update add postgresql-client

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app/
WORKDIR /app/

CMD ["python", "src/index.py"]
