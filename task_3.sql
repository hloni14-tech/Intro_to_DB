import getpass
import sys
try:
  import mysql.connector
  from mysql.connector import Error
except ImportError:
 print("mysql-connector-python is not installed.")

"USE alx_book_store";

TABLES = [(SHOW TABLES)]
