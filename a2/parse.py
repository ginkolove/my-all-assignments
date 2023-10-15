import os, sys
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
def read_layout_problem(file_path):
    #Your p1 code here
    prob = open(file_path)
    lines = prob.readlines()
    area = lines[1:]
    seed = lines[0].split()[-1]
    wall = lines[1].split()[-1]
    width_wall = len(wall)
    length_wall = len(lines) - 1
    width_pacman = width_wall - 2
    length_pacman = length_wall - 2
    wallposition = find_goal('%', area)
    ghostWposition = find_goal('W', area)[-1]
    ghostXposition = find_goal('X', area)
    ghostYposition = find_goal('Y', area)
    ghostZposition = find_goal('Z', area)
    pacmanposition = find_goal('P', area)[-1]
    foodposition = find_goal('.', area)
    emptyposition = find_goal(' ', area)
    game = map(width_wall, length_wall, wallposition, ghostWposition, pacmanposition, emptyposition, foodposition)
    problem = {"seed": seed, "width_wall": width_wall, "length_wall": length_wall,
               "width_pacman": width_pacman, "length_pacman": length_pacman, "wallposition": wallposition,
               "ghostWposition": ghostWposition, "ghostXposition": ghostXposition, "ghostYposition": ghostYposition,
               "ghostZposition": ghostZposition, "pacmanposition": pacmanposition, "foodposition": foodposition,
               "emptyposition": emptyposition, "game": game}
    return problem

def find_goal(goalthing, area):
    position=[]
    for i in range(len(area)):
        for j in range(len(area[i])):
            if area[i][j]==goalthing:
                position.append([i,j])
    return position
if __name__ == "__main__":
    if len(sys.argv) == 3:
        problem_id, test_case_id = sys.argv[1], sys.argv[2]
        problem = read_layout_problem(os.path.join('test_cases','p'+problem_id, test_case_id+'.prob'))
        print(problem)
    else:
        print('Error: I need exactly 2 arguments!')