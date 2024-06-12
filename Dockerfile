FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

RUN python ./model.py

EXPOSE 5000

CMD ["python", "./app.py"]