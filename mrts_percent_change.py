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
query = ("""
        SELECT
            DATE_FORMAT(CONCAT(year, '-', LPAD(month, 2, '0'), '-01'), '%Y-%m-01') AS date,
            sales
        FROM mrts_sales
        WHERE kind_of_business = "Food services and drinking places"
        ORDER BY date;
        """)
                     
# execute query
cursor.execute(query)

date = []
sales = []

# print all the rows
for row in cursor.fetchall():
    print(row)
    date.append(row[0])
    sales.append(row[1])
    
cursor.close()
cnx.close()

df = pd.DataFrame({'Date': date, 'Sales': sales})
df['Rolling Window'] = df['Sales'].rolling(window = 6).mean()
df = df.dropna(subset=['Rolling Window'])
 

plt.plot(df['Date'], df['Rolling Window'])
plt.xlabel('Date')
plt.ylabel('Sales Rolling Time Windows')
plt.title('Food services and drinking places')
plt.tight_layout()
plt.ylim(min(df['Rolling Window']), max(df['Rolling Window']))
plt.show()

