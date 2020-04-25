matrice = [[2, -1, 0], 
		   [-1, 2, -1],
		   [0, -1, 2]]
r = 0 #Indice de ligne du dernier pivot trouvé
for j in range(3):
	k = matrice[j].index(max(matrice[j]))  #k indice de ligne du maximun

	if matrice[j][k] != 0: #Valeur max différente de 0
		r += 1             #r désigne l'indice de la futur ligne servant de pivot
		diviseur = matrice[j][k]

		for i in range(len(matrice[j])):
			matrice[j][i] = matrice[j][i] / diviseur
		print(matrice)
		