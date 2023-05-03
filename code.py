import random
import collections
import sys,time
game = ""
inventoryarchive = []
balance = 0
listofallitems = [
  "Worm", "Shrimp", "Snail", "Deer", "Salmon", "Tuna", "Bear", "Bird", "Goat",
  "Catfish", "Crab", "Turkey", "Clam", "Buffalo", "Time Capsule",
  "Government Files", "AmongUs Plushie", "Red Pogostick", "Glue", "C4", "World Globe", "Plate", "Kangaroo Plushie", "BookOfIntelligence", "Yellow Buggati","Lamborghini"
]
valuelist = [
  3, 4, 5, 10, 15, 20, 25, 10, 100, 23, 50, 600, 20, 700, 200, 600, 700, 1000, 50, 900, 300, 20, 700, 999, 25000, 10000
]
def prompt(str):
  for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)
def getnumoflist(list):
  count=0
  for element in list:
    count += 1 
  return count
prompt("Keep in mind when referring to items make sure its properly capatilized.")
print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬛️⬜️⬜️⬛️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬛️⬜️⬜️⬜️⬜️⬛️⬜️\n⬜️⬜️⬛️⬛️⬛️⬛️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
while game != "STOP":
  def UpdateInventory():
    duplicates = collections.Counter(inventoryarchive)
    inventory = [
      f"{value} {key}" if value > 1 else key
      for (key, value) in duplicates.items()
    ]
    print(inventory)
  game = (input("What would u like to do? Type info to read all cmds: \n"))
  def ValueVerify(item):
    value = (listofallitems.index(item))
    ammount = valuelist[value]
    return (ammount)

  if game == "info":
    print("Gathering Commands:\n" + "Dig\n" + "Hunt\n" + "Fish\n" +
          "Misc Commands:\n" + "Inventory\n" + "Sell\n" + "Balance\n" + "Shop\n" + "iShop")
  elif game == "Dig" or game == "dig":
    digginglist = [
      "AmongUs Plushie", "Worm", "Time Capsule", "Government Files", "Snail"
    ]
    print("You acquired 1x ")
    item = (random.choices(digginglist, weights=(2, 60, 5, 3, 40), k=1))
    inventoryarchive += item
    print(item)
  elif game == "Inventory" or game == "inv" or game == "inventory":
    if inventoryarchive == []:
      print("You got nothin")
    else:
      UpdateInventory()
  elif game == "Fish" or game == "fish":
    fishinglist = ["Shrimp", "Salmon", "Tuna", "Catfish", "Crab", "Clam"]
    print("You acquired 1x")
    fishitem = (random.choices(fishinglist, weights=(70, 30, 10, 9, 4, 2),
                               k=1))
    inventoryarchive += fishitem
    print(fishitem)
  elif game == "Hunt" or game == "hunt":
    huntinglist = ["Deer", "Bear", "Bird", "Goat", "Turkey", "Buffalo"]
    print("You acquired 1x")
    huntingitem = (random.choices(huntinglist, weights=(70, 30, 20, 8, 3, 2)))
    inventoryarchive += huntingitem
    print(huntingitem)
  elif game == "Sell" or game == "sell":
    UpdateInventory()
    itemfind = input("Enter an item from ur inventory to sell: \n")
    if itemfind in inventoryarchive:
      value = ValueVerify(itemfind)
      reply = input(("Are you sure u want to sell this " + itemfind + "? \n"))
      if reply == "Yes" or reply == "yes" or reply == "y":
        countofitems = inventoryarchive.count(itemfind)
        if countofitems > 1:
          quantity = input("How many of these would you like to sell?")
          if int(quantity) > countofitems:
            print("You dont own that many.")
          elif int(quantity) <= countofitems:
            reply1 = input(("Are you sure you want to sell " + quantity + " " + itemfind + "?"))
            if reply1 == "Yes" or reply1 == "yes" or reply1 == "y":
              balance = value * int(quantity) + balance
              for i in range(int(quantity)):
                inventoryarchive.remove(itemfind)
            elif reply1 == "No" or reply1 == "no" or reply1 == "n":
              print("Okay.")
            else:
              print("You spelled something wrong")
        elif countofitems == 1:
          balance = balance + value
          inventoryarchive.remove(itemfind)
      elif reply == "No" or reply == "no" or reply == "n":
        print("Okay.")
      else:
        print("You spelled something wrong")
    else:
      print("You do not have this item")

  elif game == "Balance" or game == "balance" or game == "bal":
    print("Your total balance is $",balance)
  elif game == "infoshop" or game == "ishop" or game == "ishop" or game == "iShop":
    prompt("All available items for sale on the market:")
    list = len(listofallitems)
    for i in range(list):
        print(str(listofallitems[i])+" |COST EACH: "+str(valuelist[i] + 2))
  elif game == "shopbuy" or game == "buy" or game == "Shop" or game == "shop":
    itemfind = input("What would you like to purchase? \n")
    if itemfind in listofallitems:
      tax = ValueVerify(itemfind) + 2
      if balance < tax:
        print("You do not have enough money.")
      else:
        reply = input(("Are you sure u want to buy this", itemfind + " for "+ str(tax) + "? \n"))
        if reply == "Yes" or reply == "yes" or reply == "y":
          inventoryarchive.append(itemfind)
          balance = balance - tax
          print("Congratulations on your purchase!")
        elif reply == "No" or reply == "no" or reply == "n":
          print("Have a good day!")
        else:
          print("This was a yes or no question...")
    else:
      print("This item doesn't exist, be aware its cap sensitive.")
  elif game == "dev test":
    balance = balance + 1000
    inventoryarchive.append("Lamborghini")
  elif game == "invarchive":
    print(inventoryarchive)
  elif game == "gambling":
    gameopt = input("What game would you like to play?")
    if gameopt == "blackjack":
      cards = [1,2,3,4,5,6,7,8,9,10]
      lettercards = [10,10,11]
      bust = False
      letters = ["K","Q","A"]
      yourcards = [random.randint(1,10),random.randint(1,10)]
      dealerscards = [random.randint(1,10),random.randint(1,10)]
      print("Your cards are: ")
      print(yourcards)
      print("Dealers cards are: \n[" + str(dealerscards[1]) + ", ?]")
      if bust == False: 
        hitorstand = input("Would you like to Hit or Stand?\n")
        if hitorstand == "Hit":
          yourcards = yourcards + random.randint(1,10)
          if sum(yourcards) > 21:
            print("You lost")
            bust == True
          elif sum(yourcards) < 21:
            print("Your new cards are:\n" + yourcards + "\n")
    else:
      print("Not yet made")