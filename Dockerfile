FROM ubuntu

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev tree

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app/nba-match-predictor
EXPOSE 5000
# launch app
CMD ["python3", "/app/nba-match-predictor/api/app.py"]