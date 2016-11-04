import settings
import web

db = web.database(dbn='mysql', db='forpy', user=settings.USERNAME, pw=settings.PASSWORD)

class User:
    def all_users(self):
        users = db.select('user', where='1=1')
        return users

    def current_user(self):
        uid = 0
        try:
            uid = web.cookies().get('uid')
        except Exception, e:
            pass
        finally:
            return uid

    def id2name(self, id):
        username = db.select('user', what='username', where='id=$id', vars=locals())
        if username:
            return username[0].username
        else:
            return 0

    def login(self, username, password):
        users = db.select('user', what='id', where='username=$username AND password=$password', vars=locals())
        if users:
            return users[0].id
        else:
            return 0


class Record:
    def add(self, username, rundate, runtime, length, feeling):
        return db.insert('records', username=username, rundate=rundate, runtime=runtime, length=length, feeling=feeling)

    def find(self, uname):
        records = db.select('records', where='username=$uname', order="dt DESC", vars=locals())
        return records