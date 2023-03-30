import tkinter as tk
import requests
from bs4 import BeautifulSoup
def getdata():
    response=requests.get("https://myself-bbs.com/portal.php")
    soup=BeautifulSoup(response.text,"html.parser")
    result=soup.find_all("div",class_="module cl xl xl1")
    week=[]
    for i in range(7):
        day=[]
        detail=result[i].select("font")
        d=1
        for time in detail:
            if(d%3==1):
                name=time.getText()
            elif(d%3==0):
                channel=time.getText()
                d=0
                day.append((name,channel))
                
            d=d+1
        week.append(day)
    return week
def switch_1():
    task(1)
def switch_2():
    task(2)
def switch_3():
    task(3)
def switch_4():
    task(4)
def switch_5():
    task(5)
def switch_6():
    task(6)
def switch_7():
    task(7)
def task(w):
    
    
    window = tk.Tk()
    window.title('動漫列表')
    window.geometry('420x600')
    window.configure(background='white')
    
    week=getdata()
    
    for t in range(len(week[w-1])):
        
        test=tk.Label(window,text=week[w-1][t][0])
        test.place(x=80,y=30+30*t)
        test=tk.Label(window,text=week[w-1][t][1])
        test.place(x=250,y=30+30*t)
global window
window = tk.Tk()
window.title('動漫更新表')
window.geometry('420x50')
window.configure(background='white')
week_1 = tk.Button(text='一',command=switch_1)
week_1.place(x=0,y=0)

week_2 = tk.Button(text='二',command=switch_2)
week_2.place(x=66,y=0)
week_3 = tk.Button(text='三',command=switch_3)
week_3.place(x=132,y=0)
week_4 = tk.Button(text='四',command=switch_4)
week_4.place(x=198,y=0)
week_5 = tk.Button(text='五',command=switch_5)
week_5.place(x=264,y=0)
week_6 = tk.Button(text='六',command=switch_6)
week_6.place(x=330,y=0)
week_7 = tk.Button(text='日',command=switch_7)
week_7.place(x=396,y=0)


window.mainloop() 

        

