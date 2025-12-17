# Group Chat Application 💬

This project is a real-time group chat application built with Django. It allows users to register, log in, and communicate with each other in a chat room. The application features user authentication, message persistence, and basic user management functionalities like blocking/unblocking users. It provides a simple and intuitive interface for seamless communication.

## 🚀 Key Features

- **User Authentication:** Secure registration, login, and logout functionality. 🔐
- **Real-time Messaging:** Send and receive messages instantly within the chat room. ✉️
- **Message Persistence:** Chat messages are stored in a database for later retrieval. 💾
- **User Blocking:** Administrators can block/unblock users. 🚫
- **Admin Interface:** Django admin panel for managing users and messages. ⚙️
- **Customizable Development Server Port:** The development server defaults to port 8080. ⚙️

## 🛠️ Tech Stack

*   **Backend:** Python, Django
*   **Database:** SQLite (default)
*   **Frontend:** HTML, CSS, JavaScript
*   **Authentication:** Django's built-in authentication system
*   **Other:**
    *   `os`
    *   `sys`
    *   `pathlib`
    *   `json`
    *   `django.shortcuts`
    *   `django.contrib.auth`
    *   `django.contrib.auth.models`
    *   `django.http`
    *   `django.views.decorators.csrf`
    *   `django.views.decorators.cache`
    *   `django.utils.timezone`
    *   `django.views.decorators.http`
    *   `django.core.exceptions`

## 📦 Getting Started

### Prerequisites

- Python 3.6+ installed
- pip package installer

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3.  Activate the virtual environment:

    -   On Windows:

        ```bash
        venv\Scripts\activate
        ```

    -   On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5.  Apply migrations:

    ```bash
    python manage.py migrate
    ```

6.  Create a superuser (admin account):

    ```bash
    python manage.py createsuperuser
    ```

### Running Locally

1.  Start the development server:

    ```bash
    python manage.py runserver
    ```

    (This will default to port 8080 due to the custom `runserver` command.)

2.  Open your web browser and navigate to `http://localhost:8080/`.

## 💻 Usage

1.  **Register:** Create a new user account via the registration page.
2.  **Login:** Log in with your credentials.
3.  **Chat:** Start chatting in the main chat room.
4.  **Admin Panel:** Access the admin panel at `http://localhost:8080/admin/` to manage users and messages.

## 📂 Project Structure

```
group_chat/
├── manage.py               # Django management script
├── group_chat/           # Project settings and configurations
│   ├── __init__.py
│   ├── settings.py       # Project settings
│   ├── urls.py           # Project URL configuration
│   ├── asgi.py
│   └── wsgi.py
├── chat/                 # Chat application
│   ├── __init__.py
│   ├── admin.py          # Admin configurations
│   ├── apps.py
│   ├── models.py         # Data models (Message, Profile)
│   ├── views.py          # View functions
│   ├── urls.py           # Chat app URL configuration
│   ├── signals.py        # Signal handlers
│   ├── migrations/       # Database migrations
│   │   └── ...
│   ├── templates/
│   │   └── chat/         # HTML templates
│   │       └── ...
│   └── management/
│       └── commands/
│           └── runserver.py # Custom runserver command
├── static/               # Static files (CSS, JavaScript)
│   └── ...
├── templates/            # Project-level templates
│   └── ...
├── venv/                   # Virtual environment (not committed to the repo)
└── requirements.txt        # Project dependencies
```

## 📸 Screenshots

<img width="440" height="468" alt="image" src="https://github.com/user-attachments/assets/977eb692-e81f-4d07-bfc6-364ea32601ed" />

<img width="419" height="404" alt="image" src="https://github.com/user-attachments/assets/ea09f6d2-06e1-4ede-ae02-6a529e07378e" />

<img width="449" height="266" alt="image" src="https://github.com/user-attachments/assets/fa36dae6-4f07-4b5f-a173-efb035988a2e" />

<img width="452" height="288" alt="image" src="https://github.com/user-attachments/assets/c9efdbc8-3609-4299-85b3-32b4a6b80c13" />

<img width="677" height="569" alt="image" src="https://github.com/user-attachments/assets/1d9cfb07-e8c3-44ad-b482-c66e42198473" />


