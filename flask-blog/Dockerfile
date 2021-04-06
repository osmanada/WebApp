#create python image
FROM python:3.8

#this working directory will be created into the container
WORKDIR /flask-blog  

#copy the requirements file in the working directory of the container
COPY requirements.txt .

#install all the dependencies
RUN pip install -r requirements.txt

#copy the app folder from local directory to the container
COPY ./app ./app

#execution cmd inside the container
CMD ["python", "./app/myflask1.py"]