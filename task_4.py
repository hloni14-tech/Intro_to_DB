import getpass
import sys
try:
  import mysql.connector
  from mysql.connector import Error
except ImportError:
 print("mysql is not connecting or installed.")

DB = "alx_book_store"

SHOW TABLE books;