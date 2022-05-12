from cryptography.fernet import Fernet
from PIL import Image, ImageTk
import io
import os

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
        with open(keyPath, 'rb') as keyFile:
            keyString = keyFile.read()
            self.f = Fernet(keyString)

    def createFernetObject(self) -> Fernet:
        # Create a Fernet object, used to encrypt AND decrypt using this specific key
        with open(f"{self.keyPath}", 'rb') as bufferedKey:
            key = bufferedKey.read()
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
        with open(self.filepath, 'rb') as cipher:
            cipherBytes = cipher.read()
            decryptedFile = self.f.decrypt(cipherBytes)
            print("Decryption complete")
            return decryptedFile

    def exportDecryptedFile(self, decryptedFile) -> None:
        originalName = f'{self.filepath.rpartition("_KEY=")[0]}'
        name, dot, ext = originalName.rpartition(".")
    
        newName = f'{name}-decrypted{dot}{ext}'


        if os.path.isfile(newName):  # check for a collision
            raise FileExistsError(f'Cannot overwrite existing "{newName}" file')
            
        with open(f"{newName}", 'wb') as file: # write new file
            file.write(decryptedFile)
            print(f"Wrote file: {newName}")

    def viewImage(decryptedFile):
        # Use Pillow lib to open and view the image without saving it
        img = Image.open(io.BytesIO(decryptedFile))
        img.show()