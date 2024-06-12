#FROM alpine:3.14
FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

#ENTRYPOINT ["python"]
#RUN ["python", "model.py"]
RUN python ./model.py

EXPOSE 5000
CMD python ./app.py

#CMD ["python", "./app.py"]

#CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]