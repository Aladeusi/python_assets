from flask import Flask,request,Response
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def responsify(status,message,data={}):
    code = int(status)
    a_dict = {"data":data,"message":message,"code":code}
    try:
        return Response(json.dumps(a_dict), status=code, mimetype='application/json')
    except:
        return Response(str(a_dict), status=code, mimetype='application/json')


@app.route("/urlauth")
def test_auth():
    if "Authorization" in request.headers:
        auth = request.headers["Authorization"]
        return responsify(200,"auth attached",auth)
    else:
        return responsify(401,"No Auth")

      
@app.route("/get")
def test():
    return "hello world!"


@app.route("/hello/<path:input>")
def test2(input):
    return "Hello %s!" % input


@app.route("/urlquery")
def test_query():
    return responsify(200,"query params",dict(request.args))



@app.route("/post_test_json",methods=["POST"])
def test_json():
    formdata = request.get_json(force=True)
    return responsify(200,"body attached",formdata)

@app.route("/post_test_form",methods=["POST"])
def test_form():
    formdata = request.form
    return responsify(200,"body attached",formdata)



if __name__ == "__main__": 
    app.run()