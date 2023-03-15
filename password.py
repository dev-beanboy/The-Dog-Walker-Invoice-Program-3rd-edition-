from cryptography.fernet import Fernet

global key 
global cipher_suite
import os

key = os.environ['key']
cipher_suite = Fernet(key)



from pathlib import Path
txt = Path("login_info/a/password").read_text()
print(txt)

passwordDB = cipher_suite.decrypt(txt)
passwordDB = passwordDB.decode("utf-8")
print(passwordDB)
