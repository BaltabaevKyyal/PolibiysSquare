from tkinter import *
import sqlite3
import tkinter.messagebox as mb
from tkinter import scrolledtext

class Authorization():
    def __init__(self, enter):
        #Окно авторизации
        self.enter = enter
        self.window = Tk()
        self.window.title('Шифрование квадратом Полибия')
        self.window.geometry('320x120')

        self.lbl = Label(self.window, text='Авторизуйтесь')
        self.lbl.grid(column=1, row=0)
        self.lbl1 = Label(self.window, text='Логин')
        self.lbl1.grid(column=0, row=1)
        self.lbl2 = Label(self.window, text='Пароль')
        self.lbl2.grid(column=0, row=2)
        self.text_box = Entry(self.window, width=30)
        self.text_box.grid(column=1, row=1)
        self.text_box1 = Entry(self.window, width=30, show='*')
        self.text_box1.grid(column=1, row=2)
        self.btn = Button(self.window, text='Войти', command = lambda:self.login(self.text_box.get(), self.text_box1.get()))
        self.btn.grid(column=1, row=3)
        self.btn1 = Button(self.window, text='Регистрация', command=self.registration)
        self.btn1.grid(column=0, row=4)
        self.btn2 = Button(self.window, text='Выход', command=self.window.destroy)
        self.btn2.grid(column=2, row=4)
        self.window.mainloop()
    def login(self, log, paswd):
        #Авторизация
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS users(
            userid INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL,
            password TEXT NOT NULL)''')
        cur.execute('SELECT login FROM users WHERE login = ? AND password = ?', (log, paswd,))
        result = cur.fetchone()
        if result is None:
            mb.showerror("Ошибка", "Логин или пароль введены некорректно")
        else:
            mb.showinfo("Авторизация", "Авторизация успешна")
            self.enter[0] = True
            self.window.destroy()
        conn.commit()
    def registration(self):
        #Окно регистрации
        reg_window = Tk()
        reg_window.title('Регистрация')
        reg_window.geometry('270x200')

        lbl_center = Label(reg_window, text='Регистрация')
        lbl_center.grid(column=1, row=0)
        lbl1 = Label(reg_window, text='Логин')
        lbl1.grid(column=0, row=1)
        lbl2 = Label(reg_window, text=' ')
        lbl2.grid(column=0, row=2)
        lbl3 = Label(reg_window, text='Пароль')
        lbl3.grid(column=0, row=3, rowspan = 2)
        text_box1 = Entry(reg_window, width=30)
        text_box1.grid(column=1, row=1)
        text_box2 = Entry(reg_window, width=30, show='*')
        text_box2.grid(column=1, row=3)
        text_box3 = Entry(reg_window, width=30, show='*')
        text_box3.grid(column=1, row=4)
        btn1 = Button(reg_window, text='Зарегистрироваться', command=lambda:self.add_to_base(text_box1.get(), text_box2.get(), text_box3.get()))
        btn1.grid(column=1, row=5)
        lbl4 = Label(reg_window, text=' ')
        lbl4.grid(column=1, row=6)
        btn2 = Button(reg_window, text='Вернуться назад', command=reg_window.destroy)
        btn2.grid(column=1, row=7)
        reg_window.mainloop()
    def add_to_base(self, log, pas1, pas2):
        #Регистрация
        if log == '' or pas1 == '' or pas2 == '':
            mb.showerror("Ошибка", "Логин или пароль введены некорректно")
        elif pas1 != pas2:
            mb.showerror("Ошибка", "Пароли не совпадают")
        elif pas1 == pas2:
            conn = sqlite3.connect('users.db')
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS users(
                userid INTEGER PRIMARY KEY AUTOINCREMENT, 
                login TEXT NOT NULL, 
                password TEXT NOT NULL)''')
            cur.execute('SELECT login FROM users WHERE login = ?', (log,))
            result = cur.fetchone()
            if result is not None:
                mb.showerror("Ошибка", "Данный логин уже используется")
            else:
                user = (log, pas1)
                cur.execute('INSERT INTO users(login, password) VALUES(?, ?)', user)
                mb.showinfo("Регистрация", "Регистрация успешна")
            conn.commit()
