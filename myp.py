import mysql.connector as sqltor
from tkinter import*
from functools import partial
import random
mycon=sqltor.connect(host='localhost',user='root',passwd='')
global cur
cur=mycon.cursor()
root = Tk()
def back(uname):
    bac=Toplevel()
    bac.geometry('400x400+0+0')
    bac.title('Bus Ticket Booking')
    photo1= PhotoImage(file='Capture.GIF')
    Label(bac, image=photo1,bg="white").grid(row=0,column=0)
    bac_r = Label(bac)
    bac_r.grid(row=15,column=0)
    def hell1(uname):
        bac.withdraw()
        third(uname)
        partial(third,uname)
    def hell2():
        bac.withdraw()
        show()
        partial(show)
    def show():
        sh=Toplevel()
        sh.geometry('400x400+0+0')
        sh.title('Bus Ticket Booking')
        photo1= PhotoImage(file='Capture.GIF')
        Label(sh, image=photo1,bg="white").grid(row=0,column=0)
        sh_r = Label(sh)
        sh_r.grid(row=15,column=0)
        Label(sh,text="Enter Ticket Number:",font="Times").grid(row=1,column=0,sticky=W)
        s=StringVar()
        tn = Entry(sh, textvariable=s,width=25).grid(row=1, column=0,sticky=E)
        def m(s):
            sch=Toplevel()
            sh.withdraw()
            sch.geometry('400x400+0+0')
            sch.title('Booking Details')
            sch_r = Label(sch)
            sch_r.grid(row=15,column=0)
            s=s.get()
            try:
                cur.execute("select * from jd where tno={};".format(int(s)))
                data=cur.fetchall()
                if data==[]:
                    sch_r.config(text="No tickets booked with this ticket Number")
                else:
                    Label(sch,text="Ticket Number:").grid(row=1,column=0)
                    Label(sch,text="Traveller's Name:").grid(row=2,column=0)
                    Label(sch,text="Traveller's Age:").grid(row=3,column=0)
                    Label(sch,text="Gender:").grid(row=4,column=0)
                    Label(sch,text="Origin:").grid(row=5,column=0)
                    Label(sch,text="Destination:").grid(row=6,column=0)
                    Label(sch,text="Date:").grid(row=7,column=0)
                    Label(sch,text="Time:").grid(row=8,column=0)
                    Label(sch,text="Preference:").grid(row=9,column=0)
                    Label(sch,text="Seat Number:").grid(row=10,column=0)
                    Label(sch,text="Bus Code:").grid(row=11,column=0)
                    Label(sch,text="Fair:").grid(row=12,column=0)
                    tokra = Label(sch)
                    tokra.grid(row=1,column=2)  
                    tokrb = Label(sch)
                    tokrb.grid(row=2,column=2)
                    tokrc = Label(sch)
                    tokrc.grid(row=3,column=2)
                    tokrd = Label(sch)
                    tokrd.grid(row=4,column=2)
                    tokre = Label(sch)
                    tokre.grid(row=5,column=2)
                    tokrf = Label(sch)
                    tokrf.grid(row=6,column=2)
                    tokrg = Label(sch)
                    tokrg.grid(row=7,column=2)
                    tokrh = Label(sch)
                    tokrh.grid(row=8,column=2)
                    tokri = Label(sch)
                    tokri.grid(row=9,column=2)
                    tokrj = Label(sch)
                    tokrj.grid(row=10,column=2)
                    tokrk = Label(sch)
                    tokrk.grid(row=11,column=2)
                    tokrl = Label(sch)
                    tokrl.grid(row=12,column=2)
                    tokra.config(text=data[0][0])
                    tokrb.config(text=data[0][2])
                    tokrc.config(text=data[0][3])
                    tokrd.config(text=data[0][4])
                    tokre.config(text=data[0][5])
                    tokrf.config(text=data[0][6])
                    tokrg.config(text=data[0][7])
                    tokrh.config(text=data[0][8])
                    tokri.config(text=data[0][9])
                    tokrj.config(text=data[0][10])
                    tokrk.config(text=data[0][11])
                    tokrl.config(text=data[0][12])
            except:
                sch_r.config(text="Invalid ticket number")
            def l():
                sch.withdraw()
                sh.deiconify()
            def cv():
                sch.withdraw()
                login()
            a=Button(sch, text="Previous", command=l,bg="light cyan").grid(row=15, column=1)
            a=Button(sch, text="Logout", command=cv,bg="light cyan").grid(row=16, column=1)
            sch.mainloop()
        def cv():
            sh.withdraw()
            login()
        h=partial(m,s)
        a=Button(sh, text="Check", command=h,bg="light cyan").grid(row=2, column=0)
        a=Button(sh, text="Quit", command=sh.destroy,bg="light cyan").grid(row=2, column=0,sticky=E)
        a=Button(sh, text="Logout", command=cv,bg="light cyan").grid(row=2, column=0,sticky=W)
        sh.mainloop()
            
    c1=partial(hell1,uname)
    c2=partial(hell2)
    a=Button(bac, text="Book Ticket", command=c1,bg="light cyan").grid(row=5, column=0)    
    a=Button(bac, text="Check Booking", command=c2,bg="light cyan").grid(row=6, column=0)
    a=Button(bac, text="Quit", command=bac.destroy,bg="light cyan").grid(row=7, column=0)
    bac.mainloop()
    
