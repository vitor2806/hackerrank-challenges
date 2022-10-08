numberOfQueries = int(input())
phoneBook = {}

for time in range(numberOfQueries):
  name, phone = input().split()
  phoneBook[name] = phone

while True:
  try:
    query = input()
    if (query in phoneBook):
      print(query+"="+phoneBook[query])
    else:
      print("Not found")
      
  except:
    break