# DatabaseApp

DatabaseApp is a desktop application written in Python for working with MySQL databases.  
The application allows you to connect to a server and browse tables through a graphical interface.

## Features

- Connect to a MySQL server
- Browse tables in the selected database
- Display table data
- Graphical user interface built with PySide6

## Technologies

- Python 3
- PySide6
- mysql-connector-python

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/username/DatabaseApp.git
cd DatabaseApp
```

### 2. Create a virtual environment

Linux / macOS:

```bash
python3 -m venv .venv
source venv/bin/activate
```

Windows:

```bash
python -m venv .venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python -m dbapp
```

## License

This project is licensed under the MIT License.