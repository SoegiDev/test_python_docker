# create image
docker build -t test-python:1.0 . 

# create container
docker container create --name test-python -p 8000:5000 test-python:1.0

# start container
docker container start test-python
