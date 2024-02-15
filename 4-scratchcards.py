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


    total_points = 0

    for line in input:
        winning_numbers = []
        my_numbers = []
        round_points = 0

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
                if round_points == 0:
                    round_points = 1
                else:
                    round_points *= 2
        
        total_points += round_points
    
    print(total_points)