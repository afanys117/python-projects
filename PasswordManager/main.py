from tkinter import messagebox
import tkinter
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generatePassword():
    passwordLetters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    passwordSymbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    passwordNumbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    passwordList = passwordLetters + passwordSymbols + passwordNumbers
    random.shuffle(passwordList)
    password = "".join(passwordList)

    passwordEntry.delete(0, tkinter.END)
    passwordEntry.insert(0, password)
    # To copy password to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def saveData():
    websiteEntryData = websiteEntry.get()
    emailEntryData = emailUsernameEntry.get()
    passwordEntryData = passwordEntry.get()
    newData = {
        websiteEntryData: {
            "email": emailEntryData,
            "password": passwordEntryData
        }
    }

    if len(websiteEntryData) == 0 or len(emailEntryData) == 0 or len(passwordEntryData) == 0:
        messagebox.showinfo(title="Error", message="Please make sure that you have not left any fields empty.")
    else:
        isOk = messagebox.askokcancel(title=websiteEntryData,
                                      message=f"These are the details entered:\n Email: \n{emailEntryData}"
                                              f"\nPassword: {passwordEntryData} \n Is it ok to save?")
        if isOk:
            try:
                with open("data.json", "r") as dataFile:
                    # Reading the old data
                    data = json.load(dataFile)
            except FileNotFoundError:
                with open("data.json", "w") as dataFile:
                    json.dump(newData, dataFile, indent=4)
            else:
                # Updating the old data
                data.update(newData)
                with open("data.json", "w") as dataFile:
                    # Saving the new data
                    json.dump(data, dataFile, indent=4)
            finally:
                # To clear the entries
                websiteEntry.delete(0, tkinter.END)
                emailUsernameEntry.delete(0, tkinter.END)
                passwordEntry.delete(0, tkinter.END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def findPassword():
    websiteEntryData = websiteEntry.get()

    if len(websiteEntryData) == 0:
        messagebox.showinfo(title="Error", message="Please make sure that you have not left any fields empty.")
    else:
        try:
            with open("data.json", "r") as dataFile:
                # Reading the data
                data = json.load(dataFile)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data file found.")
        else:
            if websiteEntryData in data.keys():
                email = data[websiteEntryData]["email"]
                password = data[websiteEntryData]["password"]
                messagebox.showinfo(title=websiteEntryData,
                                    message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for the {websiteEntryData} exist.")
        finally:
            # To clear the entries
            websiteEntry.delete(0, tkinter.END)
            emailUsernameEntry.delete(0, tkinter.END)
            passwordEntry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = tkinter.Canvas(height=200, width=200)
logoImage = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logoImage)
canvas.grid(row=0, column=1)

# Labels
websiteLabel = tkinter.Label(text="Website:")
websiteLabel.grid(row=1, column=0)
emailUsernameLabel = tkinter.Label(text="Email/Username:")
emailUsernameLabel.grid(row=2, column=0)
passwordLabel = tkinter.Label(text="Password:")
passwordLabel.grid(row=3, column=0)

# Entries
websiteEntry = tkinter.Entry(width=38)
websiteEntry.grid(row=1, column=1)
websiteEntry.focus()
emailUsernameEntry = tkinter.Entry(width=57)
emailUsernameEntry.grid(row=2, column=1, columnspan=2)
# emailUsernameEntry.insert(0, "name@gmail.com")
passwordEntry = tkinter.Entry(width=38)
passwordEntry.grid(row=3, column=1)

# Buttons
generateButton = tkinter.Button(text="Generate Password", command=generatePassword)
generateButton.grid(row=3, column=2)
addButton = tkinter.Button(text="Add", command=saveData, width=48)
addButton.grid(row=4, column=1, columnspan=2)
searchButton = tkinter.Button(text="Search", command=findPassword, width=14)
searchButton.grid(row=1, column=2)

window.mainloop()
