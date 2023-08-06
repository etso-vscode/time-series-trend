import yaml
import pandas as pd
import mysql.connector

# connect to MySQL
# safe_load() function of the PyYAML module loads a YAML file with object serialization

db = yaml.safe_load(open('db.yaml'))
config = {
    'user':     db['user'],
    'password': db['pwrd'],
    'host':     db['host'],
    'database': db['db'],
    'auth_plugin': 'mysql_native_password'
     }

# connecting to database
cnx = mysql.connector.connect(**config)

# cursor to run queries in MySQL
cursor = cnx.cursor()

# query to count sales totals for 2019
query = ("""
        SELECT year, count(kind_of_business)
        FROM mrts_sales
        GROUP BY year;
        """)
                     
# execute query
cursor.execute(query)

# print all the rows
for row in cursor.fetchall():
    print(row)
    
cursor.close()
cnx.close()
