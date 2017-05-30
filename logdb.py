import psycopg2

DBNAME = "news"


# function to get the 3 most popular articles of all time
def articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # query to create a view
    c.execute("""create or replace view ui as select path, COUNT(*)
              as cnt from(select substring(path,10) as path from log
              where path like '/article/%') as table1 GROUP
              BY path ORDER BY COUNT(*) desc limit 3""")
    # query to select final result
    c.execute("""select title, cnt from ui join articles
              on articles.slug = ui.path""")
    # fetching of data
    a = c.fetchall()
    db.close()
    return a


# function to get the most popular authors of all time
def authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # view number 1 is created here
    c.execute("""create or replace view ss as select substring(path,10)
              as path from log where path like '/article/%'""")
    # view number 2 is created here
    c.execute("""create or replace view rr as select
              articles.author, count(*) from
              articles join ss on articles.slug = ss.path group by
              articles.author order by count(*) desc""")
    # view number 3 is created here
    c.execute("""create or replace view tt as select authors.name,
              authors.id from
              authors join articles on articles.author = authors.id
              group by authors.id""")
    # query to select final result
    c.execute("select name, count from tt,rr where tt.id = rr.author")
    # fetching of data
    a = c.fetchall()
    db.close
    return a


# function to get the day with error % more than 1%
def errors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # view number 1 is created here
    c.execute("""create or replace view gg as select
              time::timestamp::date as date,
              count(*) from log group by date order by count(*) desc""")
    # view number 2 is created here
    c.execute("""create or replace view ff as
              select time::timestamp::date as date,
              count(*) from log where status
              like '40%' group by date order by count(*) desc""")
    # query to select final result
    c.execute("""select gg.date,round((ff.count*100.0)/(gg.count), 2)
              as percentage
              from gg join ff on gg.date = ff.date
              where round((ff.count*100.0)/(gg.count),2)>1.00""")
    # fetching of data
    a = c.fetchall()
    db.close
    return a
