import re
from operator import getitem

N_ROUNDS = 20

with open('data/day-11.csv') as f:
    notes = f.read().split('\n')

# Process instructions
instructions = {}
item_i = 0
for line in notes:
    if line.startswith('Monkey'):
        monkey_number = re.findall(r'\d', line)[0]
        instructions[monkey_number] = {'items': {}, 'counter': 0}
    if line.strip().startswith('Starting'):
        starting_worry = [int(x) for x in re.findall(r'\d{1,2}', line)]
        for item in starting_worry:
            instructions[monkey_number]['items'][item_i] = item
            item_i += 1
    if line.strip().startswith('Operation'):
        operation_name = re.findall(r'[\*\+]', line)[0]
        instructions[monkey_number]['operation_name'] = operation_name
        operand_1 = line.split(operation_name)[0].split('=')[-1]
        operand_2 = line.split(operation_name)[-1]
        instructions[monkey_number]['operand_1'] = operand_1.strip()
        instructions[monkey_number]['operand_2'] = operand_2.strip()
    if line.strip().startswith('Test'):
        divisible_by = int(re.findall(r'\d{1,2}', line)[0])
        instructions[monkey_number]['test'] = divisible_by
    if 'true' in line:
        true_target = re.findall(r'\d', line)[0]
        instructions[monkey_number]['true_target'] = true_target
    if 'false' in line:
        false_target = re.findall(r'\d', line)[0]
        instructions[monkey_number]['false_target'] = false_target

for round in range(N_ROUNDS):
    for monkey in instructions.keys():
        operand_1 = instructions[monkey]['operand_1']
        operand_2_original = instructions[monkey]['operand_2']
        operation_name = instructions[monkey]['operation_name']
        divisible_by = instructions[monkey]['test']
        true_target = instructions[monkey]['true_target']
        false_target = instructions[monkey]['false_target']
        for item in list(instructions[monkey]['items'].keys()):
            instructions[monkey]['counter'] += 1
            if operand_2_original == 'old':
                operand_2 = int(instructions[monkey]['items'][item])
            else:
                operand_2 = int(operand_2_original)
            if operation_name == '*':
                new_worry_level = int(instructions[monkey]['items'][item]) * int(operand_2)
            if operation_name == '+':
                new_worry_level = int(instructions[monkey]['items'][item]) + int(operand_2)
            new_worry_level = new_worry_level // 3
            if new_worry_level % int(divisible_by) == 0:
                instructions[true_target]['items'][item] = new_worry_level
                del instructions[monkey]['items'][item]
            else:
                instructions[false_target]['items'][item] = new_worry_level
                del instructions[monkey]['items'][item]

max_used = (
    sorted(
        instructions.items(), key=lambda x: getitem(x[1], 'counter')
    )[-2:]
)
print(
    max_used[-1][1]['counter']
    * max_used[-2][1]['counter']
)