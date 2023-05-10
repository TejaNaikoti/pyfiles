phone_number = input("phone: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven"
}
output = ""
for ch in phone_number:
    output += digits_mapping.get(ch, "!") + " "
print(output)
