from flask import Flask

app = Flask(__name__)

@app.route('/hello/') #/hello - will work only with  /hello and /hello/ will work for both
def helloworld():return 'Hello World'

if __name__ == '__main__':app.run(debug=True)

#app.route(rule,options) instead of @app.route('/') rule - path , options - arguments