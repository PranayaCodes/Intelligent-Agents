#Coordinates
A=(0,0)
B=(1,0)

#History of perdeptions
percepts=[]
table={
    ((B,'Clean'),):"Right",
    ((B,'Dirty'),):"Suck",

    ((B,'Dirty'),(B,'Clean')):"Right",
    ((B,'Dirty'),(B,'Clean'),(B,'Dirty')):"Clean",
}

def lookup(percepts,table):
    action = table.get(tuple(percepts))
    return action

def table_driven_agent(percept):
    #Add the new percept to the history
    percepts.append(percept)
    #Look up the action in the table 
    action = lookup(percepts,table)
    return action

def run():
    print(table_driven_agent((B,'Dirty')),percepts) #Clean
    print(table_driven_agent((B,'Clean')),percepts) #Right
    print(table_driven_agent((A,'Dirty')),percepts) #Clean 
run()

