import time
import os

userName = ""
satchel = []
dead = False
moves = 0
hill = "not done"
bread = "not got"
birdFriend = False
birdFirstTime = True
snakeBite = False
spiderBite = False
instructions = [
    "get", "grab", "pick", "take", "look", "check", "north", "n", "south", "s",
    "west", "w", "east", "e"
]


def gameOver():
  time.sleep(3)
  print(" ~~~~~~~~~~~ ")
  print("| GAME OVER |")
  print(" ~~~~~~~~~~~ ")
  exit()


def satchelCheck():
  global satchelCount
  global moves
  satchelCount = 1
  for item in satchel:
    print(satchelCount, "-", item)
    satchelCount += 1
  if len(satchel) == 0:
    print("you haven't got anything in your satchel!")
  moves += 1


def help():
  global instructions
  print("the instructions i know are:")
  for instruction in instructions:
    print("◦", instruction)


def planeSpawn():
  global moves
  exit = False
  userChoice = ""
  key = "not got"
  outPlane = False
  global dead
  
  print(
      "your memories fade and flash in front of you, while you force your eyes to open. your head is pounding while you start to remember how you ended up here."
  )
  time.sleep(7)
  print(
      "\n\nyou're supposed to be in some sunny island in the canary islands.")
  time.sleep(4)
  print("\n \nwell.")
  time.sleep(2.5)
  print(
      "\n \nat least it's warm. and there's a beach, guessing by the sound of the waves."
  )
  time.sleep(4)
  print(
      "\nyou look up at the cloud-filled sky- wait. how is it warm if it's cloudy?"
  )
  time.sleep(4)
  print("\nyou sit up.")
  time.sleep(3)
  print("your plane has crashed in the middle of some random island.")
  time.sleep(4)
  print("you knew you should never have booked the cheapest flight.")
  time.sleep(5)
  print("nothing or no one has survived.")
  time.sleep(3)
  print(
      "only your old trusty £5 handluggage - a satchel, which has been flung next to you onto some passed out passenger. your phone is on the floor, broken beyond repair."
  )
  time.sleep(9)
  print(
      "around the plane is cliffs; the only way out is towards the *rising sun*"
  )
  time.sleep(5)
  print("\n...")
  time.sleep(2)
  print(
      "\n\nyou can smell burning. so *that's* why it's so warm. now you have to figure out how to get out (quickly). "
  )
  #INPUT STUFF
  while not exit and not dead and moves < 7:
    userChoice = str(input("> ")).lower()
    if ("look" in userChoice
        or "check" in userChoice) and "satchel" in userChoice:
      satchelCheck()
    elif "help" in userChoice:
      help()
    elif "look around" in userChoice and key == "not got":
      print(
          "you look around, and something glints out of the corner of your eye. you turn back, and discover that's it's something under a seat"
      )
      moves += 1
    elif "look around" in userChoice:
      print("nothing else interesting to see here")
      moves += 1
    elif userChoice == "look":
      print("look where??")
    elif "look" in userChoice and "seat" in userChoice and key == "not got":
      print("you look under the seat and find a shiny key!")
      moves += 1
    elif "look" in userChoice and "seat" in userChoice:
      print("there's nothing else under the seat")
      moves += 1
    elif ("get" in userChoice or "grab" in userChoice or "pick" in userChoice
          or "take" in userChoice) and ("key" in userChoice or "it"
                                        in userChoice) and key == "not got":
      print(
          "you grab the key. it's adorned with intricate patterns. on the side, you can see a faint engraving saying 'LLRL.'"
      )
      time.sleep(6)
      print("strange.")
      time.sleep(2)
      print("you put it away in your satchel")
      satchel.append("key - says LLRL")
      key = "got"
      moves += 1
    elif ("get" in userChoice or "grab" in userChoice or "pick" in userChoice
          or "take" in userChoice) and ("key" in userChoice
                                        or "it" in userChoice):
      print("you've already got key")
    elif "phone" in userChoice:
      print("you tiptoe over to your phone, picking it up. you examine it.")
      time.sleep(3)
      print("yup.")
      time.sleep(2)
      print("definitely no use for this.")
      time.sleep(2)
      print("you chuck your phone away")
      moves += 1
    elif "out" in userChoice:
      print(
          "you heave yourself out of the plane bringing the hand luggage with you."
      )
      moves += 1
      outPlane = True
    elif (userChoice == "e" or "east" in userChoice) and outPlane is True:
      exit = True
      moves += 1
    elif ((userChoice == "n" or "north" in userChoice) or
          (userChoice == "s" or "south" in userChoice) or
          (userChoice == "w" or "west" in userChoice)) and outPlane is True:
      print("you fall off the cliff and fall to your tragic death.")
      dead = True
    elif (userChoice == "e" or "east"
          in userChoice) or (userChoice == "n" or "north" in userChoice) or (
              userChoice == "s" or "south"
              in userChoice) or (userChoice == "w" or "west" in userChoice):
      print("get out of the plane first!")
    else:
      print("i don't understand. sorry.")
  if moves > 6:
    print(
        "you spend too long in the plane, and it explodes before you escape, killing you in the process."
    )
    dead = True
  if dead == True:
    gameOver()
  if exit == True:
    print(
        "you manage to get out just in time before the plane explodes."
    )
    print(
        "you look ahead, and see a valley. sunlight casts dappled light on weathered *rocks* in the *rocky* landscape."
    )
  time.sleep(6)
  print(
      "these serene *rocks* are everywhere you look- you should probably remember the rocks."
  )
  valley()


