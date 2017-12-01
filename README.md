# Analysis of Online Learner Reflection
This is the project of online learner reflection analysis. In this project, we analyse:

* the personality score of online learners
* the sentiment score of online learners' received blog post comments
* the terminology usage and coverage of online learns' blog post and comments, where the terminology pool is the total terminologies appeared in the lecture material

## Usage

*dictionary_generator.py* It is used to generate the dictionary of all the lecture materials. The dictionary contains all the terminologies and their corresponding term frequency(TF)

*senti_dict_generator.py* It is used to generate the sentiment score dictionary of all the potential using words. The score of each word is calculated by NLTK corpus SentiWordNet. We collect the positive score and negtive score of each word.

*AnalyseText.py* In this code, we collect the analysing data from the blog post, delivered comments and received comments from online learners. Afterwards, we analyse the three foregoing terms.
