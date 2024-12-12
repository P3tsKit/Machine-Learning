# use python base image
FROM python:3.12-slim

# set working directory in the container
WORKDIR /app

# copy the application files into the container
COPY . /app

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose port for flask application
EXPOSE 5000

# run the flask application
CMD ["python", "main.py"]