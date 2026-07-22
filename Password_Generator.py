import string
import secrets

chars=(
    string.ascii_uppercase +
    string.ascii_lowercase +
    string.digits +
    string.punctuation
)

def repeated_chars(password):
    for ch in set(password):
        if password.count(ch) >=4:
            return True
        
    return False

def has_sequential_chars(password):
    count = 1

    for i in range(1, len(password)):
        if password[i].islower() and password[i-1].islower():
            if ord(password[i]) == ord(password[i-1]) + 1:
                count += 1
            else:
                count = 1

        elif password[i].isupper() and password[i-1].isupper():
            if ord(password[i]) == ord(password[i-1]) + 1:
                count += 1
            else:
                count = 1

        elif password[i].isdigit() and password[i-1].isdigit():
            if ord(password[i]) == ord(password[i-1]) + 1:
                count += 1
            else:
                count = 1

        else:
            count = 1

        if count >= 4:
            return True

    return False
     
    
def reverse_sequential_chars(password):
    rev_count = 1
    for i in range(1,len(password)):
     if password[i].islower() and password[i-1].islower():
       if ord(password[i]) == ord(password[i-1])-1:
          rev_count += 1
       else:
          rev_count=1

     elif password[i].isupper() and password[i-1].isupper():
       if ord(password[i]) == ord(password[i-1])-1:
          rev_count += 1
       else:
          rev_count = 1

     elif password[i].isdigit() and password[i-1].isdigit():
        if ord(password[i]) == ord(password[i-1])-1:
          rev_count += 1
        else:
           rev_count =1

     else:
           rev_count=1
        
     if rev_count>=4:
       return True
     
    return False

    
while True:
    password = "".join(secrets.choice(chars) for _ in range(16))

    if repeated_chars(password):
        continue

    if has_sequential_chars(password):
        continue

    if reverse_sequential_chars(password):
        continue

    break
print(password)
