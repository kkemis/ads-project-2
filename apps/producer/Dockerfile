FROM python:3.9.16-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install -r requirements.txt
COPY . .
CMD ["python", "producer.py"]
