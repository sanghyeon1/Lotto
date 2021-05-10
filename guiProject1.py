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

    print("{}회차 당첨번호를 확인합니다.".format(n))
    print("당첨번호 - {}".format(num_list))
    print("보너스 번호 - {}".format(bonus))


def prd_lotto():  # 로또 번호 예측 코드
    count_num = []
    min_list = []
    bns_sum = 0
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
            # 보너스 번호를 계산하는데에 한 번만 쓰입니다.
            if j == 0:
                count_num[int(bns_num) - 1] += 1

    for i in range(7):
        # count_num 의 최솟값에 해당하는 인덱스가 tmp 에 들어감.
        tmp = count_num.index(min(count_num))
        min_list.append(tmp+1)
        count_num[tmp] = 100

    print(min_list[0:6], "+ 보너스 번호 [{}]".format(min_list[6]))


def count_prd():
    puts = ent.get()
    if type(puts) == str and puts == '':
        print("아무것도 입력되지 않았습니다.")

    elif puts != '':
        puts = int(puts)
        if 0 < puts < 11:
            print("로또 번호를 {}회 뽑습니다.".format(puts))
            for i in range(puts):
                print("{}회 : ".format(i+1))
                prd_lotto()
        elif puts >= 11:
            print("입력 값이 너무 커서 프로그램이 느려집니다.")
            print("1~10사이의 값을 입력하십시오.")
        else:
            print("Error 값입니다. 다시 입력하십시오.")


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

ent = Entry(win)
ent.pack()

# 당첨번호 예측하기 버튼
btn2 = Button(win)
btn2.config(text="당첨번호 예측하기")
btn2.config(command=count_prd)
btn2.pack()
win.mainloop()
