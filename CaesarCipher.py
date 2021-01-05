import tkinter as tk
from tkinter import messagebox
frame = tk.Tk()
frame.title("Caesar Cipher")
frame.geometry('500x300')

def encryption():

    input = msgInput.get(1.0, "end-1c")
    alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    digits = '0123456789'
    newMessage = ''
    key = keyInput.get(1.0, "end-1c")
    if key != "" and input != "":
        try:
            key = int(key)
        except:
            tk.messagebox.showinfo("Alert", "Wrong Value!")
        else:
            if key >= 1 and key <=25:
                for character in input:
                    if character in alphabet:
                        position = alphabet.find(character)
                        newPosition = (position + (2*key)) % 52
                        newCharacter = alphabet[newPosition]
                        newMessage += newCharacter
                    elif character in digits:
                        position = digits.find(character)
                        newPosition = (position + key) % 10
                        newCharacter = digits[newPosition]
                        newMessage += newCharacter
                    else:
                        newMessage += character
                lbl.config(text = 'The Encrypted message is: '+ newMessage)

            else:
                tk.messagebox.showinfo("Alert", "Wrong Value!")
    else:
        tk.messagebox.showinfo("Alert", "Wrong Value!")

def decryption():

    input = msgInput.get(1.0, "end-1c")
    alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    digits = '0123456789'
    newMessage2 = ''

    key = keyInput.get(1.0, "end-1c")
    if key != "" and input != "":
        try:
            key = int(key)
        except:
            tk.messagebox.showinfo("Alert", "Wrong Value!")
        else:
            if key >= 1 and key <=25:
                for character in input:
                    if character in alphabet:
                        position = alphabet.find(character)
                        newPosition = (position - (2*key)) % 52
                        newCharacter = alphabet[newPosition]
                        newMessage2 += newCharacter
                    elif character in digits:
                        position = digits.find(character)
                        newPosition = (position - key) % 10
                        newCharacter = digits[newPosition]
                        newMessage2 += newCharacter
                    else:
                        newMessage2 += character
                lbl.config(text = 'The Decrypted message is: '+ newMessage2)

            else:
                tk.messagebox.showinfo("Alert", "Wrong Value!")
    else:
        tk.messagebox.showinfo("Alert", "Wrong Value!")


L1 = tk.Label(frame, text = "Enter the key from 1-25:", font=1)
L1.pack()

keyInput = tk.Text(frame, height = 3, width = 30)
keyInput.pack()

L2 = tk.Label(frame, text = "Enter the message:", font=1)
L2.pack()

msgInput = tk.Text(frame, height = 3, width = 30)
msgInput.pack()

encButton = tk.Button(frame, text = "Encrypt",font=1, command = encryption)
encButton.pack()

decButton = tk.Button(frame, text = "Decrypt",font=1, command = decryption)
decButton.pack()

lbl = tk.Label(frame, text = "", font=1)
lbl.pack()
frame.mainloop()
