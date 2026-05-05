FROM ubuntu:22.04

WORKDIR /app

COPY . .

RUN apt-get update --fix-missing && \
    apt-get install -y python3 python3-pip && \
    python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8000

CMD ["python3", "application_controller.py"]