def valley():
  global moves
  global hill
  exit = False
  userChoice = ""
  sure = ""
  sureDec = "not valid"
  print("        _       _ ")
  print("       / \_    / \_                      /\ __ ")
  print("      /_   \  /    \_                  _/  /  \  ")
  print("     /  \  /\/    __ \_             _ /   /    `--.")
  print("    /    \/  \  _/  \-'\           /     _        / \ ")
  print("  /\          \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \ ")
  print(" /           / .--.--\ =-=~_=-=~=^/  _ `--.  .     `-")
  print("/           / /       `.~-^=-=~=^=.-'      \ ")
  while not exit:
    userChoice = str(input("> ")).lower()
    if (userChoice == "n" or "north" in userChoice) and hill == "done":
      exit = True
      moves += 1
      abandonedShack()
    elif (userChoice == "n" or "north" in userChoice) and hill == "not done":
      print("i would recommend going east to the hill first")
    elif "look around" in userChoice:
      print(
          "i've *literally* painted you a picture of the place. i'm not sure what else you want me to describe."
      )
    elif ("look" in userChoice
          or "check" in userChoice) and "satchel" in userChoice:
      satchelCheck()
    elif "help" in userChoice:
      help()
    elif (userChoice == "e" or "east" in userChoice) and hill == "not done":
      exit = True
      moves += 1
      print(
          "to the east, there is a hill with some glittery thing at the peak"
      )
      hill = "done"
      hillLizard()
    elif (userChoice == "e" or "east" in userChoice) and hill == "done":
      print("you can't go back to the hill.")
    elif userChoice == "s" or "south" in userChoice:
      print("you fall off the cliff and fall to your tragic death.")
      gameOver()
    elif userChoice == "w" or "west" in userChoice:
      print("that's going back to the exploded plane? are you sure?")
      while sureDec == "not valid":
        sure = input("> ").lower()
        if "ye" in sure or "west" in sure or sure == "w":
          print(
              "you (for some reason) walk towards the blazing fire of the plane. you're in great agony in your final moments, but it was worth it B)"
          )
          sureDec = "valid"
          gameOver()
        elif "no" in sure:
          print("good, try again")
          sureDec = "valid"
        else:
          print("i don't understand. sorry.")
          sureDec = "not valid"
    else:
      print("i don't understand. sorry.")


