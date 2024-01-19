import re

class Pulse:
    LOW = "low"
    HIGH = "high"

class Module:
    def __init__(self, name):
        self.dest_modules = []
        self.name = name

    def add_dest_modules(self, dest_modules):
        self.dest_modules += dest_modules
    
    def get_output(self, pulse):
        return [(self.name, dest_module, pulse) for dest_module in self.dest_modules]

# Flip-flop modules (prefix %) are either on or off; they are initially off. If
# a flip-flop module receives a high pulse, it is ignored and nothing happens.
# However, if a flip-flop module receives a low pulse, it flips between on and
# off. If it was off, it turns on and sends a high pulse. If it was on, it turns
# off and sends a low pulse.
class FlipFlopModule(Module):
    def __init__(self, name):
        self.on = False
        self.output = None
        super().__init__(name)

    def input(self, pulse: Pulse):
        if pulse == Pulse.LOW:
            self.on = not self.on
            if self.on:
                self.output = Pulse.HIGH
            else:
                self.output = Pulse.LOW
            
            #print(f"\tFlipFlopModule {self.name} on: {self.on}, input: {pulse}, output: {self.output}")
            return super().get_output(self.output)
        else:
            return []
        
    
# Conjunction modules (prefix &) remember the type of the most recent pulse
# received from each of their connected input modules; they initially default to
# remembering a low pulse for each input. When a pulse is received, the
# conjunction module first updates its memory for that input. Then, if it
# remembers high pulses for all inputs, it sends a low pulse; otherwise, it
# sends a high pulse.

class ConjunctionModule(Module):
    def __init__(self, name):
        self.last_pulses = None
        self.output = None
        super().__init__(name)
    
    def add_parent_modules(self, parent_modules):
        self.parent_modules = parent_modules

    def input(self, pulse1):
        pulses = [pm.output for pm in self.parent_modules]

        # update memory
        self.last_pulses = pulses

        # determine output 
        self.output = Pulse.HIGH
        if all([p == Pulse.HIGH for p in pulses]):
            self.output = Pulse.LOW

        #print(f"\tConjunctionModule {self.name} pulse1: {pulse1}, pulse2: {pulse2}, output: {self.output}")
        return super().get_output(self.output)

# broadcast module
class BroadcastModule(Module):
    def input(self, pulse):
        return super().get_output(pulse)
        
def part_1(lines):
    network = {}
    broadcastModule = BroadcastModule('broadcaster')
    network[broadcastModule.name] = broadcastModule
    parents = {}

    pattern = r'([%&])?(.*) -> (.*)'
    conj_modules = []

    # parse input
    for line in lines:
        line = line.strip()
        matches = re.findall(pattern, line)
        match = matches[0]

        module_type, src, dest = match
        dest = dest.split(',')
        dest = [d.strip() for d in dest]
        #print(f"Adding {module_type} -{src}-> {dest}")
        if module_type == '%':
            # flip flop
            flipFlopModule = FlipFlopModule(src)
            network[src] = flipFlopModule
            flipFlopModule.add_dest_modules(dest)
        elif module_type == '&':
            # conjunction
            conjunctionModule = ConjunctionModule(src)
            network[src] = conjunctionModule
            conjunctionModule.add_dest_modules(dest)
            conj_modules.append(conjunctionModule)
        else:
            # broadcast
            network[src].add_dest_modules(dest)

        for d in dest:
            if d not in parents:
                parents[d] = [src]
            else:
                parents[d].append(src)

        for d in dest:
            if d not in network:
                network[d] = None
        
    # populate conjunction modules
    for conj_module in conj_modules:
        mod_parents = [network[p] for p in parents[conj_module.name]]
        #print(f"Conjunction {conj_module.name} parents: {[p.name for p in mod_parents]}")
        conj_module.add_parent_modules(mod_parents)
    
    # queue of pulses to process
    print("========================")
    num_low, num_high = 0, 0
    for i in range(1000):
        #print(f"Step {i} ==============")
        pulses = [('button', 'broadcaster', Pulse.LOW)]
        while len(pulses) > 0:
            # process pulse
            src, dest, pulse = pulses.pop(0)
            if pulse == Pulse.LOW:
                num_low += 1
            else:
                num_high += 1
            #print(f"{src} -{pulse}-> {dest}")
            if network[dest] is None:
                #print(f"Network {dest} is None")
                continue
            new_pulses = network[dest].input(pulse)
            pulses.extend(new_pulses)
            #print(pulses)

    print(f"num_low: {num_low}, num_high: {num_high}")
    return num_low*num_high
    
