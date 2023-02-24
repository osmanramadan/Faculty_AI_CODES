A='A'
B='B'
environment={ A:'dirty',B:'dirty','current':A}
def sensor():
    loc=environment['current']
    stat=environment[loc]
    return (loc,stat)
def reflex_vacuum_agent(loc,stat):
    if stat=='dirty':
        return 'suck'
    elif loc==A:
        return 'right'
    elif loc==B:
        return 'left'
def actautor(action):
    loc=environment['current']
    if action=='suck':
        environment[loc]='clean'
    elif action=='right':
        environment['current']=B
    elif action=='left':
        environment['current'] = A
def run(n):
    print("(loc1,status1)\t action \t (loc2,status2)")
    for i in range(n):
        (loc1, stat1) = sensor()
        action = reflex_vacuum_agent(loc1, stat1)
        actautor(action)
        (loc2, stat2) = sensor()
        print((loc1, stat1), '\t', action, '\t', (loc2, stat2))
run(10)


