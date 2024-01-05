# Flask File sharing application

This API allows users to login and upload files and clients to Register or log in and download the uploaded files.

## Prerequisites

Make sure you have the following installed on your system:

- Python (3.6 or higher)

## Getting Started
Follow the steps to setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Aashish-kushwaha/filesharing
    cd filesharing
    ```
2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    ```
3. **Activate the Virtual Environment**
    ```bash
    venv\Scripts\activate
    ```
    On Unix or MacOS:

    ```bash
    source venv/bin/activate
    ```
4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
5. **Start the Server**
    ```bash
    python app.py
    ```

## Usage with Postman
Open Postman and import the provided Postman dump (filesharing.postman_collection.json).

1. **User Login**:
Make a POST request to ```bash/login``` with the following parameters:
'username': Your username
'password': Your password
2. **File Upload**:

Make a POST request to ```/upload``` with the following parameters:
file: Choose a file to upload
Client Registration:

Make a POST request to /client-register with the following parameters:
email: Client email
password: Client password
clientname: Client name
Client Login and File Download:

Make a POST request to /client-login with the following parameters:

clientname: Your client name
password: Your client password
If successful, you will receive a success message along with links to download the uploaded files.

    
    

## Configuration

1. Open `app.py` and locate the following section:

    ```python
    # MongoDB configuration
    app.config['MONGO_URI'] = 'mongodb://your-mongodb-uri/your-database-name'
    ```

2. Replace `'your-mongodb-uri'` and `'your-database-name'` with your MongoDB connection URI and database name from MongoDB Atlas.

## Running the Application

Run the Flask application:

```bash
python app.py
