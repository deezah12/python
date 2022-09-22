import pathlib

path = pathlib.Path("C:/Users/Deezah/Desktop/hello.txt")
print(path)

path = pathlib.Path(r"C:/Users/Deezah/Desktop/hello.txt")
print(path)

home = pathlib.Path.home()
print(home)
abs_ = home / pathlib.Path.home()
print(abs_)

print(pathlib.Path.cwd())

print(home / "Desktop" / "hello.txt")

result = path.is_absolute()
print(result)

path = pathlib.Path.home() / "hello.txt"
print(path)


for directory in path.parents:
    print(directory)
