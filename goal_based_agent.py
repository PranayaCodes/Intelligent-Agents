A =(0,0)
B =(1,0)

state ={
    A:"Unknown",
    B:"Unknown",
    "agent_location": None
}
goal ={
    A: "Clean",
    B:"Clean"
}

def match_rules(memory,Location):
    if memory[A] == "Clean" and memory[B] == "Clean":
        return "No OP"#No operation
    if memory[Location]=="Dirty":
        return"Clean"
    if Location ==A:
        return "Right"
    return "left"

def update_state(memory,Location,status):
    memory["agent_location"] = Location
    memory[Location] = status
    return state

def goal_based_agent(percept):
    global state
    Location,status = percept
    state = update_state(state,Location,status)
    action = match_rules(state,Location)
    return action

def run():
    print(goal_based_agent((A,"Dirty")),state)
    print(goal_based_agent((A,"Clean")),state)
    print(goal_based_agent((B,"Dirty")),state)
    print(goal_based_agent((B,"Clean")),state)

run()