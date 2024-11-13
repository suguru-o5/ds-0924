
Ramya Kappagantu
  14:37
create queries for films database:
```
create table films (
	id int4 primary key,
	title varchar(50),
	release_year int4,
	country varchar(50),
	duration int4,
	language varchar(50),
	certification varchar(5),
	gross int8,
	budget int8
);
create table people(
	id int4 primary key,
	name varchar(50),
	birthdate date,
	deathdate date
);
create table reviews (
	id int4 primary key,
	film_id int4 references films(id),
	num_user int4,
	num_critic int4,
	imdb_score float4,
	num_votes int4,
	facebook_likes int4
);
create table roles (
	id int4 primary key,
	film_id int4 references films(id),
	person_id int4 references people(id),
	role varchar(50)
);
```

Ramya Kappagantu
  14:50
```
insert into films(id, title, release_year, country, duration, language, certification, gross, budget)
values(1, 'Tarnation', 2015, 'Canada', 120, 'English', 'PG', 100, 50);

insert into films(id, title, release_year, country, duration, language, certification, gross, budget)
values(2, 'My Date with Drew', 2017, 'USA', 200, 'English', 'PG', 200, 120);

insert into films(id, title, release_year, country, duration, language, certification, gross, budget)
values(3, 'A Plague So Pleasant', 2015, 'Japan', 120, 'English', 'PG', 150, 50);

insert into films(id, title, release_year, country, duration, language, certification, gross, budget)
values(4, 'The Mongol King', 2020, 'Europe', 165, 'English', 'R', 120, 100);

insert into films(id, title, release_year, country, duration, language, certification, gross, budget)
values(5, '10 Things I hate about you', 2024, 'Canada', 180, 'English', 'M', 100, 50);

commit;
```

Ramya Kappagantu
  14:55
```
insert into people(id, name, birthdate, deathdate) values (1, 'Robert Brown', '1990-01-01', NULL);
insert into people(id, name, birthdate, deathdate) values (2, 'Anne Smith', '1990-02-02', NULL);
insert into people(id, name, birthdate, deathdate) values (3, 'Amy Miller', '1990-05-14', NULL);
insert into people(id, name, birthdate, deathdate) values (4, 'Adam Waters', '1991-11-22', NULL);
insert into people(id, name, birthdate, deathdate) values (5, 'Mark Adams', '1995-05-06', NULL);

commit;
```

Ramya Kappagantu
  15:08
```
insert into reviews(id, film_id, num_user, num_critic, 
imdb_score, num_votes, facebook_likes) 
values(1, 3, 5, 5, 8.1, 60, 600);
insert into reviews(id, film_id, num_user, num_critic, 
imdb_score, num_votes, facebook_likes) 
values(2, 2, 5, 5, 8.3, 100, 600);
insert into reviews(id, film_id, num_user, num_critic, 
imdb_score, num_votes, facebook_likes) 
values(3, 1, 5, 5, 9, 60, 50);
insert into reviews(id, film_id, num_user, num_critic, 
imdb_score, num_votes, facebook_likes) 
values(4, 5, 5, 5, 9.2, 50, 200);
insert into reviews(id, film_id, num_user, num_critic, 
imdb_score, num_votes, facebook_likes) 
values(5, 4, 5, 5, 7.4, 20, 1000);
commit;
```
15:12
```
insert into roles(id, film_id, person_id, role) values(1, 1, 1, 'Actor');
insert into roles(id, film_id, person_id, role) values(2, 2, 2, 'Actor');
insert into roles(id, film_id, person_id, role) values(3, 2, 2, 'Actor');
insert into roles(id, film_id, person_id, role) values(4, 3, 3, 'Actor');
insert into roles(id, film_id, person_id, role) values(5, 3, 3, 'Actor');
commit;
```

Ramya Kappagantu
  15:19
