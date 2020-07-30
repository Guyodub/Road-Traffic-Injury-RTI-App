"# Road-Traffic-Injury-RTI-App" 

Road Traffic Injuries (RTI) Handler Project

# introduction
Road Traffic Injury (RTI) handler is an application used in management of emergencies due to road crash. The handler automates the process of the road injuries and supports timely notification of the nearest medical Centre for immediate intervention through dispatch of medical staff and booking of emergency room for rapid intervention. The RTI DB runs on Postgres and it stores information about road injuries.  


# Install the following as per requirements.txt file
pipenv shell

pipenv install flask

pipenv install psycopg2 ##database adapter

pipenv install pyscopg2-binary 

pipenv install flask-sqlalchemy ## Abstract layer to work with database

pipenv install gunicorn



## create a front_end
home.html
indel.html 
success.html

## Do a flask app
create app.py file

## Do a send.py file for sending email via mailtrap.io
go to mailtrap.io and register, you will get credentials 