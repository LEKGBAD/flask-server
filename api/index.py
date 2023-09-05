from flask import Flask,jsonify,render_template
from flask_cors import CORS

app=Flask(__name__)
CORS(app);
@app.route("/",methods=["GET"])
def home():
    return render_template('index.html')
    # return jsonify({"message":"obe eja"})
@app.route("/ext",methods=['GET'])
def ext():
    return render_template('index.html')


# if __name__ == '__main__':
#     app.run(debug=True,port="8080")
