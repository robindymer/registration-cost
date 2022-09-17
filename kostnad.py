# First of all, we clean our data
from cmath import log


filename = "./data/participants.csv"
lines = []
orders = []
UTNmember = []
ticketNumbers = []
with open(filename, 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
    lines = [line.split(",") for line in lines]

    # Save orders and remove commas
    orders = [line[2].replace(",", "") for line in lines]
    # Extract member status and remove \n
    # UTNmember = [line[4].strip() for line in lines]
    ticketNumbers = [line[3].split(" ") for line in lines]
    # Remove the headers
    orders.pop(0)
    # UTNmember.pop(0)
    ticketNumbers.pop(0)
    ticketNumbers = [line[1] for line in ticketNumbers]

# print(orders)
# print("\n\n")
# print(ticketNumbers)

totalCosts = [450 for _ in range(115)]
# [print(ticket) for ticket in ticketNumbers]

for i in range(len(orders)):
  order = orders[i]
  # isMember = int(UTNmember[i])
  ticketNumber = int(ticketNumbers[i])
  items = order.split("|")
  # print("Order:", order)
  # print("Status:", isMember)
  # print("Ticket number:", ticketNumber)
  # Order: soda, email, lunch, phone number, extra soda, extra lunch, allergies
  items = order.split("|")
  totCost = 0
  # print(items)
  # print(ticketNumber)
  
  # If items is empty (i.e items[0] == '-'), skip
  if (items[0] == '-'):
    continue

  # Ain't clean but honest work
  if "True" in items[0]:
    totCost += 10
  if "True" in items[2]:
    totCost += 30
  if "True" in items[4]:
    totCost += 10
  if "True" in items[5]:
    totCost += 30
  print(items[6])
  
  if ((ticketNumber-1) != 0):
    totalCosts[ticketNumber - 1] += totCost
  
for i in range(len(totalCosts)):
  cost = totalCosts[i]
  print("Ticket", i+1, ": cost -", cost)

# This could be used if the UTN-member API works
  # if isMember:
  #   if "True" in items[0]:
  #     totCost += 10
  #   if "True" in items[2]:
  #     totCost += 30
  #   if "True" in items[4]:
  #     totCost += 10
  #   if "True" in items[5]:
  #     totCost += 30
  # else:
  #   if "True" in items[0]:
  #     totCost += 15
  #   if "True" in items[2]:
  #     totCost += 40
  #   if "True" in items[4]:
  #     totCost += 15
  #   if "True" in items[5]:
  #     totCost += 40