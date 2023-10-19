    
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def outputsumm(input_text,num_s=5,reverse=False):
	stopWords = set(stopwords.words("english"))
	words = word_tokenize(input_text)
	f = dict()
	for i in words:
		i = i.lower()
		if i in stopWords:
			continue

		if i in f:
			f[i] += 1
		else:
			f[i] = 1
	sentences = sent_tokenize(input_text)
	fsent = dict()
	for j in sentences:
		for x, y in f.items():
			if x in j.lower():
				if j in fsent:
					fsent[j] += y
				else:
					fsent[j] = y
	count = 0
	for k in fsent:
		count += fsent[k]
	average = int(count / len(fsent))
	output_text = ''
	c=0
	if reverse==False:
		for i in range(num_s):
			if sentences[i] in fsent:
				output_text+=" "+sentences[i]
	else:
		output_t = ''
		length=len(sentences)
		for i in range(num_s):
			if sentences[length-i-1] in fsent:
				output_text += " "+sentences[length-i-1]
	return output_text
