def find_first_digit(text):
    number = ''
    found_number = False
    index = 10000  

    for i, char in enumerate(text):
        if char.isdigit() and not found_number:
            number = char
            found_number = True
            index = i  
            break  

    if number:
        return int(number), index
    else:
        return None, index

def find_last_digit(text):
    number = ''
    found_number = False
    index = -1
    
    for i, char in enumerate(text):
        if char.isdigit():
            number = char
            found_number = True
            index = i  # Update index for each found digit
    
    if found_number:
        return int(number), index  
    else:
        return None, index

def find_first_number(text):
    spelled_out_numbers = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    min_index = len(text)  # Initialize min_index with a large value
    result_number = None

    for word, number in spelled_out_numbers.items():
        index = text.find(word)
        if index != -1 and index < min_index:
            min_index = index
            result_number = int(number)

    return result_number, min_index


def find_last_number(text):
    spelled_out_numbers = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    max_index = -1  # Initialize max_index with -1
    result_number = None

    for word, number in spelled_out_numbers.items():
        index = text.rfind(word)  # rfind searches for the last occurrence
        if index > max_index:
            max_index = index
            result_number = int(number)

    return result_number, max_index



total = 0

with open('input.txt', 'r') as file:
    file_lines = file.readlines()
for line in file_lines:
    line = line.strip()
    f_number_1,f_index_1 = find_first_digit(line)
    f_number_2 ,f_index_2 = find_first_number(line)
    l_number_1,l_index_1 = find_last_digit(line)
    l_number_2 ,l_index_2 = find_last_number(line)
    
    if f_index_1 < f_index_2 : 
        first = f_number_1
    else : first = f_number_2
    
    if l_index_1 > l_index_2 : 
        last = l_number_1
    else : last = l_number_2
    print(line)
    print(f_index_1,f_index_2,'\t',l_index_1,l_index_2)
    print(f_number_1,f_number_2,'\t',l_number_1,l_number_2)
    print(first, last)
    print(first*10+last)
    print()
    total = total +first*10+last
    
    
print(total)