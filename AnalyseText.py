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
post1_dict = {}
post2_dict = {}
post3_dict = {}
post4_dict = {}

student_dicts = {}

for subdir, dirs, files in os.walk(rootdir):

	#Collect all the data in blog posts and comments
	
	student_name = os.path.basename(os.path.normpath(subdir))
	#Create a collector for each individual students
	if (student_name != 'blog and comments'):
		student_dicts[student_name] = {}

	for file in files:
		#Collect data for blog post 1 from all students
		if file == 'Blog Post 1.txt':
			with open(os.path.join(subdir,file),'r') as f:
				word_dict = {}
				article = f.read()
				wordlist = nltk.WordPunctTokenizer().tokenize(article)
				d = enchant.Dict("en_US")
				#Lowercase
				wordlist = map(lambda x:x.lower(),wordlist)
				for word, pos in nltk.pos_tag(wordlist):

					#Check if the word is a valid english word
					if (d.check(word) and len(word) >= 2):
						#Select nouns as our target terminologies
						if ((pos == 'NN') or (pos == 'NNS') or (pos == 'NNP') or (pos == 'NNPS') ):
							if word not in word_dict:
								word_dict[word] = 0
							word_dict[word] += 1


				#Update blog post for individual students
				student_dicts[student_name].update(word_dict)
				#Collect blog post 1 for all students
			(post1_dict.update(word_dict))

		if file == 'Blog Post 2.txt':
			with open(os.path.join(subdir,file),'r') as f:
				word_dict = {}
				article = f.read()
				wordlist = nltk.WordPunctTokenizer().tokenize(article)
				d = enchant.Dict("en_US")
				#Lowercase
				wordlist = map(lambda x:x.lower(),wordlist)
				for word, pos in nltk.pos_tag(wordlist):

					#Check if the word is a valid english word
					if (d.check(word) and len(word) >= 2):
						#Select nouns as our target terminologies
						if ((pos == 'NN') or (pos == 'NNS') or (pos == 'NNP') or (pos == 'NNPS') ):
							if word not in word_dict:
								word_dict[word] = 0
							word_dict[word] += 1


							
				#Update blog post for individual students
				student_dicts[student_name].update(word_dict)
				#Collect blog post 2 for all students
			(post2_dict.update(word_dict))

		if file == 'Blog Post 3.txt':
			with open(os.path.join(subdir,file),'r') as f:
				word_dict = {}
				article = f.read()
				wordlist = nltk.WordPunctTokenizer().tokenize(article)
				d = enchant.Dict("en_US")
				#Lowercase
				wordlist = map(lambda x:x.lower(),wordlist)
				for word, pos in nltk.pos_tag(wordlist):

					#Check if the word is a valid english word
					if (d.check(word) and len(word) >= 2):
						#Select nouns as our target terminologies
						if ((pos == 'NN') or (pos == 'NNS') or (pos == 'NNP') or (pos == 'NNPS') ):
							if word not in word_dict:
								word_dict[word] = 0
							word_dict[word] += 1

							
				#Update blog post for individual students
				student_dicts[student_name].update(word_dict)
				#Collect blog post 3 for all students
			(post3_dict.update(word_dict))

		if file == 'Blog Post 4.txt':
			with open(os.path.join(subdir,file),'r') as f:
				word_dict = {}
				article = f.read()
				wordlist = nltk.WordPunctTokenizer().tokenize(article)
				d = enchant.Dict("en_US")
				#Lowercase
				wordlist = map(lambda x:x.lower(),wordlist)
				for word, pos in nltk.pos_tag(wordlist):

					#Check if the word is a valid english word
					if (d.check(word) and len(word) >= 2):
						#Select nouns as our target terminologies
						if ((pos == 'NN') or (pos == 'NNS') or (pos == 'NNP') or (pos == 'NNPS') ):
							if word not in word_dict:
								word_dict[word] = 0
							word_dict[word] += 1
							
				#Update blog post for individual students
				student_dicts[student_name].update(word_dict)
				#Collect blog post 4 for all students
			(post4_dict.update(word_dict))

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
				word_dict = {}
				wordlist = nltk.WordPunctTokenizer().tokenize(article)
				d = enchant.Dict("en_US")
				#Lowercase							
				wordlist = map(lambda x:x.lower(),wordlist)
				for word, pos in nltk.pos_tag(wordlist):

					#Check if the word is a valid english word
					if (d.check(word) and len(word) >= 2):
						#Select nouns as our target terminologies
						if ((pos == 'NN') or (pos == 'NNS') or (pos == 'NNP') or (pos == 'NNPS') ):
							if word not in word_dict:
								word_dict[word] = 0
							word_dict[word] += 1

							
				#Update blog post for individual students
				student_dicts[student_name].update(word_dict)

				#Collect blog post for all students
				if (index == 0):
					(post1_dict.update(word_dict))
				if (index == 1):
					(post2_dict.update(word_dict))
				if (index == 2):
					(post3_dict.update(word_dict))
				if (index == 3):
					(post4_dict.update(word_dict))



print(len(post1_dict))
print(len(post2_dict))
print(len(post3_dict))
print(len(post4_dict))
print(len(student_dicts), student_dicts.keys())