def part_2(lines):
    network = {}
    broadcastModule = BroadcastModule('broadcaster')
    network[broadcastModule.name] = broadcastModule
    parents = {}
    parents[broadcastModule.name] = []

    pattern = r'([%&])?(.*) -> (.*)'
    conj_modules = []

    # parse input
    for line in lines:
        line = line.strip()
        matches = re.findall(pattern, line)
        match = matches[0]

        module_type, src, dest = match
        dest = dest.split(',')
        dest = [d.strip() for d in dest]
        #print(f"Adding {module_type} -{src}-> {dest}")
        if module_type == '%':
            # flip flop
            flipFlopModule = FlipFlopModule(src)
            network[src] = flipFlopModule
            flipFlopModule.add_dest_modules(dest)
        elif module_type == '&':
            # conjunction
            conjunctionModule = ConjunctionModule(src)
            network[src] = conjunctionModule
            conjunctionModule.add_dest_modules(dest)
            conj_modules.append(conjunctionModule)
        else:
            # broadcast
            network[src].add_dest_modules(dest)

        for d in dest:
            if d not in parents:
                parents[d] = [src]
            else:
                parents[d].append(src)

        for d in dest:
            if d not in network:
                network[d] = None
        
    # populate conjunction modules
    for conj_module in conj_modules:
        mod_parents = [network[p] for p in parents[conj_module.name]]
        #print(f"Conjunction {conj_module.name} parents: {[p.name for p in mod_parents]}")
        conj_module.add_parent_modules(mod_parents)
    
    print(f"Network built - contains {len(network)} modules")

    # queue of pulses to process
    print("========================")
    num_low, num_high = 0, 0
    i = 0
    target_found = False
    while not target_found:
        i += 1
        if i % 100 == 0:
            quit()

        #print(f"Step {i} ==============")


        pulses = [('button', 'broadcaster', Pulse.LOW)]

        while not target_found and len(pulses) > 0:
            # process pulse
            src, dest, pulse = pulses.pop(0)
            if pulse == Pulse.LOW:
                num_low += 1
            else:
                num_high += 1
            #print(f"{src} -{pulse}-> {dest}")
            if network[dest] is None:
                #print(f"Network {dest} is None")
                continue
            new_pulses = network[dest].input(pulse)
            for p in new_pulses:
                _, dest, val = p
                if dest == 'rx' and val == Pulse.LOW:
                    target_found = True
                    break
                
            pulses.extend(new_pulses)
            #print(pulses)
        
        # print output values
        counter_nodes = ['fv', 'jd', 'vm', 'lm']
        counter1_nodes = ['jl', 'js', 'hq', 'gl', 'mc', 'xt', 'ss', 'mz', 'sp', 'gh', 'rg','zq', 'qj']
        counter1_nodes.reverse()
        c1_outputs = [1 if network[n].output == Pulse.LOW else 0 for n in counter1_nodes]
        c1_outputs = ''.join([str(c) for c in c1_outputs])
        print(f"Step {i:05}: {c1_outputs}")

    print(f"num_low: {num_low}, num_high: {num_high}")
    return num_low*num_high
    

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        test_lines = f.readlines()

    with open('test_2.txt', 'r') as f:
        test_2_lines = f.readlines()

    #with open('test_3.txt', 'r') as f:
    #    test_3_lines = f.readlines()

    #with open('test_4.txt', 'r') as f:
    #    test_4_lines = f.readlines()

    #with open('test_5.txt', 'r') as f:
    #    test_5_lines = f.readlines()

    with open('input.txt', 'r') as f:
        input_lines = f.readlines()
    
    print("Part 1 ======================")
    test_vals = part_1(test_lines)
    print(f"Test output: {test_vals}\n")
    test_vals = part_1(test_2_lines)
    print(f"Test output: {test_vals}\n")
    input_vals = part_1(input_lines)
    print(f"Real output: {input_vals}")

    print("Part 2 ======================")
    #test_vals = part_2(test_lines)
    #print(f"Test output: {test_vals}")
    input_vals = part_2(input_lines)
    print(f"Real output: {input_vals}")