from random import randrange


s = input("heads or tails, call it in the air:")

coin = randrange (2)

if coin == 0 and s == 'heads':
  print("You won the coin toss")
  print("Will you kickoff or receive?")
elif coin ==1 and s == 'tails':
    print("You won the coin toss")   
else:
   print("I WON THE COIN TOSS")

   print ("Let's Start the Game!")