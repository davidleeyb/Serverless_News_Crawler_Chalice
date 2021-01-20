Branchy Lambda with Chalice
==============================

This projetc is to use a chalice framework to create, and deploy the lambda function[a news crawler] to AWS.

Project Organization
------------

    
    ├── README.md               <- The top-level README for developers using this project.
    │
    ├── NewsCrawler             <- chalice app project folder.
    │   │
    │   ├── .chalice            <- .chalice structure
    │   │   │
    │   │   └── deployed        <- List of deployed files
    │   │   │
    │   │   └── deploymnet      <- binary deployment history
    │   │   │
    │   │   └── config.json     <- .chalice config file
    │   │
    │   ├── app.py              <- serverless main app
    │   │
    │   └── requirements.txt    <- app deployment dependancy
    │
    └── requirements.txt        <- The requirements file for reproducing the dev environment


--------

## **Steps to run the project**
1. Python -m venv env
2. .\env\scripts\activate
3. pip install -r requirements.txt
4. cd NewsCrawler 
5. chalice deploy 
--------
***Please configure your AWS credentials before initiating the deployment**

