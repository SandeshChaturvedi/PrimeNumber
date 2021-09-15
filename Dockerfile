FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python3-pip
	
#RUN pip install flask
#RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

CMD [ "python3", "./app.py" ]
#ENTRYPOINT Flask_app= /opt/source-code/app3.py flask run
