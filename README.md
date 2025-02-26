Appfodev CodeBot MVP

Public Testing Documentation - Version 1.1
Date: 01/012025

Overview

Appfodev CodeBot is an AI-powered tool designed to generate code from natural language prompts. This Minimum Viable Product (MVP) is released for public developer testing to validate core functionalities, including:

Code generation accuracy across industries (Agri-tech, Healthcare, Fintech).

User experience (UI/UX), performance, and security feedback.

Scalability for future deployment.



---

MVP Features

1. Natural Language to Code: Converts prompts like “Create a REST API” into Python/JavaScript code.


2. Code Editor: Uses Monaco Editor for syntax-highlighting with read-only mode.


3. History Tracking: Saves and displays past code generations.


4. Docker Sandbox: Executes generated code in isolated Docker containers for security.




---

Prerequisites

Software Requirements:

Python 3.10+

Node.js 16+

Docker Desktop (for sandbox execution)

Git


Required Accounts:

OpenAI API Key (Sign up here)

AWS/GCP account (Optional: For cloud deployment)



---

Setup Guide

Step 1: Clone the Repository

git clone https://github.com/appfodev-codebot/Appfodev-CodeBot-MVP.git
cd Appfodev-CodeBot-MVP

Step 2: Backend Setup

Navigate to the backend folder:

cd backend

Install dependencies:

pip install -r requirements.txt

Configure environment variables:
Create a .env file inside the backend/ folder and add the following:

OPENAI_API_KEY=your_openai_key
SECRET_KEY=your_django_secret_key
DATABASE_URL=postgres://user:password@localhost/codebot

Run database migrations:

python manage.py migrate

Start the server:

python manage.py runserver


---

Step 3: Frontend Setup

Navigate to the frontend folder:

cd ../frontend

Install dependencies:

npm install

Start the React app:

npm start


---

Step 4: Docker Sandbox Setup (Optional)

Ensure Dockerfile Exists:
Check that backend/Dockerfile.sandbox exists. If not, create it before proceeding.

Build and Run Docker Sandbox:

docker build -t codebot-sandbox -f backend/Dockerfile.sandbox .
docker run --rm -p 5000:5000 codebot-sandbox


---

Testing Scenarios

Scenario 1: Basic Code Generation

Prompt: "Create a Python function to calculate factorial."

Expected Output:


def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

Scenario 2: Agri-Tech Use Case

Prompt: "Generate JavaScript code to plot soil moisture data from an IoT sensor."

Expected Output:


const plotSoilMoisture = (data) => {
    // Code to render chart using Chart.js
};

Scenario 3: Error Handling

Prompt: "Create a Python script to read a non-existent file."

Expected Behavior:
Generated code includes try-except blocks for error handling.



---

Feedback Guidelines

How to Submit Feedback:

Report issues via GitHub Issues:
GitHub Issues Page

Feedback Template:

Issue Type: [Bug / Feature Request]  
Description:  
Steps to Reproduce:  
Expected Behavior:  
Actual Behavior:  
Severity: [Low / Medium / High / Critical]

Focus Areas for Feedback:

Code accuracy (AI-generated code correctness).

Performance & Security (Any vulnerabilities).

UI/UX Improvements (Enhancements to editor & interface).



---

Known Issues & Workarounds

Issue: Limited language support

Workaround: Manually edit code for unsupported languages.


Issue: Missing imports in generated code

Workaround: Add necessary import statements manually.



---

Contribution Guidelines

1. Fork the repository:



git fork https://github.com/appfodev-codebot/Appfodev-CodeBot-MVP.git

2. Create a feature branch:



git checkout -b feature/your-idea

3. Commit changes and push:



git add .
git commit -m "Added new feature"
git push origin feature/your-idea

4. Submit a pull request (PR).



Priority Contributions:

Add support for Go & Rust.

Improve Docker sandbox security.



---

License

This project is licensed under the MIT License.


---

Contact

Mohd Wasil: aabanab007@gmail.com

GitHub Repository: Appfodev CodeBot


⚠ Disclaimer: This is a beta release. Do not use in production environments without additional testing.


---

Happy Coding! 🚀

Now you can easily copy-paste everything without formatting issues! Let me know if you need any further refinements.

