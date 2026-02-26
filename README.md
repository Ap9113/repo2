# Flask To-Do List

A simple interactive to-do list web application built with Flask, SQLAlchemy, and Flask-Migrate. You can add tasks, mark them as done, and delete them. The frontend uses the Fetch API to interact with a RESTful backend, providing a smooth user experience without full page reloads.

## Features
- Add new tasks
- Mark tasks as completed/uncompleted
- Delete tasks
- RESTful JSON API
- Interactive frontend with vanilla JavaScript

## Tech Stack
- Python 3.7+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite (default)

## Project Structure

```
flask-todo-list/
├── .flaskenv
├── .gitignore
├── config.py
├── migrations/            # Database migrations
├── app.db                # SQLite database (auto-created)
├── requirements.txt
├── run.py                # Application entry point
├── README.md
├── app/
│   ├── __init__.py       # App factory
│   ├── models.py         # SQLAlchemy models
│   ├── main.py           # Main blueprint (serves UI)
│   ├── api.py            # API blueprint (JSON endpoints)
│   ├── templates/
│   │   └── index.html    # Frontend HTML
│   └── static/
│       ├── css/
│       │   └── styles.css
│       └── js/
│           └── app.js
```

## Getting Started

### 1. Clone the repository
```
git clone https://github.com/yourusername/flask-todo-list.git
cd flask-todo-list
```

### 2. Create a virtual environment and install dependencies
```
python3 -m venv venv
source venv/bin/activate    # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Initialize the database
```
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 4. Run the application
```
flask run
```

Navigate to http://127.0.0.1:5000 in your browser to see the app in action.

## API Endpoints

GET    /api/tasks           - List all tasks
POST   /api/tasks           - Create a new task `{ "title": "Buy milk" }`
PUT    /api/tasks/<id>      - Update a task `{ "done": true }` or `{ "title": "New title" }`
DELETE /api/tasks/<id>      - Delete a task

## License
This project is licensed under the MIT License.
