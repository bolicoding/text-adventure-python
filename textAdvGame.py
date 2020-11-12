import time

answer_A = ["a", "A"]
answer_B = ["b", "B"]
answer_C = ["c", "C"]

def displayIntro():
  print("You are walking home from your friend's house and its very late.") 
  print("As you get to your car you notice you have a flat.")
  print("You kneel down to take a look at it and BAM you hear a noise... You will:")
  time.sleep(1)
  print("""  A. Get in your car call for help
  B. Drive off with a flat tire
  C. Go investigate""")
  
  choice = input("-->")
  if choice in answer_A:
    print("While you're calling for help the serial that made the noises approaches you and now you're dead.")
  elif choice in answer_B:
    print("You drove off all panicked you lose control crash and die.")
  elif choice in answer_C:
    print("Well you're dumb. That noise was made by a serial killer and now you're dead. What we learn?")
  else:
    print("required")
    displayIntro()
    
  playAgain = "yes"
  while playAgain == "yes" or playAgain == "y":
    playAgain = input("Do you want to play again? yes or y to continue playing: ")
    displayIntro()
displayIntro()


  