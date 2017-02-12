#user.py
from geopy.geocoders import Nominatim
geolocator = Nominatim()

#both mentor/mentee questions
#name
communication = ['email', 'phone', 'Skype', 'text', 'in-person'] #preference--select all that apply
age = ['10-15', '16-20', '21-25', '26-30', '30+']
#location #zipcode
gender = ['female', 'male', 'nonbinary', 'prefer not to say']
spokenLanguages = ['English', 'Chinese', 'Spanish', 'Arabic', 'Portuguese', 'Japanese', 'Malaysian', 'Russian', 'French', 'German']
relationshipGoals = ['casual', 'formal']
mentorType = ['basic programming skills', 'improving skills/language', 'career guidance']

#mentor-specific
occupationMentor = ['undergraduate', 'graduate student', 'PhD student', 'working professional', 'self-employed', 'retired', 'other']
codingLanguages = ['HTML/CSS', 'JavaScript', 'Python', 'Java', 'PHP', 'Ruby', 'SQL', 'C#', 'C++', 'iOS', 'other'] #select all that apply
#skillLevel = [0, 1, 2, 3, 4] #mentor ranks their level of skill when they select languages
#resume #could be linkedIn url
#mentorBio

#mentee-specific
occupationMentee = ['middle school student', 'high school student', 'undergraduate', 'graduate student', 'working professional', 'other']
interests = ['front end/web development', 'back end', 'data analysis', 'hardware', 'cybersecurity', 'hackathons', 'tech conferences', 'tech meet-ups']

#example mentors
mentors = {"Alison Savage", "Hye Sun Yun", "Karina Lin", "Jess Cherayil", "Clara Sorensen"}