```
select * 
from films
where 
(country='Canada' and release_year>2014)
and
(country='Japan' and certification='PG');
```
15:21
```
select *
from
people
where deathdate is not NULL;
```
15:24
```
--Name of the actors who were born in the year 1990
select name
from
people
where birthdate >= '1990-01-01' and birthdate <= '1990-12-31';
```
15:27
```
--Names of the actors with 'i' in their name
select name
from
people
where name like '%i%';
```
15:30
```
--Names of the actors with 't' as the last but one character in their name
select name
from
people
where name like '%t_';
```

Ramya Kappagantu
  15:36
```
--Count the number of films according to number of votes
select 
count(film_id) as num_films_votes, num_votes
from reviews
group by num_votes;
```
15:38
```
select 
count(film_id) as num_films_votes, num_votes
from reviews
group by num_votes
order by num_votes desc;
```
15:39
```
select 
count(film_id) as num_films_votes, num_votes
from reviews
order by num_votes desc
group by num_votes;

ERROR:  syntax error at or near "group"
LINE 5: group by num_votes;
        ^ 

SQL state: 42601
Character: 91
```

15:44
```
--Use aliased field in order by
select 
count(film_id) as num_films_acted,
person_id
from roles
group by person_id
order by num_films_acted asc;
```
15:46
```
--Changing the order of 'having', 'group by'
select 
count(film_id) as num_films_acted,
person_id
from roles
having count(film_id) > 1
group by person_id
order by num_films_acted asc;

ERROR:  syntax error at or near "group"
LINE 6: group by person_id
        ^ 

SQL state: 42601
Character: 91
```
15:48
```
--Correct usage of 'having'
select 
count(film_id) as num_films_acted,
person_id
from roles
group by person_id
having count(film_id) > 1
order by num_films_acted asc;
```
15:53
```
--Error with count function
select 
count(distinct film_id, person_id)
from 
roles;

ERROR:  function count(integer, integer) does not exist
LINE 2: count(distinct film_id, person_id)
        ^
HINT:  No function matches the given name and argument types. You might need to add explicit type casts. 

SQL state: 42883
Character: 9
```

Ramya Kappagantu
  14:29
```
--aggregate functions
select
sum(budget) as sum_of_film_budgets,
min(budget) as min_budget,
max(budget) as max_budget,
round(avg(budget)) as avg_budget_rounded,
count(budget) as count_budget
from 
films;
```
14:30
```
--round the average budget to 3 places
select
sum(budget) as sum_of_film_budgets,
min(budget) as min_budget,
max(budget) as max_budget,
round(avg(budget), 3) as avg_budget_rounded,
count(budget) as count_budget
from 
films;
```
14:31
```
--round function converts the entire result to 0 if the decimal value is greater than the number of digits
select
sum(budget) as sum_of_film_budgets,
min(budget) as min_budget,
max(budget) as max_budget,
round(avg(budget), -3) as avg_budget_rounded,
count(budget) as count_budget
from 
films;
```
14:34
```
--aggregate functions and where clause
select
round(avg(duration),0) as avg_duration_canadian_films
from 
films
where country='Canada' 
and release_year>=2010;
```
14:36
```
select
round(avg(duration),0) as avg_duration_canadian_films,
count(id) as film_count
from 
films
where country='Canada' 
and release_year>=2010;
```
14:37
```
--error with aggregate function
select
round(avg(duration, budget),0) as avg_duration_budget_canadian_films,
count(id) as film_count
from 
films
where country='Canada' 
and release_year>=2010;

ERROR:  function avg(integer, bigint) does not exist
LINE 2: round(avg(duration, budget),0) as avg_duration_budget_canadi...
              ^
HINT:  No function matches the given name and argument types. You might need to add explicit type casts. 

SQL state: 42883
Character: 14
```
14:38
```
select
round(avg(duration),0) as avg_duration_canadian_films,
round(avg(budget)) as avg_budget_canadian_films,
count(id) as film_count
from 
films
where country='Canada' 
and release_year>=2010;
```
14:43
```
--apply sum() on varchar field
select
count(film_id) as total_films_by_actor,
count(id) as total_id,
count(person_id) as total_persons,
sum(role) as total_roles
from
roles
group by person_id;

ERROR:  function sum(character varying) does not exist
LINE 5: sum(role) as total_roles
        ^
HINT:  No function matches the given name and argument types. You might need to add explicit type casts. 

SQL state: 42883
Character: 106
```
14:44
```
select
count(film_id) as total_films_by_actor,
count(id) as total_id,
count(person_id) as total_persons,
count(role) as total_roles
from
roles
group by person_id;
```
14:46
```
--sorting based on aliased field
select
count(film_id) as total_films_by_actor,
count(id) as total_id,
count(person_id) as total_persons,
count(role) as total_roles
from
roles
group by person_id
order by total_id;
```
14:48
```
--using aliased field in where clause
select
count(film_id) as total_films_by_actor,
count(id) as total_id,
count(person_id) as total_persons,
count(role) as total_roles
from
roles
where total_films_by_actor=2;

ERROR:  column "total_films_by_actor" does not exist
LINE 8: where total_films_by_actor=2;
              ^ 

SQL state: 42703
Character: 150
```
14:51
```
--having with aggregate function
select
count(film_id) as total_films_by_actor,
count(id) as total_id,
count(person_id) as total_persons,
count(role) as total_roles
from
roles
having count(film_id)=2;
```
14:54
```
--arithmetic function
select
gross,
budget,
(gross-budget) as profit
from 
films;
```
14:55
```
--arithmetic function on varchar
select
(country - title)
from 
films;

ERROR:  operator does not exist: character varying - character varying
LINE 2: (country - title)
                 ^
HINT:  No operator matches the given name and argument types. You might need to add explicit type casts. 

SQL state: 42883
Character: 17
```
14:57
```
--arithmetic operation - division
select
(duration / budget)
from 
films;
```
14:58
```
--multiple arithmetic operations
select
(duration / budget),
(duration * budget)
from 
films;
```

