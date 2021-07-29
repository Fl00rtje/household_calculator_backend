# Flora's Household Calculator
Welcome! Flora's household calculator is a hobby project. 
I got the idea of creating a calculating tool when I moved to a new apartment and was wondering what my new costs of housing were going to be.

### How to start the project
1. Create a new directory
2. Create a virtual environment for the project
3. Clone the project to your computer: git clone https://github.com/Fl00rtje/household_calculator_backend.git
4. Install the requirements: pip install -r requirements.txt
5. Create a PostgreSQL database and start the server
6. Create a conf.py file in the household_calculator_backend folder with the following database details:

```
db_credentials = {
    "user": <the user you created, for example: "bigbird">,
    "password": <the password you created, for example: "elmo">
    "localhost": <where you can reach the database, for example: "@localhost:5432/household_calculator_2021">
}
```

7. Start the program by running: python v5.py

### Specifications
- Python
- PostgreSQL
- SQLalchemy

