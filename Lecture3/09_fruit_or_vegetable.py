product = input()

output = "unknown"

if product == "banana" or product == "apple" or product == "kiwi" or product == "cherry" \
    or product == "lemon" or product == "grapes":
    output = "fruit"
elif product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot":
    output = "vegetable"

print(output)