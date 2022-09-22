
play_list = []

print(input("Enter your 5 favourite shakespearean plays\n"))

for i in range(5):
    play_name = input(f"play %d: {i + 1}")
    play_list.append(play_name)

print("index\t\tvalue")

for i in range(len(play_list)):
    print(f"%9d  %-25s{i + 1, play_list[i]}")
