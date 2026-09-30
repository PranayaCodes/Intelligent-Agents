A = (0,0)
B = (1,0)

def relex_agent(percept):
    location, status = percept
    if status == 'Dirty':
        return 'Clean'
    elif location == A:
        return 'Right'
    elif location == B:
        return 'Left'
def run():
    print(relex_agent((A, 'Dirty'))) 
    print(relex_agent((A, 'Clean'))) 
    print(relex_agent((B, 'Dirty'))) 
    print(relex_agent((B, 'Clean'))) 
run()


