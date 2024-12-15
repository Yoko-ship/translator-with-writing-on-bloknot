from googletrans import Translator
from tkinter import *

class Perevodchick:
    def translator(self,text,translateInto):
        self.text = text
        self.translateInto = translateInto

        translator =  Translator()
        self.result = translator.translate(self.text,translateInto)
        return self.result.text
    

class Tkint:
    def __init__(self,size,title):
        self.size = size
        self.title = title
        self.font = ("Arial",15)
    

    def open(self):
        self.root = Tk()
        self.root.geometry((self.size))
        self.root.title(self.title)
        Label(self.root,text="Текст",font=self.font).pack(pady=5)
        self.text = StringVar()
        self.entry = Entry(self.root,textvariable=self.text,width=100,font=self.font).pack(anchor="n")
        self.var = StringVar(self.root,"EN")
        Radiobutton(self.root,text="EN",variable=self.var,value="en",font=self.font).pack(anchor="n")
        Radiobutton(self.root,text="RU",variable=self.var,value="ru", font=self.font).pack(anchor="n")
        Radiobutton(self.root,text="UZ",variable=self.var,value="uz",font=self.font).pack(anchor="n")
        Button(self.root,text="Подтвердить",foreground="white",background="green",command=self.__get_values,font=self.font).pack(anchor="n")
        self.root.mainloop()
        


    def __get_values(self):
        self.result = self.var.get()
        self.text_variable = self.text.get()
        self.another_text = self.text_variable
        self.text.set("")
        try:

            perevodchick = Perevodchick()
            self.data = perevodchick.translator(self.another_text,self.result)
            Label(self.root,text=self.data,font=self.font).pack(anchor="w")
            with open("bloknot.txt","a") as fIle:
                fIle.write(self.another_text + "            " + self.data + " \n ")
        except TypeError:
            self.error = StringVar()
            self.error.set("Пожалуста заполните все поля")
            self.label = Label(self.root,textvariable=self.error,font=self.font).pack(anchor="n")

        except Exception:
            self.message = StringVar()
            Label(self.root,textvariable=self.message,font=self.font).pack(anchor="n")

        

tkinter = Tkint("700x700","Translator")
test = tkinter.open()

