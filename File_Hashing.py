import hashlib

running = True

def SHA_256(data):
    sha_256 = hashlib.sha256()
    sha_256.update(data)
    return sha_256.hexdigest()

def MD_5(data):
    md_5 = hashlib.md5()
    md_5.update(data)
    return md_5.hexdigest()

def SHA_1(data):
    sha_1 = hashlib.sha1()
    sha_1.update(data)
    return sha_1.hexdigest()

def SHA_512(data):
    sha_512 = hashlib.sha512()
    sha_512.update(data)
    return sha_512.hexdigest() 

def SHA3_256(data):
    sha3_256 = hashlib.sha3_256()
    sha3_256.update(data)
    return sha3_256.hexdigest() 

def SHA3_512(data):
    sha3_512 = hashlib.sha3_512()
    sha3_512.update(data)
    return sha3_512.hexdigest()

def BLAKE2b(data):
    blake2b = hashlib.blake2b()
    blake2b.update(data)
    return blake2b.hexdigest()


while running:
   file_path = input("Enter the file path: ").strip()
   if file_path =="":
       print("Please enter a valid file path!")
       continue
   
   try:  
        with open(file_path , "rb") as file:
          data = file.read()

   except(FileNotFoundError):
        print("File not found!")
        continue
   
   except(PermissionError):
        print("You don't have permission to use this file!!")
        continue
   
   except(IsADirectoryError):
        print("This is a directory(folder)")
        continue

   except(OSError):
       print("The given path is invalid!")
       continue
 

   while True:
        choice = input('''Select an algorithm for your file
            1. SHA-1
            2. SHA-256
            3. SHA-512
            4. SHA3-256
            5. SHA3-512
            6. BLAKE2b
            7. MD5
            8. EXIT

            Enter your choice(number or name): ''').lower()
        if choice == "1" or choice == "sha-1":
            print(f"Hash value is : {SHA_1(data)}")
            break
        elif choice == "2" or choice == "sha-256":
            print(f"Hash value is : {SHA_256(data)}")
            break
        elif choice == "3" or choice == "sha-512":
            print(f"Hash value is : {SHA_512(data)}")
            break
        elif choice == "4" or choice == "sha3-256":
            print(f"Hash value is : {SHA3_256(data)}")
            break
        elif choice == "5" or choice == "sha3-512":
            print(f"Hash value is : {SHA3_512(data)}")
            break
        elif choice == "6" or choice == "blake2b":
            print(f"Hash value is : {BLAKE2b(data)}")
            break
        elif choice == "7" or choice == "md5":
            print(f"Hash value is : {MD_5(data)}")
            break
        elif choice == "8" or choice == "exit":
            running = False
            break
        else:
            print("Invalid Input!")

 
   