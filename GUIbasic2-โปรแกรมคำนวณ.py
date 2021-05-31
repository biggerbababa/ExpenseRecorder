from tkinter import *
from tkinter import ttk
# ttk is theme of Tk
import csv
from datetime import datetime
GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย By Big')
GUI.geometry('500x500+500+50')


# B1 = ttk.Button(GUI,text='Hello')
# B1.pack(ipadx=50,ipady=20) #.pack() ติดปุ่มเข้ากับ GUI หลัก

Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH, expand=1)

icon_t1 = PhotoImage(file='t1_expense.png')
icon_t2 = PhotoImage(file='t2_expenselist.png')


Tab.add(T1, text=f'{"ค่าใช้จ่าย":^{30}}',image=icon_t1,compound='left')
Tab.add(T2, text=f'{"ค่าใช้จ่ายทั้งหมด":^{30}}',image=icon_t2,compound='left')





F1 = Frame(T1)
#F1.place(x=100,y=50)
F1.pack()
days = {'Mon':'จันทร์',
       'Tue':'อังคาร',
       'Wed':'พุธ',
       'Thu':'พฤหัส',
       'Fri':'ศุกร์',
       'Sat':'เสาร์',
       'Sun':'อาทิตย์'}

def Save(event=None):
        expense = v_expense.get()
        price = v_price.get()
        quantity = v_quantity.get()
        total = int(price) *int(quantity)
        #.get()ดึงค่ามาจาก v_expense = StringVar()
        print('รายการ:{} ราคา: {}' .format(expense,price))
        print('จำนวน:{} รวมทั้งหมด: {} บาท' .format(quantity,total))
        #clear ข้อมูลเก่า
        v_expense.set('')
        v_price.set('')
        v_quantity.set('')

        #บันทึกข้อมูลลง csv อย่าลืม import ลง csv ด้วย
        today = datetime.now().strftime('%a') # days['Mon'] = 'จันทร์'
        dt = datetime.now() .strftime('%Y-%m-%d-{} %H:%M:%S')
        dt = days[today] + '-' + dt
        with open('savedata.csv','a',encoding='utf-8',newline='') as f:
        # with คือสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
        # 'a' การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
        #newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
                fw = csv.writer(f) #เป็นการสร้างฟังชั่นสำหรับเขียนข้อมูล
                data = [expense,price]
                fw.writerow(data)
                
        #ทำให้เคอเซอร์กลับไปตำแหน่งแรก E1
        E1.focus()        
#ทำให้สามารถกด enter ได้
GUI.bind('<Return>',Save) #ต้องเพิ่มใน def save(event=None) ด้วย


                
FONT1 = (None,20) # None เปลี่ยนเป็น 'Angsana New'

#------------image----------------

main_icon = PhotoImage(file='icon_money.png')

mainicon = Label(F1,image=main_icon)
mainicon.pack()







#---------------Text1--------------

L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack()
v_expense = StringVar()
#StringVar() ตัวแปรพิเศษสำหรับเก็บข้อมูลGUI
E1 = ttk.Entry(F1,textvariable=v_expense, font=FONT1)
E1.pack()
#----------------------------------

#---------------Text2--------------

L = ttk.Label(F1,text='ราคา (บาท)',font=FONT1).pack()
v_price = StringVar()
#StringVar() ตัวแปรพิเศษสำหรับเก็บข้อมูลGUI
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()
#----------------------------------
 
#---------------Text3--------------
L = ttk.Label(F1,text='จำนวน (ชิ้น)',font=FONT1).pack()
v_quantity = StringVar()
#StringVar() ตัวแปรพิเศษสำหรับเก็บข้อมูลGUI
E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack()

icon_b1 = PhotoImage(file='b_save.png')



B2 = ttk.Button(F1,text=f'{"Save": >{15}}',image=icon_b1,compound='left',command=Save)
B2.pack(ipadx=50,ipady=20,pady=20 )
#----------------------------------



GUI.mainloop()

