from tkinter import *
import wikipedia

window=Tk()
window.geometry('300x300')

def Clear():
    my_input.delete(0,END)
    text_area.delete(0.0,END)


def Search():
    wikipedia.set_lang("tr")
    result= wikipedia.page(my_input.get())
    
    text_area.insert(0.0,result.content)

my_label_frame= LabelFrame(window,text='Search arama')#label frame açıyoruz
my_label_frame.pack(padx=20,pady=20)#label frame açtık

my_input=Entry(my_label_frame)#input girdik label framein içine koyduk
my_input.pack(padx=20,pady=20, fill=X)#input girdik label framein içine koyduk

text = Frame(window, height=150)
text.pack(padx=20, fill=X)
text.pack_propagate(False)  #  çerçevenin büyümesini engeller


vertical_scroll= Scrollbar(text,orient='vertical')#dikeyde olan scroolbar
vertical_scroll.pack(side=RIGHT,fill=Y)#dikeyde olan scroolbar

horizontal_scroll= Scrollbar(text,orient='horizontal')#yatayda olan scroolbar
horizontal_scroll.pack(side=BOTTOM,fill=X)#yatayda olan scroolbar


text_area = Text(text, height=5,yscrollcommand=vertical_scroll.set,xscrollcommand=horizontal_scroll.set,wrap='none')#textarea
text_area.pack(fill=BOTH, expand=True)#textarea

vertical_scroll.config(command=text_area.yview)#bunu tanıtmamız lazım scrool için
horizontal_scroll.config(command=text_area.xview)#bunu tanıtmamız lazım scrool için

button_frame=Frame(window,height=250)#button frame
button_frame.pack(padx=10,fill=BOTH, expand=True)#button frame
button_frame.pack_propagate(False) #button frame

button=Button(button_frame,text='Search',command=Search)#search butonu
button.grid(column=0,row=0,padx=10)#search butonu

temizle_button= Button(button_frame,text='Clear',command=Clear)#clear butonu
temizle_button.grid(column=1,row=0,padx=10)#clear butonu


window.mainloop()