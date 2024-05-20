dishwasher_detergent = int(input())

dishwasher_detergent = dishwasher_detergent * 750
dishes_washed = 0
pots_washed = 0
counter = 0

while True:
    counter += 1
    user_input = input()
    if user_input == "End":
        print("Detergent was enough!")
        print(f"{dishes_washed} dishes and {pots_washed} pots were washed.")
        print(f"Leftover detergent {dishwasher_detergent} ml.")
        break
    user_input = int(user_input)
    if counter == 3:
        detergent_used = 15 * user_input
        dishwasher_detergent -= detergent_used
        counter = 0
        pots_washed += user_input
    else:
        detergent_used = 5 * user_input
        dishwasher_detergent -= detergent_used
        dishes_washed += user_input
    if dishwasher_detergent < 0:
        print(f"Not enough detergent, {abs(dishwasher_detergent)} ml. more necessary!")
        break
