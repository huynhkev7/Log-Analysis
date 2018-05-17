# Project 3: Log Analysis
### By Kevin Huynh
A python program that prints out a report for a news database [Udacity Full Stack Web Developer Nanodegree course](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004). 

## Prequisites
In order to run project, Python 2.x is required to be installed. Link to download Python can be found [here](https://www.python.org/downloads/).

## How to Create Views
### popular_articles view
```
create or replace view popular_articles as
select ar.title, ar.author, count(l.id) num_views
from articles ar, log l
where concat('/article/',ar.slug) = l.path
group by ar.title, ar.author
order by num_views desc;
```
### popular_authors view
```
create or replace view popular_authors as
select au.name, sum(pa.num_views) num_views
from popular_articles pa, authors au
where pa.author = au.id
group by au.name
order by num_views desc;
```
### error_day_stats view
```
create or replace view error_day_stats as
select time::timestamp::date days, round(100.0 * (sum(case when status !='200 OK' then 1 else 0 end) /count(status)::decimal),2) percent_error
from log l
group by days
order by percent_error desc;
```
## How to Run Project

## Authors
-Created by Kevin Huynh