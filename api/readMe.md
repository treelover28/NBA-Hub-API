# NBA Match Predictor API

### Installation/Setup (localhost)

- Install MongoDB server package on your computer
- Start a mongod instance on your computer. For example, on Linux Ubuntu

```
    sudo systemctl start mongod // Start the mongod server
    sudo mongod // runs the server
```

- To get all the dependencies required, you can either install all required dependencies on your computer or (if you're on Linux Ubuntu like I am!) start the virtual environment accompanied with this project

To install directly on your local computer

```

  cd api // go to api directory
  pip3 install requirements.txt // if you are using Python 3
  pip install requirements.text // if you are using Python 2

```

To start virtual environment instead, do:

```
    // Assuming you are in project's root directory /NBA-Match-Predictor
    source ./virtualenv/bin/activate

```

- Start the API

```
    // Assuming you are in project's root directory /NBA-Match-Predictor
    // go into api directory
    cd api
    python3 app.py
```

- If this is your first time starting the API, your local MongoDB database is probably empty.

  - The API is configured to auto-update the database immediately after startup.
  - **NOTE** the first update will take roughly ~3-4 minutes since it is filling up your local mongoDB database with data from all 5 seasons from 2015-2020.

- Test your API is running by running the main function in client.py which attempts to:
  - Simulate a game between Clippers and Lakers
  - Simulate games on Christmas Day 12/25/2019
