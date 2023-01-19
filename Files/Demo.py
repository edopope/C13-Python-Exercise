import pathlib

path1 = pathlib.Path("C:\imagea\whatsapp\hello.txt")
path2 = pathlib.Path.home()
path3 = path2 / "private.jpg"
print(path1)
print(path2)
print(path3)
print(path1.is_absolute())
