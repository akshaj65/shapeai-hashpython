import hashlib
import os
salt=os.urandom(16)

message = input("Enter the string: ")
saltedMessage=str(salt)+message

print("sha256: "+hashlib.sha256(saltedMessage.encode()).hexdigest())
print("md5: "+hashlib.md5(saltedMessage.encode()).hexdigest())
print("sha512: "+hashlib.sha512(saltedMessage.encode()).hexdigest())
print("")
smessage=input("Enter the string: ")
hmessage=input("Enter the hashed value: ")
saltedHmessage=str(salt)+smessage

if(len(hmessage)==64):
   hresult=hashlib.sha256(saltedHmessage.encode()).hexdigest()
   algo="sha256"
elif(len(hmessage)==128):
   hresult=hashlib.sha512(saltedHmessage.encode()).hexdigest()
   algo="sha512"
elif(len(hmessage)==32):
   hresult=hashlib.md5(saltedHmessage.encode()).hexdigest()
   algo="md5"
if(hresult==hmessage):
   print("{ "+str(smessage)+" } is the string for the given hash "+algo)
   print("salt used was: "+saltedHmessage[:-(len(smessage))])
else:
    print("string does not match with the hash "+algo)
