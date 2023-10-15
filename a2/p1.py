import sys, random, grader, parse,copy
def map(width_wall,length_wall,wallposition,ghostWposition,pacmanposition,emptyposition,foodposition):
    game = [[None for _ in range(width_wall)] for _ in range(length_wall)]
    for i in range(length_wall):
        for j in range(width_wall):
            if [i, j] in wallposition:
                game[i][j] = '%'
            if [i, j] == pacmanposition:
                game[i][j] = 'P'
            if [i, j] == ghostWposition:
                game[i][j] = 'W'
                continue
            if [i, j] in emptyposition:
                game[i][j] = ' '
            if [i, j] in foodposition:
                game[i][j] = '.'

    return game
def ghostWwin(pacmanposition, ghostWposition):
    if pacmanposition == ghostWposition:
        return True
def pacmanwin( foodposition):
    if len(foodposition)==0:
        return True
def directionnumget(emptypositions, judge_position):
    directionnum=[]
    for a in range(len(emptypositions)):
        if abs(emptypositions[a][0]-judge_position[0])+abs(emptypositions[a][1]-judge_position[1])==1:
            directionnum.append([emptypositions[a][0]-judge_position[0],emptypositions[a][1]-judge_position[1]])
    return directionnum
def directionwordjude(directionnum):
    directionword=[]
    for i in range(len(directionnum)):
        if directionnum[i][0]==1:
            directionword.append('S')
        if directionnum[i][0]==-1:
            directionword.append('N')
        if directionnum[i][1]==1:
            directionword.append('E')
        if directionnum[i][1]==-1:
            directionword.append('W')
    directionword=tuple(directionword)
    return directionword
def move(direction,goalposition):
    if direction=='S':
        goalposition[0]+=1
    if direction=='N':
        goalposition[0]-=1
    if direction=='W':
        goalposition[1]-=1
    if direction=='E':
        goalposition[1]+=1
    return goalposition
def eatfood(pacmanposition, foodposition,value):
    if pacmanposition in foodposition:
        foodposition.remove(pacmanposition)
        value+=10
    return foodposition,value
def list_str(game):
    mapstr=""
    for row in game:
        mapstr+="".join(row)+"\n"
    mapstr=mapstr.rstrip()
    return mapstr
def random_play_single_ghost(problem):
    # Your p1 code here
    seed = int(problem["seed"])
    # print(f"seed: {seed}")
    # print(0)
    game = problem["game"]
    mapstr = "seed: " + str(seed) + "\n" + "0\n" + list_str(game) + "\n"
    # print(map_str)
    width_wall = problem["width_wall"]
    length_wall = problem["length_wall"]
    ghostWposition = problem["ghostWposition"]
    wallpositions = problem["wallposition"]
    pacmanposition = problem["pacmanposition"]
    foodpositions = problem["foodposition"]
    emptypositions = problem["emptyposition"]
    random.seed(seed, version=1)
    # mapstr=""
    count = 0
    value = 0
    while True:
        oldpacman = copy.deepcopy(pacmanposition)
        maybearea = foodpositions + emptypositions
        maybearea.append(ghostWposition)
        directionnum = directionnumget(maybearea, pacmanposition)
        directionword = sorted(directionwordjude(directionnum))
        # print(directionword)
        directionpacman = random.choice(directionword)
        # print(directionpacman)
        pacmanposition = move(directionpacman, pacmanposition)
        value -= 1
        emptypositions.append(oldpacman)
        if pacmanposition in emptypositions:
            emptypositions.remove(pacmanposition)
        foodpositions, value = eatfood(pacmanposition, foodpositions, value)
        game = map(width_wall, length_wall, wallpositions, ghostWposition, pacmanposition, emptypositions,
                   foodpositions)
        count += 1
        mapstr += str(count) + ": P moving " + directionpacman + "\n" + list_str(game) + "\n"
        if ghostWwin(pacmanposition, ghostWposition) == True:
            value -= 500
            mapstr += "score: " + str(value) + "\n" + "WIN: Ghost"
            break
        if pacmanwin(foodpositions) == True:
            value += 500
            mapstr += "score: " + str(value) + "\n" + "WIN: Pacman"
            break
        mapstr += "score: " + str(value) + "\n"
        # print(mapstr)
        oldghpstW = copy.deepcopy(ghostWposition)
        maybearea = foodpositions + emptypositions
        maybearea.append(pacmanposition)
        directionnum = directionnumget(maybearea, ghostWposition)
        directionword = sorted(directionwordjude(directionnum))
        directionghost = random.choice(directionword)
        ghostWposition = move(directionghost, ghostWposition)
        if ghostWposition in emptypositions:
            emptypositions.remove(ghostWposition)
        if oldghpstW not in foodpositions:
            emptypositions.append(oldghpstW)
        game = map(width_wall, length_wall, wallpositions, ghostWposition, pacmanposition, emptypositions,
                   foodpositions)
        count += 1
        mapstr += str(count) + ": W moving " + directionghost + "\n" + list_str(game) + "\n"
        if ghostWwin(pacmanposition, ghostWposition) == True:
            value -= 500
            mapstr += "score: " + str(value) + "\n" + "WIN: Ghost"
            break
        mapstr += "score: " + str(value) + "\n"
        # print(mapstr)
    return mapstr

if __name__ == "__main__":
    try: test_case_id = int(sys.argv[1])
    except: test_case_id = -6
    problem_id = 1
    grader.grade(problem_id, test_case_id, random_play_single_ghost, parse.read_layout_problem)