Ramya Kappagantu
  15:08
```
--using 'where' after 'group by'
select
count(id) as total_id,
count(title) as all_titles,
max(release_year) as latest_release,
count(distinct country) as different_countries_released,
avg(duration) as average_duration,
count(distinct language) as different_languages_released,
certification
from 
films
group by certification
where release_year=2024
having avg(duration) > 150
order by latest_release
;

ERROR:  syntax error at or near "where"
LINE 12: where release_year=2024
         ^ 

SQL state: 42601
Character: 295
```
15:10
```
select
count(id) as total_id,
count(title) as all_titles,
max(release_year) as latest_release,
count(distinct country) as different_countries_released,
avg(duration) as average_duration,
count(distinct language) as different_languages_released,
certification
from 
films
where release_year=2024 and certification='R'
group by certification
having avg(duration) > 150
order by latest_release
limit 1
;
```

Ramya Kappagantu
  15:04
```
create table states(
country varchar(50),
indep_year int4
);

create table presidents(
country varchar(50),
continent varchar(50),
president varchar(50)
);

create table prime_ministers(
country varchar(50),
continent varchar(50),
prime_minister varchar(50)
);

create table monarchs(
country varchar(50),
continent varchar(50),
monarch varchar(50)
);

create table prime_minister_terms(
prime_minister varchar(50),
pm_start int4
);
```
15:06
```
--presidents table
insert into presidents(country, continent, president) values('Egypt', 'Africa', 'Abdel Fattah');
insert into presidents(country, continent, president) values('Portugal', 'Europe', 'Marcelo Rebelo');
insert into presidents(country, continent, president) values('USA', 'North America', 'Joe Biden');
insert into presidents(country, continent, president) values('Uruguay', 'South America', 'Luis Lacalle');
insert into presidents(country, continent, president) values('Pakistan', 'Asia', 'Arif Alvi');
insert into presidents(country, continent, president) values('Chile', 'South America', 'Gabriel Boric');
insert into presidents(country, continent, president) values('India', 'Asia', 'Ram Nath Kovind');
commit;
--prime_ministers table
insert into prime_ministers(country, continent, prime_minister) values('Egypt', 'Africa', 'Mustafa Madbouly');
insert into prime_ministers(country, continent, prime_minister) values('Portugal', 'Europe', 'Antonio Costa');
insert into prime_ministers(country, continent, prime_minister) values('Pakistan', 'Asia', 'Shehbaz Sharif');
insert into prime_ministers(country, continent, prime_minister) values('United Kingdom', 'Europe', 'Boris Johnson');
insert into prime_ministers(country, continent, prime_minister) values('India', 'Asia', 'Narendra Modi');
insert into prime_ministers(country, continent, prime_minister) values('Australia', 'Oceania', 'Scott Morrison');
insert into prime_ministers(country, continent, prime_minister) values('Norway', 'Europe', 'Jonas Gahr');
insert into prime_ministers(country, continent, prime_minister) values('Brunei', 'Asia', 'Hassanal Bolkiah');
insert into prime_ministers(country, continent, prime_minister) values('Oman', 'Asia', 'Haitham Bin');
insert into prime_ministers(country, continent, prime_minister) values('New Zealand', 'Oceania', 'Jacinda Ardern');
commit;
```


