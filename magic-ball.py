# Setup
import random

name = 'Alex'
question = 'Will I win the game?'
answer = ''

# Generate and store a random number
random_number = random.randint(1, 9)

# Little logic to our program
if random_number == 1:
  answer = 'Yes - definitely.'
elif random_number == 2:
  answer = 'It is decidedly so.'
elif random_number == 3:
  answer = 'Without a doubt.'
elif random_number == 4:
  answer = 'Reply hazy, try again.'
elif random_number == 5:
  answer = 'Ask again later.'
elif random_number == 6:
  answer = 'Better not tell you now.'
elif random_number == 7:
  answer = 'My sources say no.'
elif random_number == 8:
  answer = 'Outlook not so good.'
elif random_number == 9:
  answer = 'Very doubtful.'
else:
  answer = 'Error'

# Seeing the results
print(name + ' asks: ' + question)
print('Magic 8-Ball\'s answer: ' + answer)


# Extra Challenges
# If the name string is empty
if name == '':
  print('Question: ' + question)

# If no question is provided
if question == '':
  print('You have not asked me anything! I cannot provide a fortune unless you ask me.')
else:
    print(name + ' asks: ' + question)
    print('Magic 8-Ball\'s answer: ' + answer)
    
