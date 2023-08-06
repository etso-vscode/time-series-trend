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

cnx = mysql.connector.connect(**config)

    
cursor = cnx.cursor()

# read in CSV file to DataFrame
mrts_sales_data = r"C:\Users\Tola\Desktop\sample\Projects\Module8\MRTS.csv"
df = pd.read_csv(mrts_sales_data, delimiter=',')
df =df[['kind_of_business','month','year','sales']]

        
    
query = """INSERT INTO MRTS_sales (kind_of_business, month, year, sales)
                     VALUES (%s, %s, %s, %s)"""

for row in df.itertuples(index=False):
    cursor.execute(query, row)
    
cnx.commit()     



# print all the rows
for row in cursor.fetchall():
    print(row)
    
cursor.close()
cnx.close()