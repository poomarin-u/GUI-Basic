from tkinter import*
from tkinter import ttk # import Tk เพิ่มเติม เพื่อรูปแบบความสวยงาม
from tkinter import messagebox

# เก็บ CSV
#import csv
from datetime import datetime

# DATABASE
from db_maintenance import *


# def writecsv(record_list):
#     with open('data.csv','a',newline='',encoding=('utf-8')) as file:
#         fw = csv.writer(file)
#         fw.writerow(record_list)

GUI = Tk()
GUI.geometry('800x600+50+50')
GUI.title('Maintenanec by SBI')

# Font 
font1 = font=('angsna new',14,'bold')
font2 = font=('angsna new',12,'bold')
font3 = font=('angsna new',12)

# TAB
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
Tab.add(T1,text='ใบแจ้งซ่อม')
Tab.add(T2,text='ดูใบแจ้งซ่อม')
Tab.add(T3,text='สรุปแจ้งซ่อม')
Tab.pack(fill=BOTH,expand=1)




#Widget
# หัวเรื่อง ใบแจ้งซ่อม
L = ttk.Label(T1,text='ใบแจ้งซ่อม',font=font1)
L.place(x=150,y=10)

# ชื่อผู้แจ้ง
L = ttk.Label(T1,text='ชื่อผู้แจ้ง :',font=font2)
L.place(x=10,y=50)
V_name = StringVar()  # StringVar() ตัวแปรพิเศษใช้กับ T1
E1 = ttk.Entry(T1,textvariable=V_name,font=font3)
E1.place(x=150,y=50)

# แผนก
L = ttk.Label(T1,text='แผนก :',font=font2)
L.place(x=10,y=90)
V_Departmant = StringVar()
E2 = ttk.Entry(T1,textvariable=V_Departmant,font=font3)
E2.place(x=150,y=90)


# อุปกรณ์/เครื่อง
L = ttk.Label(T1,text='อุปกรณ์/เครื่อง :',font=font2)
L.place(x=10,y=130)
V_Machine = StringVar()
E3 = ttk.Entry(T1,textvariable=V_Machine,font=font3)
E3.place(x=150,y=130)

# อาการเสีย
L = ttk.Label(T1,text='อาการเสีย :',font=font2)
L.place(x=10,y=170)
V_Problem = StringVar()
E4 = ttk.Entry(T1,textvariable=V_Problem,font=font3)
E4.place(x=150,y=170)

# รหัสเครื่อง/อุปกรณ์
L = ttk.Label(T1,text='รหัสเครื่อง/อุปกรณ์ :',font=font2)
L.place(x=10,y=210)
V_Number = StringVar()
E5 = ttk.Entry(T1,textvariable=V_Number,font=font3)
E5.place(x=150,y=210)

# เบอร์โทร
L = ttk.Label(T1,text='เบอร์โทร :',font=font2)
L.place(x=10,y=250)
V_Call = StringVar()
E6 = ttk.Entry(T1,textvariable=V_Call,font=font3)
E6.place(x=150,y=250)


def save():
    name = V_name.get()
    Departmant = V_Departmant.get()
    machine = V_Machine.get()
    problem = V_Problem.get()
    number = V_Number.get()
    Phone = V_Call.get()

    text = 'ชื่อผู้แจ้ง:'+ name +'\n' # '\n' คือขั้นบรรทัดใหม่
    text = text + 'แผนก:'+ Departmant +'\n'
    text = text + 'เครื่อง/อุปกรณ์:'+ machine +'\n'
    text = text + 'ปัญหา/อาการ:'+  problem +'\n'
    text = text + 'รหัสเครื่อง/อุปกรณ์:'+ number +'\n'
    text = text + 'เบอร์โทร:'+ Phone +'\n'

    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tsid = str(int(datetime.now().strftime('%Y%m%d%H%M%S')) + 114152147165)
    insert_mtworkorder(tsid,name,Departmant,machine,problem,number,Phone)

    V_name.set('')
    V_Departmant.set('')
    V_Machine.set('')
    V_Problem.set('')
    V_Number.set('')
    V_Call.set('')
    update_table()



    #datalist = [dt,name,Departmant,machine,problem,number,Phone]
    #writecsv(datalist)    
    #messagebox.showinfo('กำลังบันทึกข้อมูล...',text)

B = ttk.Button(T1,text='บันทึกใบแจ้งซ่อม',command=save)
B.place(x=250,y=330)


###   TAB2    #######################################################################
header = ['TSID','ชื่อ','แผนก','อุปกรณ์','อาการเสีย','หมายเลข','เบอร์โทรผู้แจ้ง']
headerw = [100,100,100,100,150,100,150]

mtworkorderlist = ttk.Treeview(T2,columns=header,show='headings',height=20)
mtworkorderlist.pack()


