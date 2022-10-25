TNPG: STEVE. Roster: Ryan, Joseph, Samson
10/24/2022

DISCO:
Databases don't have a file extension.
sqlite shell commands use semicolons.

Creating a database:
$ touch <database name>

Opening a database in sqlite:
$ sqlite3 <database name>

Creating a database through sqlite shell:
Step 1: Run the sqlite shell by opening a database
$ sqlite3 <database name>
Note: If the database doesn't exist then it will access an empty database. This doesn't mean that the database is created yet.

Step 2: Create a table by typing
CREATE TABLE <table name> (<column name> <data type>, ...);
Note: After creating a table in an empty database, the database file will be created.

Basics in the sqlite shell:

Creating a table:
CREATE TABLE <table name> (<column name> <data type>, ...);

Inserting data into a table column:
INSERT INTO <table name> VALUES (<field 1>, <field 2>, ...);
