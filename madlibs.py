#string concanetion (aka how to put stings together)
#suppose we want to create a string that says "subscibe to ______"
#youtuber = "Kylie Ying" #some string variable

#a few ways to do this 
#print("Subscribe to " + youtuber)
#print("Subscribe to {}" .format(youtuber))
#print(f"Subscribe to {youtuber}")


#example
name = input("Name: ")
writer = input("Writer: ")
school = input("School: ")
villain = input("Villain: ")

madlib = f"{name} is a series of fantasy novel by a British writer, {writer}. This novel tells about the adventure of teenager magician named {name} and his friends, Ron and Hermione.Who are students of {school}. Harry has an enemy named {villain}"

print(madlib)