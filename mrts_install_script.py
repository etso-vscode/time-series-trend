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

# query to create a database and table for MRTS data
query = ("""
        DROP DATABASE IF EXISTS `MRTS`;
        CREATE DATABASE IF NOT EXISTS `MRTS`;
        USE `MRTS`;
         
        SET NAMES UTF8MB4;
        SET character_set_client = UTF8MB4;
         
        CREATE TABLE `MRTS_sales`(
            `kind_of_business` varchar(100) NOT NULL,
            `month` int NOT NULL,
            `year` int NOT NULL,
            `sales` int NULL
            ) ENGINE = InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=utf8mb4_0900_ai_ci;
            """)
                     
# execute query
cursor.execute(query)

    
cursor.close()
cnx.close()


db = yaml.safe_load(open('db.yaml'))
config = {
    'user':     db['user'],
    'password': db['pwrd'],
    'host':     db['host'],
    'database': db['db'],
    'auth_plugin': 'mysql_native_password'
     }

cnx = mysql.connector.connect(**config)

    
cursor = cnx.cursor()

# read in CSV file to DataFrame
mrts_sales_data = r"C:\Users\Tola\Desktop\sample\Projects\Module8\MRTS.csv"
df = pd.read_csv(mrts_sales_data, delimiter=',')
df =df[['kind_of_business','month','year','sales']]

        
# query to insert data in to MRTS_sales table    
query = """INSERT INTO MRTS_sales (kind_of_business, month, year, sales)
                     VALUES (%s, %s, %s, %s)"""

# looping through the rows to add data
for row in df.itertuples(index=False):
    cursor.execute(query, row)

# commiting the changes  
cnx.commit()     



# print all the rows
for row in cursor.fetchall():
    print(row)
    
cursor.close()
cnx.close()