#See hack 1 above, InfoDB lists
#See hack 2 above, InfoDB loops
def tester():
  # List with dictionary records placed in a list
  InfoDb = []
  
  InfoDb.append({  
       "FirstName": "Aadya",  
       "LastName": "Daita",  
       "Favorite Number": "30",  
       "Age": "15",  
       "Favorite Color": "green",  
       "Favorite_subjects":["CSP", "Math", "Chem", "History"]  
      })
  
  InfoDb.append({  
                 "FirstName": "John",  
                 "LastName": "Mortensen",  
                 "Favorite Number": "21",  
                 "Age": "30",  
                 "Favorite Color": "blue",  
                 "Favorite_subjects":["Math", "Science", "English", "Art"]  
                })  
  
  InfoDb.append({  
                 "FirstName": "Sunny",  
                 "LastName": "Naidu",  
                 "Favorite Number": "2",  
                 "Age": "30",  
                 "Favorite Color": "purple",  
                 "Favorite_subjects":["A","B","C"]  
                })  

  
  def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Cars: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Favorite_subjects"]))  # join allows printing a string list with separator
    print()

#for loop
#Python For Loops
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages. With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
#The range() Function:
#To loop through a set of code a specified number of times, we can use the range() function,
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

    
  def for_loop():
    for n in range(3):
      print_data(n)

  print("For loop")
  for_loop()
  
 #while loop 
  #With the while loop we can execute a set of statements as long as a condition is true or false.
  def while_loop():
    n = 0
    while n < 3:
      print_data(n)
      n += 1
      
  print("While loop")
  while_loop()

#recursive loop
#Recursion means a defined function can call itself.
#The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. There must be a termination/exit condition that allows the function to exit without calling itself. This condition allows the recursion to stop - that is, without it the function would call itself over and over again, resulting in an error. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
  
  def recursive_loop(n):
    if n < len(InfoDb):
      print_data(n)
      n +=1 
      recursive_loop(n)
    return
          
  print("Recursive loop") 
  recursive_loop(0)


tester()


#MY PRINTER LOGIC W/O FUNCTIONS


#input_person = int(input("which person...0,1 or 2?"))
#input_cat = int(input("what category do you want...0,1,2,3,4,5?"))
#input_n = int(input("n = "))
#if input_cat == 4:
#  x = InfoDb[input_person]["Owns_Cars"][input_n]
#  print(x)


