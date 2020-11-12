import time

answer_A = ["a", "A"]
answer_B = ["b", "B"]
answer_C = ["c", "C"]

def displayIntro():
  print("You are walking home from your friend's house and its very late.") 
  print("As you get to your car you notice you have a flat.")
  print("You kneel down to take a look at it and BAM you hear a noise... You will:")
  time.sleep(5)
  print("""  A. Get in your car call for help
  B. Drive off with a flat tire
  C. Go investigate""")
  
  choice = input("-->")
  if choice in answer_A:
    print("While you're calling for help the serial killer that made the noises approaches you and now you're dead.")
  elif choice in answer_B:
    print("You drove off all panicked you lose control crash and die.")
  elif choice in answer_C:
    option_look()
  else:
    print("required")
    displayIntro()


answer_run = ["run", "Run"]
answer_surrender = ["surrender", "Surrender"]
    
def option_look():
  print("You notice there is some movement behind a dumpster and you step closer to see what it is...")
  time.sleep(1)
  print("you see its a man holding a knife... You will:")
  print("Run or Surrender") 
  
  choice = input("-->")
  if choice in answer_run:
    print("YOU ESCAPED")
  elif choice in answer_surrender:
    print("you died")
  else:  
    print("required")
    option_look()

playAgain = " "
if playAgain == "yes" or playAgain == "y":
  displayIntro()
  playAgain = input("Do you want to play again? type yes or y to continue")

displayIntro()


  