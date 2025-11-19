# ✈️ Welcome to iFly!

This is the central guide for the iFly application, your platform for tracking and managing flight or sighting data.

---

## 🚀 What is iFly?

The iFly application is a web-based tool designed to help you view, manage, and interact with specific **sighting records** (likely related to aircraft or other observed phenomena).

### Key Features (Likely)

* View Sighting Records: See a list or map of all recorded sightings.
* Add New Sightings: Input new data, including time, location, and details.
* User Management: Secure login and profile management.

---

## 📚 User Manual & Help

The most important place to find detailed instructions on how to use all the features of the iFly application is in our dedicated user guide.

* 👉 **Find detailed usage instructions here:** [`UserManual.md`](UserManual.md)

---

## 💻 Getting Started (Accessing the App)


### Local Access (For Testing or Development)

If you are running the application on your own computer, follow these general steps:

1.  **Start the Server:** The application is run using a file called `server.py`. Once all technical setup is complete (see the next section for technical staff), the server is typically started with a simple command:
    ```bash
    python server.py
    ```
2.  **Open in Browser:** After the server starts successfully, open your web browser and navigate to the address provided in your terminal (usually **`http://localhost:5000`**).

---

## ⚙️ For Technical Users & Installers

This section is for developers or IT staff responsible for setting up or maintaining the application.

| File/Folder | Purpose |
| :--- | :--- |
| **`flask_app/`** | Contains the core code for the web application. |
| **`server.py`** | The main file that runs the application. |
| **`requirements.txt` / `Pipfile`** | Lists the necessary software libraries (**dependencies**) to make the app run. |
| **`sightings_erd.mwb`** | The **database blueprint** (schema) file, required for setting up the MySQL database. |
| **`Procfile`** | Instructions for deployment (e.g., how to run the app on Heroku). |

> **Note on Database:** This application requires a **MySQL** database setup according to the blueprint found in `sightings_erd.mwb`.

---

## ❓ Need Assistance?

* Check the [`UserManual.md`](UserManual.md) 

---
