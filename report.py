#! /usr/bin/env python
import psycopg2


def articles():
    articles_query = '''
        SELECT title, COUNT(*) AS num
        FROM articles, log
        WHERE articles.slug = SUBSTR(log.path, 10)
        GROUP BY title
        ORDER BY num DESC LIMIT 3;
    '''
    results = get_query(articles_query)
    print('\nWhat are the most popular three articles of all time?\n')
    for i in results:
        print ('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')


def authors():
    authors_query = '''
        SELECT name, COUNT(*) AS num
        FROM authors, articles, log
        WHERE articles.slug = SUBSTR(log.path,10)
        AND articles.author = authors.id
        GROUP BY name
        ORDER BY num DESC;
    '''
    results = get_query(authors_query)
    print('\nWho are the most popular article authors of all time?\n')
    for i in results:
        print ('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')


def errors():
    errors_query = '''
        SELECT to_char(totalLogs.day,\'Mon DD, YYYY\'),
        ROUND(totalErrors.stats * 100.0 / totalLogs.stats, 2) AS error
        FROM (
            SELECT DATE(time) AS day, COUNT(id) AS stats
            FROM log
            GROUP BY day
        ) AS totalLogs
        INNER JOIN (
            SELECT DATE(time) AS day, COUNT(id) AS stats
            FROM log
            WHERE status != '200 OK'
            GROUP BY day
        ) AS totalErrors ON totalLogs.day = totalErrors.day
        WHERE ROUND(totalErrors.stats * 100.0 / totalLogs.stats, 2) > 1.00
        ORDER BY error DESC;
    '''
    results = get_query(errors_query)
    print('\nOn which days did more than 1% of requests lead to errors?\n')
    for i in results:
        print ('\t' + str(i[0]) + ' - ' + str(i[1]) + ' errors')


def get_query(query):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    return c.fetchall()


# Run each function and print results
articles()
authors()
errors()
