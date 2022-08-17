user_input = str(input("Enter a phase: "))
print(user_input)
text = user_input.split()
acronyms = " "
for i in text:
    acronyms = acronyms + str(i[0]).upper()
print("Acronyms of the phase is : ",acronyms)
