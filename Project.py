import sqlite3 as st
conn=st.connect("Student_data.db")
cursors=conn.cursor()
while True:
    print("="*100)
    print("------------------------------Welcome to the DATABASE system Fetching------------------------")
    print("PRESS 1 for fetching by roll number.")
    print("PRESS 2 for fetching by name.")
    print("PRESS 3 for Adding data in DATABASE name,roll number,subject,Email.")
    print("PRESS 4 for Deleting  Data")
    print("PRESS 5 for UPDATING  Data")
    print("PRESS 6 for Checking  FEE/ Join used")
    print("PRESS 7 for exiting from program")
    print("By PRESSING 0 you go back")
    print("="*30)
    
    choose=int(input("Enter your Answer :"))
    match choose:
        case 1:
            while True:
                inter=int(input("Enter The Roll number :"))
                if inter==0:
                    break
                cursors.execute(" select * from moiz WHERE Roll_no=?",(inter,))
                data=cursors.fetchone()
                if data:
                  print(data)

        case 2:
            while True: 
                inter=input("Enter the name of student :")
                if inter=="0":
                    break
                cursors.execute("select * from moiz where Name=?",(inter,))
                data=cursors.fetchone()
                if data:
                 print(data)
        case 3:
            while True:
                NAME=input("Enter the name of student :")
                if NAME=="0":
                    break
                else:
                 ROLL_NUM=int(input("Enter the roll num of student :"))
                 SUBJECT=input("Enter the subject of student :")
                 EMAIL=input("Enter the email you want:")
                 conn.execute(""" 
                   insert into moiz("Name",Roll_no,"Subject","Email_ID")VALUES
                         (?,?,?,?)
                         """,(NAME,ROLL_NUM,SUBJECT,EMAIL))
                 conn.commit()
                 print(f"{NAME} has been Succesfully entered to data")
        case 4:
          while True:
             delete=int(input("Enter the Roll number to DELETE :"))
             if delete==0:
                break
             else:
               conn.execute("DELETE from moiz where Roll_no=?",(delete,))
               conn.commit()
               
               print(f"{delete} Deleted Succesfully")
        case 5:
          while True:
             Old_rollnum=int(input("Enter the roll num to update"))
             if Old_rollnum==0:
                break
             else:
              New_Name=input("Enter the name :")
              New_Subject=input("Enter the name of Subject :")
              New_Email=input("Enter the Email :")
              conn.execute("update moiz set Name=?,Subject=?,Email_ID=? where Roll_no=?",(New_Name,New_Subject,New_Email,Old_rollnum,))
              conn.commit()
              
              print("UPDATED SUCCESFULLY!")
        case 6:
          while True:
             print("-------------------------------FOR checking fee ----------------------------------------")
             rollnumber=int(input("Enetr the Roll number :"))
             if rollnumber==0:
                break
             else:
                cursors.execute("Select m.Roll_no,m.Name,f.Fees from moiz as m inner join fees as f on m.Roll_no=f.Roll_no where m.Roll_no=?",(rollnumber,))
                data=cursors.fetchone()
                if data:
                   print(data)
                else:
                   print("Invalid entry")

            
        case _:
            print("Exiting from the program")
            break
conn.close()
conn.close()
conn.close()
conn.close()