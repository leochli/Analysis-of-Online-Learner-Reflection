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
lecture_dicts_rootdir = 'lecture_word_dicts/'
post1_dict = {}
post2_dict = {}
post3_dict = {}
post4_dict = {}

student_dicts = {}
received_comments_dicts = {}

total_lecture_dict = {}

#To load all the text for analysing, including: blog posts and comments from each assignment, individual texts

def load_analysing_text():

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
							#Select words as our target terminologies

							#Update blog post for individual students
							if word not in student_dicts[student_name]:
								student_dicts[student_name][word] = 0
							student_dicts[student_name][word] += 1

							#Collect blog post 1 for all students
							if word not in post1_dict:
								post1_dict[word] = 0
							post1_dict[word] +=1

			if file == 'Blog Post 2.txt':
				with open(os.path.join(subdir,file),'r') as f:
					article = f.read()
					wordlist = nltk.WordPunctTokenizer().tokenize(article)
					d = enchant.Dict("en_US")
					#Lowercase
					wordlist = map(lambda x:x.lower(),wordlist)
					for word, pos in nltk.pos_tag(wordlist):

						#Check if the word is a valid english word
						if (d.check(word) and len(word) >= 2):					

							#Update blog post for individual students
							if word not in student_dicts[student_name]:
								student_dicts[student_name][word] = 0
							student_dicts[student_name][word] += 1

							#Collect blog post 2 for all students
							if word not in post2_dict:
								post2_dict[word] = 0
							post2_dict[word] +=1

			if file == 'Blog Post 3.txt':
				with open(os.path.join(subdir,file),'r') as f:
					article = f.read()
					wordlist = nltk.WordPunctTokenizer().tokenize(article)
					d = enchant.Dict("en_US")
					#Lowercase
					wordlist = map(lambda x:x.lower(),wordlist)
					for word, pos in nltk.pos_tag(wordlist):

						#Check if the word is a valid english word
						if (d.check(word) and len(word) >= 2):

							#Update blog post for individual students
							if word not in student_dicts[student_name]:
								student_dicts[student_name][word] = 0
							student_dicts[student_name][word] += 1
								
							#Collect blog post 3 for all students
							if word not in post3_dict:
								post3_dict[word] = 0
							post3_dict[word] +=1

			if file == 'Blog Post 4.txt':
				with open(os.path.join(subdir,file),'r') as f:
					article = f.read()
					wordlist = nltk.WordPunctTokenizer().tokenize(article)
					d = enchant.Dict("en_US")
					#Lowercase
					wordlist = map(lambda x:x.lower(),wordlist)
					for word, pos in nltk.pos_tag(wordlist):

						#Check if the word is a valid english word
						if (d.check(word) and len(word) >= 2):
								
							#Update blog post for individual students
							if word not in student_dicts[student_name]:
								student_dicts[student_name][word] = 0
							student_dicts[student_name][word] += 1

							#Collect blog post 4 for all students
							if word not in post4_dict:
								post4_dict[word] = 0
							post4_dict[word] +=1

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
					# print(subdir, len(article_comments[0]),len(article_comments[1]),len(article_comments[2]),len(article_comments[3]))

				for index, article in enumerate(article_comments):
					wordlist = nltk.WordPunctTokenizer().tokenize(article)
					d = enchant.Dict("en_US")
					#Lowercase							
					wordlist = map(lambda x:x.lower(),wordlist)
					for word, pos in nltk.pos_tag(wordlist):

						#Check if the word is a valid english word
						if (d.check(word) and len(word) >= 2):

							#Update blog post for individual students
							if word not in student_dicts[student_name]:
								student_dicts[student_name][word] = 0
							student_dicts[student_name][word] += 1

							#Collect comments for all students
							if (index == 0):
								#Collect commnets 1 for all students
								if word not in post1_dict:
									post1_dict[word] = 0
								post1_dict[word] +=1

							if (index == 1):
								if word not in post2_dict:
									post2_dict[word] = 0
								post2_dict[word] +=1

							if (index == 2):
								if word not in post3_dict:
									post3_dict[word] = 0
								post3_dict[word] +=1
							if (index == 3):
								if word not in post4_dict:
									post4_dict[word] = 0
								post4_dict[word] +=1

