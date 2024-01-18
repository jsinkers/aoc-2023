import re

class Pulse:
    LOW = False
    HIGH = True

class Module:
    def __init__(self, name):
        self.dest_modules = []
        self.name = name

    def add_dest_module(self, dest_module):
        self.dest_modules.append(dest_module)
    
    def output(self, pulse):
        return [(self.name, dest_module, pulse) for dest_module in self.dest_modules]

# Flip-flop modules (prefix %) are either on or off; they are initially off. If a flip-flop module receives a high pulse, it is ignored and nothing happens. However, if a flip-flop module receives a low pulse, it flips between on and off. If it was off, it turns on and sends a high pulse. If it was on, it turns off and sends a low pulse.
class FlipFlopModule(Module):
    def __init__(self, name):
        self.on = False
        super().__init__(name)

    def input(self, pulse: Pulse):
        if pulse == Pulse.LOW:
            self.on = not self.on
            if self.on:
                return Pulse.HIGH
            else:
                return Pulse.LOW
        else:
            return None
        
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
        self.super().__init__(name)
    
    def input(self, pulse1, pulse2):
        # determine output 
        output = Pulse.HIGH
        if self.last_pulse_1 == Pulse.HIGH and self.last_pulse_2 == Pulse.HIGH:
            output = Pulse.LOW

        # update memory
        self.last_pulse_1 = pulse1
        self.last_pulse_2 = pulse2

        return super().output(output)

# broadcast module
class BroadcastModule(Module):
    def input(self, pulse):
        return super().output(pulse)
        
def part_1(lines):
    # parse input
    total = 0

    network = {}
    broadcastModule = BroadcastModule('broadcast')
    network[broadcastModule.name] = broadcastModule
    modA = FlipFlopModule('a')
    modB = FlipFlopModule('b')
    network[modA.name] = modA
    network[modB.name] = modB
    broadcastModule.add_dest_module('a')
    broadcastModule.add_dest_module('b')
    
    # queue of pulses to process
    pulses = [('button', 'broadcast', Pulse.LOW)]
    while len(pulses) > 0:
        # process pulse
        src, dest, pulse = pulses.pop()
        print(f"{src} -{pulse}-> {dest}")
        network[dest].input(pulse)
        pulses.extend(network[dest].output(pulse))
        print(pulses)
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