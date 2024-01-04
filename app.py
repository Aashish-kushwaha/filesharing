from flask import Flask,request,render_template, jsonify, redirect, url_for
import os
from models import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
app=Flask(__name__)
ALLOWED_EXTENSIONS = {'pptx', 'docx', 'xlsx'}

app.config['UPLOAD_FOLDER']='uploads'


#========Login function==============================
@app.route('/login',methods=['GET','POST'])
def user_login():
    username=request.form.get('username')
    password=request.form.get('password')
    print(username)
    print(password)
    user=db.LoginUser.find_one(({'username':username, 'password':password}))
  
    if user:
        return redirect(url_for('upload_file'))
    else:
        return render_template('index.html')  


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_file')
def upload_file():
    return render_template('upload.html')

  

@app.route('/client-login',methods=['POST'])
def client_login():
    clientname=request.form.get('clientname')
    cpassword=request.form.get('password')
    
    # print(clientname)
    # print(cpassword)

    # print(db.LoginUser)

    user= db.Client.find_one({'clientname':clientname})
    # print(user)
    # print(user['cpassword'])
  
    if user and check_password_hash(user['cpassword'],cpassword):
        return jsonify({'message':'login successful'})
    else:
        return jsonify({'message':'login failed'}),401


@app.route('/client-register',methods=['POST'])
def client_register():
    email=request.form.get('email')
    password=request.form.get('password')
    clientname=request.form.get('clientname')
    collection_name = db.Client.name
    # print("email:",email)
    # print("password:",password)
    # print("clientname:",clientname)
    # print("collection:",collection_name)

    
    existing_user= db.Client.find_one({'clientemail':email})
    # print(existing_user)
 
    if existing_user:
        return jsonify({'message':'Email already registered'}),400
    else:
        hashpassword = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)        
        db.Client.insert_one({'clientemail':email,'cpassword':hashpassword,'clientname':clientname})
        return jsonify({'message':'User registered Successfully'}),201


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS






@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    # print(file.filename)

    if file and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))

        
    return str(file)


if __name__ == '__main__':
    app.run(debug=True)