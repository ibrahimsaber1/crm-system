# CRM Application Using Django

## Project Overview
This project is a comprehensive CRM (Customer Relationship Management) application built using Django, Python, and MySQL. It includes essential features like creating, reading, updating, and deleting records (CRUD operations), user authentication, and version control with Git.

## Features
- **User Authentication**: Secure login/logout functionality for users.
- **CRUD Operations**: Ability to create, read, update, and delete customer data.
- **Version Control**: Managed with Git for tracking changes.
- **API Support**: Integrated Django Rest Framework (DRF) to build and manage APIs.
- **Image Handling**: Used Pillow for handling image uploads and management.
- **Password Security**: Incorporated bcrypt for password hashing.

## Technologies Used
- **Backend**: Django, Python, MySQL
- **Frontend**: HTML, CSS, Bootstrap
- **Version Control**: Git
- **Libraries**:
  - Django Rest Framework (DRF)
  - bcrypt
  - Pillow

## Installation

1. Clone the repository:
   ```bash
     git clone https://github.com/ibrahimsaber1/crm-django.git
     cd crm-django
   ```
2. Set up a virtual environment and activate it:

```bash
  python -m venv env
  source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
Configure the database settings in settings.py to connect to your MySQL database.
```

4. Run the migrations:

```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```
## Usage
Once the server is running, you can access the application in your browser at `http://127.0.0.1:8000/`. Register, log in, and start managing customer data with the CRUD interface.

## Contributing
If you'd like to contribute to this project, please fork the repository, create a new branch, and submit a pull request.

## License
This project is licensed under the MIT License.
