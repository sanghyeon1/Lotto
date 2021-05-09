from tkinter import *
import requests
import random
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


def prd_lotto():  # 로또 번호 예측 코드
    count_num = []
    min_list = []
    for i in range(1, 46):
        count_num.append(0)

    # 랜덤 범위 설정 후 로또번호 예측
    b = random.randint(101, 962)
    a = b - 50
    for i in range(a, b):
        pre_url = "https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(i)
        req = requests.get(pre_url)
        soup = BeautifulSoup(req.text, "html.parser")
        txt = soup.find("div", attrs={"class", "win_result"}).get_text()
        lotto_num = txt.split("\n")[7:13]
        bns_num = txt.split("\n")[-4]
        for j in range(6):
            count_num[int(lotto_num[j]) - 1] += 1

    for i in range(6):
        # count_num의 최솟값에 해당하는 인덱스가 tmp에 들어감.
        tmp = count_num.index(min(count_num))
        min_list.append(tmp+1)
        count_num[tmp] = 100

    print(min_list)


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

# 당첨번호 예측하기 버튼
btn2 = Button(win)
btn2.config(text="당첨번호 예측하기")
btn2.config(command=prd_lotto)
btn2.pack()
win.mainloop()



