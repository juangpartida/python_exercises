name = "Juan"

question = "Will I win the lottery?"

answer = ""

## situating the variables that will be used below.

import random

## need to import the random index, as we will need this to replicate the random "8 ball" answers.

random.randint(1,9)

## situating the range of numbers that the random function will choose from. ie 1 - 9.

random_number = random.randint(1,10)

print(random_number)

if random_number == 1:
  answer = "Yes - definitely."

elif random_number == 2:
  answer = "It is decidedly so."

elif random_number == 3:
  answer = "Without a doubt."

elif random_number == 4:
  answer = "Reply hazy, try again."

elif random_number == 5:
  answer = "Ask again later."

elif random_number == 6:
  answer = "Better not tell you now."

elif random_number == 7:
  answer = "My sources say no."

elif random_number == 8:
  answer = "Outlook not so good."

elif random_number == 9:
  answer = "Very doubtful."

elif random_number == 10:
  answer = "SUIII!!!!"

print(name + " asks: " + question)

print("Magic 8-Ball's answer: " + answer)


