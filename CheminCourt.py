#author louise MURARASU

import turtle
import random



turtle.speed(11)

lig = int(input("Choissisez un nombre de ligne:"))
col = int(input("Choissiser un nombre de colonne:"))

    

#initialisation de la liste de voisins de la grille
def init_Voisins():
    nbSommets = lig*col
    V = [[] for i in range(nbSommets)]
    B = [ 0 for i in range(nbSommets)]
    D = [ 0 for i in range(nbSommets)]
    
    for i in range(lig):
        for j in range(col):
            p0 = random.randint(1,5)
            p1 = random.randint(1,5)
            s = i*col + j
            S = V[s]
            
            if i!=lig-1 and j!=col-1:
                V1 = [s+1, p0]
                S.append(V1)
                VJ = [s+col, p1]
                S.append(VJ)
                D[s] = p0
                S1 = V[s+1 ]
                S1.append([s,p0])

                SJ = V[s+col]
                SJ.append([s, p1])
                B[s] = p1
                
            if i!= lig-1 and j==col-1:
                VJ = [s+col, p1]
                S.append(VJ)
                B[s] = p1
                
                SJ = V[s+col]
                SJ.append([s, p1])
                
            if i==lig-1 and j!=col-1:
                V1 = [s+1, p0]
                S.append(V1)
                
                S1 = V[s+1]
                S1.append([s,p0])
                D[s] = p0
    return V, B, D


#Acceseurs

# Récupére le Nombre de Voisins d'un sommet S
def nb_voisins(S):
    return len(S)

#Récupére l'indice du v-iéme voisin de S
def ind_voisin(S,v):
    voisins = V[S]
    paire = voisins[v]
    return paire[0]

#Récupére le poids du v-iéme voisin de S
def poids_voisin(S,v):
    voisins = V[S]
    paire = voisins[v]
    return paire[1]


#Dessine les 2 murs de chaque cellule
def draw_cell(i,j):
    s = i*col +j
    #Dessine les 2 murs avec l'epaisseur demandé
    turtle.width(B[s]*2)
    turtle.forward(100)
    turtle.left(90)
    turtle.width((D[s])*2)
    turtle.forward(100)
    #Remet la position de la tortue en bas à gauche de la cellule suivante
    turtle.up()
    turtle.backward(100)
    turtle.right(90)
    turtle.down()

#Dessine la grille
def draw_grille():
    #Positionne le début au cord(0,0)
    turtle.home()
    #Dessine lesmurs de toute les cellules
    for i in range(lig):
        for j in range(col):
            draw_cell(i,j)
        #Replace la position à la ligne suivante
        turtle.up()
        turtle.backward(col*100)
        turtle.right(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.down()
    #Dessine le reste du tour de la grille
    turtle.up()
    turtle.left(90)
    turtle.forward(100)
    turtle.down()
    turtle.forward(lig*100)
    turtle.right(90)
    turtle.forward(100*col)
    
      



#initialisation pour l'algorithme de Dijkstra
def initialisation():
    PC[0] = 0
    ST[0] = True
    nbv = nb_voisins(V[0])
    for i in range(1,LongV):
        PC[i] = 50
    for i in range(nbv):
        v = ind_voisin(0,i)
        PC[v] = poids_voisin(0,i)


def indmin():
    min = 50
    imin = -1
    for i in range(LongV):
        if not ST[i]:
            if PC[i] < min:
                min = PC[i]
                imin = i
    return imin

#algorithme de Dijkstra
def dijkstra():
    for k in range(1,LongV):
        j = indmin()
        ST[j] = True
        nbv_j = nb_voisins(V[j])
        for i in range(nbv_j):
            v_j = ind_voisin(j,i)
            if not ST[v_j]:
                P = PC[j] + poids_voisin(j, i)
                if P < PC[v_j]:
                    PC[v_j] = P
                    CC[v_j] = j
                    
#retourne la liste de couple du chemin le plus court entre 0 et l'arrivée
def Chemin_Court(Arrivée):
    j=Arrivée
    Chemin = []
    Chemin.append(j)
    A = 50
    while A!=0:
        A = CC[j]
        Chemin.append(A)
        j = A
    C = []
    for i in range(len(Chemin)-1,0, -1):
        couple = [Chemin[i], Chemin[i-1]]
        C.append(couple)
    
    return C
    



            
def creuser(s1,s2):
    #On verifie qui on croise et vers ou on doit creuser
    ds = s2 - s1
    if ds==1:
        #DROITE
        draw_etape(s1,s2, 0)
    if ds>1:
        #BAS
        draw_etape(s1,s2, 270)
    if ds == -1:
        #GAUCHE
        draw_etape(s1,s2, 180)
    if ds<-1:
        #HAUT
        draw_etape(s1,s2, 90)
    
def draw_etape(s1,s2, a):
    #dessine un trait blanc pour faire le trou dans le mur
    turtle.color("white")
    turtle.width(25)
    turtle.setheading(a)
    turtle.forward(100)
    turtle.backward(100)
    #dessine le chemin entre le centre de chaque cellule
    turtle.color("red")
    turtle.width(5)
    turtle.forward(100)

def draw_chemin(C):
    #Positionne le début au centre de la cellule 0
    turtle.up()
    turtle.goto(50,50)
    turtle.down()
    for arc in C:
        creuser(arc[0], arc[1])

#Lancement du jeu
V, B, D = init_Voisins()#on crée la liste de voisins, de la liste des poids du mur du bas et de la liste des poids du mur de droite
draw_grille()#dessine la grille

LongV = len(V)#longueur de la liste de Voisins
PC = [0 for i in range(LongV)] #Liste avec les poids calcules et minimum de chaque sommet de 0 à ce sommet
ST = [False for i in range(LongV)] # liste de booleen qui permet de voir si on a deja vu le sommet
CC = [0 for i in range(LongV)] # Liste qui donne le sommet le plus proche à l'indice du sommet

initialisation()#initialisation pour l'algorithme de dijkstra
dijkstra()
C = Chemin_Court(lig*col -1) # On récupére la liste de couple du chemin le plus court
print("le chemin le plus court:", C)# on affiche la liste
print("son cout est de:", PC[lig*col-1])#on affiche le cout minimal
draw_chemin(C) #on dessine le chemin et on creuse les murs
 
    

