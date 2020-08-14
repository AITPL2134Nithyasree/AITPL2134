import mysql.connector
#from mysql.connector import *
con = mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()
def creat_table():
    c.execute("create table nithya_employee(emp_id varchar(10),emp_name varchar(20),salary varchar(10))")
def insert_table(id,name,sal):
    c.execute("insert into nithya_employee values(%s,%s,%s)",(id,name,sal))
    con.commit()
def select_table():
    c.execute('select * from nithya_employee')
    data=c.fetchall()
    for row in data:
        print(row)
def delet_row(id):
    c.execute("DELETE FROM nithya_employee WHERE emp_id={0}".format(id))
    con.commit()
def update_salary(id,sal):
    c.execute("UPDATE nithya_employee SET salary={0} WHERE emp_id={1}".format(sal,id))
    con.commit()
'''N=int(input("Enter how many employees are there:"))
details=[]
print("Employee details as:emp_id emp_name salary:")
for i in range(N):
    l=[i for i in input().split()]
    details.append(l)
#creat_table()
for i in details:
    insert_table(i[0],i[1],i[2])'''

select_table()
print("Enter the the id of employee you want to delet:")
id=input()
delet_row(id)
select_table()
#print("Enter id of employee to whome you want to update salary and updated salary:")
#id,sal=input().split()
#update_salary(id,sal)
#select_table()

c.close()
con.close()
