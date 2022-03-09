from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from encdec import fernetFile
from encdec import createNewKey
import os


root = Tk()

class FilePathBuffer():
    def __init__(self, path):
        self.path = path

def selectFile():
    fpBuffer.path = askopenfilename()
    if fpBuffer.path.endswith(".encrypted"):
        decryptBtn["state"] = "normal"
        selFileBtn["text"] = "Select Different File"
        infoLabel["text"] = "You've selected an encrypted file."
    else:
        encryptBtn["state"] = "normal"
        selFileBtn["text"] = "Select Different File"
        infoLabel["text"] = "You've selected a normal file."

    fileLabel["text"] = f"File Selected: '{os.path.split(fpBuffer.path)[1]}'"
    newKeyLabel["text"] = ''
    newKeyBtn["state"] = "disabled"

def encrypt():
    # Get key from user
    key = askopenfilename(title="Select your Key for encryption", initialdir="./")
    selFileBtn["state"] = "normal"
    # Create Fernet instance encrypt the file, export it
    fern = fernetFile(keyPath=key, filepath=fpBuffer.path)
    cipher = fern.encryptFile()
    fern.exportEncryptedFile(cipher)
    fpBuffer.path = ""
    resetLabels()

def decrypt():
    # Get key from user
    key = askopenfilename(title="Select your Key for decryption", initialdir="./")
    selFileBtn["state"] = "normal"
    # Create Fernet instance, decrypt the file, export it
    fern = fernetFile(keyPath=key, filepath=fpBuffer.path)
    decryptedFile = fern.decryptFile()
    saveName = asksaveasfilename(confirmoverwrite=True ,initialdir="./", filetypes=(("jpg file", "*.jpg"),("png file", "*.png"),("mp4 file", "*.mp4"),("All Files", "*.*") ), defaultextension=".jpg", initialfile=fern.filepath)
    fern.exportDecryptedFile(decryptedFile, saveName)
    resetLabels()

def newKey():
    keyname = createNewKey()
    newKeyLabel["text"] = f'New key generated: {keyname}'

def resetLabels():
    infoLabel["text"] = "Select a file to encrypt or decrypt"
    selFileBtn["text"] = "Select File"
    newKeyBtn["state"] = "normal"
    decryptBtn["state"] = "disabled"
    encryptBtn["state"] = "disabled"



if __name__ == "__main__":
    fpBuffer = FilePathBuffer(path="")
    infoLabel = Label(root, text="Select a file to encrypt or decrypt")
    infoLabel.pack()
    selFileBtn = Button(root, text="Select File", command=selectFile,padx=50, pady=15)
    selFileBtn.pack()
    encryptBtn = Button(root, text="Encrypt it", command=encrypt, padx=50, pady=15, state="disabled")
    encryptBtn.pack()
    decryptBtn = Button(root, text="Decrypt it", command=decrypt, padx=50, pady=15, state="disabled")
    decryptBtn.pack()
    fileLabel = Label(root, text=f"No file selected")
    fileLabel.pack()
    newKeyBtn = Button(root, text="Generate New Key", command=newKey, padx=50)
    newKeyBtn.pack()
    newKeyLabel = Label(root, text=f"")
    newKeyLabel.pack()
    authorLabel = Label(root, text=f"Simon Pequegnat 2022")
    authorLabel.pack()

    root.mainloop()
    
