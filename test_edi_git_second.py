boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

perfectcouples = zip(sorted(boys), sorted(girls))

for perfectcouple in perfectcouples:
  print(perfectcouple[0] + ' и ' + perfectcouple[1])
