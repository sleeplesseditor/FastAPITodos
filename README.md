# FastAPITodos

#### Table of Contents
- [Description](#description)
- [Example Screenshots](#example-screenshots)
- [Running the Files Locally](#running-the-files-locally)

## Description
An investigation into the use of databases with FastAPI, as part of ongoing coursework for [Eric Roby's Udemy course](https://www.udemy.com/course/fastapi-the-complete-course). This project focuses on the use of authorization (via JWT), routers and authentication of requests.

## Example Screenshots
<img width="1416" height="681" alt="Screenshot 2026-09-25 at 10 59 06" src="https://github.com/user-attachments/assets/94072ba0-6a48-4699-bff8-fcbe03d65afe" />

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
