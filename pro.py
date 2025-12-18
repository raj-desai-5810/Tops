import csv
import datetime

with open("pro.csv", "w", newline="") as f:
    line = csv.writer(f)
    line.writerow(["name", "age", "con", "gdr", "email", "vacc", "date", "time"])

    for i in range(5):
        name = input("Enter Your Name : ")
        age = int(input("Enter age : "))
        con = int(input("Enter contact no : "))
        gdr = input("Enter gender : ")
        email = input("Enter email : ")
        vacc = input("Enter vaccine dose : ")

        line.writerow([name, age, con, gdr, email, vacc, datetime.datetime.now().date(), datetime.datetime.now().time()])

print("ok")