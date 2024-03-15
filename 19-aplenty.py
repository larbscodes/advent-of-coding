from enum import Enum
from collections import namedtuple

class WORKFLOW_RESULT(Enum):
    ACCEPTED = 0
    REJCETED = 1
    NEXT_WORKFLOW = 2

Rule = namedtuple('Rule', 'category comparator rating result')

INITIAL_WORKFLOW = 'in'

def process_rule(rule, part):
    part_rating = part[rule.category]

    if rule.comparator == '<':
        return part_rating < rule.rating
    elif rule.comparator == '>':
        return part_rating > rule.rating
    else:
        return False

def process_result(result):
    if result == 'A':
        return (WORKFLOW_RESULT.ACCEPTED, result)
    elif result == 'R':
        return (WORKFLOW_RESULT.REJCETED, result)
    else:
        return (WORKFLOW_RESULT.NEXT_WORKFLOW, result)

def process_workflow(workflow, part):
    rules = workflow.split(',')
    
    for raw_rule in rules[:-1]:
        category = raw_rule[0]
        comparator = raw_rule[1]
        colon_index = raw_rule.index(':')
        rating = int(raw_rule[2:colon_index])
        result = raw_rule[colon_index + 1:]

        rule = Rule(category, comparator, rating, result)
        passed_rule = process_rule(rule, part)

        if passed_rule:
            return process_result(result)
    
    final_result = rules[-1]
    return process_result(final_result)

workflows = {}
parts = []
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
        else:
            part_ratings = line[1:-1].split(',')
            rating_dict = {}
            for part_rating in part_ratings:
                category, rating = part_rating.split('=')
                rating_dict[category] = int(rating)
            parts.append(rating_dict)

total_ratings = 0
for part in parts:
    current_result = WORKFLOW_RESULT.NEXT_WORKFLOW
    current_workflow = workflows[INITIAL_WORKFLOW]

    while current_result == WORKFLOW_RESULT.NEXT_WORKFLOW:
        workflow_result, next_workflow = process_workflow(current_workflow, part)
        current_result = workflow_result
        if next_workflow in workflows:
            current_workflow = workflows[next_workflow]
    
    if current_result == WORKFLOW_RESULT.ACCEPTED:
        for value in part.values():
            total_ratings += value
    
    print(total_ratings)