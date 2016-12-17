import web
import model
import os
import re

urls = (
    '/', 'Index',
    '/login', 'Login',
    '/logout', 'Logout',
    '/record', 'Record',
    '/myrecord', 'Myrecord',
    '/spiderdemo', 'Spiderdemo',
    '/(\d+).html', 'Static'
)

render = web.template.render(os.path.join(os.path.dirname(__file__), 'templates/'))

mobile_pattern = re.compile('android', re.IGNORECASE)

class Index:
    def GET(self): 
        return render.index()

class Login:
    def GET(self):
        # Already Login, -> Record Page.
        uid = web.cookies().get('uid')
        if uid:
            raise web.seeother('/record')
        else:
            return render.login()
    def POST(self):
        i= web.input()
        user = model.User().login(i.username, i.password)
        if user:
            # Login Success -> Record Page.
            web.setcookie('uid', str(user), 3600)
            raise web.seeother('/record')
        else:
            return render.login_fail()

class Logout:
    def GET(self):
        uid = web.cookies().get('uid')
        if uid:
            web.setcookie('uid', '', -1)
        return render.index()

class Record:
    def GET(self):
        user = web.cookies().get('uid')
        if user:
            uname = model.User().id2name(int(user))
            return render.record(uname)
        else:
            web.seeother('/')

    def POST(self):
        user = web.cookies().get('uid')
        if user:
            uname = model.User().id2name(int(user))
            i = web.input()
            try:
                model.Record().add(uname, i.rundate, i.runtime, i.length, i.feeling)
            except Exception, e:
                # Todo:
                # Show the Feedback
                pass
            else:
                web.seeother('/myrecord')
        else:
            #should not be pointed to this page.
            pass

class Myrecord:
    def GET(self):
        user = web.cookies().get('uid')
        if user:
            uname = model.User().id2name(int(user))
            records = model.Record().find(uname)
            return render.myrecord(uname, records)
        else:
            return render.index()

class Spiderdemo:
    def GET(self):
        return web.template.render(os.path.join(os.path.dirname(__file__), 'templates/kmlover')).index()

class Static:
    def GET(self, name):
        with open(os.path.join(os.path.dirname(__file__), 'templates/kmlover/kmlover_answers/' + name + '.html'), 'r') as f:
            html = f.read()
            return render.empty(html)


class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

if __name__ == "__main__":
    app = MyApplication(urls, globals())
    app.run(port=9888)


