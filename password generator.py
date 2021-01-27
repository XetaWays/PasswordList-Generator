# -*- coding: utf-8 -*-

importants = input("Enter the important things to your victim (separate by a coma without space) : ")
importantsplit = importants.split(",")

dates = input("Enter the important dates to your victim (must be an int and separate by a coma without space) : ")
datessplit = dates.split(",")

name = input("Enter the outpur file name : ")

passworlist = []
speschar = ["@", "!", "”", "#", "$", "%", "&", "’", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "[", "\\", "]", "^", "_", "`", "{", "}", "|", "~"]

count = 0

with open(name + '.txt', 'a+') as file:

  for x in importantsplit:
    #write les things important
    file.write(x + "\n")
    count+=1

  for y in datessplit:
    #write les dates important
    file.write(y + "\n")
    count+=1

  #write important + date
  for date in datessplit:
    for important in importantsplit:
      #write important things
      file.write(important + "\n")

      #write date + important things
      file.write(date + important + "\n")

      # write important +date
      file.write(important + date + "\n")
      count+=3

      for chara in speschar:
        #print important + date + char
        file.write(important + date + chara + "\n")
        file.write(important + chara + date + "\n")
        file.write(date + important + chara + "\n")
        file.write(date + chara + important + "\n")
        file.write(chara + important + date + "\n")
        file.write(chara + date + important + "\n")
        count+=6
        #print random numbers from 1914 to 2025
        for number in range(1913, 2026):
          number = str(number)
          file.write(chara + important + number + "\n")
          file.write(chara + number + important + "\n")
          file.write(important + chara + number + "\n")
          file.write(important + number + chara + "\n")
          file.write(number + chara + important + "\n")
          file.write(number + important + chara + "\n")
          count+=6

          if "e" in important or "a" in important:
            important = important.replace('e', '3')
            important = important.replace('E', '3')
            important = important.replace('a', '@')

            file.write(important + "\n")
            file.write(important + date + "\n")
            file.write(important + date + chara + "\n")
            file.write(important + chara + date + "\n")
            file.write(date + important + chara + "\n")
            file.write(date + chara + important + "\n")
            file.write(chara + important + date + "\n")
            file.write(chara + date + important + "\n")

            file.write(chara + important + number + "\n")
            file.write(chara + number + important + "\n")
            file.write(important + chara + number + "\n")
            file.write(important + number + chara + "\n")
            file.write(number + chara + important + "\n")
            file.write(number + important + chara + "\n")


print("_______________________________________________________________________________________________________")
print(str(count)+ " Password Generated")
print("_______________________________________________________________________________________________________")
