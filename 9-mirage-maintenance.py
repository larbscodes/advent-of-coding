with open('9-mirage-maintenance-input.txt') as input:
    extrapolated_sums = 0

    for line in input:
        histories = []
        first_history = list(map(lambda x: int(x), line.strip().split(' ')))
        histories.append(first_history)

        recent_history = histories[-1]
        while all(diff == 0 for diff in recent_history) == False:
            next_history = []
            for i, value in enumerate(recent_history):
                if i == 0:
                    continue
                next_history.append(value - recent_history[i - 1])
            histories.append(next_history)
            recent_history = next_history

        extrapolated_sum = 0
        for i, history in enumerate(reversed(histories)):
            extrapolated_sum += history[-1]
        extrapolated_sums += extrapolated_sum
    
    print(extrapolated_sums)