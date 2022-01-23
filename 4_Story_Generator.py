import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A Long time ago', 'On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Muskan', 'khushi', 'Lubna', 'Nayla', 'Akshu']
residence = ['Badnera', 'Amravati', 'Pune', 'Banglore', 'Paris']
went = ['School', 'Park', 'University', 'Office', 'Gym']
happened = ['made friends', 'played games', 'studied', 'worked hard', 'exercised']
print(random.choice(when)+', '+random.choice(who)+' whose name was '
      + random.choice(name) + ' that lived in ' + random.choice(residence) +
      ' went to the ' + random.choice(went) + ' and ' + random.choice(happened))
