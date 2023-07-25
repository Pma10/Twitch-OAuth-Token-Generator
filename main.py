import httpx
from tkinter import *
import tkinter.messagebox as msg
def get_OAuthToken():
    client_id = ClientIdInp.get()
    client_secret = clientSecretInp.get()
    grant_type = 'client_credentials'

    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': grant_type
    }

    response = httpx.post(url, params=params)
    data = response.json()

    if 'access_token' in data:
        oauth_token = data['access_token']
        output.configure(state='normal')
        output.insert(END,oauth_token)
        output.configure(state='disabled')
        msg.showinfo(title='성공',message='오른쪽의 출력값을 확인해주세요')
    else:
        msg.showwarning(title='실패',message='올바른 Client ID 와 올바른 Client Secret을 입력해주세요')
root = Tk()
root.title('트위치 API OAuth 토큰 생성기')
root.geometry('650x100+100+100')

title = Label(root,text='트위치 API OAuth 토큰 생성기')
title.grid(row=0,column=0)

inpFrame = Frame(root)
inpFrame.grid(row=1,column=0)
ClientIdInp = Entry(inpFrame,width=30)
clientSecretInp = Entry(inpFrame,width=30)
btn = Button(inpFrame,text='생성하기',width=30,command=get_OAuthToken)
accessTokenText = Label(inpFrame,text='Client Id 입력 : ')
clientSecretText = Label(inpFrame,text='Client Secret 입력 : ')
accessTokenText.grid(row=0,column=0)
ClientIdInp.grid(row=0,column=1)
clientSecretText.grid(row=1,column=0)
clientSecretInp.grid(row=1,column=1)
blank = Label(root,text='   ')
blank.grid(row=1,column=1)
output = Text(root,width=40,height=5)
output.grid(row=1,column=2)
output.configure(state='disabled')
btn.grid(row=2,column=1)
root.mainloop()
