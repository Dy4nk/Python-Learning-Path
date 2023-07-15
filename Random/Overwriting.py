"""
Day 03 - 14:08
That feeling when you accidentally click "Accept" and you overwrite that really important documeent
"""

documents = ["Thesis_FINAL", "FamilyPhotos", "BankCredentials"]

write = input("What file do you want to upload?: ")

if(documents.count(write) == True):
    documents.remove(write)
    documents.append(write)
    print(write, "has been overwritten successfully.")
else:
    documents.append(write)
    print(write, "uploaded successfully.")
    print("List of documents: ", documents)