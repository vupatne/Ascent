# Ascent
Simple python web application with mysql, flask and html.

# Install a mysql database to you machine. Then create a database as below and run queries. 
CREATE DATABASE ascent;

use ascent;

SET SQL_SAFE_UPDATES = 0;

CREATE TABLE users (
  id int NOT NULL AUTO_INCREMENT,
  userid int NOT NULL,
  firstname varchar(50) DEFAULT NULL,
  lastname varchar(50) DEFAULT NULL,
  email varchar(50) DEFAULT NULL,
  phone varchar(20) DEFAULT NULL,
  address varchar(100) DEFAULT NULL,
  reference varchar(20) DEFAULT NULL,
  idpassword varchar(20) DEFAULT NULL,
  createddate datetime DEFAULT NULL,
  modifieddate datetime DEFAULT NULL,
  isactive varchar(1) DEFAULT NULL,
  PRIMARY KEY (id)
);


# Run App.
1. Clone this repo to your machine.
2. Update database name, user name and passed in config/dbQueries.py file.
3. You should have python installed in your machine. Check using python -V. Python 3 or greater must be installed.
4. Install all dependency listed in requirements.txt using pip install.
pip install flask gunicorn psycopg2 requests base58 mailjet_rest
5. You should have an IDE like pycharm.
6. Run app.py from pycharm.
7. Hit http://localhost:8080/ in your web browser.
