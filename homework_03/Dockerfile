#  docker build . -t homework_03
#  docker run -p 8000:8000 -it homework_03

FROM python:3.12.2-bookworm

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm -rf /root/.cashe/pip

COPY app ./

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]