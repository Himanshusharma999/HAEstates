# HAEstates tsk213, wxj782



## Initialization ✔

Clone / download repository files and run the following to install the required packages (preferably within a venv):

    pip install -r requirements.txt

Create a new database in pgAdmin (preferably named GreenGroceries) and add the following to your .env file (normally
.env should be a private file containing user secrets, in this case we have kept it inside the project files for easy
access for the TAs):

    SECRET_KEY=<secret_key>
    DB_USERNAME=postgres || <postgres_user_name>
    DB_PASSWORD=<postgres_user_password>
    DB_NAME=GreenGroceries || <postgres_db_name>

When all this information is present (and correct) the server can be started with:

    flask run

## Folder setup 📁

The app is divided into multiple folders similar to the structure of the example project, with a few tweaks:

- __blueprints__: Contains all the separate blueprints of the app (submodules of the app the store different parts of
  the functionality)
- __dataset__: Contains the csv file used to import the produce data
- __static__: Contains static files like images, css and js files (in this case javascript was not needed in the
  frontend)
- __templates__: This is the template folder of the app that stores all html files that are displayed in the user
  browser
- __utils__: Contains the sql files and script that generate the postgresql database. Also contains a script that
  generates custom choices objects for flask forms used in SelectFields taken from the dataset.

At the root folder of the app (./GreenGroceries) six more scripts are present with the following roles:

- __\_\_init\_\_.py__: Initializes the flask app and creates a connection to the database (and a cursor object for
  future queries)
- __app.py__: Runs the app created by \_\_init__.py
- __filters.py__: Implements custom template filters for nicer formatting of data in the frontend
- __forms.py__: Implements forms used to save data from users (similar to the example project)
- __models.py__: Implements custom classes for each of the database tables to store data in a clean OOP manner (again,
  similar to the example project, but our models inherit the dict class for faster and more readable lookups)
- __queries.py__: Implements functions for each needed query to the database used inside the app (similar to the
  functional part of the models.py file within the example project)

## Routes 📌

Both implemented blueprints come with a __routes.py__ file that initialize a __Blueprint__ object and define _routes_
for the app.

- __Login__:
    - __/home__: Home page
    - __/about__: About page

- __Property__:
    - __/Search__: Search page for all properties in the database
    - __/Browse__: Page for filtering the properties in the database
    
## Disclaimer 
- This project has used the example project "GreenGroceries" as a starting point. 

## Some known backend issues / Intended features ⁉

- The browse feature was intended to be able to filter through the dataset, and return the now filtered dataset, but we have not been able to get to work. 

- The solution should be very simular to how we implemented the search feature, and with a bit more time, we would have been able to solve this. 



## Known frontend issues ☹

- The Browse feature lets the user interact with the filters but it does not do anything since the backend is not complete. 

- The search feature can be used as intended, allthough the resulting list of properties is not very user friendly, and could be made more easy to read and navigate through. 
