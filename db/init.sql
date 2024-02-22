create database workoutTypes;
use workoutTypes;

create table gym (
    id INT unsigned NOT NULL AUTO_INCREMENT,
    name varchar(30),
    body varchar(20),
    type varchar(15)
    primary key (id)
)

create database workoutHistory;
use workoutHistory;

create table volleyball_games (
    id INT unsigned NOT NULL AUTO_INCREMENT,
    partners TEXT,
    hours ,
    matches varchar(3),
    injury TEXT,
    primary key (id)
)
