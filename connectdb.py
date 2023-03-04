import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('complaint.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS customerdetail')
print("table dropped successfully");
# create table again
conn.execute('CREATE TABLE customerdetail(complaint_ID TEXT PRIMARY KEY,date_received TEXT, submitted TEXT, issue TEXT, timely_response TEXT)')
print("table created successfully");

# open the file to read it into the database
with open('customercomplaint/Consumer_Complaints (1) (2).csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        complaint_ID= (row[17])
        date_received = row[0]
        submitted = row[12]
        issue = row[3]
        timely_response = row[15]

        cur.execute('INSERT INTO customerdetail VALUES (?,?,?,?,?)', (complaint_ID,date_received,submitted,issue,timely_response))
        conn.commit() 

        

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS bankdetail')
print("table dropped successfully");
# create table again
conn.execute('CREATE TABLE bankdetail(ids INTEGER PRIMARY KEY AUTOINCREMENT, complaint_ID TEXT,products TEXT , subproducts TEXT,company_name TEXT,company_response TEXT)')
print("table created successfully");

# open the file to read it into the database
with open('customercomplaint/Consumer_Complaints (1) (2).csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        complaint_ID = row[17] 
        products = row[1]
        subproducts = row[2]
        company_name = row[7]
        company_response = row[14]
        
        cur.execute('INSERT INTO bankdetail VALUES (NULL,?,?,?,?,?)', (complaint_ID,products,subproducts,company_name,company_response))
        conn.commit()

print("data parsed successfully");
conn.close()

        
        