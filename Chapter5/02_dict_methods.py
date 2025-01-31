marks = {
    "pathe": 100,
    "shubham": 57,
    "rohan": 23,
    0: "pathe"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"pathe": 99})
# print(marks)

print(marks.get("pathe2")) # Prints None
print(marks["pathe2"]) # Returns an error