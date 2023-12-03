import random, time

def ok(gri,lign, col, num):
    for i in range(9):
        if gri[lign][i]==num or gri[i][col]==num:
            return False

    debL=3*(lign//3) #calcule le coin supérieur gauche de la case 3×3 dans la grille sudoku qui contient la cellule
    debC=3*(col//3) #VERIFICATION CASE
    for i in range(3):
        for j in range(3):
            if gri[i + debL][j + debC]==num:
                return False
    return True

def solve(grille):
    fd=False
    for i in range(9):
        for j in range(9):
            if grille[i][j]==0:
                lign, col=i, j
                fd=True
                break
        if fd:
            break
    else:
        return True 

    num=list(range(1, 10))
    random.shuffle(num)
    printfit(grille)
    for i in num:
        if ok(grille, lign, col, i):
            grille[lign][col]=i
            if solve(grille):
                return True
            grille[lign][col]=0  #backtrack

    return False

def remo(grille): #enlever 30 cases au hasard
    for i in range(30):
        print("REMOVE ONE CASE : ")
        printfit(grille)
        lig,col=random.randint(0, 8), random.randint(0, 8)
        while grille[lig][col]==0:
            lig, col=random.randint(0, 8), random.randint(0, 8)
        grille[lig][col]=0

def printfit(gri):
    print()
    for i in gri:
        print(i)
    time.sleep(0.2)


def generer():
    grille = [[0 for i in range(9)] for j in range(9)]
    solve(grille)
    remo(grille)



generer()
