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
codingTutorials = ['Hour of Code', 'BBC Bitesize', 'Tynker', 'Code Academy', 'Code Wars', 'Coursera', 'edX', 'Dash']
conferences = ['Grace Hopper', 'WeCode', 'ACM Richard Tapia Celebration of Diversity in Computing']
scholarships = [('Ann Arbor Women in Computing Scholarship', 'Women Techmakers Scholars Program', 'Palentir Scholarship for Women in Technology', 
	'SAE Women Engineers Committee Scholarship', 'Gamers In Real Life (GIRL) Game Design Competition Scholarship Program', 'SWE Scholarships',
	'Women in Technology Scholarship (WITS) Program', 'Carnegie Mellon Executive Women\'s Forum INI Fellowship', 'CWIT Scholars',
	'Michigan Council of Women in Technology Scholarships', 'NCWIT Award for Aspirations in Computing') ]
preCollege = ['Aspirations in Computing', 'AspireIT', 'Girls Who Code', 'National Girls Collaborative Program', 'Girls RiseNET']

def resourcesForMiddleSchool():
	codingTutorials[0:1] + codingTutorials[3:4] + codingTutorials[6:7]
	preCollege

def resourcesForHighSchool():
	codingTutorials[0:1] + codingTutorials[3:4] + codingTutorials[6:7]
	scholarships[8:10]

def resourcesForCollege():
	scholarships[0:7] + scholarships[9:10]
	conferences


