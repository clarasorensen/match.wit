-- match table

use whack17;

drop table if exists `match`;

create table `match` (
	mentee_email varchar(100),
	mentor_email varchar(100),
	INDEX(email),
	FOREIGN KEY (mentee_email) REFERENCES accounts (email)
	) 