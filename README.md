 Welcome to iFly! - Virtual Flying Experience
===============================================

This is the central guide for the **iFly** application, your platform for tracking, reviewing, and managing virtual flight experiences.

🚀 What is iFly?
----------------

The iFly application is a web-based platform designed for enthusiasts of flight simulators and virtual aviation. It uses a robust backend to store flight logs and data, which is then presented through a dynamic web interface.

### Key Features 

*   **Virtual Flight Logging:** 
    
*   **Experience Review:** 
    
*   **Database Management:** Centralized storage for all flight data using MySQL.
    
*   **Dynamic Interface:** Interactive elements built with **JavaScript** and rendered using **Jinja2** templates.
    
    

💻 Getting Started (Accessing the App)
--------------------------------------

### Online Access

If the iFly application is already deployed on a web server (like Heroku), you can access it directly:

*   **Application URL:** \[Insert Live URL Here\]
    
*   **Supported Browsers:** We recommend using the latest versions of **Chrome, Firefox, or Edge**.
    

### Local Access (General Instructions)

If you are running the application on your own computer, follow these general steps:

1.  python server.py
    
2.  **Open in Browser:** After the server starts successfully, open your web browser and navigate to the address provided in your terminal (usually **http://localhost:5000**).
    

🛠️ Local Development Setup
---------------------------

This guide walks technical users through setting up the environment, dependencies, and database required to run the application locally.

### Prerequisites

You must have the following software installed:

*   **Python 3** (3.8+ recommended)
    
*   **MySQL Server** (version 8.0+ recommended)
    
*   **Git**
    

### Installation Steps

1.  git clone \[Your Repository URL\]cd \[Your Project Folder Name\]
    
2.  **Install Python Dependencies**This project uses either Pipenv or standard pip for dependency management.
    
    *   \# Install all required packages (as listed in Pipfile/Pipfile.lock)pipenv install# Activate the virtual environmentpipenv shell
        
    *   \# Create a virtual environment (best practice)python3 -m venv venvsource venv/bin/activate # On Windows, use: .\\venv\\Scripts\\activate# Install packagespip install -r requirements.txt
        
3.  **Database Configuration (MySQL)**This step requires a running MySQL server instance.
    
    1.  CREATE DATABASE ifly\_db;
        
    2.  **Apply Schema:** The required tables and relationships are defined in the **MySQL Workbench** file: sightings\_erd.mwb. You will need to use this file to generate and execute the necessary SQL statements to create the table structure in the ifly\_db database.
        
    3.  \# Example .env contentDATABASE\_URL="mysql+pymysql://:@localhost/ifly\_db"SECRET\_KEY="your\_flask\_secret\_key"
        
4.  python server.pyThe server should now be running, accessible at the local address specified in the console output.
    

⚙️ For Technical Users & Installers (Summary)
---------------------------------------------

This section provides a quick technical overview of the application's components.

Stack Component

Files/Technologies Used

Purpose

**Backend Framework**

server.py, flask\_app/

The core application logic built using **Flask**.

**Database**

sightings\_erd.mwb

**MySQL** is the required database, managed via **Flask-SQLAlchemy**.

**Frontend**

flask\_app/templates/

**Jinja2** is used for dynamic HTML templating, and **JavaScript** powers the front-end interactivity.

**Configuration**

requirements.txt, Pipfile, Procfile

Manages Python dependencies and deployment on platforms like Heroku.

> **Note on Database:** This application requires a **MySQL** database setup according to the blueprint found in sightings\_erd.mwb.

