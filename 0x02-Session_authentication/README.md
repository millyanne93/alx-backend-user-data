# Session Authentication

This project demonstrates how to implement session-based authentication in a web application. It builds on basic authentication mechanisms to provide a more user-friendly and persistent authentication system using session IDs stored both in-memory and in a database.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Tasks](#tasks)
  - [0. Et moi et moi et moi!](#0-et-moi-et-moi-et-moi)
  - [1. Empty session](#1-empty-session)
  - [2. Create a session](#2-create-a-session)
  - [3. User ID for Session ID](#3-user-id-for-session-id)
  - [4. Session cookie](#4-session-cookie)
  - [5. Before request](#5-before-request)
  - [6. Use Session ID for identifying a User](#6-use-session-id-for-identifying-a-user)
  - [7. New view for Session Authentication](#7-new-view-for-session-authentication)
  - [8. Logout](#8-logout)
  - [9. Expiration?](#9-expiration)
  - [10. Sessions in database](#10-sessions-in-database)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **Session Authentication** project is designed to enhance user authentication by storing session IDs. Users authenticate by starting a session which persists between requests and can be stored in-memory or in a database for longevity. This project extends the basic authentication approach to improve usability and security.

## Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- Flask
- `uuid` module
- A compatible web browser

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/alx-backend-user-data.git
   cd alx-backend-user-data
Navigate to the Session Authentication directory:

bash
Copy code
cd 0x02-Session_authentication
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Set environment variables:

bash
Copy code
export AUTH_TYPE=session_auth
export SESSION_NAME=_my_session_id
Run the application:

bash
Copy code
python3 -m api.v1.app
Access the application via http://localhost:5000 in your web browser.

Tasks
0. Et moi et moi et moi!
Copy Work: Copy all files from 0x01-Basic_authentication to 0x02-Session_authentication.
New Endpoint: Add a new endpoint GET /users/me to retrieve the authenticated user.
1. Empty session
Create SessionAuth Class: Add a new class SessionAuth in api/v1/auth/session_auth.py which inherits from Auth.
Environment Variable Switch: Update api/v1/app.py to use SessionAuth based on the AUTH_TYPE environment variable.
2. Create a session
Session Management: Implement create_session method in SessionAuth class to generate and store session IDs.
3. User ID for Session ID
Retrieve User ID: Implement user_id_for_session_id method in SessionAuth class to fetch the user ID from the session ID.
4. Session cookie
Session Cookie: Add session_cookie method to auth.py to get the session ID from the request cookies.
5. Before request
Update @app.before_request: Modify api/v1/app.py to check for session cookies and authorization headers.
6. Use Session ID for identifying a User
Current User: Implement current_user method in SessionAuth class to get the user from the session ID.
7. New view for Session Authentication
New Route: Create POST /auth_session/login in api/v1/views/session_auth.py to handle user login.
8. Logout
Destroy Session: Add destroy_session method in SessionAuth to handle logout and session invalidation.
New Route: Create DELETE /api/v1/auth_session/logout to handle logout requests.
9. Expiration?
Session Expiration: Create SessionExpAuth class to handle session expiration based on a set duration.
10. Sessions in database
Persistent Sessions: Create SessionDBAuth class to store session IDs in a database.
User Session Model: Create UserSession model in models/user_session.py to store session data.
Testing
Run tests to verify the functionality:

bash
Copy code
pytest
Contributing
Feel free to submit issues or pull requests. Please ensure your code follows the existing style and passes all tests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

r
Copy code

### Additional Steps:

- **If you want to create the file directly from the command line**:
  ```bash
  cat <<EOF > README.md
  # Session Authentication

  This project demonstrates how to implement session-based authentication in a web application. It builds on basic authentication mechanisms to provide a more user-friendly and persistent authentication system using session IDs stored both in-memory and in a database.

  ## Table of Contents

  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Tasks](#tasks)
    - [0. Et moi et moi et moi!](#0-et-moi-et-moi-et-moi)
    - [1. Empty session](#1-empty-session)
    - [2. Create a session](#2-create-a-session)
    - [3. User ID for Session ID](#3-user-id-for-session-id)
    - [4. Session cookie](#4-session-cookie)
    - [5. Before request](#5-before-request)
    - [6. Use Session ID for identifying a User](#6-use-session-id-for-identifying-a-user)
    - [7. New view for Session Authentication](#7-new-view-for-session-authentication)
    - [8. Logout](#8-logout)
    - [9. Expiration?](#9-expiration)
    - [10. Sessions in database](#10-sessions-in-database)
  - [Testing](#testing)
  - [Contributing](#contributing)
  - [License](#license)

  ## Introduction

  The **Session Authentication** project is designed to enhance user authentication by storing session IDs. Users authenticate by starting a session which persists between requests and can be stored in-memory or in a database for longevity. This project extends the basic authentication approach to improve usability and security.

  ## Prerequisites

  Ensure you have the following installed:

  - Python 3.8 or higher
  - Flask
  - `uuid` module
  - A compatible web browser

  ## Installation

  1. **Clone the repository**:
     \`\`\`bash
     git clone https://github.com/your_username/alx-backend-user-data.git
     cd alx-backend-user-data
     \`\`\`

  2. **Navigate to the Session Authentication directory**:
     \`\`\`bash
     cd 0x02-Session_authentication
     \`\`\`

  3. **Install dependencies**:
     \`\`\`bash
     pip install -r requirements.txt
     \`\`\`

  ## Usage

  1. **Set environment variables**:
     \`\`\`bash
     export AUTH_TYPE=session_auth
     export SESSION_NAME=_my_session_id
     \`\`\`

  2. **Run the application**:
     \`\`\`bash
     python3 -m api.v1.app
     \`\`\`

   3. **Access the application** via \`http://localhost:5000\` in your web browser.

  ## Tasks

  ### 0. Et moi et moi et moi!

  - **Copy Work**: Copy all files from \`0x01-Basic_authentication\` to \`0x02-Session_authentication\`.
  - **New Endpoint**: Add a new endpoint \`GET /users/me\` to retrieve the authenticated user.

  ### 1. Empty session

  - **Create \`SessionAuth\` Class**: Add a new class \`SessionAuth\` in \`api/v1/auth/session_auth.py\` which inherits from \`Auth\`.
  - **Environment Variable Switch**: Update \`api/v1/app.py\` to use \`SessionAuth\` based on the \`AUTH_TYPE\` environment variable.

  ### 2. Create a session

  - **Session Management**: Implement \`create_session\` method in \`SessionAuth\` class to generate and store session IDs.

  ### 3. User ID for Session ID

  - **Retrieve User ID**: Implement \`user_id_for_session_id\` method in \`SessionAuth\` class to fetch the user ID from the session ID.

  ### 4. Session cookie

  - **Session Cookie**: Add \`session_cookie\` method to \`auth.py\` to get the session ID from the request cookies.

  ### 5. Before request

  - **Update \`@app.before_request\`**: Modify \`api/v1/app.py\` to check for session cookies and authorization headers.

  ### 6. Use Session ID for identifying a User

  - **Current User**: Implement \`current_user\` method in \`SessionAuth\` class to get the user from the session ID.

  ### 7. New view for Session Authentication

  - **New Route**: Create \`POST /auth_session/login\` in \`api/v1/views/session_auth.py\` to handle user login.

  ### 8. Logout

  - **Destroy Session**: Add \`destroy_session\` method in \`SessionAuth\` to handle logout and session invalidation.
  - **New Route**: Create \`DELETE /api/v1/auth_session/logout\` to handle logout requests.

  ### 9. Expiration?

  - **Session Expiration**: Create \`SessionExpAuth\` class to handle session expiration based on a set duration.

  ### 10. Sessions in database

  - **Persistent Sessions**: Create \`SessionDBAuth\` class to store session IDs in a database.
  - **User Session Model**: Create \`UserSession\` model in \`models/user_session.py\` to store session data.

  ## Testing

  Run tests to verify the functionality:

  \`\`\`bash
  pytest
  \`\`\`
