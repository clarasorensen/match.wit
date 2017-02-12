-- Accounts table 

use whack17;

drop table if exists mentor_survey;
drop table if exists mentee_survey;
drop table if exists `match`;
drop table if exists accounts;

create table accounts (
	email varchar(100),
	password varchar(100),
	type enum('mentor','mentee', 'admin'),
	INDEX(email)
) ENGINE = INNODB;