import os
from tkinter import *
import tkinter 
import tkinter.messagebox as msgbox
import tkinter as tk
from tkinter import ttk
import time
from datetime import datetime
from tkinter.tix import COLUMN
from typing import Protocol

root = tkinter.Tk()

root.title("Network Control Program")
root.resizable(True, True)
root.geometry("1920x1080")

user_id, password = StringVar(), StringVar()

#로그인 구현
def login_check():
    for i in range(1, 6):
        time.sleep(0.05)

        p_var.set(i)
        progressbar.update()
        print(p_var.get())

    if user_id.get() == "a" and password.get() == "b":
        msgbox.showinfo("Logged IN Successfully", "Logged IN Successfully")
        msgbox.showinfo("환영합니다.", "환영합니다" + " " + str(user_id.get())+ " " + "님.")
        
        now = datetime.now()

        f = open('d:\\logs\\' + 'Log' + '-' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) 
        + '-' + str(now.hour) + '-' + str(now.minute) + '-' + str(now.second) + ".txt", "w")
        f.write("접속 아이디: " + str(user_id.get()) + '\n' 
        + '접속 시간: ' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) 
        + '-' + str(now.hour) + '-' + str(now.minute) + '-' + str(now.second) )
        f.close

        #tap 네비게이션 구현
        notebook=tkinter.ttk.Notebook(root, width=1920, height=700)
        notebook.pack()

        tab1=tkinter.Frame(notebook)
        notebook.add(tab1, text="Firewall Controll Center")
        tab2=tkinter.Frame(notebook)
        notebook.add(tab2, text="Inbound/Outbound Rule Center")
        tab3=tkinter.Frame(notebook)
        notebook.add(tab3, text="Detection Attack Center")

        #tab1 기능 구현
        label1 = tkinter.Label(tab1)

        def F_on_btn():
            msgbox.showinfo("알림", "FireWall On 동작 확인됨")
            os.popen('NetSh Advfirewall set allprofiles state on').read()

        def F_off_btn():
            response = msgbox.askokcancel("확인/취소", "방화벽을 종료하실경우 해킹에 취약해질 수 있습니다.")
            if response == 1:
                os.popen('NetSh Advfirewall set allprofiles state off').read()
            else:
                msgbox.showerror("취소", "취소하였습니다.")
        
        def F_status_btn():
            response = msgbox.askokcancel("확인/취소", "FireWall Profiles Status 동작 확인됨")
            if response == 1:
                path = os.popen('Netsh Advfirewall show allprofiles').read()
                print(path)
                text = tkinter.Text(label1,  width=250, height=100)
                text.insert(tkinter.CURRENT, path)
                text.pack(pady=30)
            else:
                msgbox.showerror("취소", "취소하였습니다.")

        def F_reset():
            response = msgbox.askokcancel("확인/취소", "정말로 FireWall reset 동작을 실행 하시겠습니까?")
            if response == 1:
                os.popen('Netsh advfirewall reset').read()
            else:
                msgbox.showerror("취소", "취소하였습니다.")
            
        #FirewWall frame
        frame_firewall = Frame(tab1)
        frame_firewall.pack(side="top")

        #구분선 LabelFrame
        labelframe_firewall = LabelFrame(frame_firewall, relief="solid", bd=1, text="Firewall Option")
        labelframe_firewall.pack()

        #버튼 구현
        FONbtn = Button(labelframe_firewall, padx=10, pady=10 ,text="Firewall On Btn", command=F_on_btn)
        FONbtn.grid(row=0, column=0)

        FOFFbtn = Button(labelframe_firewall, padx=10, pady=10 ,text="Firewall Off Btn", command=F_off_btn)
        FOFFbtn.grid(row=0, column=1)

        FSbtn = Button(labelframe_firewall, padx=10, pady=10 ,text="Firewall Status Btn", command=F_status_btn)
        FSbtn.grid(row=0, column=2)

        FSbtn = Button(labelframe_firewall, padx=10, pady=10 ,text="Firewall Reset Btn", command=F_reset)
        FSbtn.grid(row=0, column=3)

        label1.pack()
        ################################################end tab1####################################################
        

        #tab2 기능 구현
        label2 = tkinter.Label(tab2)

        #tab2 frame
        frame_tab2 = Frame(tab2)
        frame_tab2.pack(side="top")

        #Make 구분선 LabelFrame
        labelframe_tab2 = LabelFrame(frame_tab2, relief="solid", bd=1, text="Make Inbound/Outbound Option")
        labelframe_tab2.pack()

        #Inbound/Outbound Option 구현
        protocol, name, dir, action, port, d_name = StringVar(), StringVar(), StringVar(), StringVar(), IntVar(), StringVar()

        def make_submit():
            if type(name) == tkinter.StringVar:
                if type(port) == tkinter.IntVar:
                    os.popen('netsh advfirewall firewall add rule name = "' + name.get() + '"' + ' dir = ' + dir.get() + ' action = ' + action.get() + 
                    ' protocol = ' + protocol.get() + ' localport = ' + str(port.get())).read()
                    msgbox.showinfo("알림", "IN/OUT Rule을 만들었습니다.")
                    path = os.popen('netsh advfirewall firewall show rule name = "' + name.get() + '"').read()
                    print(path)
                    global text
                    text = tkinter.Text(label2,  width=100, height=100)
                    text.insert(tkinter.CURRENT, path)
                    text.pack(pady=30)
                else:
                    msgbox.showerror("알림", "port는 항상 숫자여야 합니다.")
            else:
                msgbox.showerror("알림", "name은 항상 글자여야 합니다.")

        def delete_submit():
            if type(d_name) == tkinter.StringVar:
                response = msgbox.askokcancel("확인/취소", "정말로 삭제 하시겠습니까?")
                if response == 1:
                    os.popen('netsh advfirewall firewall delete rule name = "' + d_name.get() + '"')
                    msgbox.showinfo("알림", "삭제하였습니다.")
                    path = os.popen('netsh advfirewall firewall show rule name = "' + name.get() + '"').read()
                    text.insert(tkinter.CURRENT, path)
                    text.pack(pady=30)
                else:
                    msgbox.showerror("취소", "취소하였습니다.")

        tcp_btn = Radiobutton(labelframe_tab2, text="TCP", value="tcp", variable=protocol).grid(row=0, column=0)
        udp_btn = Radiobutton(labelframe_tab2, text="UDP", value="udp", variable=protocol).grid(row=0, column=1)

        in_btn = Radiobutton(labelframe_tab2, text="IN", value="in", variable=dir).grid(row=1, column=0)
        out_btn = Radiobutton(labelframe_tab2, text="OUT", value="out", variable=dir).grid(row=1, column=1)

        allow_btn = Radiobutton(labelframe_tab2, text="Allow", value="allow", variable=action).grid(row=2, column=0)
        block_btn = Radiobutton(labelframe_tab2, text="Block", value="block", variable=action).grid(row=2, column=1)

        ttk.Label(labelframe_tab2, text = "Name : ").grid(row = 3, column = 0, padx = 10, pady = 10)
        ttk.Entry(labelframe_tab2, textvariable = name).grid(row = 3, column = 1, padx = 10, pady = 10)

        ttk.Label(labelframe_tab2, text = "Port : ").grid(row = 4, column = 0, padx = 10, pady = 10)
        ttk.Entry(labelframe_tab2, textvariable = port).grid(row = 4, column = 1, padx = 10, pady = 10)

        submit_btn = Button(labelframe_tab2, text="Make", command=make_submit).grid(row = 5, column = 0, padx = 10, pady = 10)

        #Delete 구분선 LabelFrame
        labelframe_tab2 = LabelFrame(frame_tab2, relief="solid", bd=1, text="Delete Inbound/Outbound Option")
        ttk.Label(labelframe_tab2, text = "Name : ").grid(row = 0, column = 0, padx = 10, pady = 10)
        ttk.Entry(labelframe_tab2, textvariable = d_name).grid(row = 0, column = 1, padx = 10, pady = 10)
        d_submit_btn = Button(labelframe_tab2, text="Delete", command=delete_submit).grid(row = 1, column = 0, padx = 10, pady = 10)
        labelframe_tab2.pack()

        label2.pack()
        ################################################end tab2####################################################
        

        #tab3 기능 구현
        label3 = tkinter.Label(tab3)

        #tab3 frame
        frame_tab3 = Frame(tab3)
        frame_tab3.pack(side="top")

        #Make 구분선 LabelFrame
        SYNframe_tab3 = LabelFrame(frame_tab3, relief="solid", bd=1, text="Detection SYN Flooding")
        SYNframe_tab3.pack()

        ARPframe_tab3 = LabelFrame(frame_tab3, relief="solid", bd=1, text="Detection ARP Spoofing")
        ARPframe_tab3.pack()

        block = IntVar()

        def block_submit():
            scan = os.popen('netstat -na').read()
            scan_list = scan.split()
            del scan_list[:8]
            count = scan_list.count("SYN_RECV")
            block_cnt = block.get()
            print(type(block_cnt))
            print(type(count))
            if block_cnt < count:
                msgbox.showwarning("위험", "SYNFlooding 공격이 의심됩니다")
            else:
                msgbox.showinfo("알림", "SYNFlooding 공격이 없습니다")

        ttk.Label(SYNframe_tab3, text = "How many SYN request Block?: ").grid(row = 0, column = 0, padx = 10, pady = 10)
        ttk.Entry(SYNframe_tab3, textvariable = block).grid(row = 0, column = 1, padx = 10, pady = 10)
        submit_btn = Button(SYNframe_tab3, text="Let's block", command=block_submit).grid(row = 1, column = 0, padx = 10, pady = 10)

        # input_mac = StringVar()
        def arp_table_scan():
            
            for r in range(1, 6):
                time.sleep(0.5)

                p_var2.set(r)
                progressbar2.update()
                print(p_var2.get())

            scan_ip = os.popen('ipconfig').read()
            scan_arp = os.popen('arp -a').read()

            ip_scan_list = scan_ip.split('\n')
            arp_scan_list = scan_arp.split()

            ip_count = ip_scan_list.index('이더넷 어댑터 이더넷:')
            gateway_count = ip_count + 6
            del ip_scan_list[:gateway_count]
            gateway_info = ip_scan_list[0]
            gateway_ip = gateway_info[26:]

            arp_count = arp_scan_list.index(gateway_ip)

            arp_list = arp_scan_list[arp_count:]
            gateway_mac = arp_list[1]



            now = datetime.now()

            f2 = open('d:\\options\\' + 'Arp_Options-' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) 
            + '-' + str(now.hour) + '-' + str(now.minute) + '-' + str(now.second) + ".txt", "w")
            f2.write(gateway_ip + ' ' + gateway_mac)
            f2.close

            # if gateway_ip:
            #     if cmd_gateway_mac == gateway_mac:
            #         msgbox.showinfo('탐지되지 않음', 'arp 공격이 탐지되지 않았습니다')
            #     else:
            #         msgbox.showwarning('탐지됨', 'arp 공격이 탐지되었습니다.')
            #         os.popen('netsh interface ip delete arpcache').read()

        
        # ttk.Label(ARPframe_tab3, text = "Gateway Mac Address: ").grid(row = 0, column = 0, padx = 10, pady = 10)
        # ttk.Entry(ARPframe_tab3, textvariable = MAC).grid(row = 0, column = 1, padx = 10, pady = 10)
        arp_table_btn = Button(ARPframe_tab3, text="Detection ARP Spoofing ", command=arp_table_scan).grid(row = 1, column = 0, padx = 10, pady = 10)

        p_var2 = DoubleVar()
        progressbar2 = ttk.Progressbar(frame_tab3, maximum=5, length=200, variable=p_var2)
        progressbar2.pack(pady=5)
            

        label3.pack()
        ################################################end tab3####################################################
    else:
        msgbox.showerror("Check your Username/Password", "Check your Username/Password")

# 로그인 frame
frame_login = Frame(root)
frame_login.pack()

labelframe_login = LabelFrame(frame_login, relief="solid", bd=1, text="Login First")
labelframe_login.pack(side="top")

ttk.Label(labelframe_login, text = "Username : ").grid(row = 0, column = 0, padx = 10, pady = 10)
ttk.Label(labelframe_login, text = "Password : ").grid(row = 1, column = 0, padx = 10, pady = 10)
ttk.Entry(labelframe_login, textvariable = user_id).grid(row = 0, column = 1, padx = 10, pady = 10)
ttk.Entry(labelframe_login, textvariable = password).grid(row = 1, column = 1, padx = 10, pady = 10)
ttk.Button(labelframe_login, text = "Login", command = login_check).grid(row = 2, column = 1, padx = 10, pady = 10)

p_var = DoubleVar()
progressbar = ttk.Progressbar(root, maximum=5, length=200, variable=p_var)
progressbar.pack(pady=5)

root.mainloop()