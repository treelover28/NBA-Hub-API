FROM ubuntu

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev build-essential

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install pymongo[srv]
COPY . /app/nba-match-predictor
EXPOSE 5000
EXPOSE 8000
# launch app
ENV FLASK_APP=app.py
CMD ["python3", "-b", "/app/nba-match-predictor/api/deploy.py"]
# CMD ["python3", "/app/nba-match-predictor/api/app.py"]