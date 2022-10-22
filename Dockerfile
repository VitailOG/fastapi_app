FROM python:3.10-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1 && PYTHONUNBUFFERED 1

ENV PROJECT="app"
ENV SETUP_PATH="/$PROJECT"
ENV UNITY_ENV="$SETUP_PATH/.env"


COPY requirements-backend.txt .

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev libjpeg

RUN apk add build-base && apk add libffi-dev

RUN pip install --upgrade pip && pip install -r requirements-backend.txt

COPY . .

RUN chmod 777 $UNITY_ENV

RUN $UNITY_ENV
