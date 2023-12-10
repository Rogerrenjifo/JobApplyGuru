# JobApplyGuru
JobApplyGuru is an innovative API designed to simplify the job application process and empower job seekers in their quest for career success. This repository contains the source code, documentation, and resources for JobApplyGuru, an intelligent tool that assists users in creating compelling CVs and tailored cover letters.

# URL

The service is deployed in:

> https://apidockerimage.azurewebsites.net/ 


# tasks
# move the tasks to github projects 
## licence headers               configured in .vscode/settings.json
## Docstring                     define, add wiki, and if it is possible add linters for the docstring style                      
## linters                       configuredd (settings.json, test_requirements.txt, .pylintrc)
## unit tests                    
## asertions
## loggers
## swagger documentation
## autentication
## databases
## api Testing
## database Testing
## Gui Testing
## generate artifacts
## set  the exit criteria for the linter unit test an coverage.
## add security review
## change the name of the app service
## update azzure steps to deploy
## add documentation for the secrets


# ci commands
pylint --generate-rcfile > .pylintrc
pylint guru/
python -m unittest discover -s guru/test -v
coverage run -m unittest discover -s guru/test/
coverage report
coverage html
pytest --html=pytest_report/report.html
pytest --cov=guru --cov-report term-missing

# azzure steps
- create an account. freetier
- in all services search for "app services"
- create a new service
- create a new resource group.
- select plan 


## Document reference

https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#check-the-sqlalchemy-documentation
https://flask-restx.readthedocs.io/en/latest/
https://docs.github.com/en/actions/quickstart
https://portal.azure.com/

### Create a workflow dispatch event
> https://docs.github.com/en/rest/actions/workflows?apiVersion=2022-11-28#create-a-workflow-dispatch-event
### Slack commands 
> https://api.slack.com/interactivity/slash-commands
> https://www.bing.com/videos/riverview/relatedvideo?q=create%20commands%20slack&mid=49DB823936A23EAF9A7749DB823936A23EAF9A77&ajaxhist=0