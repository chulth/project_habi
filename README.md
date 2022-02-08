# project_habi
technical test Habi

## Usage

All responses will have the form:

'''json
[
    {
        "address": "calle 95 # 78 - 49", "description": "hermoso acabado, listo para estrenar", "price": 120000000, "city": "bogota", "state": 3
        }
]

or

[
     {
         "message": "Description of whats happend"
         }  
]
'''

**Functional Requirements**

`The project must be in a GITHUB repository`
`Include readme`
`Create microservice to check the status of real estate`
`   -Create a json  of moock data that wait from front`
`   -Don't modify any records in the database`
`Handle the exceptions`

**Extra Points**

`Do the unit tests`
`Improve model of current database structure`



**Issues**

`I Use query parameters in place of json body with parameters to filter, because is a good practice.`


***second requirement***
**No Functional Requirements**
we must add a table called "tracking_likes", it must have the foreign keys of authorized user ID, property ID, ID, date of creation and date of modification, as a plus I would add a comment field so that the client tells us why Did you like the property, or if so why did you dislike it?

**SQL code to create table Tracking likes**

~~~~sql

CREATE TABLE TRACKING_LIKES(
    id int(11) NOT NULL  AUTO_INCREMENT,
    auth_user_id int(11) NOT NULL,
    property_id int(11) NOT NULL,
    create_on datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    modified_at timestamp default now() on update now(),
    comments text,
    liked  tinyint(1),
    PRIMARY KEY (id),
    FOREIGN KEY (auth_user_id) REFERENCES AUTH_USER(id),
    FOREIGN KEY (property_id) REFERENCES PROPERTY(id),
);
~~~~sql


**Diagram**


![Tracking_likes](https://user-images.githubusercontent.com/30079428/152918003-d408d2b0-e71f-4707-a7ce-2c0c7e1fc5d7.jpg)



