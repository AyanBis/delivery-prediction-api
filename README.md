# Delivery Prediction API

A Flask-based API that predicts delivery time using distance and package weight. The model is serialized using Pickle and tested with Postman.

## Features
- Flask REST API
- Pickle model integration
- Delivery time prediction
- Postman testing support

## Project Structure

```bash
delivery_project/
│
├── app.py
├── train.py
├── delivery_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

```bash
git clone https://github.com/AyanBis/delivery-prediction-api.git
cd delivery-prediction-api

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Run

Train model:

```bash
python train.py
```

Start Flask server:

```bash
python app.py
```

Server runs at:

```bash
http://127.0.0.1:5000
```

## API Endpoint

POST Request:

```bash
http://127.0.0.1:5000/predict
```

Request Body:

```json
{
    "distance": 10,
    "weight": 5
}
```

Response:

```json
{
    "estimated_delivery_time": 3.0
}
```

## Technologies Used
- Python
- Flask
- Pickle
- Postman

## Author
Ayan Biswas