def load_comment_text():
	for subdir, dirs, files in os.walk(comments_rootdir):
		for file in files:
			#Create a directory for each student id
			if file.endswith('.txt'):
				sid = file[:-4]
				if sid not in received_comments_dicts:
					received_comments_dicts[sid] = {}

				with open(os.path.join(subdir,file), 'r') as comments_f:
					article = comments_f.read()
					wordlist = nltk.WordPunctTokenizer().tokenize(article)
					d = enchant.Dict("en_US")
					#Lowercase
					wordlist = map(lambda x:x.lower(),wordlist)
					for word, pos in nltk.pos_tag(wordlist):
						#Check if the word is a valid english word
						if (d.check(word) and len(word) >= 2):

							if word not in received_comments_dicts[sid]:
								received_comments_dicts[sid][word] = 0
							received_comments_dicts[sid][word] += 1

def load_lecture_text():
	with open(lecture_dicts_rootdir + 'total_word_dict.txt', 'rb') as lecture_f:
		lines = lecture_f.readlines()
		for line in lines:
			line = line.split()
			if line[0] not in total_lecture_dict:
				total_lecture_dict[line[0]] = line[1]

def read_senti_dict():
	with open('senti_dict.txt', 'rb') as senti_f:
		senti_data = json.load(senti_f)
	return senti_data

#After getting all the analysing text, start our analysing

#First Sentiment Analysis -- personality analysis

def personality_analysis():
	senti_data = read_senti_dict()
	for student_name, individual_dict in student_dicts.iteritems():
		pos_score = 0
		neg_score = 0
		text_length = 0
		for word in individual_dict:
			text_length += individual_dict[word]

			if word in senti_data:
				pos_score = pos_score + senti_data[word]['pos'] * individual_dict[word]
				neg_score = neg_score + senti_data[word]['neg'] * individual_dict[word]
			else:
				pos_score = pos_score + 0
				neg_score = neg_score + 0
		if pos_score > neg_score:
			polarity = 1
		elif (pos_score < neg_score):
			polarity = -1
		else:
			polarity = 0


		print('Student Name: ' + student_name +
			', Text Length ' + str(text_length) +
			', Personality Scores: Positive -- ' + str(pos_score/text_length * 100 * 20) + 
			' Critical -- ' + str(neg_score/text_length * 100 * 20) +
			', Polarity: ' +  str(polarity) + '\n')

#Second Sentiment Analysis -- comment analysis

def sentiment_analysis():
	senti_data = read_senti_dict()
	for sid, comment_dict in received_comments_dicts.iteritems():
		pos_score = 0
		neg_score = 0
		text_length = 0
		for word in comment_dict:
			text_length += comment_dict[word]

			if word in senti_data:
				pos_score = pos_score + senti_data[word]['pos'] * comment_dict[word]
				neg_score = neg_score + senti_data[word]['neg'] * comment_dict[word]
			else:
				pos_score = pos_score + 0
				neg_score = neg_score + 0
		if pos_score > neg_score:
			polarity = 1
		elif (pos_score < neg_score):
			polarity = -1
		else:
			polarity = 0

		print('Student ID: ' + sid +
			', Text Length ' + str(text_length) +
			', Sentiment Score: Positive -- ' + str(pos_score/text_length) +
			', Negative -- ' + str(neg_score/text_length) +
			', Polarity: ' + str(polarity) + '\n')

#Third Terminology Coverage Analysis -- TCA

def coverage_analysis():
	terminology_usage = 0
	terminology_coverage = 0
	for student_name, individual_dict in student_dicts.iteritems():

		for word in total_lecture_dict:
			if word in individual_dict:
				terminology_coverage += 1
				terminology_usage += individual_dict[word]

		print('Student Name: ' + student_name,
		 'Terminology Coverage: ' + str(terminology_coverage), 
		 'Total terminologies: ' + str(len(total_lecture_dict)))
		print('Student Name: ' + student_name,
		 'Terminology Usage: ' + str(terminology_usage), 
		 'Total terminologies: ' + str(len(total_lecture_dict)))
		print('\n')




load_analysing_text()
load_comment_text()
load_lecture_text()

personality_analysis()
sentiment_analysis()
coverage_analysis()



