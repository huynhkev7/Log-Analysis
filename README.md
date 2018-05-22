# Project 3: Log Analysis
### By Kevin Huynh
This Python program is a reporting tool that prints out a neatly formatted summary of data for a newspaper site. Based on logs from the newspaper database, the report answers the following important questions:
- What are the most popular three articles of all time?
- what are the most popular three articles of all time?
- On which days did more than 1% of requests lead to errors?
This project is an assignment for the [Udacity Full Stack Web Developer Nanodegree course](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004). 
## Prequisites
In order to run project, the following steps will need to be done.
### Installing Python
Python 2.x is required to be installed. Link to download Python can be found [here](https://www.python.org/downloads/).
### Installing the Virtual Machine
VirtualBox is the software that actually runs the virtual machine. You can download it [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.
### Installing Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. You can download it [here](https://www.vagrantup.com/downloads.html). Install the version for your operating system.
### Download the News Data
Download the news data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql
### Download the VM configuration
Download the VM configuration by forking or cloning the Udacity [fullstack-nanodegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm)
Once above repository is downloaded, copy the contents of this repository and paste into
the ```fullstack-nanodegree-vm/vagrant``` directory. 
## How to Use
1. Make sure that both log.py and newsdata.sql are inside the ```fullstack-nanodegree-vm/vagrant``` directory.
2. Launch the terminal and ```cd``` into the ```fullstack-nanodegree-vm/vagrant``` directory.
3. Run the command ```vagrant up```. This will download the Linux operating system and install it.
4. When completed, run ```vagrant ssh``` to login into the VM.
5. Run the command ```psql -d news -f newsdata.sql```. Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
6. Run the command ```psql -d news``` to connect to the news database. 
7. In order for the reporting tool to work, you need to create the following views in the news database. Run the following commands under the **Create the Views Using PostgreSQL (PSQL)** section.
8. Run the reporting tool with the following command: ```python log.py```
9. Answers to the reporting questions should be printed to the console, as well as a text file called ```output.txt```
### Create the Views Using PostgreSQL (PSQL)
#### popular_articles view
View returning article title, author, and number of views
```
CREATE VIEW popular_articles AS
SELECT ar.title, ar.author, count(l.id) AS num_views
FROM articles ar, log l
WHERE concat('/article/',ar.slug) = l.path
GROUP BY ar.title, ar.author
ORDER BY num_views DESC;
```
### popular_authors view
View returning author names and number of views
```
CREATE VIEW popular_authors AS
SELECT au.name, SUM(pa.num_views) AS num_views
FROM popular_articles pa, authors au
WHERE pa.author = au.id
GROUP BY au.name
ORDER BY num_views DESC;
```
### error_day_stats view
View returning dates and percentage of errors
```
CREATE VIEW error_day_stats AS
SELECT time::timestamp::date days,
ROUND(100.0 * (SUM(CASE WHEN status !='200 OK' THEN 1 ELSE 0 END) /COUNT(status)::decimal),2) percent_error
FROM log l
GROUP BY days
ORDER BY percent_error DESC;
```
## Authors
Created by Kevin Huynh