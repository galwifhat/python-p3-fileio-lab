def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode='w', encoding='utf-8') as file:
        file.write(file_content)
    return file_content

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode='a', encoding='utf-8') as file:
        file.write(append_content)
    return append_content

def read_file(file_name):
    with open(f'{file_name}.txt', mode='r', encoding='utf-8') as file:
        return file.read()



print(write_file(file_name="logfile", file_content="Log 1: 5 bananas added" ))
print(append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted"))
print(read_file(file_name="logfile"))
