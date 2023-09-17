# 1. Take user input and turn it into the users move
# 2. Make a random number generator to generate computers move
# 3. compare and secide winner 
# 4. Best out of 3.  display winner and reset game 

#Player input

def player_move():
  m = ""
  
  while True:
    print("Allowed Inputs: R, P, S \n\n")
    move = input("Whats your move: ")
    m = move
    
    if m == "R" or m == "P" or m == "S":
      print()
      print(f"You chose {m}\n")
      break
    
    else:
      print()
      print("Wrong move \n")

  return m



#---------------

#Now the machines move 

#We will make a random number generator between 1-3 
def computer_move():
  c = ""
  
  import random
  random_num = random.randint(1,3)

  if random_num == 1:
    c = "R"

  elif random_num == 2:
    c = "P"

  else:
    c = "S"

  print(f"Computer: {c}")
  print("---------------------------")
  return c
  


# comparison 

def comparison():
  games = 0
  count_p = 0
  count_c = 0
  
  

  while games < 3:
    a = player_move()
    b = computer_move()
    if a == b:
      print("TIE ")
      games += 1
      count_p += 1
      count_c += 1
      #rock vs Paper
    elif a == "R" and b == "P":
      games += 1
      count_c += 1
      #Paper vs Siccors
    elif a == "P" and b == "S":
      games += 1
      count_c += 1
      # Scissors vs rock
    elif a == "S" and b == "R":
      games += 1
      count_c += 1

    elif b == "R" and a == "P":
      games += 1
      count_p += 1
      #Paper vs Siccors
    elif b == "P" and a == "S":
      games += 1
      count_p += 1
      # Scissors vs rock
    elif b == "S" and a == "R":
      games += 1
      count_p += 1
      
  if count_c > count_p:
    print("Conputer won")
  else:
    print("Player won")

comparison()