def hillLizard():
  global moves
  global hill
  global userName
  talkAnswer = ""
  talkLen = 0
  splitTalk = ""
  riddleAns = ""
  warning = 0
  wrong = 0
  exit = False
  userChoice = ""
  print(
      "you walk towards the hill that is dotted with flowers dancing in the wind."
  )
  time.sleep(4)
  print(
      "perched proudly at the summit, a small lizard grimaces at you."
  )
  time.sleep(4)
  print("is he judging you??")
  time.sleep(4)
  print("how dare he.")
  time.sleep(4)
  print("...")
  time.sleep(3)
  print(".........")
  time.sleep(3)
  print("sorry, just waiting for you to climb up this huge hill")
  time.sleep(4)
  print("nearly there.....")
  time.sleep(3)
  print(
      "gasping for breath, you finally reach the top. the hill is taller than it looks."
  )
  time.sleep(4)
  print(
      "the lizard is *definitely* judging you now. and to your astonishment, it starts talking"
  )
  time.sleep(4)
  print(f"'well {userName}, you took your time,' it says.")
  time.sleep(4)
  print(
      "do you...talk to him? or do you run away, all the way back down hill. he might have something interesting to say..."
  )
  while not exit:
    userChoice = str(input("> ")).lower()
    if userChoice == "n" or "north" in userChoice:
      print("you can't go north")
    elif ("look" in userChoice
          or "check" in userChoice) and "satchel" in userChoice:
      satchelCheck()
    elif "help" in userChoice:
      help()
    elif ("run" in userChoice or "away" in userChoice
          or "back" in userChoice) and warning == 0:
      print("i wouldn't do that, try again")
      moves += 1
      warning = 1
    elif ("run" in userChoice or "away" in userChoice
          or "back" in userChoice) and warning == 1:
      print(f"look. {userName}.")
      time.sleep(3)
      print("i'm not letting you do that.")
      time.sleep(3)
      print("this is a significant part of your journey, so give it a go, ok?")
      warning = 2
    elif ("run" in userChoice or "away" in userChoice
          or "back" in userChoice) and warning == 2:
      print("talk. to. the. lizard.")
    elif "talk" in userChoice:
      moves += 1
      talkAnswer = input("what do you say to the lizard? ")
      talkLen = len(talkAnswer)
      talkLen = int(talkLen)
      if talkLen % 2 == 0:  #even
        for i in range(0, int(talkLen / 2)):
          splitTalk = splitTalk + talkAnswer[i]
      else:  #odd
        for i in range(0, int((talkLen + 1) / 2)):
          splitTalk = splitTalk + talkAnswer[i]
      print("you begin to speak, '" + splitTalk + "-'")
      print(
          "'look. sorry to interrupt. but i'm only paid to say a riddle. i'm too tired for this.'"
      )
      time.sleep(6)
      print("\ni have two arms, but i'm not alive;")
      time.sleep(3)
      print("shiny and silver, i cut like a knife;")
      time.sleep(3)
      print("i'm really struggling to make this rhyme;")
      time.sleep(3)
      riddleAns = input("so answer the question: what am i? ").lower()
      while not exit:
        if "scissor" in riddleAns and wrong == 0:
          print("'yes! well done! first try.'")
          time.sleep(3)
          exit = True
        elif "scissor" in riddleAns and wrong < 3:
          print("'yes, good job,' the lizard grins.")
          time.sleep(3)
          print("you never thought you'd see him smile.")
          time.sleep(4)
          print("i mean, you never thought you'd see *any* lizard smile")
          time.sleep(3)
          exit = True
        elif "scissor" in riddleAns:
          print("'finally...we got there in the end.'")
          time.sleep(3)
          print("the lizard....is he smiling?")
          time.sleep(3)
          print("surely not.")
          time.sleep(3)
          exit = True
        else:
          print("'no. try again.'")
          wrong += 1
          moves += 1
          riddleAns = str(input("> ")).lower()
    else:
      print("i don't understand. sorry.")
  print("you walk back down the hill. what was that all about?")
  time.sleep(4)
  print("a talking lizard?")
  time.sleep(3)
  print("no, not just talking. he asked you a riddle.")
  time.sleep(3)
  print("and judged you.")
  time.sleep(3)
  print("and even smiled at you.")
  time.sleep(3)
  print("you look back towards the lizar-")
  time.sleep(3)
  print("wait. he's disappeared?!")
  time.sleep(4)
  print("right. the answer to that riddle must be important then.")
  time.sleep(3)
  print("you know, if the riddle is told by a magical lizard.")
  time.sleep(4)
  print("you have reached the bottom of the hill, and are now in the valley.")
  hill = "done"
  valley()


