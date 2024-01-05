from flask import Flask,request,render_template, jsonify, redirect, url_for,send_file
import os
from models import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from bson import ObjectId
app=Flask(__name__)
ALLOWED_EXTENSIONS = {'pptx', 'docx', 'xlsx'}

app.config['UPLOAD_FOLDER']='uploads'




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_file')
def upload_file():
    return render_template('upload.html')

@app.route('/download')
def download():
    rows = list(db.Fileupload.find())
    print("sdfghjkk")
    return render_template('download.html',rows=rows)

#   user login function
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
    

#   client login function
@app.route('/client-login',methods=['POST'])
def client_login():
    clientname=request.form.get('clientname')
    cpassword=request.form.get('password')
    
    print(clientname)
    print(cpassword)

    print(db.LoginUser)

    user= db.Client.find_one({'clientname':clientname})
    print(user)
    print(user['cpassword'])
  
    if user and check_password_hash(user['cpassword'],cpassword):
        print("aa gya")
        return redirect(url_for('download'))
    else:
        return render_template('index.html')  


#     Client register function
@app.route('/client-register',methods=['POST'])
def client_register():
    email=request.form.get('email')
    password=request.form.get('password')
    clientname=request.form.get('clientname')
    collection_name = db.Client.name
    existing_user= db.Client.find_one({'clientemail':email})
    if not email or not password or not clientname:
        return jsonify({'message':'all fields are required'})
    if existing_user:
        return jsonify({'message':'Email already registered'}),400
    else:
        hashpassword = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)        
        db.Client.insert_one({'clientemail':email,'cpassword':hashpassword,'clientname':clientname})
        return jsonify({'message':'User registered Successfully'}),201


 
 #     download function
@app.route('/download_file/<_id>',methods=['GET', 'POST'])
def download_file(_id):
     obj_id=ObjectId(_id)
     print("id recieved:",_id)
     print(type(obj_id))
     file_info = db.Fileupload.find_one({'_id':obj_id})
     print("file_info:", file_info)
     if file_info:
        return send_file(file_info['furl'], as_attachment=True)
     else:
        return 'File not found'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#    upload function 
     
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    print(file)

    if file and allowed_file(file.filename):
       file_path= os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
       file.save(file_path)
       print(file_path)
       db.Fileupload.insert_one({'filename':file.filename,'furl':file_path})
         
    return jsonify({'message':'File uploaded successfully'}),201


if __name__ == '__main__':
    app.run(debug=True)