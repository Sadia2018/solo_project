# ✈️ Welcome to iFly\! - Virtual Flying Experience

This is the central guide for the **iFly** application, your platform for booking and managing virtual flight experiences.

-----

## 🚀 What is iFly?

The iFly application is a web-based platform designed for enthusiasts of flight simulators and virtual aviation. 


-----

## 💻 Getting Started (Accessing the App)


### Local Access (General Instructions)

If you are running the application on your own computer, follow these general steps:

1.  **Start the Server:** The application is run using a file called `server.py`. Once all technical setup is complete (see the **Local Development Setup** below), the server is typically started with a simple command:
    ```bash
    python server.py
    ```
2.  **Open in Browser:** After the server starts successfully, open your web browser and navigate to the address provided in your terminal (usually **`http://localhost:5000`**).

-----

## 🛠️ Local Development Setup

This guide walks technical users through setting up the environment, dependencies, and database required to run the application locally.

### Prerequisites

You must have the following software installed:

  * **Python 3** (3.8+ recommended)
  * **MySQL Server** (version 8.0+ recommended)
  * **Git**

### Installation Steps

#### 1\. Clone the Repository

Open your terminal and clone the source code:

```bash
git clone [Your Repository URL]
cd [Your Project Folder Name]

### Local Access (General Instructions)

If you are running the application on your own computer, follow these general steps:

1.  **Start the Server:** The application is run using a file called `server.py`. Once all technical setup is complete (see the **Local Development Setup** below), the server is typically started with a simple command:
    ```bash
    python server.py
    ```
2.  **Open in Browser:** After the server starts successfully, open your web browser and navigate to the address provided in your terminal (usually **`http://localhost:5000`**).

-----

## 🛠️ Local Development Setup

This guide walks technical users through setting up the environment, dependencies, and database required to run the application locally.

### Prerequisites

You must have the following software installed:

  * **Python 3** (3.8+ recommended)
  * **MySQL Server** (version 8.0+ recommended)
  * **Git**

### Installation Steps

#### 1\. Clone the Repository

Open your terminal and clone the source code:

```bash
git clone [Your Repository URL]
cd [Your Project Folder Name]
2. Install Python DependenciesThis project uses either Pipenv or standard pip for dependency management.Option A: Using Pipenv (Recommended)Bash# Install all required packages (as listed in Pipfile/Pipfile.lock)
pipenv install

# Activate the virtual environment
pipenv shell
Option B: Using pip (via requirements.txt)Bash# Create a virtual environment (best practice)
python3 -m venv venv
source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate

# Install packages
pip install -r requirements.txt

3. Database Configuration (MySQL)This step requires a running MySQL server instance.Create the Database: Log into your MySQL server and create a new schema.SQLCREATE DATABASE ifly_db;
Apply Schema: The required tables and relationships are defined in the MySQL Workbench file: sightings_erd.mwb. You will need to use this file to generate and execute the necessary SQL statements to create the table structure in the ifly_db database.Set Environment Variables: Create a local .env file (or set variables in your shell) to provide the application with database connection credentials. This is crucial for Flask-SQLAlchemy to connect.# Example .env content
DATABASE_URL="mysql+pymysql://<USER>:<PASSWORD>@localhost/ifly_db"
SECRET_KEY="your_flask_secret_key"

4. Run the Application With dependencies installed and the database configured, you can start the Flask server:Bashpython server.py

The server should now be running, accessible at the local address specified in the console output.

