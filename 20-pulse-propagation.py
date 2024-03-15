from pprint import pprint
from collections import namedtuple
from enum import Enum

# broadcaster

# flip flop modules %
# # # initially off
# # # ignores high pulses
# # # flip flops between on and off
# # # sends high pulse when turned on
# # # sends low pulse when turned off

# conjunction modules &
# # # remembers low pulse initially
# # # remembers last pulse from all inputs
# # # When a pulse is received, record that pulse, then
# # # if remembers all high pulses, send low pulse
# # # else send high pulse

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

class Pulse:
    def __init__(self, type, source, destination):
        self.type = type
        self.source = source
        self.destination = destination

class Flipflop:
    def __init__(self, name, outputs, state):
        self.name = name
        self.outputs = outputs
        self.state = state

class Conjunction:
    def __init__(self, name, outputs, inputs):
        self.name = name
        self.outputs = outputs
        self.inputs = inputs

class PulseType(Enum):
    LOW = 0
    HIGH = 1

class FlipFlopState(Enum):
    OFF = 0
    ON = 1

def flip_state(module: Flipflop):
    if module.state == FlipFlopState.ON:
        module.state = FlipFlopState.OFF
    else:
        module.state = FlipFlopState.ON

def push_button(broadcaster, conjunctions, flip_flops):
    low_pulse_count = 1
    high_pulse_count = 0
    pulses: list[Pulse] = []
    for dest in broadcaster:
        pulses.append(Pulse(PulseType.LOW, 'broadcaster', dest))
    
    while pulses:
        pulse = pulses.pop(0)
        type = pulse.type
        source = pulse.source
        destination = pulse.destination

        if type == PulseType.LOW:
            low_pulse_count += 1
        else:
            high_pulse_count += 1

        if destination in flip_flops:
            pulses += send_pulse_flipflop(type, flip_flops[destination])
        if destination in conjunctions:
            pulses += send_pulse_conjunction(type, source, conjunctions[destination])
    
    return(low_pulse_count, high_pulse_count)

def send_pulse_flipflop(pulse_type, module: Flipflop):
    emit: list[Pulse] = []
    if pulse_type == PulseType.HIGH:
        return emit
    flip_state(module)
    emitted_type = PulseType.HIGH if module.state == FlipFlopState.ON else PulseType.LOW

    for dest in module.outputs:
        emit.append(Pulse(emitted_type, module.name, dest))

    return emit  

def send_pulse_conjunction(pulse_type, input_name, module: Conjunction):
    emit: list[Pulse] = []

    module.inputs[input_name] = pulse_type

    emitted_type = PulseType.LOW if all(
        pulse_type == PulseType.HIGH for pulse_type in module.inputs.values()
        ) else PulseType.HIGH
    
    for dest in module.outputs:
        emit.append(Pulse(emitted_type, module.name, dest))
    
    return emit

broadcaster = []
conjunctions = {}
flip_flops = {}
with open('20-pulse-propagation-input.txt') as input:
    for line in input:
        line = line.strip()

        hyphen_index = line.index('-')
        name = line[1:hyphen_index-1]
        arrow_index = line.index('>')
        destination_string = line[arrow_index + 2:]
        
        if 'broadcaster' in line:
            broadcaster += destination_string.split(', ')
        elif line[0] == '%': # flipflop
            destinations = destination_string.split(', ')
            flip_flops[name] = Flipflop(name, destinations, FlipFlopState.OFF)
        elif line[0] == '&': # conjunction
            destinations = destination_string.split(', ')
            conjunctions[name] = Conjunction(name, destinations, {})

for k, v in flip_flops.items():
    for name in v.outputs:
        if name in conjunctions:
            conjunctions[name].inputs[k] = PulseType.LOW

button_pushes = 1000
lows = 0
highs = 0
while button_pushes > 0:
    low, high = push_button(broadcaster, conjunctions, flip_flops)
    lows += low
    highs += high
    button_pushes -= 1

print(lows*highs)