import web


urls = (
    '/', 'Index',
    '/login', 'Login'
)

render = web.template.render('templates')

class Index:
    def GET(self):

        return render.index()

    def POST(self):

        i = web.input()
        # with i's value, write into the database

class Login:
    def GET(self):

        return render.login()

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()