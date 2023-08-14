from tkinter import Tk, Label, Button
from tkinter.messagebox import showinfo
import os

root = Tk()

def info():
    showinfo(title='О программе', message='MineLauncher - лучший лаунчер который поддерживает версию 1.14\nНаш лаунчер безопасный и слабая,тоесть\nНЕНАДО ИМЕТЬ ХОРОШИЙ ПК ИЛИ НОУТБУК!\nЛаунчер имеет свой интерфейс чтобы облегчить!\nФайл будет сохранятся в папке %AppData%\.minecraft\nСделано студией BebrikGolma \n\n\n BebrikGolma Copyright @2023')

def game():
    os.system('start start.bat')


root['bg'] = 'gray22'
root.title('MineLauncher')
root.geometry('400x400')
root.resizable(width=False, height=False)

lbl = Label(text='Minecraft 1.14 Java Edition')
lbl.pack()
btn = Button(text='Играть', command = game)
btn.pack()

btn1 = Button(text='О программе', command = info)
btn1.pack()

ins = Label(text='Инструкция:\n1.У вас должно быть скачено JDK\n2.Нажимайте на кнопку Играть\n3.В другом окне пишите там никнейм и ОЗУ')
ins.pack()

root.mainloop()