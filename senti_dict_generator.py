import os
from os import listdir
import json
import nltk
import csv
import enchant
from nltk.corpus import words
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn


rootdir = 'blog and comments/'
comments_rootdir = 'received blog comments/'


senti_dict = {}

for subdir, dirs, files in os.walk(rootdir):

	#Collect all the data in blog posts and comments

	for file in files:
		#Collect data for blog post 1 from all students
		if file == 'Blog Post 1.txt':
			with open(os.path.join(subdir,file),'r') as f:
				article = f.read()
				wordlist = nltk.WordPunctTokenizer().tokenize(article)
				d = enchant.Dict("en_US")
				#Lowercase
				wordlist = map(lambda x:x.lower(),wordlist)
				for word, pos in nltk.pos_tag(wordlist):

					#Check if the word is a valid english word
					if (d.check(word) and len(word) >= 2):

						#Construct sentiment directory
						if word not in senti_dict:
							senti_dict[word] = {'pos':0, 'neg':0}
							if wn.synsets(word):
								senti_word = wn.synsets(word)[0]
								pos = swn.senti_synset(senti_word.name()).pos_score()
								neg = swn.senti_synset(senti_word.name()).neg_score()
								senti_dict[word]['pos'] = pos
								senti_dict[word]['neg'] = neg


		if file == 'Blog Post 2.txt':
			with open(os.path.join(subdir,file),'r') as f:
				article = f.read()
				wordlist = nltk.WordPunctTokenizer().tokenize(article)
				d = enchant.Dict("en_US")
				#Lowercase
				wordlist = map(lambda x:x.lower(),wordlist)
				for word, pos in nltk.pos_tag(wordlist):

					if (d.check(word) and len(word) >= 2):
						#Construct sentiment directory
						if word not in senti_dict:
							senti_dict[word] = {'pos':0, 'neg':0}
							if wn.synsets(word):
								senti_word = wn.synsets(word)[0]
								pos = swn.senti_synset(senti_word.name()).pos_score()
								neg = swn.senti_synset(senti_word.name()).neg_score()
								senti_dict[word]['pos'] = pos
								senti_dict[word]['neg'] = neg
							

		if file == 'Blog Post 3.txt':
			with open(os.path.join(subdir,file),'r') as f:
				article = f.read()
				wordlist = nltk.WordPunctTokenizer().tokenize(article)
				d = enchant.Dict("en_US")
				#Lowercase
				wordlist = map(lambda x:x.lower(),wordlist)
				for word, pos in nltk.pos_tag(wordlist):

					if (d.check(word) and len(word) >= 2):
						#Construct sentiment directory
						if word not in senti_dict:
							senti_dict[word] = {'pos':0, 'neg':0}
							if wn.synsets(word):
								senti_word = wn.synsets(word)[0]
								pos = swn.senti_synset(senti_word.name()).pos_score()
								neg = swn.senti_synset(senti_word.name()).neg_score()
								senti_dict[word]['pos'] = pos
								senti_dict[word]['neg'] = neg


		if file == 'Blog Post 4.txt':
			with open(os.path.join(subdir,file),'r') as f:
				article = f.read()
				wordlist = nltk.WordPunctTokenizer().tokenize(article)
				d = enchant.Dict("en_US")
				#Lowercase
				wordlist = map(lambda x:x.lower(),wordlist)
				for word, pos in nltk.pos_tag(wordlist):

					if (d.check(word) and len(word) >= 2):
						#Construct sentiment directory
						if word not in senti_dict:
							senti_dict[word] = {'pos':0, 'neg':0}
							if wn.synsets(word):
								senti_word = wn.synsets(word)[0]
								pos = swn.senti_synset(senti_word.name()).pos_score()
								neg = swn.senti_synset(senti_word.name()).neg_score()
								senti_dict[word]['pos'] = pos
								senti_dict[word]['neg'] = neg
							

		if file.endswith('.csv'):
			with open(os.path.join(subdir,file), 'r') as file_comments:
				reader = csv.reader(file_comments)
				article_comments = list()
				article_comments.append('')
				article_comments.append('')
				article_comments.append('')
				article_comments.append('')

				for row in reader:
					if (row[0] != 'Message'):
						#Update comment 1
						if (int(row[0]) <= 4 and int(row[0]) >= 1 and len(row[3])>0):
							article_comments[0] = article_comments[0] + row[3]
						#Update comment 2
						if (int(row[0]) <= 8 and int(row[0]) >= 5 and len(row[3])>0):
							article_comments[1] = article_comments[1] + row[3]						
						#Update comment 3
						if (int(row[0]) <= 12 and int(row[0]) >= 9 and len(row[3])>0):
							article_comments[2] = article_comments[2] + row[3]						
						#Update comment 4
						if (int(row[0]) <= 16 and int(row[0]) >= 13 and len(row[3])>0):
							article_comments[3] = article_comments[3] + row[3]

				#print the length of each(postly blog comments of each students
				print(subdir, len(article_comments[0]),len(article_comments[1]),len(article_comments[2]),len(article_comments[3]))

			for index, article in enumerate(article_comments):
				wordlist = nltk.WordPunctTokenizer().tokenize(article)
				d = enchant.Dict("en_US")
				#Lowercase							
				wordlist = map(lambda x:x.lower(),wordlist)
				for word, pos in nltk.pos_tag(wordlist):

					if (d.check(word) and len(word) >= 2):
						#Construct sentiment directory
						if word not in senti_dict:
							senti_dict[word] = {'pos':0, 'neg':0}
							if wn.synsets(word):
								senti_word = wn.synsets(word)[0]
								pos = swn.senti_synset(senti_word.name()).pos_score()
								neg = swn.senti_synset(senti_word.name()).neg_score()
								senti_dict[word]['pos'] = pos
								senti_dict[word]['neg'] = neg

for subdir, dirs, files in os.walk(comments_rootdir):
	for file in files:
		if file.endswith('.txt'):
			with open(os.path.join(subdir,file), 'rb') as comments_f:
				article = comments_f.read()
				wordlist = nltk.WordPunctTokenizer().tokenize(article)
				d = enchant.Dict("en_US")
				#Lowercase
				wordlist = map(lambda x:x.lower(),wordlist)
				for word, pos in nltk.pos_tag(wordlist):
					#Check if the word is a valid english word
					if (d.check(word) and len(word) >= 2):
						#Construct sentiment directory
						if word not in senti_dict:
							senti_dict[word] = {'pos':0, 'neg':0}
							if wn.synsets(word):
								senti_word = wn.synsets(word)[0]
								pos = swn.senti_synset(senti_word.name()).pos_score()
								neg = swn.senti_synset(senti_word.name()).neg_score()
								senti_dict[word]['pos'] = pos
								senti_dict[word]['neg'] = neg
						


with open('senti_dict.txt','wb') as senti_f:
	senti_f.write(json.dumps(senti_dict, indent = 4, sort_keys=True))


print(len(senti_dict))


