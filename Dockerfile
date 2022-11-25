# app/Dockerfile
# https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker

FROM python:3.9-slim

EXPOSE 8501

COPY . .

WORKDIR /

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    ffmpeg libsm6 libxext6 \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "src/appv2a.py", "--server.port=8501", "--server.address=0.0.0.0"]