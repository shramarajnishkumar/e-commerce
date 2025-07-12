# Scarpa Shoes - Django E-commerce Project

This is a Django-based e-commerce website for selling shoes. It provides functionalities for users to browse products, manage their cart, and for administrators to manage the store's inventory.

## Features

*   User registration and authentication.
*   Product catalog with categories and search functionality.
*   Shopping cart for users to add and manage products.
*   Admin panel for managing products, orders, and users.

## Tech Stack

*   **Framework:** Django 4.0.2
*   **Language:** Python
*   **Database:** SQLite3 (default)

## Setup and Installation

Follow these steps to get the project up and running on your local machine.

**1. Prerequisites:**

*   Python 3.x
*   pip

**2. Clone the repository:**

```bash
git clone <repository-url>
cd scarpa-shoes-master
```

**3. Create and activate a virtual environment:**

```bash
# For Linux/macOS
python3 -m venv myenv
source myenv/bin/activate

# For Windows
python -m venv myenv
myenv\Scripts\activate
```

**4. Install dependencies:**

It seems the `req.txt` file is not in the standard format. A typical `requirements.txt` for this project would look like this. You can create a new `requirements.txt` file with the following content:

```
Django==4.0.2
asgiref==3.5.0
# Add other necessary packages here
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

**5. Apply database migrations:**

```bash
python manage.py migrate
```

**6. Create a superuser:**

To access the admin panel, you need to create a superuser.

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin username and password.

**7. Run the development server:**

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

## Project Structure

*   `mysite/`: Contains the main project settings, URLs, and WSGI configuration.
*   `myapp/`, `shoesapp/`: Django apps containing the core logic for the e-commerce platform.
*   `media/`: Directory where uploaded product images are stored.
*   `db.sqlite3`: The SQLite database file.
*   `manage.py`: Django's command-line utility for administrative tasks.

## Configuration and Security

**IMPORTANT:** The `mysite/settings.py` file contains sensitive information like `SECRET_KEY` and email credentials.

*   **SECRET_KEY:** Do not use the hardcoded `SECRET_KEY` in a production environment. It is recommended to load it from an environment variable.
*   **Email Settings:** The `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` are hardcoded. This is a significant security risk. For production, use environment variables or another secure method to handle these credentials.

Example for `settings.py`:

```python
import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
```

