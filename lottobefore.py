import requests
from tkinter import *
from bs4 import BeautifulSoup


def ent_p():
    a = ent.get()
    print(a)


def lotto_p():
    n = ent.get()
    url = "https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(n)
    #  div class="win_result"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    txt = soup.find("div", attrs={"class", "win_result"}).get_text()
    num_list = txt.split("\n")[7:13]
    bonus = txt.split("\n")[-4]

    print("당첨번호")
    print(num_list)
    print("보너스 번호")
    print(bonus)


win = Tk()
win.geometry("300x200")
win.option_add("*Font", "궁서 20")

ent = Entry(win)
ent.pack()

# 일반 로또 당첨번호 확인 버튼
btn = Button(win)
btn.config(text="로또 당첨 번호 확인")
btn.config(command=lotto_p)
btn.pack()

win.mainloop()
