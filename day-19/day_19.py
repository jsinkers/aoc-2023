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
    workflows = True
    workflow_dict = {}
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
        
    # sort parts
    accepted_parts = []
    val_ranges = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
    
    # conduct dfs of workflow graph
    stack = [('in', val_ranges)]
    accepted_parts = []
    while len(stack) > 0:
        workflow_name, permissible_values = stack.pop()
        accepted = None
        # process rules
        #print(f"{workflow_name}, {permissible_values}")
        if workflow_name == 'R':
            #accepted = False
            continue
        elif workflow_name == 'A':
            #accepted = True
            accepted_parts.append(permissible_values)
            continue

        workflow = workflow_dict[workflow_name]
        #print(workflow)
        no_more_rules = False
        for rule in workflow:
            if no_more_rules:
                break

            #print(f"{rule}: {permissible_values}")
            if len(rule) == 1:
                workflow_name = rule[0]
                stack.append((workflow_name, permissible_values))
                break

            attr, op, val, next_rule = rule
            start, end = permissible_values[attr]
            true_start, true_end = start, end
            false_start, false_end = start, end
            if op == '<':
                if val < start:
                    # no permissible values on this path
                    # next rule gets to use all values
                    break
                    
                elif val < end:
                    # some values permissible on this path
                    true_end = val - 1
                    false_start = val
                    false_end = end
                elif val > end:
                    # current values all permissible
                    # next rule gets to use no values - i.e. no execution
                    no_more_rules = True

            elif op == '>':
                if val > end:
                    # no permissible values on this path
                    # next rule gets to use all values
                    break
                    
                elif val > start:
                    # some values permissible on this path
                    true_start = val + 1
                    false_end = val
                    false_start = start
                elif val < start:
                    # current values all permissible
                    # next rule gets to use no values - i.e. no execution
                    no_more_rules = True
    
            # add new values to stack for next rule
            new_val_range = permissible_values.copy()
            new_val_range[attr] = (true_start, true_end)
            stack.append((next_rule, new_val_range))
            # update rejected values for application of next rule
            permissible_values[attr] = (false_start, false_end)

    print(accepted_parts)
    combs = []
    for part in accepted_parts:
        #print(part)
        num_combinations = 1
        for v in part.values():
            num_combinations *= (v[1] - v[0] + 1)
        
        combs.append(num_combinations)
        
    print(combs)
    # find number of distinct combinations
    return sum(combs)
    

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        test_lines = f.readlines()

    with open('input.txt', 'r') as f:
        input_lines = f.readlines()
    
    # print("Part 1 ======================")
    # test_vals = part_1(test_lines)
    # print(f"Test output: {test_vals}")
    # input_vals = part_1(input_lines)
    # print(f"Real output: {input_vals}")

    print("Part 2 ======================")
    test_vals = part_2(test_lines)
    print(f"Test output: {test_vals}")
    input_vals = part_2(input_lines)
    print(f"Real output: {input_vals}")