### ปรับ Style ตราง
style = ttk.Style()
style.configure('Treeview.Heading',padding=(5,5),font=('Angsana New',16,'bold'))
style.configure('Treeview',rowheight=25,font=('Angsana New',14))

for h,w in zip(header,headerw):
    # h='TSID' , W=50 ----> h='ชื่อ' w=100
    mtworkorderlist.heading(h,text=h)
    mtworkorderlist.column(h,width=w,anchor='center')
mtworkorderlist.column('TSID',anchor='w')

#mtworkorderlist.insert('','end',values=['A','B','C','D','E','F','G'])
def update_table():
    mtworkorderlist.delete(*mtworkorderlist.get_children()) #clear ข้อมูลเก่า
    data =viwe_mtworkorder()
    #print(data)
    for d in data:
        d = list(d) #แปลง Tuper เป็น list
        del d[0] #ลบ ID จาก database ออก
        mtworkorderlist.insert('','end',values=d)

### หน้าสำหรับแก้ไขข้อความ

def EditPage_mtworkorder(event=None):
    select = mtworkorderlist.selection()
    output = mtworkorderlist.item(select)
    op = output['values']

    tsid = op[0]
    t_name = op[1]
    t_Departmant = op[2]
    t_machine = op[3]
    t_problem = op[4]
    t_number = op[5]
    t_Phone = '0{}'.format(op[6])


    GUI2 = Toplevel()
    GUI2.title('หน้าแก้ไขข้อมูลใบแจ้งซ่อม')
    GUI2.geometry('500x500')

    #Widget
    # หัวเรื่อง ใบแจ้งซ่อม
    L = ttk.Label(GUI2,text='ใบแจ้งซ่อม',font=font1)
    L.place(x=150,y=10)

    # ชื่อผู้แจ้ง
    L = ttk.Label(GUI2,text='ชื่อผู้แจ้ง :',font=font2)
    L.place(x=10,y=50)
    V_name2 = StringVar()  # StringVar() ตัวแปรพิเศษใช้กับ GUI2
    V_name2.set(t_name)
    E1 = ttk.Entry(GUI2,textvariable=V_name2,font=font3)
    E1.place(x=150,y=50)

    # แผนก
    L = ttk.Label(GUI2,text='แผนก :',font=font2)
    L.place(x=10,y=90)
    V_Departmant2 = StringVar()
    V_Departmant2.set(t_Departmant)
    E2 = ttk.Entry(GUI2,textvariable=V_Departmant2,font=font3)
    E2.place(x=150,y=90)


    # อุปกรณ์/เครื่อง
    L = ttk.Label(GUI2,text='อุปกรณ์/เครื่อง :',font=font2)
    L.place(x=10,y=130)
    V_Machine2 = StringVar()
    V_Machine2.set(t_machine)
    E3 = ttk.Entry(GUI2,textvariable=V_Machine2,font=font3)
    E3.place(x=150,y=130)

    # อาการเสีย
    L = ttk.Label(GUI2,text='อาการเสีย :',font=font2)
    L.place(x=10,y=170)
    V_Problem2 = StringVar()
    V_Problem2.set(t_problem)
    E4 = ttk.Entry(GUI2,textvariable=V_Problem2,font=font3)
    E4.place(x=150,y=170)

    # รหัสเครื่อง/อุปกรณ์
    L = ttk.Label(GUI2,text='รหัสเครื่อง/อุปกรณ์ :',font=font2)
    L.place(x=10,y=210)
    V_Number2 = StringVar()
    V_Number2.set(t_number)
    E5 = ttk.Entry(GUI2,textvariable=V_Number2,font=font3)
    E5.place(x=150,y=210)

    # เบอร์โทร
    L = ttk.Label(GUI2,text='เบอร์โทร :',font=font2)
    L.place(x=10,y=250)
    V_Call2 = StringVar()
    V_Call2.set(t_Phone)
    E6 = ttk.Entry(GUI2,textvariable=V_Call2,font=font3)
    E6.place(x=150,y=250)


    def edit_save():
        name = V_name2.get()
        Departmant = V_Departmant2.get()
        machine = V_Machine2.get()
        problem = V_Problem2.get()
        number = V_Number2.get()
        Phone = V_Call2.get()

        update_mtworkorder(tsid,'name',name)
        update_mtworkorder(tsid,'Departmant',Departmant)
        update_mtworkorder(tsid,'machine',machine)
        update_mtworkorder(tsid,'problem',problem)
        update_mtworkorder(tsid,'number',number)
        update_mtworkorder(tsid,'Phone',Phone)

        update_table()
        GUI2.destroy()

    B = ttk.Button(GUI2,text='บันทึกใบแจ้งซ่อม',command=edit_save)
    B.place(x=250,y=330)




    GUI2.mainloop()
mtworkorderlist.bind('<Double-1>',EditPage_mtworkorder)





### Startup
update_table()

GUI.mainloop()
