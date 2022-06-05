import tkinter as tk

lst_five = []

f = open('banana.txt')
for line in f:
    string = line.strip('\n')
    if len(string) == 5:
        lst_five.append(string)

class txt_five:
    def __init__(self, root, word, index):
        self.root = root
        self.word = word
        self.index = index
        self.lst_match = self.word_validate()
        self.draw()
    
    def word_validate(self):
        lst_match = [0, 0, 0, 0, 0]
        master_word = 'penis'
        txt_succ, txt_fail = '', ''
        for i in range(5):
            if self.word == master_word:
                top = tk.Toplevel(root)
                top.geometry("750x250")
                top.title("good job")
                tk.Label(top, text= "you got the word!").place(x=150,y=80)
                break
            elif self.word[i] == master_word[i]:
                lst_match[i] = 1
                if not self.word[i] in txt_succ:
                    txt_succ = lblSucc2['text']
                    txt_succ += self.word[i]
                    lblSucc2['text'] = txt_succ
            elif self.word[i] in master_word:
                lst_match[i] = 2
                if not self.word[i] in txt_succ:
                    txt_succ = lblSucc2['text']
                    txt_succ += self.word[i]
                    lblSucc2['text'] = txt_succ
            else:
                lst_match[i] = 0
                if not self.word[i] in txt_fail and not self.word[i] == '_':
                    txt_fail = lblFail2['text']
                    txt_fail += self.word[i]
                    lblFail2['text'] = txt_fail
        return lst_match

    def draw(self):
        lst_colour = []
        if self.word == '_____':
            lst_colour = ['#F0F0F0', '#F0F0F0','#F0F0F0','#F0F0F0','#F0F0F0']
        else:
            for item in self.lst_match:
                if item == 1:
                    lst_colour.append('#8deb7a')
                elif item == 2:
                    lst_colour.append('#e3eb7a')
                else:
                    lst_colour.append('#cc5947')

        for i in range(5): 
            tk.Label(self.root, text = self.word[i], bg = lst_colour[i], height = 1, width = 5, relief=tk.RAISED, borderwidth=1).grid(row = self.index, column = i, padx = 3, pady = 2)

def draw_five(word, index):
    obj_draw = txt_five(frmBottom, word, index)

def acquire_words():
    lst_five = []
    f = open('banana.txt')
    for line in f:
        string = line.strip('\n')
        if len(string) == 5:
            lst_five.append(string)
    return(lst_five)

def check_word():
    word = entTemp.get()

    #length check
    if not len(word) == 5:
        lblUser['text'] = 'Make sure you only enter 4 letters'
        return (None)

    #lpha check
    if word.isalpha():
        pass
    else:
        lblUser['text'] = 'Make sure you only enter letters'
        return (None)
    
    #letters check
    charWord = list(word)
    word = ''
    for i in range(5):
        word += charWord[i].lower()
    if word in lst_five:
        entTemp.delete(0, tk.END)
        return(word)
    else:
        lblUser['text'] = 'Make sure you enter actual words'
        return(None)
        

def input_word(e):
    global lst_words
    global int_words
    stor = check_word() 
    if not(stor == None):
        lst_words[int_words] = stor
        for i in range(6):
            draw_five(lst_words[i],i)
        int_words += 1
    
lst_five = acquire_words()

root = tk.Tk()
root.title('Penisdle')
root.geometry('342x183+40+40')
root.resizable(False, False) 

frmTop = tk.Frame(root, relief=tk.RAISED, borderwidth=1)
frmTop.grid(row=1, column = 0, sticky= 'nsew')
lblUser = tk.Label(frmTop, text = 'Enter your guess; must be five letters')
lblUser.grid(row = 0, column = 0, sticky= 'nsew')
entTemp = tk.Entry(frmTop)
entTemp.grid(row = 1, column = 0, sticky= 'nsew')

frmBottom = tk.Frame(root, relief=tk.RAISED, borderwidth=1)
frmBottom.grid(row = 0, column = 0, sticky= 'nsew')

frmRight = tk.Frame(root, relief=tk.RAISED, borderwidth=1)
frmRight.grid(row = 0, column = 1, rowspan = 2, sticky= 'nsew')
lblSucc = tk.Label(frmRight, text = 'Success Letters Here')
lblSucc.grid(row = 0, column = 0, sticky= 'nsew')
lblSucc2 = tk.Label(frmRight, text = '', height = 4)
lblSucc2.grid(row = 1, column = 0, sticky= 'nsew')
lblFail = tk.Label(frmRight, text = 'Failed Letter Here')
lblFail.grid(row = 2, column = 0, sticky= 'nsew')
lblFail2 = tk.Label(frmRight, text = '', height = 4)
lblFail2.grid(row = 3, column = 0, sticky= 'nsew')

global lst_words
global int_words
lst_words = ['_____','_____','_____','_____','_____','_____']
int_words = 0
for i in range(6):
    draw_five(lst_words[i],i)

root.bind('<Return>',input_word)

root.mainloop()

