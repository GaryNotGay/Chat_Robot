# @Author  :  lijishi
# @Contact :  lijishi@emails.bjut.edu.cn
# @Software:  Pycharm
# @EditTime:  Feb 3,2020
# @describe:  A Boring Robot
# @LICENSE :  GNU GENERAL PUBLIC LICENSE Version 3

import os
import time
import base64
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models

zhanggif = r'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'
zhangico = r'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2v/c3dv/1tfV/9HS0P/R0tD/0dLQ/9LT0f/U1dP/1dbU/9XW1P/V1tT/1dbU/9XW1P/V1tT/1dbU/9XW1P/V1tT/1dbU/9XW1P/V1tT/1dbU/9XW1P/V1tT/1dbU/9XW1P/V1tT/1dbU/9XW1P/Q0c//ycrI/5ydnP+ioqH/r6+v/7m5uf/CwsL/ysrK/9PT0//e3t7/6urq//Dw8P/z8/P/9PT0//T09P/y8vL/8vLy/xoZG/8aGRv/Gxoc/xoZG/8cGx3/Gxoc/xwbHf8cGx3/HRwe/xwbHf8dHB7/HRwe/x4dH/8dHB7/Gxoc/1paWv/Nzsz/2NnX/9vc2v/W19X/z9DO/87Pzf/Q0c//0tPR/9TV0//V1tT/1dbU/9bX1f/W19X/19jW/9fY1v/X2Nb/19jW/9fY1v/X2Nb/19jW/9fY1v/W19X/1tfV/9bX1f/V1tT/1dbU/9XW1P/V1tT/1dbU/9XW1P/U1dP/0dLQ/8vMyv/LzMr/s7Sy/6ampv+1tbX/wcHB/8zMzP/X19f/5ubm/+7u7v/y8vL/9PT0//T09P/z8/P/8vLy//Dw8P8ZGBr/GRga/xkYGv8bGhz/Ghkb/xoZG/8bGhz/Gxoc/xoZG/8cGx3/Gxoc/x0cHv8cGx3/HRwe/42Njv/Z2dn/19jW/9na2P/W19X/1NXT/9TV0//U1dP/1dbU/9XW1P/W19X/19jW/9fY1v/Y2df/2NnX/9rb2f/a29n/2tvZ/9rb2f/a29n/2tvZ/9rb2f/a29n/2tvZ/9na2P/X2Nb/19jW/9bX1f/W19X/1dbU/9XW1P/V1tT/1dbU/9PU0v/R0tD/ycrI/8zNy//ExMT/sLCw/8HBwf/Q0ND/3t7e/+rq6v/w8PD/8/Pz//T09P/z8/P/8vLy//Hx8f+fn5//GRga/xkYGv8ZGBr/Ghkb/xoZG/8YFxn/Ghkb/xoZG/8aGRv/Gxoc/xoZG/8bGhz/JSUm/62trf/W19b/1dbU/9bX1f/V1tT/1dbU/9XW1P/W19X/1tfV/9fY1v/Y2df/2drY/9ra2f/b29v/29vb/9zd3P/c3Nz/3N3b/93e3P/d3tz/3N3b/9zd2//d3tz/3+De/9/g3v/e393/3N3b/9rb2f/Z2tj/19jW/9fY1v/W19X/1dbU/9XW1P/U1dP/1dbU/9TV0//P0M7/zs/N/83OzP/AwMD/1NTU/+Tk5P/t7e3/8fHx//Ly8v/y8vL/8fHx//Hx8f/a2dr/KCgp/xgXGf8YFxn/GBcZ/xgXGf8YFxn/GRga/xkYGv8YFxn/GRga/xoZG/8aGRv/KCgp/7q6uv/W19X/1dbU/9bX1f/V1tT/1dbU/9XW1P/W19X/19jW/9jZ1//a29n/3N3b/93e3P/f397/39/f/9/f3//f39//39/f/+Dh3//f4N7/3+De/9/g3//g4N//4uPi/+Xl5P/m5+b/5ebl/+Lj4f/f397/3N3b/9rb2f/a29n/2NnX/9fY1v/W19X/1dbU/9XW1P/V1tT/1dbU/9PU0v/T1NL/0tLS/9DQ0P/l5eX/7e3t//Dw8P/w8PD/8vLy//Hx8f/Nzc3/NzY3/xYVF/8YFxn/GBcZ/xgXGf8YFxn/GBcZ/xgXGf8YFxn/GRga/xkYGv8YFxn/JCMk/7m5uf/W19X/1dbU/9XW1P/V1tT/1dbU/9bX1f/X2Nb/2drY/9vc2v/d3tz/3+De/+Dh4P/h4eD/4eHh/+Hh4f/h4eH/4uLi/+Hh4f/i4uL/4+Pj/+Li4v/i4uL/4uLi/+Xl5f/o6Oj/6enp/+np6f/o6Oj/5eXl/+Li4v/f397/3N3c/9rb2f/Z2tj/19jW/9bX1f/V1tT/1dbU/9XW1P/V1tT/1dbU/9fY1v/BwcD/np6e/7a2tv+7u7r/ubm5/5+fn/9hYGH/Gxob/xYVF/8WFRf/FxYY/xcWGP8WFRf/FxYY/xcWGP8YFxn/GBcZ/xkYGv8YFxn/Ghkb/6urq//W19X/1dbU/9XW1P/V1tT/1tfV/9bX1f/Y2df/29za/97e3f/g4d//4OHf/+Hh4P/i4uH/4uLi/+Li4v/j4+P/4+Pj/+Tk5P/l5eX/5eXl/+Xl5f/l5eX/5ubm/+Xl5f/o6Oj/6urq/+zs7P/s7Oz/6+vr/+rq6v/o6Oj/5OTk/+Dg4P/d3tz/3N3c/9rb2v/a29n/2NnX/9bX1f/V1tT/1dbU/9XW1P/V1tT/2NnX/05PTv8VFRX/FhYW/xUUFf8WFRb/FxYY/xcWGP8XFhj/FhUX/xYVF/8XFhj/FhUX/xYVF/8WFRf/FxYY/xcWGP8YFxr/FhUX/4mJif/W19X/1dbU/9XW1P/V1tT/1tfV/9jZ1//a29n/3t7d/9/g3//g4OD/4ODg/+Hh4f/i4uL/4+Pj/+Pj4//l5eX/5eXl/+bm5v/m5ub/5+fn/+fn5//n5+f/6Ojo/+jo6P/o6Oj/6+vr/+3t7f/u7u7/7u7u/+7u7v/t7e3/7e3t/+vr6//p6en/5eTk/9jX1//T09L/2djY/+Hh3//d3tv/2NnX/9bX1f/V1tT/1dbU/9XW1P/Jycj/JCQk/xYVF/8XFhj/FxYY/xUUFv8WFRf/FhUX/xYVF/8VFBb/FhUX/xYVF/8WFRf/FhUX/xcWGP8XFhj/FxYY/1NTVP/Y2df/1dbU/9XW1P/V1tT/1dbU/9bX1f/b3Nr/3t7e/9/f3//f39//4ODg/+Hh4f/j4+P/5OTk/+Xl5f/l5eX/5ubm/+fn5//o6Oj/6Ojo/+np6f/q6ur/6+vr/+vr6//s7Oz/7Ozs/+7u7v/x8fH/8vLy//Ly8v/y8vL/8PDw/9TU0/+hn57/dnNw/1pXUv9TUEz/U1BM/1lWUv9nZWD/iIaD/6+urf/a2Nf/2NnX/9XW1P/U1dP/19fW/5KSk/8VFBb/FRQW/xYVF/8WFRf/FhUX/xYVF/8WFRf/FhUX/xYVF/8WFRf/FhUX/xYVF/8WFRf/FhUX/yMjI//Jycj/1tfV/9XW1P/V1tT/1dbU/9fY1v/b3Nr/3t/d/9/f3//f39//4ODg/+Li4v/j4+P/5OTk/+bm5v/m5ub/6Ojo/+jo6P/p6en/6urq/+vr6//s7Oz/7u7u/+7u7v/v7+//7+/v//Hx8f/z8/P/9PT0//X19f/y8vL/ysnJ/316ef9STkv/RkI//0A7N/9BPTr/RUA9/0pFQv9PSkf/UEtI/05JR/9TT07/bWlo/7Kvrv/c3Nv/1tfV/9TV0//Y2dj/Pz8//xUUFv8VFBb/FRQW/xUUFv8WFRf/FRQW/xUUFv8VFBb/FRQW/xUUFv8VFBb/FRQW/xQUFP+HiIb/19jW/9XW1P/V1tT/1dbU/9fY1v/Z2tn/3d3d/9/g3//g4OD/4eHh/+Li4v/k5OT/5eXl/+bm5v/n5+f/6enp/+np6f/r6+v/7Ozs/+3t7f/v7+//8PDw//Hx8f/z8/P/9PT0//X19f/19fX/9vf3//X29v/e3Nz/h4aD/1dUUP9MSET/SUZB/1BMR/9dWVX/aWVg/3Ftaf92c27/dnNu/3Fuaf9kYF3/Uk5L/01KRv9WUlD/kI2M/9va2P/X19X/1dbU/6eop/8TExT/FRQW/xUUFv8VFBb/FRQW/xUUFv8UExX/ExIU/xUUFv8VFBb/FRQW/xUUFv8vLy//1tbV/9XW1P/V1tT/1dbU/9bX1f/Z2tj/3N3b/97e3v/g4OD/4eHh/+Pj4//k5OT/5ubm/+fn5//o6Oj/6enp/+rq6v/r6+v/7u7u/+/v7//x8fH/8/Pz//T09P/09PT/9fX1//f39//4+Pj/+Pj4//Lw8P+qpqb/Yl9f/1JNS/9MR0L/VlFN/2diXv9uamX/bGhj/2tlYv9pZmP/aWdj/2tnZP9tZ2T/dG9s/3x3dP9oYl//UUxK/1RNTf+MiYj/2tvZ/9bX1f/Y2df/Pj4//xQTFf8UExX/FBMV/xUUFv8UExX/FBMV/xMSFP8VFBb/FBMV/xQTFf8UExT/jY2N/9XW1P/V1tT/1dbU/9bX1f/Z2tj/3d3c/9/g3//g4OD/4eHh/+Pj4//l5eX/5ubm/+fn5//o6Oj/6+vr/+zs7P/t7e3/7+/v//Ly8v/z8/P/9PT0//b29v/29vb/+Pf3//f4+P/6+vn/+fn4/8/Ozf95dnT/ZF9e/09KSP9KR0P/YVxY/2llYP9iXVj/R0M+/zEtKf8gHx3/GBkX/xwdG/8tLSv/R0RB/2NgXP9uaWX/d3Ft/3Jtav9TTkv/VlFP/6Sjof/a29n/1dXU/5eXmP8UExX/FBMV/xQTFf8UExX/FBMV/xQTFf8UExX/FBMV/xQTFf8UExX/IiEi/9TU1P/V1tT/1dbU/9XW1P/Y2df/3d7c/+Hh4f/i4uL/4eHh/+Pj4//l5eX/5+fn/+jo6P/p6en/6urq/+3t7f/v7+//8fHx//Ly8v/19fX/9vb2//f39//4+Pj/+Pj4//n5+f/6+vr/3Nzb/5aTkf9uamX/bmpn/1NOTf9KRUP/Y15b/2JdWv9IRUL/IR8e/xoYF/8WFRb/FBMV/xMTFP8XFxj/ICAh/ysqK/8uMC7/T09L/3VvbP96dXL/cm1p/1VQTf9cWVj/zMzK/9bX1f/U1dT/Hx8g/xMSFP8UExX/ExIU/xQTFf8TEhT/FBMV/xMSFP8UExX/ExIU/2trbP/X19f/1dbU/9XW1P/X2Nb/29za/+Li4v/l5eX/5OTk/+Tk5P/k5OT/5ubm/+jn5//q6er/7Ovs/+7u7v/x8fD/8/Py//f2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uf/FwLz/x8K+/8jDwf+6tbT/mZWU/3Btbf88Ozz/Hx8g/xYVF/8TERT/EhET/xISE/8SEhT/EhET/xIRE/8SERP/EhET/xMSFP8TEhT/ExIU/xIRE/8TEhT/EhET/xIRE/8TEhT/EhET/xIRE/8SERP/EhET/xIRE/8TEhT/EhET/xIRE/8SERP/EhET/xIRE/8REBL/ExIU/xIRE/8SERP/EhET/xIRE/8SERP/EhET/xIRE/8SERP/EhET/xEQEv8SERP/EhET/xIRE/8SERP/ExIU/xYVFv8dGxz/JCAh/zQyMf9KSEf/X11b/25qaf92cnH/eHRz/3Zzcv9vbGv/Y2Bf/1BOTf83NDX/JSIj/x0bHP8VFRb/EhET/xIRE/8SERP/ExIU/xIRE/8SERP/ExIU/xMSFP8SERP/ExIU/xIRE/8TEhT/EhET/xIRE/8SERP/EhET/xMSFP8SERP/EhET/xIRE/8TEhT/ExIU/xIRE/8SERP/EhET/xMSFP8SERP/EhET/xIRE/8SERP/EhET/xIRE/8REBL/EhET/xIRE/8TEhT/ExIU/xIRE/8SERP/EhET/xMSFP8REBL/EhET/xIRE/8SERP/ERAS/xIRE/8REhP/EhIT/xIRE/8TEhP/ExIT/xQTFf8XFRf/FxYY/xcWGP8XFhj/FhQW/xQTFf8UExT/EhEU/xMRE/8REhP/EhET/xMSFP8SERP/ExIU/xIRE/8SERP/EhET/xIRE/8SERP/EhET/xMSFP8SERP/ExIU/xIRE/8SERP/EhET/xEQEv8TEhT/EhET/xIRE/8SERP/ExIU/xIRE/8SERP/ExIU/xIRE/8SERP/EhET/xIRE/8TEhT/ExIU/xIRE/8SERP/EhET/xMSFP8SERP/ExIU/xIRE/8SERP/ExIU/xMSFP8SERP/EhET/xMSFP8TEhT/EhET/xIRE/8SERP/EhET/xIRE/8TEhT/ExIU/xMSFP8SERP/EhET/xIRE/8SERP/EhET/xIRE/8REBL/ExIU/xIRE/8SERP/ERAS/xIRE/8SERP/EhET/xIRE/8SERP/ExIU/xMSFP8REBL/ERAS/xMSFP8TEhT/ExIU/xIRE/8SERP/EhET/xIRE/8TEhT/EhET/xIRE/8REBL/EhET/xIRE/8SERP/EhET/xIRE/8REBL/ERAS/xIRE/8REBL/EhET/xMSFP8SERP/EhET/xMSFP8SERP/EhET/xMSFP8SERP/EhET/xIRE/8SERP/ExIU/xMSFP8SERP/ExIU/xIRE/8SERP/ExIU/xIRE/8TEhT/EhET/xIRE/8SERP/EhET/xIRE/8SERP/ERAS/xIRE/8SERP/EhET/xIRE/8REBL/ERAS/xIRE/8TEhT/EhET/xIRE/8TEhT/EhET/xIRE/8TEhT/EhET/xIRE/8REBL/ERAS/xIRE/8SERP/EhET/xIRE/8SERP/EhET/xMSFP8REBL/EhET/xIRE/8SERP/ExIU/xIRE/8SERP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='

