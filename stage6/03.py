#WAP to play the cards game where cards are all arranged front and back
# and we need to remove a card if it is 0 and flip all the other cards if it is 1
# at the last if the is 1 we win else we loose

cards = '10011101000001'
cards = list(cards)
#1 - filp all
#0 - remove

while len(cards)>1:
	card = cards[0]

	if card=='0':
		cards.pop(0)

	if card == '1':
		for i in range(1,len(cards)):
			card = cards[i]
			if card=='0':
				cards[i]='1'
			elif card=='1':
				cards[i]='0'
		cards.pop(0)

if cards[0] == '1':
	print('win')
else:
	print('loose')


