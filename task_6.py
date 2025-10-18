import getpass
import sys
try:
  import mysql.connector
  from mysql.connector import Error
except ImportError:
 print("mysql is not connecting.")

DB = "alx_book_store"

INSERT INTO customer (customer_id, customer_name,
email, address)
VALUES (2, 'Blessing Malik', 'bmalik@sandtech.com',
'124 Happines Ave.'), 
             (3, 'Obed Ehoneah', 'eobed@sandtech.com', 
'125 Happiness Ave.'),
              (4, 'Nehemial Kamolu', 'nkamolu@sandtech.com',
'126 Happiness Ave.');

