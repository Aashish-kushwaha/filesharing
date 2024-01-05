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
    .\venv\Scripts\activate
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
check the body of ```\login``` for existing user details and login using those details.\
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
If successful, you will receive a success message along with links to download the uploaded files.\
use this link to download the files.\

## Important Notes
The application uses MongoDB Atlas, and the database is open to all IPs.

## How do you plan on deploying this to the production environment
To put my Flask app on the internet, I choose a reliable cloud service, set up a strong web server, and use a tool like Gunicorn to run my app smoothly. I keep things secure by managing secrets like passwords properly and keeping an eye on any issues with logging. I think about handling more users by scaling up or out as needed. Automation tools help with testing and updating my app, making it easier to manage. I use monitoring tools to catch and fix problems, have a backup plan just in case, and write clear instructions so everyone knows how things work. This way, my Flask app runs smoothly and securely for users.
 