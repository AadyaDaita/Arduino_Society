#See hack 1 above, InfoDB lists
#See hack 2 above, InfoDB loops
def tester():
  # List with dictionary records placed in a list
  InfoDb = []
  
  InfoDb.append({  
       "FirstName": "Aadya",  
       "LastName": "Daita",  
       "DOB": "December 30",  
       "Residence": "San Diego",  
       "Email": "aadyadaita@gmail.com",  
       "Owns_Cars":["Tesla Model E","Tesla Model Y","Tesla Model X"]  
      })
  
  InfoDb.append({  
                 "FirstName": "John",  
                 "LastName": "Mortensen",  
                 "DOB": "October 21",  
                 "Residence": "San Diego",  
                 "Email": "jmortensen@powayusd.com",  
                 "Owns_Cars":["2015 Fusion","2011 Ranger","2003 Excursion","1997 F-350", "1969 Cadillac"]  
                })  
  
  InfoDb.append({  
                 "FirstName": "Sunny",  
                 "LastName": "Naidu",  
                 "DOB": "August 2",  
                 "Residence": "San Diego",  
                 "Email": "snaidu@powayusd.com",  
                 "Owns_Cars":["A","B","C"]  
                })  

  
  def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Cars: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Cars"]))  # join allows printing a string list with separator
    print()

#for loop
  def for_loop():
    for n in range(3):
      print_data(n)

  print("For loop")
  for_loop()
  
 #while loop 
  def while_loop():
    n = 0
    while n < 3:
      print_data(n)
      n += 1
      
  print("While loop")
  while_loop()

#recursive loop
  def recursive_loop(n):
    if n < len(InfoDb):
      print_data(n)
      n +=1 
      recursive_loop(n)
    return
          
  print("Recursive loop") 
  recursive_loop(0)


tester()

"""
MY PRINTER LOGIC W/O FUNCTIONS


input_person = int(input("which person...0,1 or 2?"))
input_cat = int(input("what category do you want...0,1,2,3,4,5?"))
input_n = int(input("n = "))
if input_cat == 4:
  x = InfoDb[input_person]["Owns_Cars"][input_n]
  print(x)



"""