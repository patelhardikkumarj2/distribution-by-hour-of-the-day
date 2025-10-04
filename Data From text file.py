fh = input("Enter File Name: ")
text = open(fh)
t_hours = []
emptydict = {}
for words in text:
    if not words.startswith("From "):
        continue
    sender = words.split()
    hours = sender[5].split(':')
    t_hours.append(hours[0])

for each in t_hours:
    emptydict[each]=emptydict.get(each,0) + 1

for k, v in sorted (emptydict.items()):
   print(k,v)