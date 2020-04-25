import numpy as np

#Saisie des différents paramètres
def saisie(choix):
	if choix == 1: text = "Nombre de vecteur: "
	elif choix == 2: text = "Dimension des vecteurs: "
	
	while True:
		nb = input(text)
		if int(nb) and int(nb) > 0:
			return int(nb)
		print("Mauvaise saisie")

#Saisie des coordonnés des vecteurs
def saisieVecteur(nbVecteur, dimVecteur):
	vecteurs = []
	for i in range(nbVecteur):
		vecteur = np.empty(dimVecteur)
		for j in range(dimVecteur):
			while True:
				text = "Vecteur "+str(i)+", coordonnée "+str(j)+" :"
				coord = input(text)
				if int(coord) or int(coord) == 0:
					vecteur[j] = int(coord)
					break
				print("Mauvaise saisie")
		print(vecteur)
		vecteurs.append(vecteur)
		print()
	return vecteurs

#Renvoie la norme du vecteur
def unitaire(x):
	return np.linalg.norm(x)

#Renvoie la projection jusqu'au nième vecteur
def projN(etab, v, dim):
	scal = np.zeros(dim)
	for e in etab:
		scal += (np.vdot(e, v))*e
	return scal

#Algorithme de GramSchmidt
def gramSchmidt(vecteur, nbVecteur, dim):
	eTab = []
	eTab.append(vecteur[0]/unitaire(vecteur[0]))

	for i in range(1,nbVecteur):
		e = vecteur[i] - projN(eTab, vecteur[i], dim)
		eTab.append(e/unitaire(e))
	return eTab

if __name__ == '__main__':


	nbVecteur = saisie(1)                                      #Saisie du nombre de vecteur
	dimVecteur = saisie(2)									   #Saisie de la dimension des vecteurs
	vecteur = saisieVecteur(nbVecteur, dimVecteur)             #Saisie des coordonnées des vecteurs
	
	eTab = gramSchmidt(vecteur, nbVecteur, dimVecteur)         #Famille orthonormale

	for value in eTab:
		print(value)