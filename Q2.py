file = open("textInput.txt", "r")
allValid = True
errorCodes = []
file = file.read().splitlines()
for record in file:
    record = record.split(" ")
    if 'false' in record:
        errorCodes.append(record[2])
        allValid = False

if allValid is True:
    print("Yes")
else:
    print("No")
    print(" ".join(errorCodes))