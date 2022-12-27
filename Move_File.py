import shutil
import os

source = r"C:\Users\Nikhil\Downloads\Pro-C111 Automate File Segregation 1\Move_Files"
destination = r"C:\Users\Nikhil\Downloads\Pro-C111 Automate File Segregation 1\Document_Files"
# move = shutil.move(source, destination)
# print("Success")

files = os.listdir(source)

for file_name in files:
  name, extension = os.path.splitext(file_name)
  # print(name)
  # print(extension)

  if extension == '':
      continue
  if extension in ['.txt', '.pdf', '.doc', '.docx']:
      path1 = source + '/' + file_name
      path2 = destination + '/' + "Document_Files"
      path3 = destination + '/' + "Document_Files" + '/' + file_name
      if os.path.exists(path2):
        print("Moving " + file_name + ".....")
        shutil.move(path1, path3)

      else:
        os.makedirs(path2)
        print("Moving " + file_name + ".....")
        shutil.move(path1, path3)
