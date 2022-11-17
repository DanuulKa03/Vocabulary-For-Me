from random import randint
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

def loadVocabulary():
    global Russia, English
    with open("Слова.txt", "r", encoding='utf-8') as file:
        for line in file.readlines():
            x = list(line.split())
            English.append(x[0])
            Russia.append(x[1])


def _key_(x):
    if textVocabulary.get() == "" or textVocabulary.get() == " ":
        pass
    else:
        entryButton.invoke()


def runVocabulary():
    global count_Word
    x = textVocabulary.get()
    textVocabulary.delete(0, END)
    if (x.title()) == English[digitWord]:
        messagebox.showinfo("Ответ:", "Привильно!!!")
    else:
        count_Word += 1
        word_Count["text"] = f"Кол-во неправильных слов: {count_Word}"
        messagebox.showinfo("Ответ:",f"Неправильно, правильный ответ был {English[digitWord]}! - твой {x.title()}")
        #чтобы текст появлялся ровным в лобой момент игры
        if count_Word > 1:
            txt.insert(INSERT, f"\n{English[digitWord]} - {Russia[digitWord]}")
        else:
            txt.insert(INSERT, f"{English[digitWord]} - {Russia[digitWord]}")
    randWord()


def runTranslation():
    global count_Word
    count_Word += 1
    word_Count["text"] = f"Кол-во неправильных слов: {count_Word}"
    if count_Word > 1:
        txt.insert(INSERT, f"\n{English[digitWord]} - {Russia[digitWord]}")
    else:
        txt.insert(INSERT, f"{English[digitWord]} - {Russia[digitWord]}")
    textForPaper["text"] = str(English[int(digitWord)])
    # textForPaper["text"] = str(Russia[int(digitWord)])


def randWord():
    global digitWord, countWord
    digitWord = randint(0, len(Russia)-1)
    #цикл который ищет рандомное слово которого не будет в списке
    while (Russia[digitWord] in listVocabulary) and (len(listVocabulary) < len(Russia)):
        digitWord = randint(0, len(Russia) -1)
    #так как может быть такое, что цикл не испольнается, бывает баг из-за которого слова выводятся повторно
    if not(Russia[digitWord] in listVocabulary):
        countWord += 1
        wordCount["text"] = f"Кол-во слов: {countWord}"
        textForPaper["text"] = Russia[digitWord]
        listVocabulary.append(Russia[digitWord])


def stopVocabulary():
    global digitWord, count_Word, countWord
    digitWord, countWord, count_Word = 0
    listVocabulary.clear()


# ================================================================================================================
Russia = []
English = []
listVocabulary = []
WIDTH = 1280
HEIGHT = 720
digitWord = 0
countWord = 0
count_Word = 0 #число не отгаданых слов
# ================================================================================================================

root = Tk()
# центр моего экрана
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_vrootheight() // 2 - HEIGHT // 2
root.title("Мой словарь")
root.resizable(False, False)
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")


# загрузка листочка
road_paper = PhotoImage(file="image.png")
paper = Label(root, image=road_paper)
paper.place(relx=.5, rely=.5, anchor="center")

# оформление левого края
message = StringVar()
textVocabulary = Entry(textvariable=message, width=20, bd=2, font="Arial 18")
textVocabulary.place(x=80, y=352)
textForVocabulary = Label(root, text="Перевод:", font="Arial 15")
textForVocabulary.place(x=80, y=320)

# кнопка
entryButton = Button(width=11, text="Ввод", font="Arial 15",
                     background="#438297", command=runVocabulary)
entryButton.place(x=80, y=400)

# кнопка перевода
buttuonTranslation = Button(width=13, text="Перевести",
                            font="Arial 20", background="#FF6666", command=runTranslation)
buttuonTranslation.place(x=920, y=90)

# text for paper
textForPaper = Label(root, text="", font="Arial 17")
textForPaper.place(relx=.5, rely=.5, anchor="center")
textForPaper.config(background="snow")

# button start
# startButton = Button(background="#FF0000", width=10,
#                      font="Arial 15", text="Начать", command=randWord)
# startButton.place(x=80, y=50)

# button start
stopButton = Button(background="#FF0000", width=10,
                    font="Arial 15", text="СБРОС", command=stopVocabulary)
stopButton.place(x=80, y=450)

#для подсчета угаданых слов
wordCount = Label(root, text=f"Кол-во слов: {countWord}",font="Arial 17")
wordCount.place(x=80, y=220)

#для неотгаданых
word_Count = Label(root, text=f"Кол-во неправильных слов: {count_Word}",font="Arial 17")
word_Count.place(x=80, y=260)

#еще одна надпись
yourMistakes = Label(root, text="Your mistakes:", font="Arial 17")
yourMistakes.place(x=920,y=168)


#подключение скрола для вывода незнающих слов
txt = scrolledtext.ScrolledText(root, width=30, height=21, font="Arial 14")
txt.place(x=920,y=198)


#запрогать клавишу (забиньдить)
root.bind("<Return>", _key_)

#добавление версии в приложение
versionProgramm = Label(root, text="Version Beta-test: 0.1.0234", font="Arial 13")
versionProgramm.place(x=10, y=690)

# вызов словаря
loadVocabulary()
randWord()

root.mainloop()
