# ML-END-TO-END-PROJECT-
This is a machine learning project where all end to end deployement code is available.

# Software and account Requirement: - 
Github Account
Heroku Account
VS Code IDE
GIT cli
GIT Documentation
Creating conda environment

conda create -p venv python==3.7 -y
conda activate venv/
OR

conda activate venv
pip install -r requirements.txt
To Add files to git

git add .
OR

git add <file_name>
Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status

git status
To check all version maintained by git

git log
To create version/commit all changes by git

git commit -m "updated"
To send version/changes to github

git push origin main
To check remote url

git remote -v
To setup CI/CD pipeline in heroku we need 3 information

HEROKU_EMAIL = pbannuru@gmail.com
HEROKU_API_KEY = f2ccae77-156e-4e59-be69-59531739708c
HEROKU_APP_NAME = mlcicdapp

BUILD DOCKER IMAGE

docker build -t credit:end-to-end .
Note: Image name for docker must be lowercase

To list docker image

docker images
Run docker image

docker run -p 5000:5000 -e PORT=5000 3ef4f8712454
To check running container in docker

docker ps
Tos stop docker conatiner

docker stop <container_id>
python setup.py install
Install ipykernel

pip install ipykernel

pip install six
<<<<<<< HEAD

Data Drift: When your datset stats gets change we call it as data drift


git branch <newbranchname>

git checkout <newbranchname>

git push origin <newbranchname>





STRUCTURE OF THE PROJECT

|-- Project
    |-- config
        |-- config.yaml
        |-- schema.yaml
        |-- model.yaml
    |-- credit (Project folder)
        |-- __init__.py
        |--constant (All the hardcoded values)
            |--__init__.py
        |-- component (pipeline stages)
            |-- __init__.py
            |-- data_ingestion.py
            |-- data_validation.py
            |-- data_transformation.py
            |-- model_train.py
            |-- model_evaluation.py
            |-- model_push.py
        |-- get_config
            |-- __init__.py
            |-- configuration.py
        |-- entity
            |-- __init__.py
            |-- config_entity.py
            |-- artifact_entity.py
        |-- exception
            |-- __init__.py
        |-- logger
            |-- __init__.py
        |-- pipeline
            |-- __init__.py
            |-- pipeline.py
        |-- util (Helper function)
            |--__init__.py
            |-- util.py
    |-- .gitignore
    |-- app.py (Entry Point to the Project)
    |-- requirements.txt
    |-- LICENSE
    |-- README.md