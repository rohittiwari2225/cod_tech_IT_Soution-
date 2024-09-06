import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

def addbook():
  bn = input("enter book name")
  ca = input("enter book code")
  t = input("total books")
  sa =  input("enter subject")
  data = (bn,ca,t,sa)
  sql = "insert into books values(%s,%s,%s,%s)"
  c = con.cursor()
  c.execute(sql,data)
  con.commit()
  print("<------------------------------------------------------>")
  print("Data Entered successfully")
  main()

def issue():
  n=input("enter name")
  r=input("enter reg_no")
  co= input("enter book code")
  d= input("enter date ")
  a = "insert into issue values(%s,%s,%s,%s)"
  data =(n,r,co,d)
  c=con.cursor()
  c.execute(a,data)
  con.commit()
  print("<-------------------------------------------------------------->")
  print("Book issued to:",n)
  bookup(co,-1)
def submitb():
  n=input("enter name")
  r=input("enter reg_no")
  co= input("enter book code")
  d= input("enter date ")
  a = "insert into issue values(%s,%s,%s,%s)"
  data =(n,r,co,d)
  c= con.cursor()
  con.commit()
  print("<-------------------------------------------------------------->")
  print("book submitted from:",n)
  bookup(co,1)
def bookup(co,u):
  a = "select TOTAL from books where BCODE = %s" 
  data =(co,)
  c= con.cursor()
  c.execute(a,data)
  myresult=c.fetchone()
  t=myresult=[0]+u
  sql ="update books set TOTAL= %s where BCODE=%s"
  d=(t,co)
  c.execute(sql,d)
  con.commit()
  main()
def dbooks():
  ac = input("enter book code") 
  a= "delete from books where BCODE=%s"
  data = (ac,)
  c=con.cursor()
  c.execute(a,data)
  con.commit()
  main()
def disbook():
  a="select * from books"   
  c=con.cursor()
  c.execute(a)
  myresult=c.fetchall()
  for i in myresult:
    print("book name ",i[0])
    print("book code",i[1])
    print("total",i[2])
    print("subject",i[3])
    print("------------------------------")
    main()

def main():
  print('''                      LIBRARY MANAGER 
  1.ADD BOOK
  2.ISSUE BOOK
  3.SUBMIT BOOK
  4.DELETE BOOK
  5.DISPLAY BOOK
  '''
  )
  choice =input("enter task no ")
  print("<-------------------------------->")
  if (choice=='1'):
    addbook()
  elif(choice=="2"):
    issue()
  elif(choice=='3'):
    submitb()
  elif(choice=='4'):
    dbooks() 
  elif(choice=='5'):
    disbook()
  else:
    print("wrong choice ")
    main()
def pswd():
  ps= input("enter passaward")
  if ps =="py143":
    main()
  else:
    print("wrong passaward")
    pswd()
pswd()           

    

