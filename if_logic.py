

message = 'The movie is about to begin, we recommend '

#wrap connection in a float() to accept decimals as numbers

connection = float(input('What is your connection speed in MBPS? '))

#if input value was higher or equal to 25

if connection >= 25:
    message = message + ' setting video to 4K.'
elif connection >= 5:
    message = message + ' setting video to 1000p.'
elif connection >= 2:
    message = message + ' setting video to 720p.'
else:
    message = message + ' finding another access network.'

print(message)