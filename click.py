from getpass import getpass as input

p1m = input ("P1 make your move: mom, dad, or minigun?")
p2m = input ("P2 make your move: mom, dad, or minigun?")
if p1m == "mom" and p2m == "dad":
  print ("Mom and Dad are the same person! (tie)")
elif p1m == "dad" and p2m == "mom":
  print ("Dad and Mom are the same person! (tie)")
elif p1m == "mom" and p2m == "minigun":
  print("Mom grounds the minigun! (mom wins)")
elif p1m == "minigun" and p2m == "mom":
  print("Mom grounds the minigun! (mom wins)")
elif p1m == "dad" and p2m == "minigun":
  print("The minigun is too powerful! (minigun wins)")
elif p1m == "minigun" and p2m == "dad":
  print("The minigun is too powerful! (minigun wins)")
elif p1m == "mom" and p2m == "mom" or p1m == "dad" and p2m == "dad" or p1m == "minigun" and p2m == "minigun": 
  print("You chose the same thing. (try again)")
  import main.py
  exec(main.py)