import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="toor",
    database="dsce_college"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM student"
mycursor.execute(sql)
myresults = mycursor.fetchall()

li_1 = []
li_2 = []

for row_1 in myresults:
    li_1.append(row_1[0])

for row_3 in myresults:
    li_2.append(row_3[2])

j = 0
for i in range(len(li_2)-1):
    if li_2[i] == li_2[j+1]:
        print(li_1[i],li_2[i])
        print(li_1[j+1],li_2[j+1])
    j+=1


mycursor.close()
mydb.close()
