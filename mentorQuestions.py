#match.wit
#mentor questions

#both mentor/mentee questions
name
communication = ['email', 'phone', 'Skype', 'text', 'in-person'] #preference--select all that apply
age = ['10-15', '16-20', '21-25', '26-30', '30+']
location #city, state, country*
gender = ['female', 'male', 'nonbinary', 'prefer not to say']
spokenLanguages = ['English', 'Chinese', 'Spanish', 'Arabic', 'Portuguese', 'Japanese', 'Malaysian', 'Russian', 'French', 'German']
relationshipHopes = ['casual', 'formal']

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

#store created profiles
def createMentorProfile():

def createMenteeProfile():

#resources
hackathons = [('San Diego Women\'s Hackathon', 'International Women\'s Hackathon', 'WHACK: Wellesley Hackathon', 'Women Who Code Hackathon',
	'WiCHacks: RIT Women in Computing Hackathon')]
codingTutorials = ['Hour of Code', 'BBC Bitesize', 'Tynker', 'Code Academy', 'Code Wars', 'Coursera', 'edX', 'Dash']
conferences = ['Grace Hopper', 'WeCode', 'ACM Richard Tapia Celebration of Diversity in Computing']
scholarships = [('Ann Arbor Women in Computing Scholarship', 'Women Techmakers Scholars Program', 'Palentir Scholarship for Women in Technology', 
	'SAE Women Engineers Committee Scholarship', 'Gamers In Real Life (GIRL) Game Design Competition Scholarship Program', 'SWE Scholarships',
	'Women in Technology Scholarship (WITS) Program', 'Carnegie Mellon Executive Women\'s Forum INI Fellowship', 'CWIT Scholars',
	'Michigan Council of Women in Technology Scholarships', 'NCWIT Award for Aspirations in Computing') ]
preCollege = ['Aspirations in Computing', 'AspireIT', 'Girls Who Code', 'National Girls Collaborative Program', 'Girls RiseNET']

def resourcesForMiddleSchool():
	return codingTutorials[0:3] + preCollege

def resourcesForHighSchool():
	return codingTutorials[0:2] + codingTutorials[3:5] + codingTutorials[6:8] + scholarships[8:11]

def resourcesForCollege():
	return codingTutorials[0:2] + codingTutorials[3:8] + scholarships[0:8] + scholarships[9:11] + conferences

def resourcesFrontEnd():
	return codingTutorials[3] + codingTutorials[5:8]

def resourcesBackEnd():
	return codingTutorials[0:8]

