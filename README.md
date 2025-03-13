# Deeper Users

This repository contains the frontend and backend of the CRUD app requested as a test by Deeper Systems. The frontend uses Vue 3 (using Vuetify), while the backend uses Python, Flask and MongoDB.

Inside the backend directory, you will find a udata.json file containing data that is to be parsed by the 'parser.py' script (instructions below).

## How to run ▶️
```bash
# Clone this repository
$ git clone <https://github.com/stonasss/deeper-fullstack-test.git>
# Inside root directory, access the backend project folder cmd
$ cd backend
# Create the .venv folder
$ py -3 -m venv .venv
# Activate the .venv environment
$ .venv\Scripts\activate
# Install dependencies
$ pip install -r requirements.txt
# Create a .env file and add environment variables following .env.example (ex: DATABASE_NAME = "test_database")
# Run the parser script
$ python parser.py
# Start the Flask server
$ flask --app server run
# Now, return to the root directory and access the frontend project folder (I used a bash terminal)
$ cd frontend
# Install dependencies
$ npm i
# Create a .env file and add the api environment variable following .env.example
# Finally, start the frontend server
$ npm run dev
```

