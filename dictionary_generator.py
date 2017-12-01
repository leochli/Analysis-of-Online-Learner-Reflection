import nltk
import os
import enchant
from nltk.corpus import words

rootdir = 'LectureNotesText/'

all_words_dict = {}
for subdir, dirs, files in os.walk(rootdir):
	# i = 0
	for file in files:
		# i = i + 1
		if file.endswith('.txt'):
			with open(os.path.join(subdir,file),'r') as f:
				word_dict = {}
				article = f.read()
				wordlist = nltk.WordPunctTokenizer().tokenize(article)
				d = enchant.Dict("en_US")
				wordlist = map(lambda x:x.lower(),wordlist)
				for word, pos in nltk.pos_tag(wordlist):
					# print(word, pos)

					#Check if the word is a valid english word
					if (d.check(word) and len(word) >= 2):
						#Select nouns as our target terminologies
						if ((pos == 'NN') or (pos == 'NNS') or (pos == 'NNP') or (pos == 'NNPS') ):
							if word not in word_dict:
								word_dict[word] = 0
							word_dict[word] += 1

							if word not in all_words_dict:
								all_words_dict[word] = 0
							all_words_dict[word] += 1


				# print(word_dict)

				#Output the word dictionary for each week
				with open('lecture_word_dicts/' + subdir[-5:] + '.txt', 'a') as output_file:
					for key, value in word_dict.iteritems():
						print(key,value)
						print(str(key) + ' ' + str(value) + '\n')
						if (str(key) != 'page'):
							output_file.write(str(key) + ' ' + str(value) + '\n')
						print(len(word_dict))

#Output the total word dictionary
with open('lecture_word_dicts/total_word_dict.txt', 'a') as output_file:
	for key, value in all_words_dict.iteritems():
		print(key,value)
		print(str(key) + ' ' + str(value) + '\n')
		if (str(key) != 'page'):
			output_file.write(str(key) + ' ' + str(value) + '\n')

	print(len(all_words_dict))

