FROM alpine:3.7
ENV APP_DIR /app
RUN apk update && \
  apk add python python3 python3-dev supervisor && \
  pip3 install --upgrade pip
RUN mkdir -p /deploy/app
COPY requirements.txt /deploy
RUN pip3 install -r /deploy/requirements.txt 
RUN python3 -m textblob.download_corpora
COPY gunicorn_config.py /deploy/gunicorn_config.py
COPY app /deploy/app
WORKDIR /deploy/app
EXPOSE 8080
CMD ["gunicorn", "--config", "/deploy/gunicorn_config.py", "main:app"]
