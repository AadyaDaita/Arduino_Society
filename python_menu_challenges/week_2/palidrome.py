string = input("Please enter your own Text : ")
str1 = ""

for i in string:
    str1 = i + str1  
print("Reverse Order :  ", str1)

if(string == str1):
   print("This is a Palindrome String")
else:
   print("This is Not a Palindrome")