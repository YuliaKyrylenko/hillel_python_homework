from string import punctuation
from keyword import kwlist

name = input("Please enter your variable name: ")
punct_replace = punctuation.replace("_","")
result = "True"

if (name[0].isdigit()
    or any(up_letter.isupper() for up_letter in name)
    or "__" in name
    or " " in name
    or any(znak in punct_replace for znak in name)
    or name in kwlist):
    result = "False"
print(result)