class User(object):

	def __init__(self,  name, communication, age, location, gender, spokenLanguages, relationshipGoals, occupation, mentorStatus=False, codingLanguages=None, resume=None, mentorBio=None, mentorType=None, interests=None):
		self.mentorStatus = mentorStatus
		self.name = name
		self.communication = communication
		self.age = age
		self.location = location
		self.gender = gender
		self.spokenLanguages = spokenLanguages
		self.relationshipGoals = relationshipGoals
		self.occupation = occupation
		self.codingLanguages = codingLanguages
		self.resume = resume
		self.mentorBio = mentorBio
		self.interests = interests

	def buildVector(d):
		vectors = []
		communicationF(d)
		location = geolocator.geocode(self.location)
		vectors.append(location[1][0]) #latitude
		vectors.append(location[1][1]) #longitude
		genderF(d)
		spokenLanguagesF(d)
		if self.relationshipGoals == 'casual':
			vector.append(0)
		else:
			vector.append(1)
		mentorTypeF(d)
		occuptionMentorF(d)
		codingXinterests(d)

	def communicationF(d):
		if '0' in self.communication: #email
			vectors.append(1)
		else:
			vectors.append(0)		
		if '1' in self.communication: #phone
			vectors.append(1)
		else:
			vectors.append(0)
		if '2' in self.communication: #Skype
			vectors.append(1)
		else:
			vectors.append(0)	
		if '3' in self.communication: #text
			vectors.append(1)
		else:
			vectors.append(0)	
		if '4' in self.communication: #in-person
			vectors.append(1)
		else:
			vectors.append(0)	

	def genderF(d):
		if '0' in self.gender: #female
			vectors.append(0)
		elif '1' in self.gender: #male
			vectors.append(1)	
		elif '2' in self.gender: #nonbinary
			vectors.append(2)
		else:
			vectors.append(3)	

	def spokenLanguagesF(d):
		if '0' in self.spokenLanguages: #English
			vectors.append(1)
		else:
			vectors.append(0)

		if '1' in self.spokenLanguages: #Chinese
			vectors.append(1)	
		else:
			vectors.append(0)

		if '2' in self.spokenLanguages: #Spanish
			vectors.append(1)
		else:
			vectors.append(0)

		if '3' in self.spokenLanguages: #Arabic
			vectors.append(1)	
		else:
			vectors.append(0)

		if '4' in self.spokenLanguages: #Portuguese
			vectors.append(1)
		else:
			vectors.append(0)

		if '5' in self.spokenLanguages: #Japanese
			vectors.append(1)
		else:
			vectors.append(0)				

		if '6' in self.spokenLanguages: #Malaysian
			vectors.append(1)
		else:
			vectors.append(0)			

		if '7' in self.spokenLanguages: #Russian
			vectors.append(1)
		else:
			vectors.append(0)

		if '8' in self.spokenLanguages: #French
			vectors.append(1)
		else:
			vectors.append(0)

		if '9' in self.spokenLanguages: #German
			vectors.append(1)
		else:
			vectors.append(0)

	def mentorTypeF(d):
		if '0' in self.mentorType: #basic programming skills
			vectors.append(1)
		else:
			vectors.append(0)

		if '1' in self.mentorType: #improving skills/language
			vectors.append(1)	
		else:
			vectors.append(0)

		if '2' in self.mentorType: #career guidance
			vectors.append(1)
		else:
			vectors.append(0)

	def occupationMentorF(d):
		if self.mentorStatus: #mentor
			if self.occupation == 'undergraduate':
				vectors.append(0)
			elif (self.occupation == 'graduate student') or (self.occupation == 'PhD student'):
				vectors.append(1)
			elif (self.occupation =='working professional') or (self.occupation == 'self-employed') or (self.occupation == 'retired'):
				vectors.append(2)
			else:
				vectors.append(3)
		else: #mentee
			if (self.occupation == 'middle school student') or (self.occupation == 'high school student'):
				vectors.append(0)
			elif self.occupation == 'undergraduate':
				vectors.append(1)
			elif (self.occupation == 'graduate student') or (self.occupation == 'working professional'):
				vectors.append(2)
			else:
				vectors.append(3)

	def codingXinterests(d):
		languageArray = [0] * 10

		'HTML/CSS', 'JavaScript', 'Python', 'Java', 'PHP', 'Ruby', 'SQL', 'C#', 'C++', 'iOS'
		if self.mentorStatus: #mentor
			if 'HTML/CSS' in self.codingLanguages:
				languageArray[0] = 1
				#languageArray[0] = self.codingLanguages.find('HTML/CSS') + len('HTML/CSS') - 1
			if 'JavaScript' in self.codingLanguages:
				languageArray[1] = 1
				#languageArray[1] = self.codingLanguages.find('JavaScript') + len('JavaScript') - 1
			if 'Python' in self.codingLanguages:
				languageArray[2] = 1
				#languageArray[2] = self.codingLanguages.find('Python') + len('Python') - 1
			if 'Java' in self.codingLanguages:
				languageArray[3] = 1
				#languageArray[3] = self.codingLanguages.find('Java') + len('Java') - 1
			if 'PHP' in self.codingLanguages:
				languageArray[4] = 1
				#languageArray[4] = self.codingLanguages.find('PHP') + len('PHP') - 1
			if 'Ruby' in self.codingLanguages:
				languageArray[5] = 1
				#languageArray[5] = self.codingLanguages.find('Ruby') + len('Ruby') - 1
			if 'SQL' in self.codingLanguages:
				languageArray[6] = 1
				#languageArray[6] = self.codingLanguages.find('SQL') + len('SQL') - 1
			if 'C#' in self.codingLanguages:
				languageArray[7] = 1
				#languageArray[7] = self.codingLanguages.find('C#') + len('C#') - 1
			if 'C++' in self.codingLanguages:
				languageArray[8] = 1
				#languageArray[8] = self.codingLanguages.find('C++') + len('C++') - 1
			if 'iOS' in self.codingLanguages:
				languageArray[9] = 1
				#languageArray[9] = self.codingLanguages.find('iOS') + len('iOS') - 1

		else: #mentee
			if '0' in self.interests:
				languageArray[0] = 1
				languageArray[1] = 1
				languageArray[4] = 1
				languageArray[5] = 1
				languageArray[9] = 1
			if '1' in self.interests:
				languageArray[2] = 1
				languageArray[3] = 1
				languageArray[8] = 1
			if '2' in self.interests:
				languageArray[2] = 1
				languageArray[6] = 1
			if '3' in self.interests:
				languageArray[7] = 1
				languageArray[8] = 1
			if '4' in self.interests:
				languageArray[1] = 1
				languageArray[2] = 1

		vectors.append(languageArray)

	def getVector():
		return vectors

import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def load(filename):
    x = np.loadtxt(filename, delimiter=',')
    y = np.loadtxt(filename, delimiter = ',', usecols = (-1,))
    
    return (x,y)

def sklearn_knn_predict(trainX, trainy, testX, k, distance_metric):
    model = KNeighborsClassifier(algorithm='brute',
                                 n_neighbors=k,
                                 metric=distance_metric)

    model.fit(trainX, trainy)
    return model.predict(testX)

def userMatch(userTest):
	trainX, trainy = load(os.path.join(datadir, 'mentors.txt'))
	predict = sklearn_knn_predict(trainX, trainy, userTest.getVector(), 1, 'euclidean')
	return mentors[predict]
