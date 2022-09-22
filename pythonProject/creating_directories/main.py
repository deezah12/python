from pathlib import Path

new_dir = Path.home() / "new directory"
new_dir.mkdir(exist_ok=True)

# if not new_dir.exists():
#   new_dir.mkdir()

# new_dir.exists()
# new_dir.is_dir()

# create a subdirectory within a directory that doesn't exit
# nested_dir = new_dir / "folder_a" / "folder_b"
# nested_dir.mkdir(parents=True)


# using path.touch method to create a file that doesn't exist
# file_path = new_dir / "file1.txt"
# file_path.touch()
# print(file_path.exists())

# file_path = new_dir / "folder_c" / "file2.txt"
# file_path.parent.mkdir()
# file_path.touch()


# for path in new_dir.iterdir():
#     print(path)
#
# print(list(new_dir.iterdir()))

# to saerch for a specific file we use.glob
# for path in new_dir.glob("*.txt"):
#     print(path)
# print(list(new_dir.glob("*.txt")))


paths = [
    new_dir / "program1.py",
    new_dir / "program2.py",
    new_dir / "folder_a" / "program3.py",
    new_dir / "folder_a" / "folder_b" / "image.jpg",
    new_dir / "folder_a" / "folder_b" / "image2.png",
]

for path in paths:
    path.touch()

# wildcard saerch
# print(list(new_dir.glob("*.py")))
# print(list(new_dir.glob("program?.py")))
# print(list(new_dir.glob("*2.??")))
# print(list(new_dir.glob("?older_?")))
# print(list(new_dir.glob("program[12].py")))


# recursive matching with **, **/* anr the r word
# print(list(new_dir.glob("**/*.txt")))
# print(list(new_dir.rglob("*.py")))


# moving, delete and replacing files
# source = new_dir / "file.txt"
# destination = new_dir/ "folder_a" / "file.txt"
# if not destination.exists():
#     source.replace(destination)


# to delete a file
# files_path = new_dir / "program1.py"
# files_path.unlink()
#
# files_path.exists()

#
# temperature_readings = [68, 65, 68, 70, 74, 72]
# from pathlib import Path
# file_path = path.home() / "temperatures.txt"
# with file_path.open(mode="a", encoding="utf-8") as file:
#     file.write(str(temperature_readings[0]))
#     for temp in temperature_readings[1: ]:
#         file.write(f", {temp}")
#
#
# with file_path.open(mode="r", encoding="utf-8")as file:
#     text = file.read()
# print(text)
#
# temperatures = text.split(",")
# print(temperatures)
#
# int_temperatures = [int(temp) for temp in temperatures]
# print(int_temperatures)

import csv

# daily_temperature = [
#     [68, 65, 68, 70, 74, 72]
#     [67, 67, 70, 72, 72, 70]
#     [68, 70, 74, 76, 74, 73]
# ]

files_path = path.home() / "temperatures.csv"
file = files_path.open(mode="w", encoding="utf-8")
writer = csv.DictWriter( )

