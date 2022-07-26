# machine_learning_project

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


My machine learning project


Creating conda env

conda create -p mlvenv python==3.7 -y

conda activate mlvenv

or 

conda activate mlvenv/

Use cmd incase terminal doesnt work for activation of conda env

pip install -r requirements.txt

To add files:

git add . or git add filename

to check status

git status

To check all versions maintained

git log

To create version/commit all changes by git

git commit -m "message"

To send version/changes to githib

git push origin main

To check remote URL

git remote -v

---

To set up Ci/CD pipeline in Heroku we need3 info

Heroku email: 
Heroku API key: <>
Heroku app name: gracy-ml-project


BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```

```
Creation of setup.py file:

python setup.py install
```
````
find_packages in setup file dynamically gets the packages(the folders that have __init__.py file)
-e . in the requrirements.txt installs the custom packages and setup.py should be present
`````

````
Create the folders for the housing package
exception, logger, pipeline, component, config, entity and create __init__.py files under each folder
````````````
````
to install ipykernel - pip install ipykernel

to access jupyter notebook from vscode for sample coding purposes