class Polibiy():
    def __init__(self):
        #Оcновное окно
        self.pol = Tk()
        self.pol.title("Шифрование квадратом Полибия")
        self.pol.geometry('880x300')
        
        self.lbl = Label(self.pol, text = 'Шифрование квадратом Полибия')
        self.lbl.grid(column=2, row=0)
        self.lbl1 = Label(self.pol, text = 'Текст')
        self.lbl1.grid(column=1, row=1)
        self.textbox1 = Entry(width = 40)
        self.textbox1.grid(column=1, row=2)
        self.btn = Button(self.pol, text = 'Зашифровать', command=self.code_extra)
        self.btn.grid(column=1, row=3)        
        self.lbl2 = Label(self.pol, text = 'Результат шифрования')
        self.lbl2.grid(column=1, row=4)
        self.textbox2 = scrolledtext.ScrolledText(self.pol, width=40, height=10)
        self.textbox2.grid(column=1, row=5)        
        self.lbl11 = Label(self.pol, text = 'Зашифрованный текст')
        self.lbl11.grid(column=3, row=1)
        self.textbox11 = Entry(width = 40)
        self.textbox11.grid(column=3, row=2)
        self.btn = Button(self.pol, text = 'Расшифровать', command=self.decode_extra)
        self.btn.grid(column=3, row=3)
        self.lbl22 = Label(self.pol, text = 'Результат расшифрования')
        self.lbl22.grid(column=3, row=4)
        self.textbox22 = scrolledtext.ScrolledText(self.pol, width=40, height=10)
        self.textbox22.grid(column=3, row=5)
        self.pol.mainloop()    
    def code_extra(self):
        fraze = self.textbox1.get()
        self.textbox2.delete("1.0", END)
        x = self.code(fraze)
        self.textbox2.insert(INSERT, x)
    def code(self, fraze):
        new_txt = ""
        for x in fraze:
            if x in dictionary:
                new_txt += dictionary.get(x)
            elif x in dictionary2:
                new_txt += dictionary2.get(x)
            else:
                new_txt += x+x
        return new_txt
    def decode_extra(self):
        fraze = self.textbox11.get()
        self.textbox22.delete("1.0", END)
        x = self.decode(fraze)
        self.textbox22.insert(INSERT, x)
    def decode(self, fraze):
        new_txt = ""
        list_fraze = []
        step = 2
        for i in range(0, len(fraze), 2):
            list_fraze.append(fraze[i:step])
            step += 2
        key_dictionary_list = list(dictionary.keys())
        val_dictionary_list = list(dictionary.values())  
        for x in list_fraze:
            if x in val_dictionary_list:
                i = val_dictionary_list.index(x)
                new_txt += key_dictionary_list[i]
            else:
                new_txt += x[0:1]
        return new_txt
dictionary = {"A":"11", "B":"12", "C":"13", "D":"14", "E":"15", "F":"16",
               "G":"21", "H":"22", "I":"23", "J":"24", "K":"25", "L":"26",
                "M":"31", "N":"32", "O":"33", "P":"34", "Q":"35", "R":"36",
                 "S":"41", "T":"42", "U":"43", "V":"44", "X":"45", "Y":"46",
                  "Z":"51", "!":"52", ",":"53", ".":"54", ":":"55", "_":"56",
                   "?":"61", ";":"62", "(":"63", ")":"64", "%":"65", "/":"66"}
dictionary2 = {"a":"11", "b":"12", "c":"13", "d":"14", "e":"15", "f":"16",
               "g":"21", "h":"22", "i":"23", "j":"24", "k":"25", "l":"26",
                "m":"31", "n":"32", "o":"33", "p":"34", "q":"35", "r":"36",
                 "s":"41", "t":"42", "u":"43", "v":"44", "x":"45", "y":"46",
                  "z":"51", "!":"52", ",":"53", ".":"54", ":":"55", "_":"56",
                   "?":"61", ";":"62", "(":"63", ")":"64", "%":"65", "/":"66"}
enter = [False]
Enter = Authorization(enter)
if enter[0] == True:
    polibiy = Polibiy()
#Функциональное тестирование
import unittest
func_test = False #False - off, True - on
class Tests(unittest.TestCase):
    def test_1_null_fraze_code(self):
        pol1 = Polibiy()
        print("Test 1")
        self.assertEqual(pol1.code(""), "")
    def test_2_low_reg_code(self):
        pol2 = Polibiy()
        print("\nTest 2")
        self.assertEqual(pol2.code("hello world"), "2215262633  ww33362614")
    def test_3_high_reg_code(self):
        pol3 = Polibiy()
        print("\nTest 3")
        self.assertEqual(pol3.code("HELLO WORLD"), "2215262633  WW33362614")
    def test_4_mix_reg_code(self):
        pol4 = Polibiy()
        print("\nTest 4")
        self.assertEqual(pol4.code("HeLlO WoRlD"), "2215262633  WW33362614")
    def test_5_numbers_code(self):
        pol5 = Polibiy()
        print("\nTest 5")
        self.assertEqual(pol5.code("123456789"), "112233445566778899")
    def test_6_simple_decode(self):
        pol6 = Polibiy()
        print("\nTest 6")
        self.assertEqual(pol6.decode("2215262633  WW33362614"), "HELLO WORLD")
    def test_7_numbers_decode(self):
        pol7 = Polibiy()
        print("\nTest 7")
        self.assertEqual(pol7.decode("112233445566778899"), "AHOV:/789")
if __name__ == '__main__' and func_test == True:
    unittest.main()