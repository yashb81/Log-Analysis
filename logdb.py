import psycopg2

DBNAME = "news"


def articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""create or replace view ui as select path, COUNT(*)
              as cnt from(select substring(path,10) as path from log
              where path like '/article/%') as table1 GROUP
              BY path ORDER BY COUNT(*) desc limit 3""")
    c.execute("""select title, cnt from ui join articles
              on articles.slug = ui.path""")
    a = c.fetchall()
    db.close()
    return a


def authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""create or replace view ss as select substring(path,10)
              as path from log where path like '/article/%'""")
    c.execute("""create or replace view rr as select
              articles.author, count(*) from
              articles join ss on articles.slug = ss.path group by
              articles.author order by count(*) desc""")
    c.execute("""create or replace view tt as select authors.name,
              authors.id from
              authors join articles on articles.author = authors.id
              group by authors.id""")
    c.execute("select name, count from tt,rr where tt.id = rr.author")
    a = c.fetchall()
    db.close
    return a


def errors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""create or replace view gg as select
              time::timestamp::date as date,
              count(*) from log group by date order by count(*) desc""")
    c.execute("""create or replace view ff as
              select time::timestamp::date as date,
              count(*) from log where status
              like '40%' group by date order by count(*) desc""")
    c.execute("""select gg.date,round((ff.count*100.0)/(gg.count), 2)
              as percentage
              from gg join ff on gg.date = ff.date
              where round((ff.count*100.0)/(gg.count),2)>1.00""")
    a = c.fetchall()
    db.close
    return a
