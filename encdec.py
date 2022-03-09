
from cryptography.fernet import Fernet
import PIL.Image as Image
import io
import os

print("For this code, the __name__ is: " + __name__)

def createNewKey() -> str:
    # Create a new key
    myKey = Fernet.generate_key()
    keyname = f"{myKey.decode()[:4]}.key" # Uses the first 4 characters of the key for the name

    # Export to .key file with a name that will match the encrypted files, for reference.
    with open(f"./{keyname}", 'wb') as key:
        key.write(myKey)
    print(f'Wrote key to file: {keyname}')
    print(f'Full key: {myKey}')
    return keyname


class fernetFile():
    def __init__(self, keyPath: str, filepath: str) -> None:
        self.keyPath = keyPath
        self.filepath = filepath
        self.f = Fernet(Fernet.generate_key()) # just so self.f be initialized

    def createFernetObject(self) -> Fernet:
        # Create a Fernet object, used to encrypt AND decrypt using this specific key
        with open(f"{self.keyPath}", 'rb') as bufferedKey:
            key = bufferedKey.read()
            print("Key: " + key)
            self.f = Fernet(key)

    def encryptFile(self) -> bytes:
        # Open the file and encrypt it
        with open(f'{self.filepath}', 'rb') as file:
            plaintext = file.read() # Read to file into memory
            cipher = self.f.encrypt(plaintext) # Encryption happens here
        return cipher

    def exportEncryptedFile(self, cipher) -> None:
        # Export encrypted file as a '.encrypted'
        filename = f'{self.filepath}_KEY={os.path.basename(self.keyPath)[:4]}.encrypted'

        with open(filename, 'wb') as encryptedFile:
            encryptedFile.write(cipher)
            print("Encryption complete")
            print(f"Wrote file: {filename}")


    def decryptFile(self) -> bytes:
        # Decrypt the cipher
        decryptedFile = self.f.decrypt(self.filepath)
        return decryptedFile

    def exportDecryptedFile(decryptedFile, filename) -> None:
        # Export the decrypted file

        if os.path.isfile(filename):  # remove existing file
            os.remove(filename)
            
        with open(f"{filename}", 'wb') as video: # write new file
            video.write(decryptedFile)

    def viewImage(decryptedFile):
        # Use Pillow lib to open and view the image without saving it
        img = Image.open(io.BytesIO(decryptedFile))
        img.show()