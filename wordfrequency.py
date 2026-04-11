user = input("Enter a sentence: ")  
data = {
    "sentence": user,
    "length": len(user)
}

print("stored dictionary:", data)
print("The length of the sentence is:", data["length"])
