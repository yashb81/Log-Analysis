#!/usr/bin/env python

import psycopg2
from flask import Flask, url_for, redirect
from logdb import articles, authors, errors


app = Flask(__name__)

html = '''\
<!DOCTYPE html>
<html>
<head>
<title>LOG ANALYSIS</title>
</head>


<h1>Log Analysis</h1>
<table>
<tr>
<td colspan='2'>
    <h3>Click on button on the right for
    getting three most popular articles</h3>
</td>
<td>
&nbsp;
</td>
<td>
<form action="/popular_articles">
<button type="submit">Click Me!!</button></form>
<form action="/popular_authors">
</td></tr>
<tr>
<td colspan='2'>
<h3>
    Click on button on the right to get most popular authors of all time
    </h3>
    </td>
<td>
&nbsp;
</td>

<td>
<button type="submit">Click ME!!</button></form>
</td></tr>
<tr>
<td colspan='2'>
<h3>Click on button on the right to get the errors</td>
<td>
&nbsp;
</td>

<td>
<form action="/request_errors">
<button type="submit">Click Me!!</button></form>
</td></tr>
</table>
<br>
<br>
<b><center>%s</center></b>
<br>
<b><center>%s</center></b>
</body>
</html>
'''


# It formats the input list in desired format


def formator(lst):
    some_list = "<table border=1>"
    some_list += "\n".join([
        "<tr> <td>&nbsp;&nbsp;{p1}&nbsp;&nbsp;"
        "</td> <td>&nbsp;&nbsp;{p2}&nbsp;&nbsp;</td>"
        "<tr>".format(p1=t1, p2=t2) for t1, t2 in lst])
    some_list += "</table>"
    return some_list


def formator2(lst):
    some_list = "<table border=1>"
    some_list += "\n".join([
        "<tr> <td>&nbsp;&nbsp;{p1}&nbsp;&nbsp;"
        "</td> <td>&nbsp;&nbsp;{p2}%&nbsp;&nbsp;</td>"
        "<tr>".format(p1=t1, p2=round(t2, 2)) for t1, t2 in lst])
    some_list += "</table>"
    return some_list


@app.route('/', methods=['GET'])
def Default():
    Main_html = html % (" ", " ")
    return Main_html


@app.route('/popular_articles', methods=['GET'])
def article():
    article = articles()
    out = formator(article)
    Main_html = html % ("The 3 most popular articles of all time are :", out)
    return Main_html


@app.route('/popular_authors', methods=['GET'])
def author():
    author = authors()
    out = formator(author)
    Main_html = html % ("The most popular article "
                        "authors of all time are :", out)
    return Main_html


@app.route('/request_errors', methods=['GET'])
def error():
    error = errors()
    out = formator2(error)
    Main_html = html % ("Days with more than 1% "
                        "of request that lead to an error :", out)
    return Main_html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
