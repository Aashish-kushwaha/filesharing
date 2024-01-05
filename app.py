from flask import Flask,request,render_template, jsonify, redirect, url_for,send_file, session
import os
from models import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from bson import ObjectId


app=Flask(__name__)
app.secret_key='Aashish'
ALLOWED_EXTENSIONS = {'pptx', 'docx', 'xlsx'}

app.config['UPLOAD_FOLDER']='uploads'



#   user login function
@app.route('/login',methods=['POST'])
def user_login():
    username=request.form.get('username')
    password=request.form.get('password')
    
    user=db.LoginUser.find_one(({'username':username, 'password':password}))
  
    if user:
        session['logged_in'] = True
        session['username'] = username
        return redirect(url_for('upload'))
    else:
        return jsonify({'error': 'Login Failed'})
    

#    upload function 
     
@app.route('/upload', methods=['GET','POST'])
def upload():

    if not session.get('logged_in'):
        return jsonify({'error': 'unwuthorized'}), 401
    
    if request.method == 'POST':
        file = request.files['file']

        if file and allowed_file(file.filename):
            file_path= os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
            file.save(file_path)
            db.Fileupload.insert_one({'filename':file.filename.replace(" ", "_"),'furl':file_path})
            return jsonify({'message':'File uploaded successfully'}), 201
        else:
            return jsonify({'error':'File upload failed'}), 400

    return "Welocome to the upload page"




#   client login function
@app.route('/client-login',methods=['POST'])
def client_login():
    clientname=request.form.get('clientname')
    cpassword=request.form.get('password')

    user= db.Client.find_one({'clientname':clientname})
 
    file_info_cursor = db.Fileupload.find({})
    f_names= [file_info['filename'] for file_info in file_info_cursor]
  
    if user and check_password_hash(user['cpassword'],cpassword):
        file_urls = [{'download-link': request.url_root.rstrip('/') + '/download_file/' + f_name.replace(" ", '_')} for f_name in f_names]
        return jsonify({'success': 'success', 'file_urls': file_urls})
    else:
        return jsonify({'error': 'client Login failed'}) 


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
@app.route('/download_file/<filename>',methods=['GET', 'POST'])
def download_file(filename):
    obj_filename=filename
    
    file_info = db.Fileupload.find_one({'filename':obj_filename})
  
    if file_info:
        return send_file(file_info['furl'], as_attachment=True)
    else:
        return jsonify({'error':'File not found'})


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



if __name__ == '__main__':
    app.run(debug=True)