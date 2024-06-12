# Lineer Regression Example API

## Build and deploy app with Docker

```docker-compose up -d```

## Installing packages with conda

```conda install --file requirements.txt```

## To train the model

```python model.py```

## Running api application

```python app.py```

## Postman Kullanımı

**BASE_URL** = http://localhost:5000

Postman'de istek atarken data türü raw JSON seçilerek json formatonda parametre gönderilecek.


| Method | Url                                                | Açıklama                              | Parametreler                                 |
|--------|----------------------------------------------------|---------------------------------------|----------------------------------------------|
| GET    | /                                                  | Test                                  |                                              |
| POST   | /predict                                           | Model Tahmini                         | { "X": [[4,4]] }                             |