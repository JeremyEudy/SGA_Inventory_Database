Author: Jeremy Eudy
For: COP-3729

File Purposes:

-FrontEnd.py
	Command line interface for the database system. Primary file for traversing SGA information.

-gridfs.pl
	Automate file upload to local MongoDB instance in conjunction with meta data scraping from SGA_Assets.txt

-SGA_Assets.txt
	.csv file converted to .txt with semicolons as delimiters. This is the sample inventory data from SGA

-/Photos/
	Directory full of .jpg photos used as sample data for the MongoDB NoSQL database.

Necessary Libraries:
	Python:
		pymongo, sys, gridfs, pprint, psycopg2
	Perl:
		MongoDB, MongoDB::GridFS, File::Basename, IO::File

Compatibility:
	Built to run on MongoDB v2.6 and PostgreSQL v9.5
	Pymongo v3.6
	Psycopg2 v2.6

Usage Order:
	1)clear;gridfs.pl
	2)clear;python3 FrontEnd.py