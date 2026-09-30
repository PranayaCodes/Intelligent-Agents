A = {0,0}
B ={1,0}

state ={
    A:"Unknown",
    B:"Unknown",
    "agent_location":None

}

def match_rules(memory, location):
    if memory[A]=="clean" and memory [B]=="clean":
        return "No OP"#No operation
    if memory[location]=="Dirty":
        return"Clean"
    if location ==A 
    return "left"

def update_state(memory, location, status):
    memory["agent_location"]=location
    memory[location]=status
    return status