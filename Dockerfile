FROM raspbian/stretch

MAINTAINER Jeremie CUADRADO <redbeard28>

WORKDIR /script

# Copy the current directory to /script
ADD script /

# Install any needed packages specified in requirements.txt
#RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

RUN apt-get update \
    && apt-get -y install python3 \
    python3-pip \
    python3-dev \
    python3-rpi.gpio

# Run app.py when the container launches
CMD ["python3", "/script/blink_led.py"]
