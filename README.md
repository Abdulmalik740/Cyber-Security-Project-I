# Cyber-Security-Project-I
Instructions to run the Project
A simple voting system built with Django, allowing users to add candidates, vote for their preferred candidates, and view voting results.

**Features**
Add new candidates
Vote for candidates
View voting results

**Requirements**
Python 3.7 or higher
Django 3.x or higher
SQLite3 (comes with Django as the default database)

**Installation**
# Clone the repository
git clone https://github.com/your-username/voting-system.git && cd voting-system && \

# Install dependencies
pip install -r requirements.txt && \

# Set up the database
python manage.py makemigrations && python manage.py migrate voting

# Start the development server
python manage.py runserver

**Project Structure**
votingsystem/: Main Django project directory.
voting/: Contains the main application for handling voting, candidates, and results.
templates/: HTML templates for the voting pages.
static/: Static files used by the app.

**Usage**
Add Candidates:

Go to http://127.0.0.1:8000/add_candidate/ to add a new candidate.
Vote for Candidates:

Visit http://127.0.0.1:8000/vote/ to cast a vote for a candidate.
View Results:

Check the results by going to http://127.0.0.1:8000/results/

**Technical Details**
Backend: Django (Python)
Frontend: HTML
Database: SQLite (default Django database)

**Contributing**
Feel free to open issues and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
