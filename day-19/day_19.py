import re

        

def part_1(lines):
    total = 0
    
    workflows = True
    workflow_dict = {}
    objects = []
    obj_strings = []
    for line in lines:
        line = line.strip()
        if line == '':
            workflows = False
        elif workflows:
            # parse workflows
            matches = re.findall(r'(.*){(.*)}', line)
            name, rules = matches[0]
            rules = rules.split(',')

            workflow_dict[name] = []
            for rule in rules:
                if ":" in rule:
                    matches = re.findall(r'(.+)([\<\>])(\d+):(.+)', rule)
                    attr, op, val, next_rule = matches[0]
                    val = int(val)
                    workflow_dict[name].append((attr, op, val, next_rule))
                else:
                    workflow_dict[name].append((rule,))
        
        else:
            # parse ratings
            matches = re.findall(r'((.)=(\d+))', line)
            new_object = {}
            obj_strings.append(line)
            for match in matches:
                attr, val = match[1], match[2]
                val = int(val)
                new_object[attr] = val
            
            objects.append(new_object)

    # sort parts
    accepted_parts = []
    for obj in objects:
        print(obj, end='')
        workflow_name = 'in'
        accepted = None
        while True:
            print(f"-> {workflow_name} ", end='')
            if workflow_name == 'R':
                #accepted = False
                break
            elif workflow_name == 'A':
                #accepted = True
                accepted_parts.append(obj)
                break

            workflow = workflow_dict[workflow_name]
            #print(workflow)
            for rule in workflow:
                #print(rule)
                if len(rule) == 1:
                    workflow_name = rule[0]
                    break

                attr, op, val, next_rule = rule
                if op == '<':
                    if obj[attr] < val:
                        workflow_name = next_rule
                        break
                elif op == '>':
                    if obj[attr] > val:
                        workflow_name = next_rule
                        break
        
        print()
                
    # add rating numbers of all accepted parts
    total = sum([sum(obj.values()) for obj in accepted_parts])

    return total
    
def part_2(lines):
    total = 0
    return total
    

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        test_lines = f.readlines()

    with open('input.txt', 'r') as f:
        input_lines = f.readlines()
    
    print("Part 1 ======================")
    test_vals = part_1(test_lines)
    print(f"Test output: {test_vals}")
    input_vals = part_1(input_lines)
    print(f"Real output: {input_vals}")

    print("Part 2 ======================")
    test_vals = part_2(test_lines)
    print(f"Test output: {test_vals}")
    input_vals = part_2(input_lines)
    print(f"Real output: {input_vals}")