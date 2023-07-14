Creatures_list = []
while True:
  name = input("what's the name of it? ")
  if not name:
     break
  hp = int(input("how much hp? "))
  dmg = int(input("how much dmg? "))
  defc = int(input("how much def? "))
  Creatures_list.extend([name, hp, dmg, defc])
print(Creatures_list)
