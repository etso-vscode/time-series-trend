import yaml
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

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
query = ("""SELECT kind_of_business, 
            year,
            SUM(sales) AS total_sales
        FROM mrts_sales
        WHERE kind_of_business = "Women's clothing stores"
        GROUP BY kind_of_business, year
        ORDER BY year;
        """)
                     
# execute query
cursor.execute(query)

year = []
sales = []

# print all the rows
for row in cursor.fetchall():
    print(row)
    year.append(row[1])
    sales.append(row[2])
    
cursor.close()
cnx.close()

plt.plot(year, sales)
plt.xlabel('Month-Year')
plt.ylabel('Total Sales')
plt.title('Women\'s clothing stores')
plt.tight_layout()
plt.show()
