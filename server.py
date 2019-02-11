import flask
import md5
app = flask.Flask(__name__)



@app.route('/')
def hello_world():
   return "<h1>Welcome to the api for decrypting md5 hashes</h1><br><h2>/md5?hash=putmd5here</h2><br>Made with ❤<br/> By Sarthak Saini"

@app.route('/md5', methods=['GET'])
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
   app.run(host="0.0.0.0",port=80)
