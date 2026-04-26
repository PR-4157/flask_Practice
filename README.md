# Flask CI/CD Pipeline using Jenkins & GitHub Actions

## Project Overview 
This project demonstrates how to implement CI/CD (Continuous Integration & Continuous Deployment) for a Flask web application using:
* Jenkins (Traditional CI/CD)
* GitHub Actions (Modern CI/CD)

The pipelines automate:
* Dependency installation
* Testing using pytest
* Build process
* Deployment to staging/production environments

## Part 1: Jenkins CI/CD Pipeline
-> Objective: To create an automated pipeline in Jenkins that:
* Fetches code from GitHub
* Installs dependencies
* Runs tests
* Deploys the application
  
-> Setup & Prerequisites: Before running the pipeline
  * Jenkins is installed (AWS EC2)
  <img width="1106" height="790" alt="Screenshot 2026-04-24 at 6 38 30 PM" src="https://github.com/user-attachments/assets/c38a53d3-8548-4ce2-b834-7926346bd7dc" />
  * Contect to Server:
<img width="640" height="572" alt="Screenshot 2026-04-24 at 6 41 50 PM" src="https://github.com/user-attachments/assets/41e38edb-17d6-455b-b3d2-e1e013f0cc66" />
  * install Python:
<img width="971" height="440" alt="Screenshot 2026-04-26 at 12 46 38 PM" src="https://github.com/user-attachments/assets/8e23eeb2-6db5-44b0-a0ff-cf0e1bf0f006" />
  * Install Jenkins:
<img width="925" height="476" alt="Screenshot 2026-04-26 at 12 31 25 PM" src="https://github.com/user-attachments/assets/9134e085-9429-49a2-bd50-e4ec6226bce2" />

-> Source Code Setup:
1. Fork the repository into your GitHub account
2. Clone it intoyour Jenkins server:
git clone https://github.com/<your-username>/flask_Practice.git
cd flask_Practice
<img width="971" height="543" alt="Screenshot 2026-04-26 at 12 32 32 PM" src="https://github.com/user-attachments/assets/3f659522-b315-41ae-8ed2-d78b45d69e7b" />

-> Jenkins Pipeline Explanation:
The pipeline is defined inside a file called Jenkinsfile.
<img width="1935" height="1135" alt="image" src="https://github.com/user-attachments/assets/5271d7ae-9015-441e-8368-7d8092d26aef" />

-> Stage-by-Stage Explanation:
1. Clone Stage
   * Pulls latest code from GitHub
   * Ensures pipeline always uses updated code
3. Build Stage
   * Installs dependencies using pip
   * Prepares environment for execution
5. Test Stage
   * Runs unit tests using pytest
   * Prevents deployment if tests fail
7. Deploy Stage
   * Runs Flask app
   * Uses background execution (nohup)

-> Pipeline Trigger:
* Configure Github Webhook

## Part 2: GitHub Actions CI/CD Pipeline
-> Objective: To automate CI/CD directly inside GitHub without using external tools.
-> GitHub Actions Workflow

-> Workflow Explanation:
1. Checkout Code
   * Downloads repository code into runner
2. Setup Python
   * Installs Python environment
3. Install Dependencies
   * Installs required libraries
4. Run Tests
   * Executes pytest
   *  Stops pipeline if tests fail
5. Build
   * Prepares app for deployment
6. Deploy
   * Staging → triggered on staging branch
   * Production → triggered on release tags

## Pipeline ScreenShot:
-> I have used port 5001 is occupied on another service.
## Before adding data: 
<img width="1325" height="550" alt="image" src="https://github.com/user-attachments/assets/bdc238f1-431b-4769-88d0-e1636704d278" />
## Adding new Data: 
<img width="1331" height="626" alt="image" src="https://github.com/user-attachments/assets/b635b73a-5247-43f0-8eed-52503ee39af4" />
## Jenkins > Flask pipelines > stages:
<img width="1658" height="853" alt="image" src="https://github.com/user-attachments/assets/63d5e76f-5ef3-4bbf-bb0f-df186407710b" />
<img width="825" height="456" alt="Screenshot 2026-04-26 at 2 24 55 PM" src="https://github.com/user-attachments/assets/353ac3c7-ca77-429a-99ef-88db57a0610b" />
<img width="1318" height="564" alt="image" src="https://github.com/user-attachments/assets/339e0921-36b9-4e63-add6-733d7669f32f" />

## Conclusion:
This project demonstrates:
* End-to-end CI/CD automation
* Integration of testing into deployment
* Difference between:
  * Jenkins (manual setup, powerful control)
  * GitHub Actions (cloud-based, easier setup)
Overall, it simulates a real-world DevOps pipeline used in modern software development.
