🚀 Automate CI/CD Pipelines using AWS Lambda
🏗️ Architecture Diagram
<img width="1536" height="1024" alt="ChatGPT Image Jun 20, 2026, 03_47_54 PM" src="https://github.com/user-attachments/assets/ebe40d9b-4e13-4e52-a0f0-45ce7fd65a55" />


🎯 Purpose

This project demonstrates how to automatically trigger AWS CodePipeline using AWS Lambda, enabling a fully automated CI/CD pipeline without manual intervention.

Whenever a trigger event occurs, Lambda starts the pipeline execution and initiates the deployment process.

☁️ AWS Services Used
AWS Lambda
AWS CodePipeline
AWS IAM
GitHub (Source Repository)
⚙️ Workflow
Code is pushed to GitHub repository
AWS Lambda function is triggered (manual or event-based)
Lambda calls AWS CodePipeline API
CodePipeline execution starts automatically
Build and deployment stages run in pipeline


🖼️ Screenshots
⚡ Lambda Function
<img width="1836" height="732" alt="Screenshot 2026-06-20 154938" src="https://github.com/user-attachments/assets/58712112-c0ef-4040-bdec-bb310fdeba20" />



🔄 CodePipeline Execution
<img width="1913" height="811" alt="Screenshot 2026-06-20 155039" src="https://github.com/user-attachments/assets/ae4173a3-bd7b-4819-891e-9f9feeb00e8f" />


🔐 IAM Role Permissions
<img width="1545" height="706" alt="Screenshot 2026-06-20 155128" src="https://github.com/user-attachments/assets/4fe3e100-6c67-4525-9d34-734c15af3c69" />


📁 GitHub Repository
https://github.com/dongareajar-dotcom/aws-lambda-codepipeline-automation

🚀 Key Features
Fully Automated CI/CD Pipeline
Event-driven deployment using Lambda
No manual pipeline execution required
Scalable AWS serverless automation
🎯 Outcome

This project demonstrates how AWS Lambda can be used to automate CI/CD pipelines, improving deployment speed, reducing manual effort, and ensuring consistent delivery.