def abandonedShack():
  global moves
  global spiderBite
  exit = False
  userChoice = ""
  dagger = "not got"
  right = "no"
  killOrNot = ""
  killValid = False
  print(" ^  ^  ^   ^      ___I_      ^  ^   ^  ^  ^   ^  ^")
  print("/|\/|\/|\ /|\    /\-_--\    /|\/|\ /|\/|\/|\ /|\/|\ ")
  print("/|\/|\/|\ /|\   /  \_-__\   /|\/|\ /|\/|\/|\ /|\/|\ ")
  print("/|\/|\/|\ /|\   |[]| ↑  |   /|\/|\ /|\/|\/|\ /|\/|\ ")
  print(
      "an abandoned shack lies hidden beneath overgrown vines "
  )
  time.sleep(4)
  print("there is a crooked door, hanging from its hinges. ")
  time.sleep(3)
  print(
      "you can go inside, or find out what's on the right and left side of the shack. or you could go south back to the *rock-filled* valley?"
  )
  while not exit:
    userChoice = str(input("> ")).lower()
    if ("look" in userChoice
        or "check" in userChoice) and "satchel" in userChoice:
      satchelCheck()
    elif "help" in userChoice:
      help()
    elif "south" in userChoice or userChoice == "s":
      print("you go back to the *rocky* valley")
      exit = True
      valley()
    elif "left" in userChoice:
      print("ok. you're not gonna be happy to hear this")
      time.sleep(4)
      print(
          "i'm sorry :( but even after coming so far....you're not immune to spider bites"
      )
      time.sleep(6)
      print("turns out there's a deadly spider here. it bites you")
      time.sleep(5)
      print(
          "you have to use your remaining moves wisely if you want to get out of this fustrating island."
      )
      spiderBite = True
      moves += 10
    elif "right" in userChoice:
      print(
          "as you go the to right side of the shack, you notice a dagger hanging on the wall, held by a single rusty hook. strange."
      )
      moves += 1
      right = "yes"
    elif (
        "get" in userChoice or "grab" in userChoice or "pick" in userChoice
        or "take" in userChoice
    ) and "dagger" in userChoice and right == "yes" and dagger == "not got":
      print("you get the dagger and put it in your satchel")
      dagger = "got"
      satchel.append("dagger")
      moves += 1
    elif ("get" in userChoice or "grab" in userChoice or "pick" in userChoice
          or "take"
          in userChoice) and "dagger" in userChoice and right == "no":
      print("go to the right side of the shack first!")
    elif ("get" in userChoice or "grab" in userChoice or "pick" in userChoice
          or "take"
          in userChoice) and "dagger" in userChoice and dagger == "got":
      print("you have already got the dagger!")
    elif "inside" in userChoice and dagger == "not got":
      print(
          "you venture inside the shack, and the door locks behind you."
      )
      time.sleep(3)
      print("how cliché.")
      time.sleep(2)
      print("the only way out is forward.")
      time.sleep(1)
      print(
          "in front of you, there lies a sleeping snake. you only have one option — to make your way around the creature, treading carefully to continue your path."
      )
      pathGame()
    elif "inside" in userChoice and dagger == "got":
      print(
          "you venture inside the abandoned shack, and the door locks behind you."
      )
      time.sleep(3)
      print("how cliché.")
      time.sleep(2)
      print("the only way out is forward.")
      time.sleep(1)
      print(
          "bin front of you, there lies a sleeping snake. it is time to make a crucial decision: do you kill the snake with the dagger?"
      )
      while not killValid:
        killOrNot = input("> ").lower()
        if "leave it" in killOrNot or "walk" in killOrNot or "don't kill" in killOrNot or "no" in killOrNot:
          pathGame()
          exit = True
        elif "ye" in killOrNot or "kill" in killOrNot:
          print("with a swift strike of the dagger, the snake is murdered")
          killValid = True
          moves += 1
          exit = True
        else:
          print("i don't understand. sorry.")
    else:
      print("i don't understand. sorry")
  backShack()


