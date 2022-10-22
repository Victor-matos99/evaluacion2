# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install mysql-connector-python==8.0.29
RUN pip install -r requirements.txt
EXPOSE 65534
EXPOSE 8080
EXPOSE 443
COPY . .
CMD ["flask", "run"]