def Icon():
    global  zhangico
    with open('tmp.ico', 'wb') as tmp:
        tmp.write(base64.b64decode(zhangico))

def Gif():
    global  zhanggif
    with open('temp.gif', 'wb') as temp:
        temp.write(base64.b64decode(zhanggif))
    zhang_gif = tk.PhotoImage(file="temp.gif")

def Tencent_ChatRobot(text):
    global confidence
    global return_text

    try:
        cred = credential.Credential("Your ID", "Your Secret")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "nlp.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

        req = models.ChatBotRequest()
        params_1 = '{"Flag":0,"Query":"'
        params_2 = '"}'
        params = params_1 + text + params_2
        req.from_json_string(params)

        resp = client.ChatBot(req)
        resp_text = resp.to_json_string()

        flag_confidence = 0
        confidence_text = ''
        for index in range(len(resp_text)):
            if resp_text[index] == ",":
                break
            if flag_confidence:
                confidence_text += resp_text[index]
            if resp_text[index - 1] == ":":
                flag_confidence = 1
        if confidence_text == '1':
            confidence = int(confidence_text) * 100
        else:
            confidence = round(float(confidence_text) * 100, 1)

        flag_text = 0
        return_text = ''
        for index in range(len(resp_text)):
            if resp_text[index] == "\"" and flag_text == 2:
                break
            if flag_text == 2:
                return_text += resp_text[index]
            if resp_text[index - 2] == ":":
                flag_text += 1

    except TencentCloudSDKException as err:
        tk.messagebox.showerror("TencentCloudError", err)
        scr.delete(1.0, END)
        scr.insert("insert", "TencentCloudNLP ")
        scr.insert("insert", now_time)
        scr.insert("insert", "\n")
        scr.insert("insert", "TencentCloudError!")

