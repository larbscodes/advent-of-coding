from collections import namedtuple
from copy import deepcopy

workflows = {}

with open('19-aplenty-input.txt') as input:
    reading_workflows = True
    for line in input:
        if line == '\n':
            reading_workflows = False
            continue

        line = line.strip()
        
        if reading_workflows:
            opening_bracket_index = line.index('{')
            workflow_name = line[:opening_bracket_index]
            workflow = line[opening_bracket_index+1:-1]
            workflows[workflow_name] = workflow

Step = namedtuple('Step', 'name ranges')

queue = [Step('in', {
    'x': range(1,4001), 
    'm': range(1,4001), 
    'a': range(1,4001), 
    's': range(1,4001)
    })]

def sum_ranges(ranges):
    sum = 1
    for range in ranges.values():
        sum *= range.stop - range.start
    return sum

posses = 0
while queue:
    step = queue.pop(0)

    rules = workflows[step.name].split(',')
    ranges = deepcopy(step.ranges)
    for raw_rule in rules[:-1]:
        category = raw_rule[0]
        comparator = raw_rule[1]
        colon_index = raw_rule.index(':')
        rating = int(raw_rule[2:colon_index])
        result = raw_rule[colon_index + 1:]


        passing_range = deepcopy(ranges)
        if comparator == '<':
            passing_range[category] = range(passing_range[category].start, rating)
            ranges[category] = range(rating, ranges[category].stop)
        else:
            passing_range[category] = range(rating + 1, passing_range[category].stop)
            ranges[category] = range(ranges[category].start, rating + 1)
        if result == 'A':
            posses += sum_ranges(passing_range)
        elif result == 'R':
            continue
        else:
            queue.append(Step(result, passing_range))
    
    final_result = rules[-1]
    if final_result == 'A':
        posses += sum_ranges(ranges)
    elif final_result != 'R':
        queue.append(Step(final_result, ranges))

print(posses)
