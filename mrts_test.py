import csv

# Open File
with open(r"C:\Users\Tola\Desktop\sample\Projects\Module8\MRTS test.csv") as csv_file:
    
    # read csv file
    csv_reader = csv.reader(csv_file, delimiter = ',')
    
    # loop through data
    for row in csv_reader:
        print(row)