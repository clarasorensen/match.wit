-- Mentee Survey Result Table
--created by : Hye Sun and Karina

use whack17;

drop table if exists mentee_survey;

create table mentee_survey (

	email varchar(100),
	name varchar(50),
	communication varchar(5),
	age enum('10-15', '16-20', '21-25', '26-30', '30+'),
	location char(5),
	gender enum('female', 'male', 'nonbinary', 'prefer not to say'),
	spokenLang varchar(10),
	relationshipGoals enum('casual', 'formal'),
	mentorType varchar(3),

	occupationMentee enum('middle school student', 'high school student', 'undergraduate', 'graduate', 'working professional', 'other'),
	interests varchar(8),

	INDEX(email),
	FOREIGN KEY(email) REFERENCES accounts (email)
) ENGINE = INNODB;