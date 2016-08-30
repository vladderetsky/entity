ENTITY REST API
===============


This is a JSON based REST API application that implements an Entity operations such as add, sum, and update.

##Endpoints

###Endpoint /addEntity

Receives an array of integers along with a unique ID and returns a set of arrays which contain all unique permutations of the order of the integers.

- Path: /addEntity
- Request: POST


    Example:
    {
        “enity ": 1,
        "data": [1, 2, 3]
    }
    Response:
    {
        “permutations”: [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ]
    }


###Endpoint /sumEntity/entityID

Receives a unique ID and returns the sum of all integers that belong to the entity that was added using end point.

- Path: /sumEntity/entityID
- Request: GET


    Example: /1
    Response:
    {
        “sum”:36
    }

###Endpoint /updateEntity

- Path: /updateEntity
- Request: POST


    Example:
    {
        "entityID ": 1,
        "add": -1
    }
    Response:
    {
        "results": [
            [0, 1, 2],
            [0, 2, 1],
            [1, 0, 2],
            [1, 2, 0],
            [2, 0, 1],
            [2, 1, 0]
        ]
    }


##Installation

Application is written in Python and requires Python 2.7.

###Git clone

To run an application, you can clone this repository.

###Install required packages using pip


    $ pip install -r requirements.txt


## Configuration

To run application, you have to specify its configuration in config/restsrv.ini file:


    [restsrv]
    host: 0.0.0.0
    port: 8080


##Run Application


    $ cd <directory where application was cloned or copied>
    $ export FLASK_APP=app.py
    $ flask run
      or
    $ python -m flask run


###REST API Calls using the curl tool


    $ curl -H "Content-Type: application/json" -XPOST localhost:8080/addEntity -d '{"entityID": 1,"data": [1, 2, 3]}'
    $ curl localhost:8080/sumEntity/entityID/1
    $ curl -H "Content-Type: application/json" -XPOST localhost:8080/updateEntity -d '{"entityID":1, "add": -1}'


##Testing Application

Install nosetest package or any other python test engine before running the UnitTest suite for this application.

    $ cd <directory where application was cloned or copied>
    $ pip install -r requirements-test.txt


To run the Unit Test set, just execute the following:


    $ nosetests tests


or if pytest package was installed then use the following:


    $ py.test tests




