import shutil
import os

source = r"C:\Users\Nikhil\Downloads\Pro-C111 Automate File Segregation 1\Move_Files\Example.pdf"
destination = r"C:\Users\Nikhil\Downloads\Pro-C111 Automate File Segregation 1\Document_Files"
move = shutil.move(source, destination)
print("Success")