# JobApplyGuru
JobApplyGuru is an innovative API designed to simplify the job application process and empower job seekers in their quest for career success. This repository contains the source code, documentation, and resources for JobApplyGuru, an intelligent tool that assists users in creating compelling CVs and tailored cover letters.

## licence headers               configured in .vscode/settings.json
## Docstring                     
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

# ci commands
pylint guru/
python -m unittest discover -s guru/test -v
coverage run -m unittest discover -s guru/test/
coverage report
coverage html
pytest --html=pytest_report/report.html
pytest --cov=guru --cov-report term-missing