def Start():
    global confidence
    global return_text

    try:
        confidence = 100
        Tencent_ChatRobot(text_in.get())
        now_time = time.strftime("%H:%M:%S", time.localtime())
        scr.delete(1.0, END)
        scr.insert("insert", "TencentCloudNLP ")
        scr.insert("insert", now_time)
        scr.insert("insert", " ")
        scr.insert("insert", str(confidence))
        scr.insert("insert", "%")
        scr.insert("insert", "\n")
        scr.insert("insert", "\n")
        scr.insert("insert", return_text)
        scr.insert("insert", "\n")
    except BaseException as err:
        tk.messagebox.showerror("UnknownError", err)
        now_time = time.strftime("%H:%M:%S", time.localtime())
        scr.delete(1.0, END)
        scr.insert("insert", "TencentCloudNLP ")
        scr.insert("insert", now_time)
        scr.insert("insert", "\n")
        scr.insert("insert", "UnknownError!")

def Tips():
    tk.messagebox.showinfo("Tips", "对话内容均来自腾讯云，与作者无关\n本软件仅用作日常娱乐，请勿用于非法用途\n若腾讯云更改免费政策，可能导致软件无法使用")

def About():
    # window centered
    about_window = Toplevel()
    screen_width = about_window.winfo_screenwidth()
    screen_heigh = about_window.winfo_screenheight()
    about_window_width = 350
    about_window_heigh = 200
    x = (screen_width - about_window_width) / 2
    y = (screen_heigh - about_window_heigh) / 2
    about_window.geometry("%dx%d+%d+%d" % (about_window_width, about_window_heigh, x, y))

    # window layout
    global zhang_gif
    Icon()
    Gif()
    about_window.title('About')
    about_window.iconbitmap(".\\tmp.ico")
    os.remove('tmp.ico')
    zhang_gif = tk.PhotoImage(file=".\\temp.gif")
    software_frame = ttk.LabelFrame(about_window, text='Software Info')
    software_frame.grid(row=0, column=0, rowspan=5, columnspan=4, padx=50, pady=5)
    ttk.Label(software_frame, image=zhang_gif, compound='left').grid(row=0, rowspan=3, column=0)
    ttk.Label(software_frame, text="Chat Robot Version 1.0").grid(row=0, column=1, sticky = W)
    ttk.Label(software_frame, text="@Author    :   lijishi").grid(row=1, column=1, sticky = W)
    ttk.Label(software_frame, text="@EditTime  :   Feb 3,2020").grid(row=2, column=1, sticky = W)
    os.remove('temp.gif')

    copyright_frame = ttk.LabelFrame(about_window, text='LICENSE Info')
    copyright_frame.grid(row=5, column=0, rowspan=3, columnspan=4, padx=50, pady=5)
    ttk.Label(copyright_frame, text = "Github @ Chat_Robot").grid(row=5, column=0)
    ttk.Label(copyright_frame, text="Powered By Tencent Cloud NLP").grid(row=6, column=0)
    ttk.Label(copyright_frame, text="GNU GENERAL PUBLIC LICENSE Version 3").grid(row=7, column=0)

