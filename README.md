# Questioner-api-3

[![Build Status](https://travis-ci.com/bochiedev/Questioner-api-3.svg?branch=develop)](https://travis-ci.com/bochiedev/Questioner-api-3) [![Coverage Status](https://coveralls.io/repos/github/bochiedev/Questioner-api-3/badge.svg?branch=develop)](https://coveralls.io/github/bochiedev/Questioner-api-3?branch=develop)

This is an API for an app that allows users to view meetups and schedule for attendance as well as ask questions and comment on questions.

#### Requirements

- Postgres database


#### API-endpoints



#### Installation

To get your build running just simply do:

* Git clone the repo to your machine;
  >  * git clone https://github.com/bochiedev/Questioner-api-3.git
  >  * cd Questioner-api-3

* Install virtualenv globally but if you got them you can skip this step;
> * pip install virtualenv

* Create a virtualenv ;
    * virtualenv ;
        > * virtualenv -p python3 venv             


* Install the requirements;
   > pip install -r requirements.txt

##### Run It!

To start the server just do;
> flask run

The server will be running on    `http://127.0.0.1:5000/`   
Now you can include an endpoint of choice;   
eg:   `http://127.0.0.1:5000/api/v1/auth`
