# USERS API
This is a backend API that makes a call to our Users database and returns the request made by the user.

## API Endpoint
> /users

Calls to the APIs

### GET All USERS
Gets all the users from the database using a GET request with no parameters. The database contains as many as a million users and will have features to accomodate that size of data with efficiency

*Endpoint*
> /users

Features
- Pagination: This will classify each select group of users into pages. That is e.g. 50 users per page. This will also enable the user making the call to be able to scroll from page to page (to and from).

- Select Page: The user can choose the page which they would like to view.

### GET SINGLE USER
Allows a call to get a specific user using parameters such as email and user_id

*Endpoint*
> /users/{param}

Features
- Returns all the details about a specific user.
- Allows to search for a specific user using the specified feature

## Running the Application
git clone the app:
> git@github.com:wanjiku-carol/users_api.git

Change directory into the app
> cd users_api

### Using Docker to Run the App

To build the containers

> docker-compose -up -d --build

To view the running containers:

> docker ps

### Running the App Locally
Create virtual env
> mkvirtualenv --python=python3 usersapi

Activate virtual env
> workon usersapi

Install requirements
> pip install -r requirements.txt

Run the app
> flask run

DB set database
> createdb userapi_db

Initiate the database
> flask db init

Run migrations
> flask db migrate

Upgrade database
> flask db upgrade
