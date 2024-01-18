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

# Flip-flop modules (prefix %) are either on or off; they are initially off. If a flip-flop module receives a high pulse, it is ignored and nothing happens. However, if a flip-flop module receives a low pulse, it flips between on and off. If it was off, it turns on and sends a high pulse. If it was on, it turns off and sends a low pulse.
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
            
            #print(f"FlipFlopModule {self.name} on: {self.on}, input: {pulse}, output: {self.output}")
            return super().get_output(self.output)
        else:
            self.output = None
            return []
        
    
# Conjunction modules (prefix &) remember the type of the most recent pulse
# received from each of their connected input modules; they initially default to
# remembering a low pulse for each input. When a pulse is received, the
# conjunction module first updates its memory for that input. Then, if it
# remembers high pulses for all inputs, it sends a low pulse; otherwise, it
# sends a high pulse.

class ConjunctionModule(Module):
    def __init__(self, name):
        self.last_pulse_1 = Pulse.LOW
        self.last_pulse_2 = Pulse.LOW
        self.output = None
        super().__init__(name)
    
    def add_parent_modules(self, parent_modules):
        if len(parent_modules) == 1:
            self.parent_module_1 = parent_modules[0]
            self.parent_module_2 = parent_modules[0]
        else:
            self.parent_module_1 = parent_modules[0]
            self.parent_module_2 = parent_modules[1]

    def input(self, pulse1):
        pulse1 = self.parent_module_1.output
        pulse2 = self.parent_module_2.output

        # determine output 
        self.output = Pulse.HIGH
        if self.last_pulse_1 == Pulse.HIGH and self.last_pulse_2 == Pulse.HIGH:
            self.output = Pulse.LOW

        # update memory
        self.last_pulse_1 = pulse1
        self.last_pulse_2 = pulse2

        return super().get_output(self.output)

# broadcast module
class BroadcastModule(Module):
    def input(self, pulse):
        return super().get_output(pulse)
        
def part_1(lines):
    # parse input
    total = 0

    network = {}
    broadcastModule = BroadcastModule('broadcaster')
    network[broadcastModule.name] = broadcastModule

    pattern = r'([%&])?(.*) -> (.*)'
    conj_modules = []

    for line in lines:
        line = line.strip()
        matches = re.findall(pattern, line)
        match = matches[0]

        module_type, src, dest = match
        dest = dest.split(',')
        dest = [d.strip() for d in dest]
        print(f"Adding {module_type} -{src}-> {dest}")
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
        
    # populate conjunction modules
    for conj_module in conj_modules:
        conj_module.add_parent_modules([m for m in network.values() if conj_module.name in m.dest_modules])
    
    # queue of pulses to process
    pulses = [('button', 'broadcaster', Pulse.LOW)]
    counter = 0
    while len(pulses) > 0:
        counter += 1
        if counter > 10:
            break
        # process pulse
        src, dest, pulse = pulses.pop(0)
        print(f"{src} -{pulse}-> {dest}")
        new_pulses = network[dest].input(pulse)
        pulses.extend(new_pulses)
        #print(pulses)
    return counter
    
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
    #input_vals = part_1(input_lines)
    #print(f"Real output: {input_vals}")

    #print("Part 2 ======================")
    #test_vals = part_2(test_lines)
    #print(f"Test output: {test_vals}")
    #input_vals = part_2(input_lines)
    #print(f"Real output: {input_vals}")