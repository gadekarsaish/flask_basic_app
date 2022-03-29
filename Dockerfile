FROM python:3.7.0-stretch
COPY . /app
WORKDIR /app
RUN pip install flask

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]