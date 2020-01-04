# open file
inFile = open("pa5.data",'r') 

print(format("Quarterback Name",'20s'),format("Team Name",'14s'),format("Passer Rating"))
print('-'*50)

for count in range (20):
    
    # load player name,team name, and numeric data
    name=inFile.readline().strip()
    team=inFile.readline().strip()
    attempts, completions, yards, touchdowns, interceptions=eval(inFile.readline().strip())
        
    # logical computations
    a = (completions / attempts * 100 - 30) * 0.05
    if a < 0:
        a=0
    if a > 2.375:
        a=2.375
        
    b = (yards / attempts - 3) * 0.25
    if b < 0:
        b=0
    if b > 2.375:
        b=2.375

    c = touchdowns / attempts * 20
    if c < 0:
        c=0
    if c > 2.375:
        c=2.375

    d = 2.375 - interceptions / attempts * 25
    if d < 0:
        d=0
    if d > 2.375:
        d=2.375

    rating=(a+b+c+d)/6*100

    # prints output
    print(format(name[0:18],'20s'), format(team[0:18],'20s'), format(rating,'6.1f'))

inFile.close()