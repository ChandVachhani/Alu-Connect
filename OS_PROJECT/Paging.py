from tkinter import *
from tkinter.ttk import Combobox
from queue import Queue
from tkinter import messagebox as mbox
import xlwt 
from xlwt import Workbook 
from paging_algo import lru,opr,fifo

ex_qu=[]
ex_size=[]
ex_page_faults=[]
ex_ans=[]
ex_str=[]
ex_algo=[]
ex_que_size=[]

def on_closing():
    if mbox.askokcancel("Quit", "Do you want to quit?"):
        wb = Workbook()
        style = xlwt.easyxf('font: bold 1, color red;') 
        sheet1 = wb.add_sheet('Sheet 1')
        sheet1.write(0,0,'Algorithm',style)
        sheet1.write(0,1,'Frame_Size',style)
        sheet1.write(0,2,'String_Length',style)
        sheet1.write(0,3,'process_String',style)
        sheet1.write(0,4,'Page_Faults',style)
        sheet1.write(0,5,'Page_Hit',style)
        sheet1.write(0,6,'String',style)
        cnt=2
        for i in ex_algo:
            sheet1.write(cnt,0,i)
            cnt=cnt+1
        cnt=2
        for i in ex_size:
            sheet1.write(cnt,1,i)
            cnt=cnt+1
        cnt=2
        for i in ex_que_size:
            sheet1.write(cnt,2,i)
            cnt=cnt+1
        cnt=2
        for i in ex_qu:
            sheet1.write(cnt,3,i)
            cnt=cnt+1
        cnt=2
        for i in ex_page_faults:
            sheet1.write(cnt,4,i)
            cnt=cnt+1
        cnt=2
        for i in ex_ans:
            sheet1.write(cnt,5,i)
            cnt=cnt+1
        cnt=2
        for i in ex_str:
            sheet1.write(cnt,6,i)
            cnt=cnt+1
        wb.save('Paging.xls')
        paging.destroy()


def get_values():
    mem_size = ""
    algo_no = ""
    str2 = ""
    temp_str=""
    process_string = ""
    final = ""
    mem_size = var1.get()
    algo_no = var2.get()
    process_string = var3.get()
    temp_str=process_string
    if process_string == "":
        mbox.showerror('Error', 'Please Enter Required Information!!')
    elif process_string.isdigit():
        if mem_size == "" or algo_no == "":
            mbox.showerror('Error', 'Please Enter Required Information!!')
        else:
            process_string = list(process_string)
            for i in range(0, len(process_string)):
                process_string[i] = int(process_string[i])
            if algo_no == "fifo":
                ans, str2 = fifo(process_string, len(process_string), int(mem_size))
            elif algo_no == "lru":
                ans, str2 = lru(process_string, len(process_string), int(mem_size))
            elif algo_no == "opr":
                ans, str2 = opr(process_string, len(process_string), int(mem_size))
            ex_final=str2
            temp = min(125, len(str2))
            for i in range(0, temp):
                final += str2[i]
        ans1 = len(process_string) - ans
        lbl1.configure(text=ans)
        lbl2.configure(text=ans1)
        lbl3.configure(text=final)
        ex_size.append(mem_size)
        ex_qu.append(temp_str)
        ex_que_size.append(len(temp_str))
        ex_algo.append(algo_no.upper())
        ex_page_faults.append(ans)
        ex_ans.append(ans1)
        ex_str.append(ex_final)

    else:
        if mem_size == "" or algo_no == "":
            mbox.showerror('Error', 'Please Enter Required Information!!')
        else:
            mbox.showinfo('Error', 'Process String Should Contain Numbers only!!')


