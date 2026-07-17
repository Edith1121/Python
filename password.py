import string
running = True
while running:
    passw = input("Enter Your Password: ")
    if len(passw) <= 8:
        print("The Password should atleast contain 8 characters")
        continue
    else:
        break

digit_count = 0
uppercase_count = 0
lowercase_count = 0
special_character_count = 0
for ch in passw:
    if ch.isdigit():
        digit_count +=1
    elif ch.isupper():
        uppercase_count +=1
    elif ch.islower():
        lowercase_count +=1
    elif ch in string.punctuation:
        special_character_count += 1



print(f"No.of integers in your pass is {digit_count}")
print(f"No.of alphabets in uppercase in your pass is {uppercase_count}")
print(f"No.of alphabets in lowercase in your pass is {lowercase_count}")
print(f"No.of special characters in your pass is {special_character_count}")

countnop = digit_count*3
countaup = uppercase_count*4
countalp = lowercase_count*2
countsplp = special_character_count*5

score = countnop+countaup+countalp+countsplp
point = ((score-16) / (50-16))*10
pointfinal = round(point,1)
print(f"The toughness of your password is {pointfinal}/10")
