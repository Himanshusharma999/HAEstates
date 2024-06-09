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
    - __/style-guide__: Style guide (displays all html elements used, just for fun and css debugging)
    - __/login__: User login page (for simplicity in debugging, password hashing was omitted even though the example
      project made it pretty clear and easy to implement with bcrypt)
    - __/signup__: User signup (creation) page
    - __/logout__: Logs user out and sends back to login page

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
3.0.7 g
We select the manufactures in a table made by combining Product and printer,
that suffice that color = ’true’ and that the price is the lowest of the table.
3.0.8 h
We select the model number and price in a combined set of computers (using
union all) of the computers(laptops and pc’s) that have a speed equal to the
highest speed in the set.
3.0.9 i
We select the manufacturer and the screen size calculated as an average and
labelled as average screen size. To retrieve the data we join the two datasets
product and laptop, by their common attribute model. We ”group” the averages
with the ”maker”
3.0.10 j
we select the manufacturers from product that have a model count of at least
three.
3.0.11 k
we select the manufacturer and the price as max price from the combined set
of product and pc, that is combined with the common attribute model.
3.0.12 l
we we select the manufacturer and the hard disk size as an avg hd size. we
combine the sets product and pc with the common attribute model, and only
include data points where the type is ’printer’
4 Exercise 4
4.1 a) Using two INSERT statements, store in the database
the fact that PC model 1100 is made by manufacturer
C, has speed 3.2, RAM 1024, hard disk 180, and sells
for $2499.
The following queries uses insert statement to insert the specified PC model:
insert into PC values(1011, 3.2, 1024, 180, 2499);
insert into Product values(’C’,1011,’PC’);
7
4.2 b) Delete all PCs with less than 100 gigabytes of hard
disk.
We delete from the table PC where the harddisk is less than 100:
delete from PC P where P.hd ¡ 100;
4.3 c) Delete all laptops made by a manufacturer that
does not make printers.
4.4 d
changes the value of the attribute maker to ’A’ where it was ’B’ prior.
4.5 e
doubles the ram and add 60 to the hard drive.
4.6 f
add the desired screen size and deducts the price by 100 for manufactures labeled
’B’
4.7 g
deletes all products
8