def third(uname):
    thir=Toplevel()
    
    thir.geometry('500x500+0+0')
    thir.title("Select Your Journey")
    tok_r = Label(thir)  
    tok_r.grid(row=15, column=0)
    Label(thir,text="Enter Journey Details",font="Times").grid(row=0,column=1)
    Label(thir,text="Traveller's Name:").grid(row=2,column=0)
    Label(thir,text="Traveller's Age:").grid(row=3,column=0)
    Label(thir,text="Gender:").grid(row=4,column=0)
    Label(thir,text="Origin:").grid(row=5,column=0)
    Label(thir,text="Destination:").grid(row=6,column=0)
    Label(thir,text="Date:").grid(row=7,column=0)
    Label(thir,text="Time:").grid(row=8,column=0)
    Label(thir,text="Set Preferences:").grid(row=9,column=0)
    origin=destination=["Delhi","Mumbai","Chennai","Gorakhpur","Lucknow","Jaipur","Agra","Bangalore","Goa","Varanasi","Bhopal","Manali","Hyderabad","Patna","Jammu","Pune","Amritsar","Chandigarh","Kota","Leh"]
    vo=StringVar()
    vd=StringVar()
    vo.set("Delhi")
    vd.set("Mumbai")
    wo=OptionMenu(thir,vo,*origin).grid(row=5,column=1)
    wd=OptionMenu(thir,vd,*destination).grid(row=6,column=1)
    sp=["AC+Non-Sleeper","AC+Sleeper","Non-AC+Sleeper","Non-AC+Non-Sleeper"]
    vs=StringVar()
    vs.set("Non-AC+Sleeper")
    ws=OptionMenu(thir,vs,*sp).grid(row=9,column=1)
    ame=StringVar()
    ge=IntVar()
    ge.set(25)
    age=[x for x in range(1,131)]
    enname = Entry(thir, textvariable=ame,width=25).grid(row=2, column=1)  
    wa=OptionMenu(thir,ge,*age).grid(row=3,column=1)
    global vg
    vg=StringVar()
    vg.set("M")
    b=Radiobutton(thir,text='Male',variable=vg,font='none',value='M').grid(row=4,column=1,sticky=W)
    b=Radiobutton(thir,text='Female',variable=vg,font='none',value='F').grid(row=4,column=1,sticky=E)
    b=Radiobutton(thir,text='Third',variable=vg,font='none',value='T').grid(row=4,column=2)
    v1 = StringVar()
    v1.set("2020")
    year=["2020"]
    v2 = StringVar()
    v2.set("01")
    month=["01","02","03","04","05","06","07","08","09","10",'11',"12"]
    v3=StringVar()
    v3.set("01")
    days=["01","02","03","04","05","06","07","08","09","10",'11',"12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
    w1 = OptionMenu(thir,v1,*year)
    w1.grid(row=7,column=1,sticky=W)
    w2 = OptionMenu(thir, v2,*month)
    w2.grid(row=7,column=1)
    w3 = OptionMenu(thir,v3,*days)
    w3.grid(row=7,column=1,sticky=E)
    t=StringVar()
    t.set("16:00")
    ti=[str(x)+":00" for x in range(4,25,4)]
    w4 = OptionMenu(thir,t,*ti)
    w4.grid(row=8,column=1)
    def No():
        thir.deiconify()
        ch.withdraw()
    if len(str(v3))==1:
        dob=str(v1)+'-'+str(v2)+'-'+'0'+str(v3)
        cur.execute("select sno from jd where date='{}' and time='{}';".format(dob,t))
        l=cur.fetchall()
    def ch(ame,ge,vg,vo,vd,v1,v2,v3,t,vs):
        enname=str(ame.get())
        ge=int(ge.get())
        vg=str(vg.get())
        vo=str(vo.get())
        vd=str(vd.get())
        v1=str(v1.get())
        v2=str(v2.get())
        v3=str(v3.get())
        t=str(t.get())
        vs=str(vs.get())
        re=Toplevel()
        thir.withdraw()
        re.geometry('800x700+0+0')
        re.title('BUS TICKET BOOKING SYSTEM')
        tokr = Label(re)
        tokr.grid(row=14,column=2)
        try:
            cur.execute("create database if not exists bub;")
            cur.execute("use bub;")
            cur.execute('''create table if not exists jd
                        (tno int(6) primary key,
                        uname varchar(30) references members(uname),
                        name varchar(50),
                        age int(4) not null,
                        gender varchar(2) default 'M',
                        origin varchar(50) references bud(origin),
                        destination varchar(50) references bud(destination),
                        tdate date,
                        time time,
                        prefernce varchar(50) not null,
                        sno int(6) unique,
                        bcode varchar(6) references bud(bcode),
                        fair int(6) references bud(fair));''')
            try:
                dob=str(v1)+'-'+str(v2)+'-'+str(v3)
                cur.execute("select tno,sno from jd where tdate='{}' and time='{}' and origin='{}' and destination='{}';".format(dob,t,vo,vd))
                tn=cur.fetchall()
                if tn==[]:
                    ttn=random.randint(10000,99999)
                    cur.execute("select bcode,fair from bud where origin='{}' and destination='{}';".format(vo,vd))
                    u=cur.fetchall()
                    s=random.randint(1,30)
                    cur.execute("insert into jd values({},'{}','{}',{},'{}','{}','{}','{}','{}','{}',{},'{}',{});".format(ttn,uname,enname,ge,vg,vo,vd,dob,t,vs,s,str(u[0][0]),u[0][1]))
                    mycon.commit()
                    cur.execute("select * from jd where tno={}".format(ttn))
                    data=cur.fetchall()
                    Label(re,text="Ticket Number:").grid(row=1,column=0)
                    Label(re,text="Traveller's Name:").grid(row=2,column=0)
                    Label(re,text="Traveller's Age:").grid(row=3,column=0)
                    Label(re,text="Gender:").grid(row=4,column=0)
                    Label(re,text="Origin:").grid(row=5,column=0)
                    Label(re,text="Destination:").grid(row=6,column=0)
                    Label(re,text="Date:").grid(row=7,column=0)
                    Label(re,text="Time:").grid(row=8,column=0)
                    Label(re,text="Preference:").grid(row=9,column=0)
                    Label(re,text="Seat Number:").grid(row=10,column=0)
                    Label(re,text="Bus Code:").grid(row=11,column=0)
                    Label(re,text="Fair:").grid(row=12,column=0)
                    tokra = Label(re)
                    tokra.grid(row=1,column=2)  
                    tokrb = Label(re)
                    tokrb.grid(row=2,column=2)
                    tokrc = Label(re)
                    tokrc.grid(row=3,column=2)
                    tokrd = Label(re)
                    tokrd.grid(row=4,column=2)
                    tokre = Label(re)
                    tokre.grid(row=5,column=2)
                    tokrf = Label(re)
                    tokrf.grid(row=6,column=2)
                    tokrg = Label(re)
                    tokrg.grid(row=7,column=2)
                    tokrh = Label(re)
                    tokrh.grid(row=8,column=2)
                    tokri = Label(re)
                    tokri.grid(row=9,column=2)
                    tokrj = Label(re)
                    tokrj.grid(row=10,column=2)
                    tokrk = Label(re)
                    tokrk.grid(row=11,column=2)
                    tokrl = Label(re)
                    tokrl.grid(row=12,column=2)
                    tokra.config(text=data[0][0])
                    tokrb.config(text=data[0][2])
                    tokrc.config(text=data[0][3])
                    tokrd.config(text=data[0][4])
                    tokre.config(text=data[0][5])
                    tokrf.config(text=data[0][6])
                    tokrg.config(text=data[0][7])
                    tokrh.config(text=data[0][8])
                    tokri.config(text=data[0][9])
                    tokrj.config(text=data[0][10])
                    tokrk.config(text=data[0][11])
                    tokrl.config(text=data[0][12])
                else:
                    bti=[]
                    for i in tn:
                        bti.append(i[0])
                    bsn=[]
                    for i in tn:
                        bsn.append(i[1])
                        
                    
                    try:
                        
                        while True:
                            ttn=random.randint(10000,99999)
                            if ttn in bti:
                                continue  
                            else:
                                cur.execute("select bcode,fair from bud where origin='{}' and destination='{}';".format(vo,vd))
                                u=cur.fetchall()
                                s=random.randint(1,30)
                                if s in bsn:
                                    continue
                                    
                                else:
                                    cur.execute("insert into jd values({},'{}','{}',{},'{}','{}','{}','{}','{}','{}',{},'{}',{});".format(ttn,uname,enname,ge,vg,vo,vd,dob,t,vs,s,str(u[0][0]),u[0][1]))
                                    mycon.commit()
                                    cur.execute("select * from jd where tno={}".format(ttn))
                                    data=cur.fetchall()
                                    Label(re,text="Ticket Number:").grid(row=1,column=0)
                                    Label(re,text="Traveller's Name:").grid(row=2,column=0)
                                    Label(re,text="Traveller's Age:").grid(row=3,column=0)
                                    Label(re,text="Gender:").grid(row=4,column=0)
                                    Label(re,text="Origin:").grid(row=5,column=0)
                                    Label(re,text="Destination:").grid(row=6,column=0)
                                    Label(re,text="Date:").grid(row=7,column=0)
                                    Label(re,text="Time:").grid(row=8,column=0)
                                    Label(re,text="Preference:").grid(row=9,column=0)
                                    Label(re,text="Seat Number:").grid(row=10,column=0)
                                    Label(re,text="Bus Code:").grid(row=11,column=0)
                                    Label(re,text="Fair:").grid(row=12,column=0)
                                    tokra = Label(re)
                                    tokra.grid(row=1,column=2)  
                                    tokrb = Label(re)
                                    tokrb.grid(row=2,column=2)
                                    tokrc = Label(re)
                                    tokrc.grid(row=3,column=2)
                                    tokrd = Label(re)
                                    tokrd.grid(row=4,column=2)
                                    tokre = Label(re)
                                    tokre.grid(row=5,column=2)
                                    tokrf = Label(re)
                                    tokrf.grid(row=6,column=2)
                                    tokrg = Label(re)
                                    tokrg.grid(row=7,column=2)
                                    tokrh = Label(re)
                                    tokrh.grid(row=8,column=2)
                                    tokri = Label(re)
                                    tokri.grid(row=9,column=2)
                                    tokrj = Label(re)
                                    tokrj.grid(row=10,column=2)
                                    tokrk = Label(re)
                                    tokrk.grid(row=11,column=2)
                                    tokrl = Label(re)
                                    tokrl.grid(row=12,column=2)
                                    tokra.config(text=data[0][0])
                                    tokrb.config(text=data[0][2])
                                    tokrc.config(text=data[0][3])
                                    tokrd.config(text=data[0][4])
                                    tokre.config(text=data[0][5])
                                    tokrf.config(text=data[0][6])
                                    tokrg.config(text=data[0][7])
                                    tokrh.config(text=data[0][8])
                                    tokri.config(text=data[0][9])
                                    tokrj.config(text=data[0][10])
                                    tokrk.config(text=data[0][11])
                                    tokrl.config(text=data[0][12])
                                    break
                                    
                    except:
                
                        pass
                              
                                 
            except:
                tokr.config(text="all tickets are booked")

        except sqltor.errors.InterfaceError as ie:
            try:
                dob=str(v1)+'-'+str(v2)+'-'+str(v3)
                cur.execute("select tno,sno from jd where tdate='{}' and time='{}' and origin='{}' and destination='{}';".format(dob,t,vo,vd))
                tn=cur.fetchall()
                if tn==[]:
                    ttn=random.randint(10000,99999)
                    cur.execute("select bcode,fair from bud where origin='{}' and destination='{}';".format(vo,vd))
                    u=cur.fetchall()
                    s=random.randint(1,30)
                    cur.execute("insert into jd values({},'{}','{}',{},'{}','{}','{}','{}','{}','{}',{},'{}',{});".format(ttn,uname,enname,ge,vg,vo,vd,dob,t,vs,s,str(u[0][0]),u[0][1]))
                    mycon.commit()
                    cur.execute("select * from jd where tno={}".format(ttn))
                    data=cur.fetchall()
                    Label(re,text="Ticket Number:").grid(row=1,column=0)
                    Label(re,text="Traveller's Name:").grid(row=2,column=0)
                    Label(re,text="Traveller's Age:").grid(row=3,column=0)
                    Label(re,text="Gender:").grid(row=4,column=0)
                    Label(re,text="Origin:").grid(row=5,column=0)
                    Label(re,text="Destination:").grid(row=6,column=0)
                    Label(re,text="Date:").grid(row=7,column=0)
                    Label(re,text="Time:").grid(row=8,column=0)
                    Label(re,text="Preference:").grid(row=9,column=0)
                    Label(re,text="Seat Number:").grid(row=10,column=0)
                    Label(re,text="Bus Code:").grid(row=11,column=0)
                    Label(re,text="Fair:").grid(row=12,column=0)
                    tokra = Label(re)
                    tokra.grid(row=1,column=2)  
                    tokrb = Label(re)
                    tokrb.grid(row=2,column=2)
                    tokrc = Label(re)
                    tokrc.grid(row=3,column=2)
                    tokrd = Label(re)
                    tokrd.grid(row=4,column=2)
                    tokre = Label(re)
                    tokre.grid(row=5,column=2)
                    tokrf = Label(re)
                    tokrf.grid(row=6,column=2)
                    tokrg = Label(re)
                    tokrg.grid(row=7,column=2)
                    tokrh = Label(re)
                    tokrh.grid(row=8,column=2)
                    tokri = Label(re)
                    tokri.grid(row=9,column=2)
                    tokrj = Label(re)
                    tokrj.grid(row=10,column=2)
                    tokrk = Label(re)
                    tokrk.grid(row=11,column=2)
                    tokrl = Label(re)
                    tokrl.grid(row=12,column=2)
                    tokra.config(text=data[0][0])
                    tokrb.config(text=data[0][2])
                    tokrc.config(text=data[0][3])
                    tokrd.config(text=data[0][4])
                    tokre.config(text=data[0][5])
                    tokrf.config(text=data[0][6])
                    tokrg.config(text=data[0][7])
                    tokrh.config(text=data[0][8])
                    tokri.config(text=data[0][9])
                    tokrj.config(text=data[0][10])
                    tokrk.config(text=data[0][11])
                    tokrl.config(text=data[0][12])
                else:
                    bti=[]
                    for i in tn:
                        bti.append(i[0])
                    bsn=[]
                    for i in tn:
                        bsn.append(i[1])
                        
                    
                    try:
                        
                        while True:
                            ttn=random.randint(10000,99999)
                            if ttn in bti:
                                continue
                            else:
                                cur.execute("select bcode,fair from bud where origin='{}' and destination='{}';".format(vo,vd))
                                u=cur.fetchall()
                                s=random.randint(1,30)
                                if s in bsn:
                                    continue
                                    
                                else:
                                    cur.execute("insert into jd values({},'{}','{}',{},'{}','{}','{}','{}','{}','{}',{},'{}',{});".format(ttn,uname,enname,ge,vg,vo,vd,dob,t,vs,s,str(u[0][0]),u[0][1]))
                                    mycon.commit()
                                    
                                    cur.execute("select * from jd where tno={}".format(ttn))
                                    data=cur.fetchall()
                                    
                                    Label(re,text="Ticket Number:").grid(row=1,column=0)
                                    Label(re,text="Traveller's Name:").grid(row=2,column=0)
                                    Label(re,text="Traveller's Age:").grid(row=3,column=0)
                                    Label(re,text="Gender:").grid(row=4,column=0)
                                    Label(re,text="Origin:").grid(row=5,column=0)
                                    Label(re,text="Destination:").grid(row=6,column=0)
                                    Label(re,text="Date:").grid(row=7,column=0)
                                    Label(re,text="Time:").grid(row=8,column=0)
                                    Label(re,text="Preference:").grid(row=9,column=0)
                                    Label(re,text="Seat Number:").grid(row=10,column=0)
                                    Label(re,text="Bus Code:").grid(row=11,column=0)
                                    Label(re,text="Fair:").grid(row=12,column=0)
                                    tokra = Label(re)
                                    tokra.grid(row=1,column=2)  
                                    tokrb = Label(re)
                                    tokrb.grid(row=2,column=2)
                                    tokrc = Label(re)
                                    tokrc.grid(row=3,column=2)
                                    tokrd = Label(re)
                                    tokrd.grid(row=4,column=2)
                                    tokre = Label(re)
                                    tokre.grid(row=5,column=2)
                                    tokrf = Label(re)
                                    tokrf.grid(row=6,column=2)
                                    tokrg = Label(re)
                                    tokrg.grid(row=7,column=2)
                                    tokrh = Label(re)
                                    tokrh.grid(row=8,column=2)
                                    tokri = Label(re)
                                    tokri.grid(row=9,column=2)
                                    tokrj = Label(re)
                                    tokrj.grid(row=10,column=2)
                                    tokrk = Label(re)
                                    tokrk.grid(row=11,column=2)
                                    tokrl = Label(re)
                                    tokrl.grid(row=12,column=2)
                                    tokra.config(text=data[0][0])
                                    tokrb.config(text=data[0][2])
                                    tokrc.config(text=data[0][3])
                                    tokrd.config(text=data[0][4])
                                    tokre.config(text=data[0][5])
                                    tokrf.config(text=data[0][6])
                                    tokrg.config(text=data[0][7])
                                    tokrh.config(text=data[0][8])
                                    tokri.config(text=data[0][9])
                                    tokrj.config(text=data[0][10])
                                    tokrk.config(text=data[0][11])
                                    tokrl.config(text=data[0][12])
                                    break
                                    
                    except:
                        pass
            except:
                tokr.config(text="Sorry all are booked")

            
        else:
            try:
                dob=str(v1)+'-'+str(v2)+'-'+str(v3)
                cur.execute("select tno,sno from jd where tdate='{}' and time='{}' and origin='{}' and destination='{}';".format(dob,t,vo,vd))
                tn=cur.fetchall()
                if tn==[]:
                    ttn=random.randint(10000,99999)
                    cur.execute("select bcode,fair from bud where origin='{}' and destination='{}';".format(vo,vd))
                    u=cur.fetchall()
                    s=random.randint(1,30)
                    cur.execute("insert into jd values({},'{}','{}',{},'{}','{}','{}','{}','{}','{}',{},'{}',{});".format(ttn,uname,enname,ge,vg,vo,vd,dob,t,vs,s,str(u[0][0]),u[0][1]))
                    mycon.commit()
                    cur.execute("select * from jd where tno={}".format(ttn))
                    data=cur.fetchall()
                    Label(re,text="Ticket Number:").grid(row=1,column=0)
                    Label(re,text="Traveller's Name:").grid(row=2,column=0)
                    Label(re,text="Traveller's Age:").grid(row=3,column=0)
                    Label(re,text="Gender:").grid(row=4,column=0)
                    Label(re,text="Origin:").grid(row=5,column=0)
                    Label(re,text="Destination:").grid(row=6,column=0)
                    Label(re,text="Date:").grid(row=7,column=0)
                    Label(re,text="Time:").grid(row=8,column=0)
                    Label(re,text="Preference:").grid(row=9,column=0)
                    Label(re,text="Seat Number:").grid(row=10,column=0)
                    Label(re,text="Bus Code:").grid(row=11,column=0)
                    Label(re,text="Fair:").grid(row=12,column=0)
                    tokra = Label(re)
                    tokra.grid(row=1,column=2)  
                    tokrb = Label(re)
                    tokrb.grid(row=2,column=2)
                    tokrc = Label(re)
                    tokrc.grid(row=3,column=2)
                    tokrd = Label(re)
                    tokrd.grid(row=4,column=2)
                    tokre = Label(re)
                    tokre.grid(row=5,column=2)
                    tokrf = Label(re)
                    tokrf.grid(row=6,column=2)
                    tokrg = Label(re)
                    tokrg.grid(row=7,column=2)
                    tokrh = Label(re)
                    tokrh.grid(row=8,column=2)
                    tokri = Label(re)
                    tokri.grid(row=9,column=2)
                    tokrj = Label(re)
                    tokrj.grid(row=10,column=2)
                    tokrk = Label(re)
                    tokrk.grid(row=11,column=2)
                    tokrl = Label(re)
                    tokrl.grid(row=12,column=2)
                    tokra.config(text=data[0][0])
                    tokrb.config(text=data[0][2])
                    tokrc.config(text=data[0][3])
                    tokrd.config(text=data[0][4])
                    tokre.config(text=data[0][5])
                    tokrf.config(text=data[0][6])
                    tokrg.config(text=data[0][7])
                    tokrh.config(text=data[0][8])
                    tokri.config(text=data[0][9])
                    tokrj.config(text=data[0][10])
                    tokrk.config(text=data[0][11])
                    tokrl.config(text=data[0][12])
                else:
                    bti=[]
                    for i in tn:
                        bti.append(i[0])
                    bsn=[]
                    for i in tn:
                        bsn.append(i[1])
                        
                    try:
                        
                        while True:
                            ttn=random.randint(10000,99999)
                            if ttn in bti:
                                continue
                            
                                
                            else:
                                cur.execute("select bcode,fair from bud where origin='{}' and destination='{}';".format(vo,vd))
                                u=cur.fetchall()
                                s=random.randint(1,30)
                                if s in bsn:
                                    continue
                                    
                                else:
                                    cur.execute("insert into jd values({},'{}','{}',{},'{}','{}','{}','{}','{}','{}',{},'{}',{});".format(ttn,uname,enname,ge,vg,vo,vd,dob,t,vs,s,str(u[0][0]),u[0][1]))
                                    mycon.commit()
                                    print('l')
                                    cur.execute("select * from jd where tno={}".format(ttn))
                                    data=cur.fetchall()
                                    print('k')
                                    Label(re,text="Ticket Number:").grid(row=1,column=0)
                                    Label(re,text="Traveller's Name:").grid(row=2,column=0)
                                    Label(re,text="Traveller's Age:").grid(row=3,column=0)
                                    Label(re,text="Gender:").grid(row=4,column=0)
                                    Label(re,text="Origin:").grid(row=5,column=0)
                                    Label(re,text="Destination:").grid(row=6,column=0)
                                    Label(re,text="Date:").grid(row=7,column=0)
                                    Label(re,text="Time:").grid(row=8,column=0)
                                    Label(re,text="Preference:").grid(row=9,column=0)
                                    Label(re,text="Seat Number:").grid(row=10,column=0)
                                    Label(re,text="Bus Code:").grid(row=11,column=0)
                                    Label(re,text="Fair:").grid(row=12,column=0)
                                    print('lk')
                                    tokra = Label(re)
                                    tokra.grid(row=1,column=2)  
                                    tokrb = Label(re)
                                    tokrb.grid(row=2,column=2)
                                    tokrc = Label(re)
                                    tokrc.grid(row=3,column=2)
                                    tokrd = Label(re)
                                    tokrd.grid(row=4,column=2)
                                    tokre = Label(re)
                                    tokre.grid(row=5,column=2)
                                    tokrf = Label(re)
                                    tokrf.grid(row=6,column=2)
                                    tokrg = Label(re)
                                    tokrg.grid(row=7,column=2)
                                    tokrh = Label(re)
                                    tokrh.grid(row=8,column=2)
                                    tokri = Label(re)
                                    tokri.grid(row=9,column=2)
                                    tokrj = Label(re)
                                    tokrj.grid(row=10,column=2)
                                    tokrk = Label(re)
                                    tokrk.grid(row=11,column=2)
                                    tokrl = Label(re)
                                    tokrl.grid(row=12,column=2)
                                    print('kl')
                                    tokra.config(text=data[0][0])
                                    tokrb.config(text=data[0][2])
                                    tokrc.config(text=data[0][3])
                                    tokrd.config(text=data[0][4])
                                    tokre.config(text=data[0][5])
                                    tokrf.config(text=data[0][6])
                                    tokrg.config(text=data[0][7])
                                    tokrh.config(text=data[0][8])
                                    tokri.config(text=data[0][9])
                                    tokrj.config(text=data[0][10])
                                    tokrk.config(text=data[0][11])
                                    tokrl.config(text=data[0][12])
                                    print('kkl')
                                    break
                                    
                    except:
                        pass
                        
            except:
                tokr.config(text="Sorry all tickets are")
        def m():
            re.withdraw()
            thir.deiconify()
        def cv():
            re.withdraw()
            login()
        a=Button(re, text="Previous", command=m,bg="light cyan").grid(row=15, column=1)
        a=Button(re, text="Logout", command=cv,bg="light cyan").grid(row=16, column=1)
        re.mainloop()
    def mp():
        thir.withdraw()
        back()
    c=partial(ch,ame,ge,vg,vo,vd,v1,v2,v3,t,vs)
    a=Button(thir, text="Confirm Booking", command=c,bg="light cyan").grid(row=10, column=1)
    a=Button(thir, text="Previous", command=mp,bg="light cyan").grid(row=11, column=1)
    thir.mainloop()
def register():
    reg=Toplevel()
    root.withdraw()
    reg.geometry('800x700+0+0')  
    reg.title('BUS TICKET BOOKING SYSTEM')
    photo1= PhotoImage(file='Capture.GIF')                  
    Label(reg, image=photo1).grid(sticky=W)
    top_r=Label(reg)
    top_r.grid(row=12,column=0)
    Label(reg,text="-------------------Register---------------",fg='black',font="Times").grid(row=2,column=0,sticky=W+N+S+E)
    Label(reg,text='Name:       ',fg='black',font="none").grid(row=3,column=0)
    Label(reg,text='Username:       ',fg='black',font="none").grid(row=4,column=0)
    Label(reg,text='Date of Birth:           ',fg='black',font="none").grid(row=5,column=0)
    Label(reg,text='Gender:     ',fg='black',font="none").grid(row=6,column=0)
    global v
    v=StringVar()
    v.set("M")
    b=Radiobutton(reg,text='Male',variable=v,fg='black',font='none',value='M').grid(row=6,column=0,sticky=E)
    b=Radiobutton(reg,text='Female',variable=v,fg='black',font='none',value='F').grid(row=6,column=1,sticky=E)
    b=Radiobutton(reg,text='Third',variable=v,fg='black',font='none',value='T').grid(row=6,column=2)
    Label(reg,text='Number: ',fg='black',font="none").grid(row=7,column=0)
    Label(reg,text='Email:',fg='black',font="none").grid(row=8,column=0)
    Label(reg,text='Password:   ',fg='black',font="none").grid(row=9,column=0)
    Label(reg,text='Confirm Password:                  ',fg='black',font="none").grid(row=10,column=0)
    global na
    global un
    global dob
    global pd1
    global pd2
    global em
    global nu
    na=StringVar()
    un=StringVar()
    dob=StringVar()
    pd1=StringVar()
    pd2=StringVar()
    em=StringVar()
    nu=IntVar()
    nu.set("")
    global v1
    v1 = StringVar()
    v1.set("2000")
    year=[str(i) for i in range(1940,2011)]
    global v2
    v2 = StringVar()
    v2.set("01")
    month=["01","02","03","04","05","06","07","08","09","10",'11',"12"]
    global v3
    v3=StringVar()
    v3.set("1")
    days=[ str(x) for x in range(1,32)]
    w1 = OptionMenu(reg,v1,*year)
    w1.grid(row=5,column=0,sticky=E)
    w2 = OptionMenu(reg, v2,*month)
    w2.grid(row=5,column=1,sticky=W)
    w3 = OptionMenu(reg,v3,*days)
    w3.grid(row=5,column=2)
    entryna=Entry(reg,textvariable=na).grid(row=3,column=0,sticky=E)
    entryun=Entry(reg,textvariable=un).grid(row=4,column=0,sticky=E)
    #entrydob=Entry(reg,textvariable=dob,fg="grey").grid(row=5,column=0,sticky=E)
    entrynu=Entry(reg,textvariable=nu).grid(row=7,column=0,sticky=E)
    entryem=Entry(reg,textvariable=em).grid(row=8,column=0,sticky=E)
    entrypd1=Entry(reg, show="*",textvariable=pd1).grid(row=9,column=0,sticky=E)
    entrypd2=Entry(reg, show="*",textvariable=pd2).grid(row=10,column=0,sticky=E)
    def new1(a,u,v1,v2,v3,v,n,m,p1,p2):
        try:
            
            na=a.get()
            un=u.get()
            v1=v1.get()
            v2=v2.get()
            v3=v3.get()
            v=v.get()
            nu=n.get()
            em=m.get()
            pd=p1.get()
            ps=p2.get()
            try:
                if pd==ps:
                    if len(str(v3))==1:
                        dob=str(v1)+'-'+str(v2)+'-'+'0'+str(v3)
                        cur.execute('create database if not exists bub;')
                        cur.execute('use bub;')
                        cur.execute("create table if not exists members( name varchar(50) not null,uname varchar(20) unique key,dob date not null,gender char(2) default 'M',number bigint(11) primary key,email varchar(31) unique key,psswd varchar(16));")
                        mycon.commit()
                        
                        cur.execute("insert into members values('{}','{}','{}','{}',{},'{}','{}');".format(na,un,dob,v,nu,em,pd))
                        mycon.commit()
                        top_r.config(text='''You have registered successfully
                                             Now login to continue.''')
                    
                    else:
                        dob=str(v1)+'-'+str(v2)+'-'+str(v3)
            
                        cur.execute('create database if not exists bub;')
                        cur.execute('use bub;')
                        cur.execute("create table if not exists members( name varchar(50) not null,uname varchar(20) unique key,dob date not null,gender char(2) default 'M',number bigint(11) primary key,email varchar(31) unique key,psswd varchar(16));")
                        mycon.commit()
                        
                        cur.execute("insert into members values('{}','{}','{}','{}',{},'{}','{}');".format(na,un,dob,v,nu,em,pd))
                        mycon.commit()
                        top_r.config(text='''You have registered
                                             Now login to continue.''')
                    
                
                else:
                    top_r.config(text="Password doesn't match")
            except:
                top_r.config(text="Invalid Details Entered")
        except:
                top_r.config(text="Invalid Details Entered")
    def new2():
        reg.withdraw()
        login()
    new=partial(new1,na,un,v1,v2,v3,v,nu,em,pd1,pd2)
    a=Button(reg, text="REGISTER",command=new,bg="light cyan").grid(row=11, column=0,sticky=W)
    a=Button(reg, text="QUIT",command=reg.destroy,bg="light cyan").grid(row=11, column=0)
    a=Button(reg, text="LOGIN",command=new2,bg="light cyan").grid(row=11, column=0,sticky=E)
    reg.mainloop()
    
def login():
    top=Toplevel()
    root.withdraw()
    top.geometry('400x400+0+0')  
    top.title('BUS TICKET BOOKING SYSTEM')
    photo1= PhotoImage(file='Capture.GIF')                  
    Label(top, image=photo1).grid(sticky=W)
    Label(top,text="-------------------Log  In---------------",fg='black',font="Times").grid(row=2,column=0,sticky=W+N+S+E)
    Label(top,text='Username:                                                   ',fg='black',font="none").grid(row=5,column=0)
    Label(top,text='Password:                                                   ',fg='black',font="none").grid(row=6,column=0)

    #Entry sites---------------------------------------------
    tot_r = Label(top)  
  
    tot_r.grid(row=10, column=0)
    global uname
    uname = StringVar()  
    psswd = StringVar()
    entryNum1 = Entry(top, textvariable=uname).grid(row=5, column=0)  
    entryNum2 = Entry(top,show ='*', textvariable=psswd).grid(row=6, column=0)
    def add_r(tot_r,n1, n2):  
        num1 = n1.get() 
        num2 = n2.get()
        try:
            cur.execute("create database if not exists bub;")
            cur.execute("use bub;")
            cur.execute("create table if not exists members( name varchar(50) not null,uname varchar(30) unique key,dob date not null,gender char(2) default 'M',number bigint(11) primary key,email varchar(31) unique key,psswd varchar(16));")
            try:
                cur.execute('select uname from members where number=9839381444;')
                q=cur.fetchall()
                if q==[]:

                    cur.execute("insert into members values('Pravin Kumar Shukla','133aspravin','2003-03-01','M',9839381444,'133aspravin@gmail.com','bus');")
                    mycon.commit()
                    st="select uname,psswd from members where uname = '{}' and psswd = '{}';".format(num1,num2)
                    cur.execute(st)
                    ah=cur.fetchall()
                    if ah==[]:
                        tot_r.config("Invalid Username and/or Password")
                    else:
                        top.withdraw()
                        back(num1)
                        z=partial(back,num1)
            except sqltor.MySQLInterfaceError:
                st="select uname,psswd from members where uname= '{}' and psswd= '{}';".format(num1,num2)
                cur.execute(st)
                x=cur.fetchall()
                if x==[]:
                    tot_r.config(text="Invalid Username and/or Password")
                else:
                    top.withdraw()
                    back(num1)
                    z=partial(back,num1)
            else:
                st="select uname,psswd from members where uname= '{}' and psswd= '{}';".format(num1,num2)
                cur.execute(st)
                x=cur.fetchall()
                if x==[]:
                    tot_r.config(text="Invalid Username and/or Password")
                else:
                    top.withdraw()
                    back(num1)
                    z=partial(back,num1)
                
                        

        except sqltor.errors.InterfaceError as ie:
            cur.execute("create database if not exists bub;")
            cur.execute("use bub;")
            cur.execute("create table if not exists members( name varchar(50) not null,uname varchar(30) unique key,dob date not null,gender char(2) default 'M',number bigint(11) primary key,email varchar(31) unique key,psswd varchar(16));")
            try:
                print('f')
                cur.execute("insert into members values('Pravin Kumar Shukla','133aspravin','2003-03-01','M',9839381444,'133aspravin@gmail.com','bus');")
                mycon.commit()
                st="select uname,psswd from members where uname = '{}' and psswd = '{}';".format(num1,num2)
                cur.execute(st)
                ah=cur.fetchall()
                if ah==[]:
                    tot_r.config(text="Invalid Username and/or Password")
                else:
                    
                    top.withdraw()
                    back(num1)
                    z=partial(back,num1)
            except:
                st="select uname,psswd from members where uname= '{}' and psswd= '{}';".format(num1,num2)
                cur.execute(st)
                ah=cur.fetchall()
                if ah==[]:
                    tot_r.config(text="Invalid Username and/or Password")
                else:
                    top.withdraw()
                    back(num1)
                    z=partial(back,num1)
    def fg():
        root.deiconify()
        top.withdraw()
            
    call_add = partial(add_r,tot_r,uname,psswd)
    addCal = Button(top, text="LOGIN", command=call_add,bg="light cyan").grid(row=8, column=0,sticky=NW)
    a=Button(top, text="Quit", command=top.destroy,bg="light cyan").grid(row=8, column=0)
    a=Button(top, text="Main Menu", command=fg,bg="light cyan").grid(row=8, column=0,sticky=NE)
    top.mainloop()

root.geometry('500x400+0+0')  
root.title('BUS TICKET BOOKING SYSTEM')
photo1= PhotoImage(file='Capture.GIF')
Label(root, image=photo1,bg="white").grid(row=0,column=0)
a=Button(root, text="LOGIN", command=login,bg="light cyan").grid(row=5, column=0)
a=Button(root, text="REGISTER", command=register,bg="light cyan").grid(row=6, column=0)
a=Button(root, text="Quit", command=root.destroy,bg="light cyan").grid(row=7, column=0)

try:
    cur.execute("create database if not exists bub;")
    cur.execute("use bub;")
    cur.execute("create table if not exists bud(bcode int(6) primary key,origin varchar(50) not null,destination varchar(30),fair int(6));")
    try:
        origin=["Delhi","Mumbai","Chennai","Gorakhpur","Lucknow","Jaipur","Agra","Bangalore","Goa","Varanasi","Bhopal","Manali","Hyderabad","Patna","Jammu","Pune","Amritsar","Chandigarh","Kota","Leh"]
        destination=["Delhi","Mumbai","Chennai","Gorakhpur","Lucknow","Jaipur","Agra","Bangalore","Goa","Varanasi","Bhopal","Manali","Hyderabad","Patna","Jammu","Pune","Amritsar","Chandigarh","Kota","Leh"]
        fair=[500,660,370,420,630,820,960,870,1520,1240,1420,900,400,600,1800]
        for i in range(1,len(origin)+1):
            for j in range(1,len(destination)+1):
                if i!=j:
                    if len(str(j))==1:
                        j="0"+str(j)
                        cur.execute("insert into bud values( {},'{}','{}',{});".format(int(str(i)+str(j)),origin[i-1],destination[int(j)-1],fair[random.randint(0,14)]))
                        mycon.commit()
                    else:
                        cur.execute("insert into bud values( {},'{}','{}',{});".format(int(str(i)+str(j)),origin[i-1],destination[int(j)-1],fair[random.randint(0,14)]))
                        mycon.commit()
    except:
        pass

except sqltor.errors.InterfaceError as ie:
    cur.execute("create database if not exists bub;")
    cur.execute("use bub;")
    cur.execute("create table if not exists bud(bcode int(6) primary key,origin varchar(50) not null,destination varchar(30),fair int(6));")
    try:
        origin=["Delhi","Mumbai","Chennai","Gorakhpur","Lucknow","Jaipur","Agra","Bangalore","Goa","Varanasi","Bhopal","Manali","Hyderabad","Patna","Jammu","Pune","Amritsar","Chandigarh","Kota","Leh"]
        destination=["Delhi","Mumbai","Chennai","Gorakhpur","Lucknow","Jaipur","Agra","Bangalore","Goa","Varanasi","Bhopal","Manali","Hyderabad","Patna","Jammu","Pune","Amritsar","Chandigarh","Kota","Leh"]
        fair=[500,660,370,420,630,820,960,870,1520,1240,1420,900,400,600,1800]
        for i in range(1,len(origin)+1):
            for j in range(1,len(destination)+1):
                if i!=j:
                    cur.execute("insert into bud values({},'{}','{}',{});".format(int(str(i)+str(j)),origin[i-1],destination[j-1],fair[random.randint(1,15)]))
                    mycon.commit()
    except:
        print('h')
root.mainloop()