def pathGame():
  path = ""
  pathValid = False
  pathMoves = 0
  correctAns = ""
  correctLetter = ""
  wrongAns = ""
  global snakeBite
  wrongLetter = ""
  global moves
  for loopCount in range(1, 5):
    if loopCount == 3:
      correctAns = "right"
      correctLetter = "r"
      wrongAns = "left"
      wrongLetter = "l"
    elif loopCount < 3 or loopCount == 4:
      correctAns = "left"
      correctLetter = "l"
      wrongAns = "right"
      wrongLetter = "r"
    pathValid = False
    while not pathValid:
      path = str(input("do you go left or right? ")).lower()
      if wrongAns in path or wrongLetter == path:
        print(
            "you misstep on the creaky floorboard and wake the snake up. grumpily, the snake strikes, and venom enters your bloodstream."
        )
        time.sleep(5)
        print(
            "you now have less time to escape - every move you make counts\n")
        snakeBite = True
        time.sleep(3)
        pathMoves += 10
        pathValid = True
      elif ("look" in path or "check" in path) and "satchel" in path:
        satchelCheck()
      elif "help" in path:
        help()
      elif correctAns in path or correctLetter == path:
        print("you step", correctAns, " and the snake stays asleep\n")
        pathMoves += 1
        pathValid = True
      elif ("look" in path or "check" in path) and "satchel" in path:
        satchelCheck()
      elif "help" in path:
        help()
      else:
        print("i don't understand. sorry")
    if pathMoves > 25:
      print(
          "you have been bitten more than twice by the same snake! that's got to be a world record."
      )
      time.sleep(4)
      print("sorry, only joking.")
      time.sleep(3)
      print("anyways, the venom from the snake's fangs kills you.")
      time.sleep(4)
      print("sorry about that.")
      time.sleep(4)
      gameOver()
  moves += pathMoves
  backShack()


def backShack():
  global moves
  exit = False
  global bread
  userChoice = ""
  print(
      "\non the table at the back of the shack lies some bread and a *newspaper*"
  )
  time.sleep(3)
  print("the only way out is north.")
  while not exit:
    userChoice = str(input("> ")).lower()
    if ("look" in userChoice
        or "check" in userChoice) and "satchel" in userChoice:
      satchelCheck()
    elif "help" in userChoice:
      help()
    elif bread == "not got" and ("get" in userChoice or "grab" in userChoice
                                 or "pick" in userChoice or "take"
                                 in userChoice) and "bread" in userChoice:
      print("you pick up the bread and put it in your satchel")
      satchel.append("bread")
      bread = "got"
      moves += 1
    elif "newspaper" in userChoice:
      print(
          "you look at the newspaper more closely. it says, 'remember newspaper for riddle.' you put it back down"
      )
      moves += 1
    elif bread == "got" and ("get" in userChoice or "grab" in userChoice
                             or "pick" in userChoice or "take"
                             in userChoice) and "bread" in userChoice:
      print("you've already got the bread")
    elif "north" in userChoice or userChoice == "n":
      exit = True
      moves += 1
      print(
          "you step outside to a hidden area filled with fluttering wings and melodic calls."
      )
      birdArea()
    else:
      print("i don't undertand. sorry")