def startAlgo():
    global var1
    global var2
    global var3
    global lbl1
    global lbl2
    global lbl3
    label = Label(
        paging,
        text="Page Replacement Algorithms",
        font=("Arial Bold", 50),
        width=100,
        bg="Bisque",
        fg="darkred",
        pady=30)
    label.pack()
    lb1 = Label(
        paging,
        text="Enter Frame Size       : ",
        font=("Arial Bold", 20),
        bg="linen",
        fg="darkred")
    lb2 = Label(paging,
                text="Enter Algorithm         : ",
                font=("Arial Bold", 20),
                bg="linen",
                fg="darkred")
    lb3 = Label(paging,
                text="Enter Process String  :  ",
                font=("Arial Bold", 20),
                bg="linen",
                fg="darkred")
    lb1.place(x=50, y=150)
    lb2.place(x=50, y=200)
    lb3.place(x=50, y=360)

    var1 = StringVar()
    data = (
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
    ms = Combobox(paging, values=data, textvariable=var1, font=("Arial Bold", 20), width=19, state="readonly")
    ms.place(x=370, y=150)

    var2 = StringVar()
    var2.set("First In First Out")
    fifo = Radiobutton(paging, text="First In First Out", variable=var2, value="fifo", bg="linen", fg="darkred",
                       font=("Arial Bold", 15))
    lru = Radiobutton(paging, text="Least Recently Used", variable=var2, value="lru", bg="linen", fg="darkred",
                      font=("Arial Bold", 15))
    opt = Radiobutton(paging, text="Optimal Page Replacement", variable=var2, value="opr", bg="linen", fg="darkred",
                      font=("Arial Bold", 15))
    fifo.place(x=370, y=200)
    lru.place(x=370, y=250)
    opt.place(x=370, y=300)

    var3 = StringVar()
    al = Entry(paging, textvariable=var3, width=20, font=("Arial Bold", 20)).place(x=370, y=360)

    btn = Button(paging,
                 text="Calculate",
                 font=("Arial Bold", 18),
                 bg="darkred",
                 fg="Bisque",
                 cursor="hand2",
                 command=get_values)
    btn.pack(pady=(270, 20))

    t1 = Label(paging,
               text="Page Fault : ",
               font=("Arial Bold", 22),
               bg="Bisque",
               width=100,
               height=1,
               fg="darkred",
               pady=7
               )
    t1.pack()
    t2 = Label(paging,
               text="Page Hit     : ",
               font=("Arial Bold", 22),
               bg="Bisque",
               width=100,
               height=1,
               fg="darkred",
               pady=7
               )
    t2.pack()
    lbl1 = Label(paging,
                 text="0",
                 font=("Arial Bold", 22),
                 bg="Bisque",
                 fg="darkred")
    lbl1.place(x=620, y=490)
    lbl2 = Label(paging,
                 text="0",
                 font=("Arial Bold", 22),
                 bg="Bisque",
                 fg="darkred")
    lbl2.place(x=620, y=540)
    lbl3 = Label(paging,
                 text="",
                 font=("Arial Bold", 15),
                 bg="Bisque",
                 fg="darkred",
                 width=85,
                 height=1,
                 pady=10
                 )
    lbl3.place(x=0, y=585)


def destroyHome():
    label.destroy()
    cal_instruction.destroy()
    btn_cal.destroy()
    about.destroy()
    startAlgo()


paging = Tk()
paging.geometry("1000x650")
paging.configure(bg="linen")
paging.resizable(0, 0)
paging.iconbitmap('i1.ico')
paging.title("Page Replacement Algorithms")

label = Label(
    paging,
    text="Page Replacement Algorithms",
    font=("Arial Bold", 50),
    width=100,
    bg="Bisque",
    fg="darkred",
    pady=30
)
label.pack()

cal_instruction = Label(
    paging,
    text="Read How To Calculate Page Replacement Algorithms\n & \nClick Here To Calculate It.",
    bg="linen",
    font=("Arial Bold", 20),
    justify="center",
    pady=30
)
cal_instruction.pack()
btn_cal = Button(
    paging,
    text="Calculate",
    font=("Arial Bold", 35),
    command=destroyHome,
    width=10,
    height=1,
    bg="darkred",
    fg="Bisque",
    cursor="hand2")
btn_cal.pack(pady=(10, 20))

about = Label(
    paging,
    text="Enter Paging Replacement Algorithm Which you want Calculate, \nEnter Process String and Size of Main Memory.\nAnd then Click on Calculate Button.",
    width=100,
    height=50,
    font=("Arial Bold", 20),
    bg="Bisque",
    fg="darkred",
    pady=30
)
about.pack()

paging.protocol("WM_DELETE_WINDOW", on_closing)
paging.mainloop()