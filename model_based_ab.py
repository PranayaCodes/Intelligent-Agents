A = "A"
B = "B"

state = {
    A: "Unknown",
    B: "Unknown",
    "agent_location": None
}

def match_rules(memory, location):
    if memory[A] == "Clean" and memory[B] == "Clean":
        return "No OP"

    if memory[location] == "Dirty":
        return "Clean"

    if location == A:
        return "Right"

    return "Left"


def update_state(memory, location, status):
    memory["agent_location"] = location
    memory[location] = status
    return memory


def model_based_agent(percept):
    global state

    location, status = percept

    state = update_state(state, location, status)

    action = match_rules(state, location)

    return action


def run():
    print(model_based_agent((A, "Dirty")))
    print(model_based_agent((A, "Clean")))
    print(model_based_agent((B, "Dirty")))
    print(model_based_agent((B, "Clean")))


run()