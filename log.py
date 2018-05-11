import psycopg2

DBNAME = "news"

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect(database=DBNAME)

def popular_articles():
    """Get three most popular articles of all time."""
    query = "select title, num_views from popular_articles limit 3"
    return execute_query(query)

def popular_authors():
    """Get most popular article authors of all time."""
    query = "select * from popular_authors"
    return execute_query(query)

def days_with_errors():
    """Get the days with more than 1% of requests being errors"""
    query = "select * from error_day_stats where percent_error > 1.0 order by percent_error desc"
    return execute_query(query)

def execute_query(query):
    """Execute DB query and return the result."""
    db = connect()
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.commit()
    db.close()
    return result
    
def print_result(result):  
    """Output query result to text file"""
    #TODO print out result to txt file
    print result

if __name__ == '__main__':
    print_result(popular_articles())
    print_result(popular_authors())
    print_result(days_with_errors())

