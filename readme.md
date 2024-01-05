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
Open Postman and import the provided Postman dumps(filesharing.postman_collection.json).

1. **User Login:**\
Make a POST request to ```/login``` with the following parameters:\
'username': Your username\
'password': Your password \
check the postman dumb for existing user details and login using those details.\
2. **File Upload:**\
Make a POST request to ```/upload``` with the following parameters:\
file: Choose a file to upload\
3. **Client Registration:**\
Make a POST request to ```/client-register``` with the following parameters:\
email: Client email\
password: Client password\
clientname: Client name\
4. **Client Login and File Download:**\
Make a POST request to /client-login with the following parameters:\
clientname: Your client name\
password: Your client password\
If successful, you will receive a success message along with links to download the uploaded files.

    
 