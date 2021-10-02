
liste = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]

for x in range(len(liste)):
	liste.append(liste[x])



def chiffrage_lettre(lettre, liste, clef):
	for i in range(len(liste)):
		if lettre == ' ':
			return ' '
		elif liste[i]==lettre:
			return str(liste[i+clef])
	return '?'

message_chiffre = str()



while True:
	message = input('Entrez votre messsage : ')
	clef = int(input('Entrez la clef (de 1 a 25) : '))
	for lettre in message:
		message_chiffre += chiffrage_lettre(lettre, liste, clef)

	print(message_chiffre)
