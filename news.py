
# !/usr/bin/env python2.7
import psycopg2

conn = psycopg2.connect("dbname=news")

print("1. What are the most popular three articles of all time?")
cursor = conn.cursor()
cursor.execute("""
 SELECT
    a.title
    ,count(a.slug) as views
  FROM
    log as l
  JOIN
    articles as a ON l.path = CONCAT('/article/',a.slug)
  GROUP BY a.title
  ORDER BY
    views DESC
  LIMIT 3;
    """)
results = cursor.fetchall()
for result in results:
    print(str(result[0]) + ' - ' + str(result[1]) + ' views')

print("")
print("2. Who are the most popular article authors of all time?")
cursor = conn.cursor()
cursor.execute("""
  SELECT
    aut.name
    ,count(art.slug) as views
  FROM
    log as l
  JOIN
    articles as art ON l.path = CONCAT('/article/',art.slug)
  LEFT JOIN
    authors as aut ON aut.id = art.author
  GROUP BY
    aut.name
  ORDER BY
    views DESC;
    """)
results = cursor.fetchall()
for result in results:
    print(str(result[0]) + ' - ' + str(result[1]) + ' views')

print("")
print("3. On which days did more than 1% of requests lead to errors?")
cursor = conn.cursor()
cursor.execute("""
  SELECT
    -- Format the date: (example: Jul 17 2016)
    to_char(time::date, 'Mon DD YYYY') as date
   -- Calculate the percents of the errors per day
    ,CAST
     (
        CAST
        (
         sum(case when l.status = '404 NOT FOUND' then 1 else 0 end)
         AS FLOAT(2)
        )
        / CAST
        (
         sum(case when l.status = '200 OK' then 1 else 0 end)
         AS FLOAT(2)
        )
        * 100
        AS DECIMAL(4,2)
     )
     AS errors_percent
  FROM
    log as l
  GROUP BY
    time::date
  HAVING
    -- Calculate again the percents of the errors per day,
    -- show only the one which are bigger than 1%
    CAST
     (
        CAST
        (
         sum(case when l.status = '404 NOT FOUND' then 1 else 0 end)
         AS FLOAT(2)
        )
        / CAST
        (
         sum(case when l.status = '200 OK' then 1 else 0 end)
         AS FLOAT(2)
        )
        * 100
        AS DECIMAL(4,2)
     ) > 1
  ORDER BY
    errors_percent DESC
    """)
results = cursor.fetchall()

for result in results:
    print(str(result[0]) + ' - ' + str(result[1]) + '%')

conn.close()
