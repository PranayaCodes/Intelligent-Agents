
A=(0,0)
B=(1,0)
C=(0,1)
D=(1,1)

rules={
    (B ,'Dirty'):'Clean',
    (D,'Dirty'):'Clean',
    (C,'Clean'):'Left'
}

def rule_match(State,rules):
    return rules.get(State)

def simple_reflex_agent(percept):
    action = rule_match(percept,rules)
    return action

def run():
    print(simple_reflex_agent((A,'Dirty')))
    print(simple_reflex_agent((A,'Clean')))
    print(simple_reflex_agent((B,'Dirty')))
    print(simple_reflex_agent((B,'clean')))
run()


# Classroom task
# [A] [B]
# [C] [D]
# (0,0) (1,0)
#(0,1) (1,1)


# Agent sees
# B dirty, B clean -> go to D
# D dirty, D clean -> go to C
# C clean
# Create a simple reflex agent that can handle this scenarior

