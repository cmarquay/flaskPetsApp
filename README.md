# Pets app

Deployment of models with TensorFlow Serving and Flask

For windows10

Run TensorFlow Serving with Docker:

    docker run -p 8501:8501 --name=pets -it -v "/path/to/saved_model/:/models/pets/1" -e MODEL_NAME=pets tensorflow/serving

Create a virtualenv:
`py -3 -m venv venv`

Activate virtualenv:
`venv\Scripts\activate`

Install the python libraries:
`pip install -r requirements.txt`

Launch the application:
`python run.py`

**Author**: Christian MARQUAY / June 2020

Made from the MOOC [Deploy Models with TensorFlow Serving and Flask](https://www.coursera.org/projects/deploy-models-tensorflow-serving-flask)