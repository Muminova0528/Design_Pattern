from file import File
from folder import Folder


computer = Folder("Computer")


documents = Folder("Documents")
documents.add(File("resume.pdf"))
documents.add(File("homework.docx"))


photos = Folder("Photos")
photos.add(File("photo1.jpg"))
photos.add(File("photo2.jpg"))


computer.add(documents)
computer.add(photos)
computer.add(File("music.mp3"))

computer.show()