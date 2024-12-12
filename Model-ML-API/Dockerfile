# use python base image
FROM python:3.10-slim

# set working directory in the container
WORKDIR /app

# copy the requirements.txt file into the container
COPY requirements.txt .

# install the dependencies in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy the entire contents of the project folder into the container
COPY . .

# set environment variables for flask
ENV FLASK_APP=main.py
ENV FLASK_ENV=production

# expose port 8080 for flask application
EXPOSE 8080

# commands to run apps with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]