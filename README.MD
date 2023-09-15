## An API that allows you to perform CRUD operations on a person resource

The hosted version of this API is available here: https://hngstagetwo-wpel.onrender.com, However, if you would like to run this on your local machine, follow the guide below.

## Requirements

1. **PYTHON**: This project is built with FastAPI which is a python framework. Run this command `python --version` to check if you have Python installed on your machine. If you dont have python, download and install Python on your machine here: https://www.python.org/downloads/. 

2. **Database**: PostgreSQL was used for this project. If you don't have it installed, download and install Postgres here: https://www.postgresql.org/download/


## SETUP

#### 1. Clone the repository

```bash
git clone https://github.com/Ideeee/hngstagetwo.git
 ```

#### 2. Create a virtual environment 

```bash
 `python3 -m venv {the-name-of-your-virtualenv}`
 ```

#### 3. Activate the virtual environment using `.\env\scripts\Activate.ps1` on Windows or ` source ./env/bin/Activate` on Linux

#### 4. Copy the contents of env.sample into your .env file and populate it with your values

#### 5. Install the project dependencies

``` bash
`pip install -r requirements.txt`
```  

#### 6. Run the database migrations 

```bash
alembic upgrade head
```

#### 7. Start the development server

```bash
 `uvicorn main:app --reload`
```
 The application should start on `localhost:8000`

#### 8. Navigate to `localhost:8000/docs` in your browser for the interactive api documentation
