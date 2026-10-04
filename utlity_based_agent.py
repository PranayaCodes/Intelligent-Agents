A=(0,0)
B =(1,0)

state ={
    A:"Unknown",
    B:"Unknown",
    "agent_location":None
}
goal = {
    A: "Clean",
    B:"Clean"
}

def update_state(memory , percept):
    Location, status = percept
    memory["agent_location"] = Location
    memory[Location] = status
    return memory

def possible_actions(state):
    location =state["agent_location"]
    actions = ["No OP"]
    if state[location]=="Dirty":
        actions.append("clean")
    if location == A:
        actions.append("Right")
    else:
        actions.append("Left")
    return actions

def predict_next_State(memory,action):
    predicted = memory.copy()#create a new copy
    location = memory("agent_location")
    if action == "clean":
        predicted[location]="Clean"
    elif action =="Right":
        predicted["agent_location"] =B
    elif action == "left":
        predicted["agent_location"]=A
    return predicted 
    
def utility(memory):
    score =0
    if memory[A]=="Clean":
        score +=10
    if memory[B]=="Clean":
        score += 10
    return score
def expected_utility(memory,action):
    predicted = predict_next_State(memory, action)
    score=utility(predicted)
    if action in ("Left","Right"):
        score -=1 #cost of moving
    if action == "NO OP" and not (predicted [A] == goal [A] and predicted [B] == goal [B]):
        score -= 5 #penalty for doing nothing when not a goal
    return score
def utility_based_agent(percept):
    global state
    state = update_state(state, percept)
    actions = possible_actions(state)
    #iterate through actions and calculate expected utility for each
    best_action = max (actions, key=lambda a: expected_utility(state, a))
    return best_action
def run():
    print(utility_based_agent((A, "Dirty")), state)
    print(utility_based_agent((A, "Clean")), state)
    print(utility_based_agent((B, "Dirty")), state)
    print(utility_based_agent((B, "Clean")), state)
    run()