def birdArea():
  global birdFirstTime
  global bread
  global birdFriend
  global moves
  exit = False
  userChoice = ""
  if birdFirstTime is True and bread == "got":
    print("decision time again!")
    time.sleep(6)
    print(
        "do you give the birds the bread that you found in the shack? or do you scare them away?"
    )
    while not exit:
      userChoice = str(input("> ")).lower()
      if ("look" in userChoice
          or "check" in userChoice) and "satchel" in userChoice:
        satchelCheck()
      elif "help" in userChoice:
        help()
      elif "give" in userChoice and "bread" in userChoice:
        print(
            "you give your bread to the birds. they happily jump around and peck at it."
        )
        bread = "given"
        birdFriend = True
        birdFirstTime = False
        moves += 1
        satchel.remove("bread")
      elif "north" in userChoice or userChoice == "n":
        exit = True
        print("you walk forwards, past the trees.")
        garden()
      elif "east" in userChoice or userChoice == "e":
        exit = True
        print("you walk east.")
        tree()
      elif "scare" in userChoice:
        print(
            "you scare the birds away. with a whoosh of flapping wings, they are gone."
        )
        birdFriend = False
        birdFirstTime = False
        moves += 1
      else:
        print("i don't understand. sorry")
  elif birdFirstTime is False and birdFriend is True:
    print("the birds look at you admiringly as you walk past")
    while not exit:
      userChoice = str(input("> ")).lower()
      if ("look" in userChoice
          or "check" in userChoice) and "satchel" in userChoice:
        satchelCheck()
      elif "help" in userChoice:
        help()
      elif "north" in userChoice or userChoice == "n":
        exit = True
        print("you walk forwards, past the trees.")
        garden()
      elif "east" in userChoice or userChoice == "e":
        exit = True
        print("you walk east.")
        tree()
      else:
        print("i don't undertand. sorry")
  elif not birdFirstTime and not birdFriend:
    print(
        "the place looks barren without the cacophany of bird calls and colours flying through the air."
    )
    while not exit:
      userChoice = str(input("> ")).lower()
      if ("look" in userChoice
          or "check" in userChoice) and "satchel" in userChoice:
        satchelCheck()
      elif "help" in userChoice:
        help()
      elif "north" in userChoice or userChoice == "n":
        exit = True
        print("you walk forwards, past the trees.")
        garden()
      elif "east" in userChoice or userChoice == "e":
        exit = True
        print("you walk east.")
        tree()
      else:
        print("i don't undertand. sorry")
  elif birdFirstTime is True and bread == "not got":
    print(
        "you stand before the vibrant birds. that bread would be nice to give them."
    )
    while not exit:
      userChoice = str(input("> ")).lower()
      if ("look" in userChoice
          or "check" in userChoice) and "satchel" in userChoice:
        satchelCheck()
      elif "help" in userChoice:
        help()
      elif "give" in userChoice and "bread" in userChoice:
        print("you dont have the bread. go back inside the shack")
      elif "inside" in userChoice or "back" in userChoice or "south" in userChoice:
        print("you go back inside the shack")
        moves += 1
        backShack()
      elif "north" in userChoice or userChoice == "n":
        exit = True
        print("you walk forwards, past the trees.")
        garden()
      elif "east" in userChoice or userChoice == "e":
        exit = True
        print("you walk east.")
        tree()
      else:
        print("i don't undertand. sorry")


def garden():
  exit = False
  userChoice = ""
  global moves
  global birdFirstTime
  print(
      "in this mystical garden, beautiful flowers bloom everywhere, creating a vibrant display of colours."
  )
  while not exit:
    userChoice = str(input("> ")).lower()
    if ("look" in userChoice
        or "check" in userChoice) and "satchel" in userChoice:
      satchelCheck()
    elif "help" in userChoice:
      help()
    elif "north" in userChoice or userChoice == "n" or "east" in userChoice or userChoice == "e" or "west" in userChoice or userChoice == "w":
      print("there's a wall that way.")
    elif "south" in userChoice or userChoice=="s":
      exit = True
      print("you walk back to the bird area.")
      birdFirstTime = False
      birdArea()
    else:
      print("i don't undertand. sorry")


