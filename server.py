import flask
import md5
app = flask.Flask(__name__)



@app.route('/')
def hello_world():
   return "<h1>Welcome bitches to the world of suckers</h1><br><h2>/mdd?hash=for-md5-hash</h2>"

@app.route('/mdd', methods=['GET'])
def md():
    user = flask.request.args.get('hash')
    if user:
        a=md5.md(user.lower())
        return(a)
    else:
        return("Empty input !! Enter md5 hash after ?hash=")    
'''
@app.route('/sha', methods=['GET'])
def mda():
    user = flask.request.args.get('hash')
    a=md5.sha(user)
    return(a)
'''


if __name__ == '__main__':
   app.run()
