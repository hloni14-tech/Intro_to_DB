import getpass
import sys
try:
  import mysql.connector
  from mysql.connector import Error
except ImportError:
 print("Error.")

DB = "alx_book_store"

INSERT INTO customer (customer_id,customer_name,
email,address)
VALUES (1, 'Cole' 'Baidoo', 'cbaidoo@sandtech.com',
123 'Happiness Ave.');