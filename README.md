# Interview Management Application

## Introduction

The Interview Management Application is designed to streamline the interview process by providing features for managing candidates, user authentication, and note-taking functionalities.

---

## Features

### User Authentication

- **Sign up:** Allow users to create an account with a unique username and password.
- **Login:** Enable registered users to securely log in to the application.

### Candidate Management

- **Create Candidates:** Authenticated users can add new candidates with details such as name, contact information, and resume.
- **View Candidates:** Users have access to a list displaying basic information about all candidates.
- **Edit Candidate Details:** Provide the ability to modify candidate information.

### Notes Management

- **Add Notes to Candidates:** Users can add notes associated with each candidate, including details about interviews, assessments, or any other relevant information.
- **View Notes:** Enable users to view all notes related to a specific candidate.
- **Edit and Delete Notes:** Allow users to modify existing notes and delete notes associated with candidates.

---

## Installation

1. Clone the repository:

   ```bash
   git clone git@bitbucket.org:hnusterdien/interview-management-application.git
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On macOS and Linux
   myenv\Scripts\activate  # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Perform database migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the application in a web browser:

   ```
   http://localhost:8000/
   ```

---

## Configuration

- **Settings:** Check the settings file (`settings.py`) for any critical configurations specific to your deployment environment.
- **Environment Variables:** Ensure any necessary environment variables are set (if applicable).

---

## Contributing

Contributions to enhance this project are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/fooBar`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some fooBar'`).
5. Push to the branch (`git push origin feature/fooBar`).
6. Create a pull request.

Please adhere to the [Code of Conduct](CODE_OF_CONDUCT.md) when contributing.

---

## License

This project is licensed under the [MIT License]. See the [MIT License](https://opensource.org/license/mit/) file for details.

Copyright (c) 2023 Hishaam Nusterdien

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