# window centered
main_window=tk.Tk()
screen_width = main_window.winfo_screenwidth()
screen_heigh = main_window.winfo_screenheight()
main_window_width = 290
main_window_heigh = 110
x = (screen_width-main_window_width) / 2
y = (screen_heigh-main_window_heigh) / 2
main_window.geometry("%dx%d+%d+%d" %(main_window_width,main_window_heigh,x,y))

# window layout
Icon()
main_window.title("Chat Robot V1.0")
main_window.iconbitmap(".\\tmp.ico")
os.remove('tmp.ico')
text_in = tk.StringVar()
text_in.set("请输入你想和智障机器人说的话......")
ttk.Entry(main_window, width = 30, textvariable = text_in).grid(row = 0, column = 0, columnspan = 2, padx=10)
ttk.Button(main_window, text = "开始", width = 5, command = Start).grid(row = 0, column = 2, pady=5)
ttk.Button(main_window, text = "提示", width = 5, command = Tips).grid(row = 1, column = 2, pady=5)
ttk.Button(main_window, text = "关于", width = 5, command = About).grid(row = 2, column = 2, pady=5)
scr = scrolledtext.ScrolledText(main_window, width = 30, height = 3, wrap=tk.WORD)
scr.grid(row = 1, column = 0, columnspan = 2, rowspan = 2, padx=5)
main_window.mainloop()