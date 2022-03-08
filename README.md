# Encrypt-Decrypt Interface
A simple GUI for encrypting and decrypting single files, and creating new encryption keys. No command line required.
No need to worry about destroying your original files, as this program will never overwrite your existing files, only make encrypted/decrypted copies.

### Quick-Start Guide:

1. Ensure you have the following dependencies installed. (These are just the versions I used. Other versions may work.)<br>
<ul>
  <li><b>Python 3.7 or higher</b></li>
  <ul>
    <li>You may download Python itself from the <a href="https://www.python.org/downloads/" target="_blank" rel="noopener noreferrer">official Python download page</a></li>
    <li>Or, download a package manager that includes Python, such as <a href="https://www.anaconda.com/products/individualAnaconda" target="_blank" rel="noopener noreferrer">Anaconda</a>, or <a href="https://docs.conda.io/en/latest/miniconda.html" target="_blank" rel="noopener noreferrer">Miniconda</a> (<-recommended)</li>
  </ul>
  <li><b>cryptography ~= 3.4.7</b> (Should already be included with Python. For doing the encryption/decryption)</li>
  <li><b>Tkinter ~= 8.6 </b>(Should already be included with Python. For displaying the GUI on your screen)</li>
  <li>
    Optional: Pillow ~= 9.0.1 (for displaying your selected images in the GUI)
    <ul><li>To install, run the command <code>pip3 install Pillow</code> in your command line of choice</li></ul>
  </li>
</ul>
2. Clone (download) this repository using the green "Clone" button on the home page for this project.<br>
3. Once downloaded, simply run the <code>main.py</code> python file found inside.

<hr>

## Summary

This tool can: 
<ul>
  <li>Generate new encryption keys</li>
  <li>Use a key to <b>encrypt</b> a file, which will have the extension: <code>.encrypted</code></li>
  <li>Use the same key to <b>decrypt</b> a <code>.encrypted</code> file</li>
</ul>
This tool uses the <a href="https://cryptography.io/en/latest/fernet/Fernet" target="_blank" rel="noopener noreferrer">Fernet</a> module, built into the Python 'cryptography' library, to perform encryption and decryption of single files.<br>
It operates with symmetrical encryption, meaning that it uses just a <b>single key for both encryting and decrypting files</b>.<br>

<hr>

## Using the interface

### Creating your first key

Start by clicking the "Generate New Key" button. This will create a random key for you to use for the rest of this process.<br>
The .key file will be saved in the same folder as the <code>main.py</code> file.<br>
The name of the .key file is the first 4 characters of the actual key found inside. This is to make it easy to keep track of which key is which.<br>
<strong>KEEP THIS KEY SAFE. YOU WILL NEED IT TO DECRYPT THE FILES LATER</strong>

> Example: A key is generated whose full text reads <code>at3ExZ0rN4eHG5hux9ggUAPeJnDZLlryn0uHWMRVRBk=</code>. The file will be named <code>at3E.key</code>.


### Select a File for Encryption or Decryption

Click "Select File". This will open up a dialog box where you can select a file.<br>

### Encrypting a File

Click "Encrypt it" and select the key you wish to use for encryption.<br>
An encrypted copy of the file will be saved in the same folder as the original file.
<b>The title of the encrypted file will include the name of the key used to encrypt it</b>

> Example: Encrypting the file <code>cats.png</code> with the key <code>at3E.key</code> will produce a file named <code>cats.png_KEY=at3E.encrypted</code>

### Decrypting a File

CLick "Select File" and choose your encrypted file.<br>
Click "Decrypt it" and select the key you originally used for encrypting this particular file (Hint: It's in the encrypted file's name)<br>
Finally, another dialog box will pop up for you to save your newly decrypted file.

> For safety, this program will not allow overwriting of existing files, so you must use a new name.

<hr>

## Future Plans
This tool is currently limited to working with files less than a few gigibytes in size. I plan to upgrade this in the future.
