def produit(T):
    S=0
    for i in T:
        S+=i
    return S

Data=[1,3,5]
print('le produit est :', produit(Data))
print('le min est :', min(Data))
print('le max est :', max(Data))
