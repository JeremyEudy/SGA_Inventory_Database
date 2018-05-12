# SGA_Inventory_Database
Inventory and budget database system for Florida Polytechnic SGA

##Getting Started
Easy clone:
```
mkdir -p ~/SGA_Inventory_Database/ && cd
git clone https://github.com/JeremyEudy/SGA_Inventory_Database
```
### Prerequisites
This project depends on MongoDB.pm, MongoDB current, Pymongo, GridFS, Psycopg2, and pprint for Python 3
```
sudo apt-get install MongoDB
cpan MongoDB
sudo pip install Pymongo
sudo pip install Psycopg2
sudo pip install pprint
```
### Compatibility
Built to run on MonoDB v2.6 or above and PostgreSQL v9.5
Pymongo v3.6
Psycopg2 v2.6

### File Purposes
FrontEnd.py
	Command line interface for the database system. Primary file for traversing SGA information.

gridfs.pl
	Automate file upload to local MongoDB instance in conjunction with meta data scraping from SGA_Assets.txt

SGA_Assets.txt
	.csv file converted to .txt with semicolons as delimiters. This is the sample inventory data from SGA

/Photos/
	Directory full of .jpg photos used as sample data for the MongoDB NoSQL database.

### Usage
Usage must go in this order when creating a new database:
```
gridfs.pl
python3 FrontEnd.py
```

### Author
Jeremy Eudy

### License
This project is licensed under the GPLv2
