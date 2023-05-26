# # pull official base image
# FROM python:3.8-alpine

# # set work directory
# WORKDIR /usr/src/app

# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # install psycopg2 dependencies
# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev

# # for images - pillow
# RUN apk add zlib zlib-dev jpeg-dev

# RUN apk add --no-cache tzdata

# ENV TZ Asia/Tashkent

# # install dependencies
# RUN pip install --upgrade pip
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt

# # copy entrypoint.sh
# COPY ./entrypoint.sh .

# # copy project
# COPY . .

# # run entrypoint.sh
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

FROM --platform=linux/amd64 python:3.9  as builder

WORKDIR /app

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

FROM --platform=linux/amd64 python:3.9

WORKDIR /app

RUN apt update && apt install -y libpq-dev gettext

ENV PATH="/opt/venv/bin:$PATH"

COPY --from=builder /opt/venv /opt/venv

COPY . .

EXPOSE 8002


CMD python manage.py collectstatic --noinput && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    # make compile-language && \
    uvicorn app.asgi:application --host 0.0.0.0 --port 8002 
