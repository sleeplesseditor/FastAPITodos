# FastAPITodos

#### Table of Contents
- [Description](#description)
- [Example Screenshots](#example-screenshots)
- [Running the Files Locally](#running-the-files-locally)

## Description
An investigation into the use of databases with FastAPI, as part of ongoing coursework for [Eric Roby's Udemy course](https://www.udemy.com/course/fastapi-the-complete-course).

## Example Screenshots
<img width="1432" height="678" alt="Screenshot 2026-09-22 at 11 08 38" src="https://github.com/user-attachments/assets/d79734d4-55b7-45d4-b22f-6a0e9f93ec0e" />

<img width="1392" height="668" alt="Screenshot 2026-09-22 at 11 09 00" src="https://github.com/user-attachments/assets/87ceeb0f-9c1b-4662-81a6-5259680b2522" />

## Running the Files Locally
To set up the environments:
- Create a virtual environment by running `python3 -m venv fastapienv`
- Start up the virtual environment with `source fastapienv/bin/activate`
- Run `pip install`

To run `database.py`
- Ensure you have sqlite3 installed
- Create a database file by running `sqlite3 todosapp.db`
- Run `uvicorn main:app --reload`
