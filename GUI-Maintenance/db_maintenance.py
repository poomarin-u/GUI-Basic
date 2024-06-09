import sqlite3


conn = sqlite3.connect('maintenance.sqlite3') # สรา้ง conn เพื่อเชื่อมต่อกับฐานข้อมมูล



c = conn.cursor() # สร้าง cursor # ตัวที่เอาไว้สั่งคำสั่ง sql

c.execute(""" CREATE TABLE IF NOT EXISTS mt_workorder (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    tsid TEXT,
                    name TEXT,
                    Departmant TEXT,
                    machine TEXT,
                    problem TEXT,
                    number TEXT,
                    Phone TEXT ) """)


#CREATE
def insert_mtworkorder(tsid,name,Departmant,machine,problem,number,phone):
    #CREATE
    with conn:
        command = 'INSERT INTO mt_workorder VALUES (?,?,?,?,?,?,?,?)'
        c.execute(command,(None,tsid,name,Departmant,machine,problem,number,phone))
    conn.commit() #Save database 


# Raed
def viwe_mtworkorder():
    command = 'SELECT * FROM mt_workorder'
    c.execute(command)
    result = c.fetchall()
    return result


# Updete
def update_mtworkorder(tsid,field,newvalue):
    with conn:
        command = 'UPDATE mt_workorder SET {} = (?) WHERE tsid=(?)'.format(field)
        c.execute(command,(newvalue,tsid))
    conn.commit()


# Delete
def delete_mtworkorder(tsid):
    with conn:
        command = 'DELETE FROM mt_workorder WHERE tsid=(?)'
        c.execute(command,([tsid]))
    conn.commit()