def tree():
  global moves
  riddle1 = ""
  riddle2 = ""
  riddle3 = ""
  riddle4 = ""
  riddle5 = ""
  print("an ancient tree stands tall amidst a forgotten clearing.")
  time.sleep(3)
  print("the bark carries some engraved riddles.")
  time.sleep(3)
  print("the first riddle reads:")
  time.sleep(3)
  print(
      "in the valley, many can be seen;\neverywhere you look, countless and serene."
  )
  while "rock" not in riddle1:
    riddle1 = str(input("> ")).lower()
    if ("look" in riddle1 or "check" in riddle1) and "satchel" in riddle1:
      satchelCheck()
    elif "help" in riddle1:
      help()
    elif "rock" in riddle1:
      print("great job :)")
    else:
      print("no, sorry. try again")
      moves += 1
  print("the second riddle reads:")
  time.sleep(2)
  print("recall, if you will; \nthe answer to the lizard's riddle")
  while "scissor" not in riddle2:
    riddle2 = str(input("> ")).lower()
    if ("look" in riddle2 or "check" in riddle2) and "satchel" in riddle2:
      satchelCheck()
    elif "help" in riddle2:
      help()
    elif "scissor" in riddle2:
      print("correct :)")
    else:
      print("no, sorry. try again")
      moves += 1
  print("the third riddle reads:")
  time.sleep(2)
  print(
      "you've got rocks and scissors, these rivals fight\ncomplete the trio, what else do you need to make it right"
  )
  while "paper" not in riddle3:
    riddle3 = str(input("> ")).lower()
    if ("look" in riddle3 or "check" in riddle3) and "satchel" in riddle3:
      satchelCheck()
    elif "help" in riddle3:
      help()
    elif "paper" in riddle3:
      print("yes :)")
    else:
      print("no, sorry. try again")
      moves += 1
  print("the fourth question reads:")
  time.sleep(2)
  print("what did you find at the back of the shack other than the bread?")
  while "newspaper" not in riddle4:
    riddle4 = str(input("> ")).lower()
    if ("look" in riddle4 or "check" in riddle4) and "satchel" in riddle4:
      satchelCheck()
    elif "help" in riddle4:
      help()
    elif "newspaper" in riddle4:
      print("absolutely :)")
    else:
      print("no, sorry. try again")
      moves += 1
  print(
      "listen carefully, and home you'll soon be. this riddle's answer is the path to set you free"
  )
  time.sleep(4)
  print(
      "ok. you have newspaper. and paper. what is the difference in these two. just one word, 4 letters"
  )
  while "news" not in riddle5:
    riddle5 = str(input("> ")).lower()
    if ("look" in riddle5 or "check" in riddle5) and "satchel" in riddle5:
      satchelCheck()
    elif "help" in riddle5:
      help()
    elif "news" in riddle5:
      print("yes!! N.E.W.S. is the way out ")
    else:
      print("no, sorry. try again")
      moves += 1
  treeDone()


def treeDone():
  pathValid = False
  correctAns = ""
  correctLetter = ""
  wrongAns = []
  wrongLetter = []
  print("you reach a maze of paths.")
  time.sleep(2)
  for loopCount in range(1, 5):
    if loopCount == 1:
      correctAns = "north"
      correctLetter = "n"
      wrongAns = ["east", "west", "south"]
      wrongLetter = ["e", "w", "s"]
    elif loopCount == 2:
      correctAns = "east"
      correctLetter = "e"
      wrongAns = ["north", "west", "south"]
      wrongLetter = ["n", "w", "s"]
    elif loopCount == 3:
      correctAns = "west"
      correctLetter = "w"
      wrongAns = ["east", "north", "south"]
      wrongLetter = ["e", "n", "s"]
    elif loopCount == 4:
      correctAns = "south"
      correctLetter = "s"
      wrongAns = ["east", "west", "north"]
      wrongLetter = ["e", "w", "n"]
    pathValid = False
    while not pathValid:
      path = input("do you go North, East, West, or South? ").lower()
      if correctAns in path or correctLetter == path:
        print("you go", correctAns)
        pathValid = True
      elif path in wrongAns or path in wrongLetter:
        print(
            "you went the wrong way. rocks stumble beneath you, and you tragically fall to your death"
        )
        gameOver()
      elif ("look" in path or "check" in path) and "satchel" in path:
        satchelCheck()
      elif "help" in path:
        help()
      else:
        print("i don't undertand. sorry")


