import sqlite3 as st
conn=st.connect("Student_data.db")
conn.execute("""
     create table IF NOT Exists moiz(
             Name VARCHAR(30),
             Roll_no INT(5),
             Subject VARCHAR(50),
             Email_ID VARCHAR(50)
             )
""")
cursors=conn.cursor()
cursors.execute("""
  insert into moiz("Name","Roll_no","Subject","Email_ID")VALUES
                ("murtaza",11234,"English","rajaabdulmoiz019@gmail.com"),
                ("mufassa",17890,"PAKstudy","rajaabdulmoiz019@gmail.com"),
                ("Ali",16789,"Science","rajaabdulmoiz019@gmail.com"),
                ("maryam",15678,"English","rajaabdulmoiz019@gmail.com"),
                ("arshad",14567,"MAth","rajaabdulmoiz019@gmail.com"),
                ("momin",13456,"Urdu","rajaabdulmoiz019@gmail.com"),
                ("raja adan",12345,"MAth","rajaabdulmoiz019@gmail.com")

""")
conn.commit()
conn.close()
