# FastAPITodos

#### Table of Contents
- [Description](#description)
- [Example Screenshots](#example-screenshots)
- [Running the Files Locally](#running-the-files-locally)

## Description
An investigation into the use of databases with FastAPI, as part of ongoing coursework for [Eric Roby's Udemy course](https://www.udemy.com/course/fastapi-the-complete-course). The application demonstrates the use of authorization and authentication, as well as examples of connection to database options for Sqlite3, Postgres and MySQL, Alembic migrations and basic uses of PyTest.

## Example Screenshots
<img width="1416" height="681" alt="Screenshot 2026-09-25 at 10 59 06" src="https://github.com/user-attachments/assets/94072ba0-6a48-4699-bff8-fcbe03d65afe" />

<img width="1392" height="668" alt="Screenshot 2026-09-22 at 11 09 00" src="https://github.com/user-attachments/assets/87ceeb0f-9c1b-4662-81a6-5259680b2522" />

## Running the Files Locally
To set up the environments:
- Create a virtual environment by running `python3 -m venv fastapienv`
- Start up the virtual environment with `source fastapienv/bin/activate`
- Run `pip install`

To run `database.py`
- Create your own `user_secrets.py` file, with a 'secret_hex_key' value. You can use the `openssl rand -hex 32` in the terminal to create a string value.
- Ensure you have sqlite3/postgres/MySQL installed
- To use it with sqlite3, create a database file by running `sqlite3 todosapp.db`. Remove the comment tag for the sqlite3 connection in `database.py` (make sure the other connection options are commented out)
- To use it with postgres, comment out the other options, remove the comment tag for the postgres option and fill out the URL correctly
- To use it with MySQL, comment out the other options, remove the comment for the MySQL option and fill out the URL correctly
- Run `uvicorn main:app --reload`
