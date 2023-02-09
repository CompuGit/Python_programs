#WAP to limit the keystrokes for a string using functions
#the input considered to the list of character and limt separated by coma
#and a given string text
#Input : lst = ['e,3','t,5','a,1','s,1']; text = 'statement is a statement'
#Output : 'statement i  ttemn'


remainingKeystrokes = ['e,3','t,5','a,1','s,1']
text = 'statement is a statement'

def limit(text, remainingKeystrokes):
	d = {}
	for every in remainingKeystrokes:
		key,value = every.split(',')
		d[key]= int(value)

	res = []
	for every in text:
		if every in d.keys():
			if d[every]!=0:
				res.append(every)
				d[every] = d.get(every)-1
		else:
			res.append(every)

	return ''.join(res)

print(limit(text, remainingKeystrokes))




