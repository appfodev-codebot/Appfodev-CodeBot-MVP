Appfodev CodeBot MVP Public Testing Documentation
Version 1.0 | Date:

1. Overview
Appfodev CodeBot is an AI-powered tool designed to generate code from natural language prompts. This MVP (Minimum Viable Product) is released for public developer testing to validate core functionalities, including code generation, security, and usability.

Key Goals: 
Test code accuracy across industries (Agri-tech, healthcare, fintech).

Gather feedback on performance, UI/UX, and security.

Prepare for scalable deployment.

2. MVP Features
Feature	Description
Natural Language to Code	Converts prompts (e.g., “Create a REST API”) into Python/JavaScript code.
Code Editor	Syntax-highlighted editor with read-only mode (Monaco Editor).
History Tracking	Saves and displays past code generations.
Docker Sandbox	Executes generated code in isolated containers for security.

3. Prerequisites
Software:

Python 3.10+

Node.js 16+

Docker Desktop

Git

Accounts:

OpenAI API Key https://platform.openai.com/ (for code generation).

AWS/GCP account (optional for cloud deployment).

4. Setup Guide
Step 1: Clone the Repository

git clone   https://github.com/appfodev-codebot/Appfodev-CodeBot-MVP.git
cd codebot-mvp  

Step 2: Backend Setup
Navigate to the backend folder:
cd backend  

Install dependencies:
pip install -r requirements.txt  

Configure environment variables:
Create a .env file in backend/config/:

OPENAI_API_KEY=your_openai_key  
SECRET_KEY=django_secret_key  
DATABASE_URL=postgres://user:password@localhost/codebot  

Run migrations:
python manage.py migrate  

Start the server:
python manage.py runserver  

Step 3: Frontend Setup
Navigate to the frontend folder:

cd ../frontend  

Install dependencies:
npm install  
Start the React app:
npm start  

Step 4: Docker Sandbox (Optional)
docker build -t codebot-sandbox -f Dockerfile.sandbox .  

5. Testing Scenarios
Scenario 1: Basic Code Generation

Prompt: “Create a Python function to calculate factorial.”  


Expected Output:

def factorial(n):  
    return 1 if n == 0 else n * factorial(n-1)  
    
Scenario 2: Agri-Tech Use Case
Prompt: “Generate JavaScript code to plot soil moisture data from an IoT sensor.”  


Expected Output: const plotSoilMoisture = (data) => {  
    // Code to render chart using Chart.js  
};  
Scenario 3: Error Handling
Prompt: “Create a Python script to read a non-existent file.”  


Expected Behavior:

Generated code includes try-except blocks for error handling.

6. Feedback Guidelines
Submit feedback via GitHub Issues.

Feedback Template: Issue Type: [Bug/Feature Request]  
Description:  
Steps to Reproduce:  
Expected Behavior:  
Actual Behavior:  
Severity: [Low/Medium/High/Critical]  


Focus Areas:

Code accuracy, security, and performance.

UI/UX improvements.

7. Known Issues
 Issue	Workaround
Limited language support	Manually edit generated code for other languages.
Dependency gaps	Add import statements manually.

8. Contribution Guidelines
Fork the repository.

Create a feature branch: git checkout -b feature/your-idea  


Submit a pull request.

Priority Contributions:

Add support for Go/Rust.

Improve Docker sandbox security.


9. License
This project is licensed under the MIT License.

Contact
Mohd Wasil: aabanab007@gmail.com

GitHub: Appfodev CodeBot:
https://github.com/appfodev-codebot/

Note: This is a beta release. Use with caution in production environments.

Happy Coding! 































