from sys import argv

# Simple python program using command line arguments and user input
script, user_name = argv
prompt = '>'

print(f'Hi {user_name}, I\'m the {script} script.')
print('I\'d like to ask you a few questions')
print(f'Do you like me {user_name}')
likes = input(prompt)

print(f'Where do you live {user_name}')
lives = input(prompt)

print('What kind of computer do you have?')
computer = input(prompt)

print(f"Alright so you said {likes} about liking me.\n"
      f"You live in {lives}. Not sure where that is.\n"
      f"A you have a {computer}. Nice!!!")
