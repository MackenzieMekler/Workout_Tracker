create database workouts;
use workouts;

create table gym_exercises (
  id int auto_increment primary key,
  exercise_date varchar(50),
  exercise_name varchar(100),
  num_sets int
);

create table gym_sets (
  id int auto_increment primary key,
  exercise_id int,
  set_num int,
  weight decimal,
  reps int,
  foreign key (exercise_id) references gym_exercises(id)
);

create table injuries (
  id int auto_increment primary key,
  exercise_type varchar(100),
  pain_index int,
  location varchar(100),
  injury_date varchar(50)
);
