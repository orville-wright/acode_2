#!/usr/bin/python3

list1 = [6,0,6,6,0,6]
list2 = [2,4,6,2,4,6]
list3 = [4,2,6,4,2,6]
list4 = [2,4,6,2,4,6]
list5 = [6,0,6,6,0,6]
list6 = [list1,list2,list3,list4,list5]

def pos_ls(x):
    for i in range(0,x):
        print(f"\u2588", end="")
    return

def neg_ls(q):
    for i in range(0,q):
        print( " ", end="")
    return

def neg_ws(a):
    for i in range(0,a):
        print( " ", end="" )
    return


for i in list6:
    for j in range(len(i)):
        if j == 0 or j == 3:
            pos_ls( i[j] )
        elif j == 1 or j == 4:
            neg_ls( i[j] )
        else:
            neg_ws( i[j] )

    print( " " )
