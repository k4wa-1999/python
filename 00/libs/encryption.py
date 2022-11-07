from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)
print(f"key =  {key}")
msg = cipher.encrypt("MTAzMzI1NDQwMDMyMTM5NjgzNg.G-IZtE.RMdqrEORjz44SSG2bgicenYgYC5eZIqn2hmABs".encode("utf-8"))
print(msg)

msg_hukugou = cipher.decrypt(msg)
print(cipher.decrypt(msg).decode("utf-8"))