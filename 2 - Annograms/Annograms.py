def annograms(word):
	words = [w.rstrip() for w in open('WORD.lst')]
	annograms=[]
	for x in range(len(words)):
		if (len(word)==len(words[x])):		# Para ser un anograma deben tener la misma cantidad de letras
			flag = True
			# Una palabra es anagrama de otra si tienen las mismas letras en distinto orden.
			# Esto quiere decir que sí y solo sí, tienen la misma cantidad de letras y todas las letras de una estan en otra y biceversa.  
			for y in range(len(word)):
				flag = flag and (word[y] in words[x])
			# Si hago solo la ida del sí solo sí, podria surgir un error.
			# Por ejemplo: stat -> rats. Debo hacer la vuelta del también.
			for y in range(len(words[x])):
				flag = flag and (words[x][y] in word)  
			if flag:
				#if not word==words[x]:		# No pregunto si es la misma palabra, ya que la misma es válida como anagrama.
				annograms.append(words[x])
	return annograms


if __name__ == "__main__":
	print(annograms("train"))
	print('--')
	print(annograms('drive'))
	print('--')
	print(annograms('python'))