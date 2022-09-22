with open('temp_file.txt', mode='w', encoding='utf-8') as file_object:
    print(file_object.tell())
    file_object.write("life is good with banke\n")
    # file_object.seek(10)
    # print(file_object.tell())
    file_object.write("life is good with banke\n")
    file_object.writelines(['life\n', 'is\n', 'bad\n', 'with\n', 'lekan\n'])


with open('temp_file.txt', 'r', encoding='utf-8')as file:
    for idx, line in enumerate(file.readlines(), start=1):
        print(f"{idx}. {line.upper()}")


from pathlib import Path

path = Path("folder/sub-folder/text.txt")

path.parent.mkdir(parents=True, exist_ok=True)
path.touch(exist_ok=True)