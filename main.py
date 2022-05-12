from email.mime import image
from tkinter import Tk, Button, Label, Frame
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageTk
from encdec import fernetFile
from encdec import createNewKey
import cv2
import os

IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.raw')
VIDEO_EXTENSIONS = ('.mp4', '.avi', '.mov', '.wmv', '.mkv', '.webm')
PREVIEW_SIZE = (350, 350)

class FilePathBuffer():
    def __init__(self, path):
        self.path = path

def selectFile():

    fpBuffer.path = askopenfilename()
    if fpBuffer.path == '': return

    if fpBuffer.path.endswith(".encrypted"):
        decryptBtn["state"] = "normal"
        selFileBtn["text"] = "Select Different File"
        confirmationLabel["text"] = "You've selected an encrypted file."
    else:
        encryptBtn["state"] = "normal"
        selFileBtn["text"] = "Select Different File"
        confirmationLabel["text"] = "You've selected a normal file. (not encrypted)"

    statusLabel["text"] = ""
    fileLabel["text"] = f"File Selected: '{os.path.split(fpBuffer.path)[1]}'"
    newKeyBtn["state"] = "disabled"

    # Depending on the file extension, display a preview thumbnail

    if fpBuffer.path.endswith(IMAGE_EXTENSIONS):
        # display the image file itself as the thumbnail
        thumb = Image.open(fpBuffer.path)

    elif fpBuffer.path.endswith(VIDEO_EXTENSIONS):
        # capture first frame of video to display as thumbnail
        videoCapture = cv2.VideoCapture(fpBuffer.path)
        ret, imageArray = videoCapture.read()
        thumb = Image.fromarray(imageArray)
    else:
        thumb = Image.open("./imgs/unknownfile.png") 
        
    displayThumbnail(thumb)

def encrypt():
    key = askopenfilename(title="Select your Key for Encryption", initialdir="./")
    if key == '': return
    fern = fernetFile(keyPath=key, filepath=fpBuffer.path) # This object holds file and key paths
    cipher = fern.encryptFile()
    fern.exportEncryptedFile(cipher)
    resetLabels()
    confirmationLabel['text'] = f'Successfully encrypted "{os.path.split(fpBuffer.path)[1]}"'
    fpBuffer.path = ""

def decrypt():
    # Decrypt it into memory
    keypath = askopenfilename(title="Select your Key for decryption", initialdir="./")
    if keypath == '': return
    fern = fernetFile(keyPath=keypath, filepath=fpBuffer.path) # This object holds file and key paths
    decryptedFile = fern.decryptFile()
    # Save the file
    fern.exportDecryptedFile(decryptedFile)
    confirmationLabel['text'] = f'Successfully decrypted: "{os.path.split(fpBuffer.path)[1]}"'
    resetLabels()

def newKey():
    keyname = createNewKey()
    confirmationLabel["text"] = f'New key generated: {keyname}'

def resetLabels():
    statusLabel["text"] = "Ready to select a file or create a new key"
    selFileBtn["text"] = "Select File"
    fileLabel["text"] = "No file selected"
    selFileBtn["state"] = "normal"
    newKeyBtn["state"] = "normal"
    decryptBtn["state"] = "disabled"
    encryptBtn["state"] = "disabled"
    displayThumbnail(Image.open("./imgs/unknownfile.png"))

def displayThumbnail(thumb):
    thumb.thumbnail(PREVIEW_SIZE, Image.ANTIALIAS)  # resize image to fit
    TkThumb = ImageTk.PhotoImage(thumb)
    imageLabel["image"] = TkThumb
    imageLabel.TkThumbnail = TkThumb

if __name__ == "__main__":
    fpBuffer = FilePathBuffer(path="")
    root = Tk()
    root.title("Encrypt/Decrypt Interface")

    # Frames
    bodyFrame = Frame(root, width="700px", height="500px")
    bodyFrame.grid(row=0, column=0, padx=10, pady=2)

    leftFrame = Frame(bodyFrame, width="300px", height="500px")
    leftFrame.grid(row=0, column=0, padx=10, pady=2)
    
    rightFrame = Frame(bodyFrame, width="300px", height="500px", highlightbackground="black", highlightthickness=1)
    rightFrame.grid(row=0, column=1, padx=10, pady=2)
    
    footerFrame = Frame(root, height="100px")
    footerFrame.grid(row=1, padx=10, pady=2)

    # Left Frame Contents    
    statusLabel = Label(leftFrame, text="Ready to select a file or create a new key")
    statusLabel.grid(row=0, padx=10, pady=2)
    selFileBtn = Button(leftFrame, text="Select File", command=selectFile,padx=50, pady=15)
    selFileBtn.grid(row=1, padx=10, pady=2)
    encryptBtn = Button(leftFrame, text="Encrypt it", command=encrypt, padx=50, pady=15, state="disabled")
    encryptBtn.grid(row=2, padx=10, pady=2)
    decryptBtn = Button(leftFrame, text="Decrypt it", command=decrypt, padx=50, pady=15, state="disabled")
    decryptBtn.grid(row=3, padx=10, pady=2)
    newKeyBtn = Button(leftFrame, text="Generate New Key", command=newKey, padx=50)
    newKeyBtn.grid(row=4, padx=10, pady=2)
    confirmationLabel = Label(leftFrame, text=f"")
    confirmationLabel.grid(row=5, padx=10, pady=2)

    # Right Frame Contents
    previewLabel = Label(rightFrame, text="Preview:")
    previewLabel.grid(row=0, padx=10, pady=2)

    imageLabel = Label(rightFrame)
    imageLabel.grid(row=1, padx=10, pady=2)
    displayThumbnail(Image.open("./imgs/unknownfile.png"))

    fileLabel = Label(rightFrame, text="No file selected")
    fileLabel.grid(row=2, padx=10, pady=2)

    # Footer Frame Contents
    authorLabel = Label(footerFrame, text="Peginaw 2022")
    authorLabel.grid(row=0, padx=10, pady=2)

    root.mainloop()

    ### DEBUGGING FRAME COLOURS
    #bodyFrame['bg'] = 'red'
    #leftFrame['bg'] = 'red'
    #rightFrame['bg'] = 'green'
    #footerFrame['bg'] = 'yellow'
    
