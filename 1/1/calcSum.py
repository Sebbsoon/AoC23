def find_first_number(text):
    number = ''
    found_number = False

    for char in text:
        if char.isdigit() and found_number==False:
            number = char
            found_number = True


    if number:
        return int(number)  
    else:
        return None  

def find_last_number(text):
    number = ''
    found_number = False

    for char in reversed(text):
        if char.isdigit() and found_number==False:
            number=char
            found_number = True

    if number:
        return int(number)  
    else:
        return None 

total = 0

with open('input.txt', 'r') as file:
    # Read the entire file content
    file_lines = file.readlines()
for line in file_lines:
    first = find_first_number(line)
    last = find_last_number(line)
    print(line,first,last)
    sum = (first*10)+last
    total = total+sum
    print (sum)
    
print(total)