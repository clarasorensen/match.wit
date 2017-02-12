-- Mentor Survey results table

drop table if exists mentor_survey;

create table mentor_survey (
	email varchar(100),
	name varchar(50),
	communcation varchar(5),
	age enum('10-15', '16-20', '21-25','26-30', '30+'),
	location char(5),
	gender enum('female', 'male', 'nonbinary', 'prefer not to say'),
	spokenLang varchar(10),
	relationshipHopes enum('casual', 'formal'),
	occupationMentor enum('undergraduate', 'graduate student', 'PhD student', 'working professional', 'self-employed', 'retired', 'other'),
	codingLang text(200),
	resume varchar(100),
	mentorBio text(10,000),
	INDEX(email),
	FOREIGN KEY (email) REFERENCES accounts (email),
	FOREIGN KEY (email) REFERENCES `match` (email)
) ENGINE = INNODB;