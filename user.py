#user.py
#both mentor/mentee questions
name
communication = ['email', 'phone', 'Skype', 'text', 'in-person'] #preference--select all that apply
age = ['10-15', '16-20', '21-25', '26-30', '30+']
location #city, state, country*
gender = ['female', 'male', 'nonbinary', 'prefer not to say']
spokenLanguages = ['English', 'Chinese', 'Spanish', 'Arabic', 'Portuguese', 'Japanese', 'Malaysian', 'Russian', 'French', 'German']
relationshipGoals = ['casual', 'formal']

#mentor-specific
occupationMentor = ['undergraduate', 'graduate student', 'PhD student', 'working professional', 'self-employed', 'retired', 'other']
codingLanguages = ['Python', 'JavaScript', 'Java', 'PHP', 'Ruby', 'SQL', 'C#', 'C++', 'iOS', 'other'] #select all that apply
skillLevel = [0, 1, 2, 3, 4] #mentor ranks their level of skill when they select languages
resume #could be linkedIn url
mentorBio

#mentee-specific
occupationMentee = ['middle school student', 'high school student', 'college student', 'working professional', 'other']
mentorType = ['basic programming skills', 'improving skills/language', 'career guidance']
interests = ['front end/web development', 'back end', 'hardware', 'cybersecurity', 'hackathons', 'tech conferences', 'tech meet-ups']


class User(object):

	def __init__(self, name, communication, age, location, gender, spokenLanguages, relationshipGoals, occupation, codingLanguages=None, resume=None, mentorBio=None, mentorType=None, interests=None):
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