def beach():
  global birdFriend
  global snakeBite
  global spiderBite
  global moves
  userChoice = ""
  userChoice2 = ""
  print("you've finally reached the beach!! ")
  if birdFriend is True and "key - says LLRL" not in satchel:
    print(
        "the colourful birds that you fed earlier swoop above your head. one of them drop a shiny key into your hands."
    )
    time.sleep(3)
    print("something tells you that you're gonna need it")
    satchel.append("key - says LLRL")
  elif birdFriend is False and "key - says LLRL" not in satchel:
    print(
        "the colourful birds that you saw earlier swoop above your head. one of them has a shiny key in its beak"
    )
    time.sleep(3)
    print(
        "ah you must have forgotten that in the plane. good thing they're here to help"
    )
    time.sleep(3)
    print("wait")
    time.sleep(3)
    print("they're not giving it to you.")
    time.sleep(3)
    print("you should have given them that bread :/")
  print(
      "there's no boat and you can't swim away - you can't see any land nearby. maybe you should look around"
  )
  while not exit:
    userChoice = str(input("> ")).lower()
    if ("look" in userChoice
        or "check" in userChoice) and "satchel" in userChoice:
      satchelCheck()
    elif "help" in userChoice:
      help()
    elif "look around" in userChoice:
      print(
          "as you walk around, kicking sand about, you find a wooden....thing."
      )
      time.sleep(4)
      print("you sweep the sand away from it...")
      time.sleep(2)
      print("it's some sort of trap door")
      time.sleep(2)
      print("you tug on the handle. it's locked. it needs a key.")
      if "key - says LLRL" in satchel:
        while not open:
          userChoice2 = str(input("> ")).lower()
          if ("look" in userChoice2
              or "check" in userChoice2) and "satchel" in userChoice2:
            satchelCheck()
          elif "help" in userChoice2:
            help()
          elif "use key" in userChoice2:
            print("you slot the key into the trapdoor.")
            time.sleep(4)
            print("you feel a slight click, and the door creaks open")
            time.sleep(4)
            print("there's a tunnel?")
            time.sleep(3)
            print(
                "not really what you were expecting. but you have no other choice"
            )
            time.sleep(4)
            print(
                "you grab a lit lantern from a wall and walk through the tunnel"
            )
            if moves > 50:
              if snakeBite is True and spiderBite is True:
                print(
                    "just as you reach for the last step of your escape, you feel your breathing get heavier, and your heartbeat drops rapidly"
                )
                print(
                    "the venom from the two creatures that bit you is finally affecting you"
                )
                time.sleep(5)
                print("you feel dizzy and sway on your feet.")
                time.sleep(4)
                print("the world blurs, while your ears ring")
                time.sleep(3)
                print("you collapse.")
                time.sleep(3)
                print("the ringing disappears.")
                time.sleep(3)
                print("the venom claims its tragic victory.")
                gameOver()
              elif snakeBite is True:
                print(
                    "just as you reach your escape, you feel your breathing get heavier, and your heartbeat drops rapidly"
                )
                print("the snake venom is finally affecting you")
                time.sleep(5)
                print("you feel dizzy and sway on your feet.")
                time.sleep(4)
                print("the world blurs, while your ears ring")
                time.sleep(3)
                print("you collapse.")
                time.sleep(3)
                print("the ringing disappears.")
                time.sleep(3)
                print("the venom claims its tragic victory.")
                gameOver()
              elif spiderBite is True:
                print(
                    "just as you reach your escape, you feel your breathing get heavier, and your heartbeat drops rapidly"
                )
                print("the spider venom is finally affecting you")
                time.sleep(5)
                print("you feel dizzy and sway on your feet.")
                time.sleep(4)
                print("the world blurs, while your ears ring")
                time.sleep(3)
                print("you collapse.")
                time.sleep(3)
                print("the ringing disappears.")
                time.sleep(3)
                print("the venom claims its tragic victory.")
                gameOver()
              else:
                print(
                    "just as you reach your escape, you feel your breathing get heavier, and your heartbeat drops rapidly."
                )
                time.sleep(3)
                print("you haven't drank water at all in this blazing heat")
                time.sleep(4)
                print("you've stayed in the island for too long")
                time.sleep(3)
                print("you feel dizzy and sway on your feet.")
                time.sleep(4)
                print("the world blurs, while your ears ring")
                time.sleep(3)
                print("you collapse.")
                time.sleep(3)
                print("the ringing disappears.")
                time.sleep(3)
                print("you try your best to stay awake, but it's not enough.")
                time.sleep(4)
                gameOver()
            print(
                "and after what seems like an eternity of walking, you emerge from the island's grasp."
            )
            time.sleep(7)
            print(" ~~~~~~~~~ ")
            print("| YOU WIN |")
            print(" ~~~~~~~~~ ")
      else:
        print("you don't have the key. it's a dead end.")
        time.sleep(3)
        print("all that work for nothing")
        time.sleep(3)
        print("you should have given that bread to the birds. or at least looked around in the plane.")
        time.sleep(4)
        print("oh well")
        time.sleep(2)
        gameOver()

print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("| WELCOME TO THIS ADVENTURE GAME |")
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\n")
userName = input(str("what is your name? \n"))
print("good luck,", userName + ", and enjoy...")
planeSpawn()