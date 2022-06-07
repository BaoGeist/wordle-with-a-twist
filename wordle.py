#imports
import tkinter as tk
lst_five = []

#importing all the valid 5 letter words
f = open('banana.txt')
for line in f:
    string = line.strip('\n')
    if len(string) == 5:
        lst_five.append(string)

'''Class for each row of the drawing
Instance Variables
- root, where the row will be placed in the UI
- word, the guessed word that will be processed
- index, the index of the guess
- master_word, the correct word, default is 'penis' but can be changed on line 28
- lst_match, a list for the matching letters between the guessed word and master word
Methods
- words_validate, returns lst_match
- letters_unique, returns a dictionary with the unique letters of a provided word
- draw, used to draw the row'''
class txt_five:
    def __init__(self, root, word, index):
        self.root = root
        self.word = word
        self.index = index
        self.master_word = 'penis'
        self.lst_match = self.word_validate()
        self.draw()
    
    def word_validate(self):
        lst_match = [0, 0, 0, 0, 0]
        master_word = self.master_word
        dic_master = self.letters_unique(self.master_word)
        dic_word = {}
        txt_succ, txt_fail = lblSucc2['text'], lblFail2['text']
        for i in range(5):
            #checks if you got the word right away
            if self.word == master_word:
                top = tk.Toplevel(root)
                top.geometry("100x100")
                top.title("good job")
                tk.Label(top, text= "you got the word!").pack()
                lst_match = [1, 1, 1, 1, 1]
                entTemp.config(state='disabled')
                break

            #checks if you got a matching letter, returns 1
            elif self.word[i] == master_word[i]:
                if not self.word[i] in dic_word.keys():
                    dic_word[self.word[i]] = 1
                else:
                    dic_word[self.word[i]] = dic_word[self.word[i]] + 1
                lst_match[i] = 1
                if not self.word[i] in txt_succ:
                    txt_succ = lblSucc2['text']
                    txt_succ += self.word[i]
                    lblSucc2['text'] = txt_succ
                    
            #chekcs if you got a letter that's also in the word, returns 2
            elif self.word[i] in master_word:
                if not self.word[i] in dic_word.keys():
                    dic_word[self.word[i]] = 1
                else:
                    dic_word[self.word[i]] = dic_word[self.word[i]] + 1
                if dic_word[self.word[i]] > dic_master[self.word[i]]:
                    lst_match[i] = 0
                else:
                    lst_match[i] = 2
                if not self.word[i] in txt_succ:
                    txt_succ = lblSucc2['text']
                    txt_succ += self.word[i]
                    lblSucc2['text'] = txt_succ
            
            #you didnt get the letter, returns 0
            else:
                if not self.word[i] in dic_word.keys():
                    dic_word[self.word[i]] = 1
                else:
                    dic_word[self.word[i]] = dic_word[self.word[i]] + 1
                lst_match[i] = 0
                if not self.word[i] in txt_fail and not self.word[i] == '_':
                    txt_fail = lblFail2['text']
                    txt_fail += self.word[i]
                    lblFail2['text'] = txt_fail

        #matching sure repeating letters that may match don't show up as green, but red
        for key in dic_master:
            try:
                if dic_master[key] < dic_word[key]:
                    for i in range(5):
                        if self.word[i] in master_word and self.word[i] != master_word[i]:
                            lst_match[i] = 0
            except:
                pass

        return lst_match

    def letters_unique(self, word: str) -> dict:
        dic_letters = {}
        for letter in word:
            if not letter in dic_letters.keys():
                dic_letters[letter] = 1
            else:
                dic_letters[letter] = dic_letters[letter] + 1
        return dic_letters
            
    def draw(self):
        lst_colour = []

        #default colouring
        if self.word == '_____':
            lst_colour = ['#F0F0F0', '#F0F0F0','#F0F0F0','#F0F0F0','#F0F0F0']
        else:
            for item in self.lst_match:
                #green
                if item == 1:
                    lst_colour.append('#8deb7a')
                #yellow
                elif item == 2:
                    lst_colour.append('#e3eb7a')
                #red
                else:
                    lst_colour.append('#cc5947')

        #draws them
        for i in range(5): 
            tk.Label(self.root, text = self.word[i], bg = lst_colour[i], height = 1, width = 5, relief=tk.RAISED, borderwidth=1).grid(row = self.index, column = i, padx = 3, pady = 2)

#function used to call the class txt_class 5 times to draw the 6 by 5 table
def draw_five(word: str, index: int) -> None:
    txt_five(frmBottom, word, index)

#checks the word to make sure its valid
def check_word():
    word = entTemp.get()

    #length check
    if not len(word) == 5:
        lblUser['text'] = 'Make sure you only enter 5 letters'
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
        
#inputs word if valid, stops program if at maximum guesses
def input_word(e):
    global lst_words
    global int_words
    stor = check_word() 
    if not(stor == None):
        lst_words[int_words] = stor
        for i in range(6):
            draw_five(lst_words[i],i)
            if i == 5 and lst_words[i] != '_____':
                top = tk.Toplevel(root)
                top.geometry("100x100")
                top.title("good job")
                tk.Label(top, text= "you fucking suck!").pack()
                entTemp.config(state='disabled')
        int_words += 1

#mainframe of the UI
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

#drawing the initial rows
global lst_words
global int_words
lst_words = ['_____','_____','_____','_____','_____','_____']
int_words = 0
for i in range(6):
    draw_five(lst_words[i],i)

#binding enter to input
root.bind('<Return>',input_word)

root.mainloop()
