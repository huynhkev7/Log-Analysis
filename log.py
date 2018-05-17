#!/usr/bin/env python2

import psycopg2

DBNAME = "news"

def connect():
    """Attempt to connect to the database and return database connection"""
    try:
        return psycopg2.connect(database=DBNAME)
    except:
        print("Error connecting to database")

def popular_articles():
    """Get three most popular articles of all time"""
    query = "select title, num_views from popular_articles limit 3"
    return execute_query(query)

def popular_authors():
    """Get most popular article authors of all time"""
    query = "select * from popular_authors"
    return execute_query(query)

def days_with_errors():
    """Get the days with more than 1% of requests being errors"""
    query = "select * from error_day_stats where percent_error > 1.0 order by percent_error desc"
    return execute_query(query)

def execute_query(query):
    """Execute DB query and return the result"""
    db = connect()
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result
    
def print_result(result, title, suffix, mode):  
    """Output query result to a text file and print to console"""
    file = open("output.txt", mode)
    output_title = "*** " + title + " ***"
    print(output_title)
    file.write(output_title + "\n")
    for column_1,column_2 in result:
        output_stats = "\t" + str(column_1) + " ----- " + str(column_2) + " " + suffix
        print(output_stats)
        file.write(output_stats + "\n")
    file.close()

if __name__ == '__main__':
    question_1 = "What are the most popular three articles of all time?"
    question_2 = "Who are the most popular article authors of all time?"
    question_3 = "On which days did more than 1% of requests lead to errors?"
    popular_articles_result = popular_articles()
    popular_authors_result = popular_authors()
    days_with_errors_result = days_with_errors()
    print_result(popular_articles_result, question_1, "views", "w")
    print_result(popular_authors_result, question_2, "views", "a")
    print_result(days_with_errors_result, question_3, "%", "a")