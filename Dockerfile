FROM python:3.8

WORKDIR /app
COPY main.py .

SHELL ["/bin/bash", "-c"]

RUN apt update
RUN apt install python3-venv -y 
RUN python3 -m venv .venv 
RUN source .venv/bin/activate 
RUN pip3 install tornado

ENTRYPOINT ["python3", "main.py"]
