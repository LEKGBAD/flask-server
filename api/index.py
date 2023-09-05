from flask import Flask,jsonify,render_template
from flask_cors import CORS

app=Flask(__name__)
CORS(app);

@app.route("/",methods=["GET"])
def home():
    return render_template('index.html')
    
@app.route('/hello',methods=['GET', 'POST', 'PUT'])
def hello():
    # return render_template('index.html')
    pass


# if __name__ == '__main__':
#     app.run(debug=True,port="8080")
