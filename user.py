#user.py
#both mentor/mentee questions
name
communication = ['email', 'phone', 'Skype', 'text', 'in-person'] #preference--select all that apply
age = ['10-15', '16-20', '21-25', '26-30', '30+']
location #country
gender = ['female', 'male', 'nonbinary', 'prefer not to say']
spokenLanguages = ['English', 'Chinese', 'Spanish', 'Arabic', 'Portuguese', 'Japanese', 'Malaysian', 'Russian', 'French', 'German']
relationshipGoals = ['casual', 'formal']
mentorType = ['basic programming skills', 'improving skills/language', 'career guidance']

#mentor-specific
occupationMentor = ['undergraduate', 'graduate student', 'PhD student', 'working professional', 'self-employed', 'retired', 'other']
codingLanguages = ['HTML/CSS', 'JavaScript', 'Python', 'Java', 'PHP', 'Ruby', 'SQL', 'C#', 'C++', 'iOS', 'other'] #select all that apply
skillLevel = [0, 1, 2, 3, 4] #mentor ranks their level of skill when they select languages
resume #could be linkedIn url
mentorBio

#mentee-specific
occupationMentee = ['middle school student', 'high school student', 'college student', 'working professional', 'other']
interests = ['front end/web development', 'back end', 'data analysis', 'hardware', 'cybersecurity', 'hackathons', 'tech conferences', 'tech meet-ups']


class User(object):

	def __init__(self, mentorStatus=False, name, communication, age, location, gender, spokenLanguages, relationshipGoals, occupation, codingLanguages=None, resume=None, mentorBio=None, mentorType=None, interests=None):
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
		communication(d)
		if self.location == 'US':
			vectors.append

	def communication(d):
		if '0' in self.communication: #email
			vectors.append(1)
		else
			vectors.append(0)		
		if '1' in self.communication: #phone
			vectors.append(1)
		else
			vectors.append(0)
		if '2' in self.communication: #Skype
			vectors.append(1)
		else
			vectors.append(0)	
		if '3' in self.communication: #text
			vectors.append(1)
		else
			vectors.append(0)	
		if '4' in self.communication: #in-person
			vectors.append(1)
		else
			vectors.append(0)	
