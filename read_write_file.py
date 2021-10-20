f = open('my_path/my_file.txt', 'r')
file_data = f.read()
f.close()

f = open('my_path/my_file.txt', 'w')
f.write("Hello there!")
f.close()

