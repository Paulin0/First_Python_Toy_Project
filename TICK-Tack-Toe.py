a_row = ["a1", "a2", "a3"]
b_row = ["b1", "b2", "b3"]
c_row = ["c1", "c2", "c3"]

separator = "-" * 18

#moves_left = 9


def table():
  print()
  print(a_row)
  print(separator)
  print(b_row)
  print(separator)
  print(c_row)
  print()
  print()


table()

c_turn = ""


#The computer logic
def computer_logic():
  import random

  char_list = ["a", "b", "c"]

  random_item = random.choice(char_list)

  last_char = random.randint(1, 3)

  computer_choice = F"{random_item}{str(last_char)}"

  return computer_choice

  #lets make a function with a loop inside with all the if statements and just run in th

  player = "X"
  computer = "O"


def fin():
  x = 1
  while x == 1:
    comp_move = computer_logic()

    if comp_move.startswith("a"):
      if comp_move.endswith("1") and a_row[0] == "a1":
        a_row[0] = "O"
        table()
        x = 0
        print(comp_move)

      elif comp_move.endswith("2") and a_row[1] == "a2":
        a_row[1] = "O"
        table()
        x = 0
        print(comp_move)

      elif comp_move.endswith("3") and a_row[2] == "a3":
        a_row[2] = "O"
        table()
        x = 0
        print(comp_move)
    elif comp_move.startswith("b"):
      if comp_move.endswith("1") and b_row[0] == "b1":
        b_row[0] = "O"
        table()
        x = 0
        print(comp_move)
      elif comp_move.endswith("2") and b_row[1] == "b2":
        b_row[1] = "O"
        table()
        x = 0
        print(comp_move)
      elif comp_move.endswith("3") and b_row[2] == "b3":
        b_row[2] = "O"
        table()
        x = 0
        print(comp_move)
    elif comp_move.startswith("c"):
      if comp_move.endswith("1") and c_row[0] == "c1":
        c_row[0] = "O"
        table()
        x = 0
        print(comp_move)
      elif comp_move.endswith("2") and c_row[1] == "c2":
        c_row[1] = "O"
        table()
        x = 0
        print(comp_move)
      elif comp_move.endswith("3") and c_row[2] == "c3":
        c_row[2] = "O"
        table()
        x = 0
        print(comp_move)


def test():

  move = input("move: ")

  #A row -----------------------------------
  if move.startswith("a"):
    if move.endswith("1"):
      #a1-----------------------------------
      if a_row[0] == "a1":
        a_row[0] = "X"
      else:
        print("\n Wrong move \n")
      table()
      #a2------------------------------------
    elif move.endswith("2"):
      if a_row[1] == "a2":
        a_row[1] = "X"
      else:
        print("\n Wrong move \n")
      table()
      #a3------------------------------------
    elif move.endswith("3"):
      if a_row[2] == "a3":
        a_row[2] = "X"
      else:
        print("\n Wrong move \n")
      table()

  #B row -------------------
  elif move.startswith("b"):
    if move.endswith("1"):
      if b_row[0] == "b1":
        b_row[0] = "X"
      else:
        print("\n Wrong move \n")
      table()
    elif move.endswith("2"):
      if b_row[1] == "b2":
        b_row[1] = "X"
      else:
        print("\n Wrong move \n")
      table()
    elif move.endswith("3"):
      if b_row[2] == "b3":
        b_row[2] = "X"
      else:
        print("\n Wrong move \n")
      table()

  #C row -------------------
  elif move.startswith("c"):
    if move.endswith("1"):
      if c_row[0] == "c1":
        c_row[0] = "X"
      else:
        print("\n Wrong move \n")
      table()
    elif move.endswith("2"):
      if c_row[1] == "c2":
        c_row[1] = "X"
      else:
        print("\n Wrong move \n")
      table()
    elif move.endswith("3"):
      if c_row[2] == "c3":
        c_row[2] = "X"
      else:
        print("\n Wrong move \n")
      table()


#----------------------------------------------------------
#Computers turn to make a move

#conditionals for winning
#First row
  if a_row.count("X") == 3:
    print("You Won")

has_won = False


#NOW ITS FINALLY TIME TO MAKE THE CONDITIONS FOR WINNING
#lets make the horizontal ones first
def win():
  global has_won
  if a_row.count("X") == 3 or a_row.count("O") == 3:
    if a_row.count("X") == 3:
      has_won = True
      return print("THE PLAYER HAS WON")
    elif a_row.count("O") == 3:
      has_won = True
      return print("THE COMPUTER HAS WON")

  elif b_row.count("X") == 3 or b_row.count("O") == 3:
    if b_row.count("X") == 3:
      has_won = True
      return print("THE PLAYER HAS WON")
    elif b_row.count("O") == 3:
      has_won = True
      return print("THE COMPUTER HAS WON")

  elif c_row.count("X") == 3 or c_row.count("O") == 3:
    if c_row.count("X") == 3:
      has_won = True
      return print("THE PLAYER HAS WON")
    elif c_row.count("O") == 3:
      has_won = True
      return print("THE COMPUTER HAS WON")
  #Now we the the verticals
    elif a_row[0] == "X" and a_row[0] == b_row[0] and b_row[0] == c_row[0]:
      has_won = True
      return print("THE PLAYER HAS WON")

    elif a_row[0] == "O" and a_row[0] == b_row[0] and b_row[0] == c_row[0]:
      has_won = True
      return print("THE COMPUTER HAS WON")

    #Now we will check the two horizontals
    elif a_row[0] == "X" and a_row[0] == b_row[1] and b_row[1] == c_row[2]:
      has_won = True
      return print("THE PLAYER HAS WON")
    elif a_row[2] == "0" and a_row[2] == b_row[1] and b_row[1] == c_row[0]:
      has_won = True
      return print("THE COMPUTER HAS WON")


def game():
  while not has_won:
    win()
    test()
    fin()
    if has_won:
      return


game()
