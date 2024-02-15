with open('4-scratchcards-input.txt') as input:

    def extract_number(index, line):
        start_index = index
        while line[start_index].isdigit():
            start_index -= 1
        start_index += 1
        end_index = start_index
        while end_index < len(line) and line[end_index].isdigit():
            end_index += 1
        return int(line[start_index:end_index])

    copies = [1 for i in range(209)]
    line_number = 0

    for line in input:
        winning_numbers = []
        my_numbers = []
        num_matches = 0

        start_index = line.index(':')

        while line[start_index] != '|':
            if line[start_index].isdigit():
                winning_number = extract_number(start_index, line)
                winning_numbers.append(winning_number)
                number_len = len(str(winning_number))
                start_index += number_len
                continue
            else:
                start_index += 1
        
        while start_index < len(line):
            if line[start_index].isdigit():
                my_number = extract_number(start_index, line)
                my_numbers.append(my_number)
                number_len = len(str(my_number))
                start_index += number_len
                continue
            else:
                start_index += 1
        
        for num in my_numbers:
            if num in winning_numbers:
                num_matches += 1
        
        for i in range(0, num_matches):
            increment_index = line_number + i + 1
            if increment_index < len(copies):
                copies[increment_index] += copies[line_number]
        line_number += 1
    
    print(sum(copies))