Ramya Kappagantu
  15:13
```
--prime_minister_terms table
insert into prime_minister_terms(prime_minister, pm_start) values('Mostafa Madbouly', 2018);
insert into prime_minister_terms(prime_minister, pm_start) values('Antonio Costa', 2015);
insert into prime_minister_terms(prime_minister, pm_start) values('Shehbaz Shariff', 2022);
insert into prime_minister_terms(prime_minister, pm_start) values('Baris Johnson', 2019);
insert into prime_minister_terms(prime_minister, pm_start) values('Narendra Modi', 2014);
insert into prime_minister_terms(prime_minister, pm_start) values('Scott Morrison', 2018);
insert into prime_minister_terms(prime_minister, pm_start) values('Jonas Gahr Store', 2021);
insert into prime_minister_terms(prime_minister, pm_start) values('Hassanal Bolkiah', 1984);
insert into prime_minister_terms(prime_minister, pm_start) values('Haitham bin Tarik', 2020);
insert into prime_minister_terms(prime_minister, pm_start) values('Jacinda Ardern', 2017);
commit;
```

Ramya Kappagantu
  15:22
```
--typo error
select prime_minister.country, presidents.continent, prime_minister, president
from
prime_ministers
inner join
presidents
on prime_ministers.country = presidents.country
and prime_ministers.continent = presidents.continent;

ERROR:  missing FROM-clause entry for table "prime_minister"
LINE 1: select prime_minister.country, presidents.continent, prime_m...
               ^ 

SQL state: 42P01
Character: 8
```
15:23
```
--ambiguity error
select country, presidents.continent, prime_minister, president
from
prime_ministers
inner join
presidents
on prime_ministers.country = presidents.country
and prime_ministers.continent = presidents.continent;

ERROR:  column reference "country" is ambiguous
LINE 1: select country, presidents.continent, prime_minister, presid...
               ^ 

SQL state: 42702
Character: 8
```
15:27
```
--filtering the join result set
select prime_ministers.country, presidents.continent, prime_minister, president
from
prime_ministers
inner join
presidents
on prime_ministers.country = presidents.country
and prime_ministers.continent = presidents.continent
and prime_ministers.country in ('India', 'Egypt')
and prime_ministers.continent like 'a%';
Wildcard matching is case-sensitive
```
15:31
```
--order of execution and errors while executing the query
select t1.country, presidents.continent, prime_minister, president
from
prime_ministers as t1
inner join
presidents as t2
on t1.country = presidents.country
and t1.continent = presidents.continent
and t1.country in ('India', 'Egypt')
and prime_ministers.continent like 'A%';

ERROR:  invalid reference to FROM-clause entry for table "presidents"
LINE 6: on t1.country = presidents.country
                        ^
HINT:  Perhaps you meant to reference the table alias "t2". 

SQL state: 42P01
Character: 139
```

Ramya Kappagantu
  15:38
