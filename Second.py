import sqlite3 as st
conn=st.connect("Student_data.db")
conn.execute("""
     create table IF NOT Exists fees(
             Roll_no INT,
             Fees INT
             )
""")
cursors=conn.cursor()
cursors.execute("""
  insert into fees("Roll_no","Fees")VALUES
                (12234,23200),
                (122,1000),
                (11234,2000),
                (12234,3000),
                (1634,5000),
                (12344,7000),
                (0,8000)

""")
conn.commit()
conn.close()
