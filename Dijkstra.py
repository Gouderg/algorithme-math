from math import inf

# Récupère les données d'utilisateur et renvoie une matrice associé
def recupData():

	# On récupère le nombre de sommets
	while True:
		try:
			sommet = int(input("Combien de sommets avez-vous: "))
			break
		except ValueError:
			print('Ce n\'est pas un nombre valide')

	# On récupère les relations entre les points
	relation = {}
	# print("Vous avez ",sommet," sommets, veuillez saisir les relations entre vos points sous la forme A: B,C,D")
	for i in range(sommet):
		nbRelation, temp = 0, {}
		while True:
			try:
				nbRelation = int(input("Combien de relations avez-vous avec "+chr(i+65)+": "))
				break
			except ValueError:
				print('Ce n\'est pas un nombre valide')

		print("Vous avez ",nbRelation," relations avec ",chr(i+65))
		
		for j in range(nbRelation):
			nom, poids = "", 0
			while True:
				try:
					nom = str(input(chr(i+65)+" est relié à: "))
					break
				except Exception as e:
					print('Ce n\'est pas une valeur valide')

			while True:
				try:
					poids = int(input("Le poids entre "+chr(i+65)+" et "+nom+" est de: "))
					break
				except ValueError:
					print('Ce n\'est pas un nombre valide')
			print('\n')
			temp[nom] = poids
		relation[chr(int(ord(str(i)) + 17))] = temp

	pStart, pEnd = "", "" 
	# On demande le point de départ
	while True:
		pStart = str(input("Veuillez choisir votre point de départ (A,B,...): "))
		if len(pStart) > 1 or ord(pStart) < 65 or ord(pStart) > 65 + sommet:
			print("Vous avez saisie une mauvaise valeur")
		else:
			break
	# On demande le point de sortie
	while True:
		pEnd = str(input("Veuillez choisir votre point de sortie (A,B,...): "))
		if len(pEnd) > 1 or ord(pEnd) < 65 or ord(pEnd) > 65 + sommet:
			print("Vous avez saisie une mauvaise valeur")
		else:
			break

	return relation, pStart, pEnd


def search_parents (parent, pStart, extremite, trajet):
	if extremite == pStart:
		return [pStart] + trajet
	else:
		return (search_parents(parent, pStart, parent[extremite], [extremite] + trajet))

def plus_court(matrice, pStart, pEnd, etape, visites, dist, parent):
	'''
		matrice: graphe étudié
		pStart: sommet de depart
		pEnd: sommet d'arrivé
		etape: sommet en cours d'études
		visites: sommet déjà visité
		dist: dictionnaire comprenant les meilleurs distances entre les sommets déjà parcourus et le point de départ
		parent: dictionnaire des pères actuels des sommets correspondant aux meilleurs chemin
		
	'''

	# Fin 
	if etape == pEnd:
		return dist[pEnd], search_parents(parent, pStart, pEnd, [])
	
	# Si c'est la première visite
	if len(visites) == 0: dist[etape] = 0

	# On test les voisins non visités
	for voisin in matrice[etape]:
		# Si c'est un voisin que nous n'avons pas visité
		if voisin not in visites:
			# On récupère la distance
			dist_voisin = dist.get(voisin, inf)
			# On calcule la nouvelle distance entre le nouveau point et le point de départ
			candidat_dist = dist[etape] + matrice[etape][voisin]

			# Si la distance est plus courte
			if candidat_dist < dist_voisin:
				dist[voisin] = candidat_dist
				parent[voisin] = etape
	
	# On ajoute l'étape visité
	visites.append(etape)
	non_visites =  dict((s, dist.get(s, inf)) for s in matrice if s not in visites)
	# Renvoie la clé ayant le poids le plus petit
	noeud_plus_proche = min(non_visites, key = non_visites.get)
	return plus_court(matrice, pStart, pEnd, noeud_plus_proche, visites, dist, parent)

# Algorithme de Dijkstra
def dijkstra(matrice, pStart, pEnd):
	return plus_court(matrice, pStart, pEnd, pStart, [], {}, {})

if __name__ == '__main__':
	
	# matrice, pStart, pEnd = recupData()
	
	pStart, pEnd = 'A', 'C'
	matrice = {'A': {'B': 4, 'D': 2}, 
				'B': {'A': 4, 'C': 3}, 
				'C': {'B': 3}, 
				'D':{'A': 2}
			    }

	poids, points = dijkstra(matrice, pStart, pEnd)


	
	print("Point de départ:",pStart,"\nPoint de sortie:",pEnd)
	print("Il faut parcourir les points",points,"avec un poids de",poids)	