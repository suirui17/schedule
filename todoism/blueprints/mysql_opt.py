import json
import pymysql
from flask_login import current_user
from sqlalchemy import event


def connect():
    return pymysql.connect(host='localhost', user='root', password='suirui1732',
                           db='schedule', charset='utf8')


def initial_items():
    sql = "select * from item where author_id=%s"
    params = '%s' % current_user.id
    return sql_template(2, sql, params)


def insert(item):
    sql = "insert into item(id, author_id, title, sdate, stime, edate, etime) values (%s, %s, %s, %s, %s, %s, %s)"
    params = (item['id'], current_user.id, item['title'], item['sdate'], item['stime'], item['edate'], item['etime'])
    return json.dumps({'rows': sql_template(1, sql, params)})


def insert_simple(item):
    sql = "insert into item(id, author_id, title, sdate) values (%s, %s, %s, %s)"
    params = (item['id'], current_user.id, item['title'], item['sdate'])
    return json.dumps({'rows': sql_template(1, sql, params)})


def delete(item):
    sql = "delete from schedule.item where id=%s"
    params = '%s' % item['id']
    return json.dumps({'rows': sql_template(1, sql, params)})


def search(item):
    sql = "select * from schedule.item where title like %s and author_id=%s"
    params = ('%%%s%%' % item['content'], item['author_id'])
    return sql_template(2, sql, params)


def show(item):
    sql = "select * from schedule.item where author_id=%s"
    params = '%s' % item['author_id']
    return json.dump({'row', sql_template(2, sql, params)})


def sql_template(type, sql, params=None):
    connection = connect()
    try:
        if type == 1:
            with connection.cursor() as cursor:
                rows = cursor.execute(sql, params)
                connection.commit()
                return rows
        else:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql, params)
                if type == 2:
                    return cursor.fetchall()
                elif type == 3:
                    return cursor.fetchone()
    finally:
        connection.close()


