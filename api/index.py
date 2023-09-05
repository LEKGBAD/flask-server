from flask import Flask,jsonify,render_template
from flask_cors import CORS

app=Flask(__name__)
CORS(app);
@app.route("/",methods=["GET"])
def home():
    return render_template('index.html')
    # return jsonify({"message":"obe eja"})
@app.route("/extapi/home",methods=['GET'])
def homeApi():
    return render_template('ext.html')


# if __name__ == '__main__':
#     app.run(debug=True,port="8080")
