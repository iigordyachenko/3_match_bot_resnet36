# Start from a base image
FROM python:3.8-slim


COPY requirements.txt /workdir/
COPY app/ /workdir/app/
COPY model/ /workdir/model/
COPY epoch_resnet_102_channel_2_main.pth /workdir/

# Set the working directory
WORKDIR /workdir

# Install the required packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uvicorn", "app.app:app", "--host=0.0.0.0", "--port=80"]