```
--inner join is the default join
select t1.country, t2.continent, prime_minister as pm, president as pr
from
prime_ministers as t1
join
presidents as t2
on t1.country = t2.country
and t1.continent = t2.continent
and t1.country in ('India', 'Egypt')
and t1.continent like 'A%';
```
15:39
```
--filtering after joining tables
--'where' can be used for filtering or can be combined with join using 'and' keyword
select t1.country, t2.continent, prime_minister as pm, president as pr
from
prime_ministers as t1
join
presidents as t2
on t1.country = t2.country
and t1.continent = t2.continent
where t1.country in ('India', 'Egypt')
and t1.continent like 'A%';
```

Ramya Kappagantu
  15:49
```
--error due to the order of execution
--'on' gets executed before 'select'
select t1.country, t2.continent, t1.prime_minister as pm, president as pr
from
prime_ministers as t1
join
presidents as t2
on t1.country = t2.country
and t1.continent = t2.continent
join 
prime_minister_terms t3
on t1.pm = t3.prime_minister;

ERROR:  column t1.pm does not exist
LINE 10: on t1.pm = t3.prime_minister;
            ^ 

SQL state: 42703
Character: 216
```

Ramya Kappagantu
  16:05
```
--left join
select t1.country, t1.continent, t1.prime_minister, president, pm_start
from
prime_ministers t1
left join
presidents t2
on t1.country = t2.country
and t1.continent = t2.continent
left join
prime_minister_terms t3
on t1.prime_minister = t3.prime_minister;
```
16:07
```
--using left and right join together
select t1.country, t1.continent, t1.prime_minister, president, pm_start
from
prime_ministers t1
left join
presidents t2
on t1.country = t2.country
and t1.continent = t2.continent
right join
prime_minister_terms t3
on t1.prime_minister = t3.prime_minister;
```
16:08
```
--right join
select t1.country, t1.continent, t1.prime_minister, president, pm_start
from
prime_ministers t1
right join
presidents t2
on t1.country = t2.country
and t1.continent = t2.continent
right join
prime_minister_terms t3
on t1.prime_minister = t3.prime_minister;
```
16:13
```
--changing the table combinations for join
select t2.country, t2.continent, t2.prime_minister, president, pm_start
from
prime_minister_terms t1
right join
prime_ministers t2
on t1.prime_minister = t2.prime_minister
right join
presidents t3
on t2.country = t3.country;
```

Ramya Kappagantu
  16:22
```
--aggregate functions, having, group by with join
select count(t2.country) country_count, count(t2.continent) continent_count, 
count(t2.prime_minister) pm_count, count(president) pr_count, pm_start
from
prime_minister_terms t1
right join
prime_ministers t2
on t1.prime_minister = t2.prime_minister
right join
presidents t3
on t2.country = t3.country
group by pm_start
having count(t2.country) = 1;
```

16:25
```
--aggregate functions with group by
select t2.country country_count, t2.continent continent_count, 
count(t2.prime_minister) pm_count, count(president) pr_count, pm_start
from
prime_minister_terms t1
right join
prime_ministers t2
on t1.prime_minister = t2.prime_minister
right join
presidents t3
on t2.country = t3.country
group by pm_start, t2.country, t2.continent
having count(t2.country) = 1;
```

16:27
```
--self join
select * 
from prime_ministers as t1
inner join
prime_ministers as t2
on t1.country = t2.country;
16:28
--error with join
select * 
from prime_ministers as t1
inner join
prime_ministers as t2;

ERROR:  syntax error at or near ";"
LINE 4: prime_ministers as t2;
                             ^ 

SQL state: 42601
Character: 70
```

Ramya Kappagantu
  16:34
```
--error with cross join
select * 
from prime_ministers as t1
cross join
presidents as t2
on t1.country = t2.country;

ERROR:  syntax error at or near "on"
LINE 5: on t1.country = t2.country;
        ^ 

SQL state: 42601
Character: 66
```
16:35
```
--cross join
select * 
from prime_ministers as t1
cross join
presidents as t2;
```