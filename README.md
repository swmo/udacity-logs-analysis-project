# Udacity Project - Logs Analysis Project

a udacity project, submitted for review

## Getting started
Make sure you have Python and PostgreSQL installed.
Script tested with Python 2.7 and PostgreSQL 9.5.14

### Prerequisites
* Install python
* Install Postgres
* make sure psycopg is installed
``` pip install psycopg2 ```

### Installing
* create a database with the name news
* make sure you restored the data into the news database: [newsdata.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2016/August/57b5f748_newsdata/newsdata.zip) (udacity sql dump)
'''psql -d news -f newsdata.sql'''

### Run
Now you can simple run the script:
```  python news.py ```

you can also have a look at output.txt, it's an example of the program's output:



