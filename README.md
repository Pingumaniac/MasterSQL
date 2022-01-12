# MasterSQL
Personal project for educational software development

## About Members and Roles

#### Young-jae Moon
* Visiting student at Stony Brook University (Fall 2021 - Spring 2022).
* Email: youngjae.moon@stonybrook.edu

## Advisor

#### Professor Alexander Kuhn
* Teaching Assistant Professor in Computer Science at SUNY Korea

## Problem
One of the advantages of employing a relational database is that people can write complex queries in Structured Query Language (SQL) skillfully. Writing complex queries make the overall code more efficient and make software development faster. Nonetheless, many people find it hard to write complex queries when dealing with relational database management systems (RDBMS). Hence they import object-relational mapping (ORM) libraries, such as SQLAlchemy and Sequelize, so that they can handle the database only through simple queries. But ORM may likely provide poor abstractions of the database, be slower than directly executing SQL queries and complex queries especially. In other words, the use of ORM libraries reduce the major advantage that RDBMS has over the others: it is easy to write and execute complex queries in the RDBMS.

## Solution
“MasterSQL” is a web-based application that helps people to learn and practice writing MySQL queries. The users can learn SQL concepts through reading materials for each section, ensure that they have learnt the concepts properly through space repetition learning. Orbit library has been used for each page of the learning materials and the review section for each test. And through signing up the Orbit library, the users will be able to recall what they have learnt skillfully.

## Tools and technologies

### Programming languages and Database Management System (DBMS) used

1. JavaScript (ECMAScript 2021)
2. MySQL (MySQL Community Edition 8.0.27)
3. Python (3.10.1)

### Frameworks used

1. Bootstrap front-end framework (v5.0.2)
2. Flask framework (v2.0.2)

### Python libraries and 3rd party packages used

1. Flask-Bootstrap (v3.3.7.1)
2. Gunicorn (v20.1.0)
3. PyMySQL (v1.0.2)
4. WerkZeug (v1.0.1)

### External Storage used

1. Amazon Relational Database Service (RDS)

## Instructions for checking out the latest stable version

### Method 1:
1. Open the main page for our GitHub repository: https://github.com/Pingumaniac/MasterSQL
2. Click the following button: <img src = "https://user-images.githubusercontent.com/63883314/115416097-69ade280-a232-11eb-8401-8c41362ab4c2.png" width="44" height="14">
3. Click 'Download ZIP' option.
4. Unzip the folder.

### Method 2:
1.  Copy the web URL to your clipboard.
2.  Open 'Git Bash' from your local computer. You must have installed Git from the following page to do this: https://git-scm.com/downloads
3.  Move to the preferred directory.
4.  Next, type the following:
```
git clone
```
5. Then, all the codes and documents in the repository can be accessed.

Note: For Method 2, if you have already cloned the repository before, then you can skip the first two steps. And type this instead for step 4:
```
git type
```

## How to build this software

### 1. Please make sure you have downloaded MySQL (v8.0.24).

* Here is the URL for downloading the MySQL installer for Windows: https://dev.mysql.com/downloads/installer/
* Here is the URL that shows the instructions to install MySQL on macOS: https://dev.mysql.com/doc/mysql-osx-excerpt/5.7/en/osx-installation.html 

### 2. Install the following python packages using pip in the terminal:

```
pip3 install flask 
pip3 install Flask-Bootstrap
pip3 install gunicorn
pip3 install PyMySQL
pip3 install Werkzeug
```

### 3. Deployment method

#### We will use Heroku to deploy the Flask. Note that:
 1. Git must be installed since Heroku uses Git. Please install Git from this website unless you have already installed: https://git-scm.com/downloads
 2. Python must be installed to use Flask. Please install Python 3.8.10 from this website unless you have already installed: https://www.python.org/downloads/

#### To install Heroku,
 1. Open the Heroku website. Here is the link for the Heroku website: https://www.heroku.com/
 2. Sign up a Heroku account.
 3. Install Heroku command-line interface (CLI) in your Terminal by following the instructions from this website: https://devcenter.heroku.com/articles/heroku-cli
 
 #### To use Heroku for deploying our application,
1. Make sure you have already installed Flask and Gunicorn. Check "How to build software" section to refer the installation processes for each of them.
2. Refer "Instructions for checking out the latest stable version" to download all the files needed to build this software.
3. Open the terminal and move to the folder directory which contains all the files for this project.
4. Login to your Heroku account in the terminal.
  ```
 heroku login
 ```
5. Use Procfile, requirements.txt and runtime.txt given in the file.
6. Go to Heroku website again and create an application (name: mastersql).
7. Clone the repository using Git.  
 ```
 heroku git:clone -a mastersql
 ```
8. Now a folder named 'mastersql' has been created. Inside this folder put all the files needed to deploy this project. 
9. Next, move to this folder in the terminal.
 ```
 cd mastersql
 ```
10. Then, input the following in the terminal:
 ```
 heroku git:remote -a "mastersql"
 git add .
 git commit -am "type whatever you wanna say here"
 git push heroku HEAD:master
```
11. If the following steps run successfully, the website URL will be printed in the console. 
```
https://mastersql.herokuapp.com/
```

## How to test this software

* To test the software, you shall initially download the latest stable version of this software or instead visit https://mastersql.herokuapp.com/. Please refer "Instructions for checking out the latest stable version" to download the correct version.
* You can download MySQL workbench (v8.0.24) and then connect with my Amazon RDS cloud. Refer def __init__() or connectDB() methods in the class DB in masterSQLAPI.py to view information about the Amazon RDS cloud. 
* If you have decided to run the software in your local terminal, please move to the right folder and then enter the following:
```
python3 app.py
```
* Now, you can test various functionalities and non-functional requirements. 

## Bug tracking

* All users can view and report a bug in "GitHub Issues" of our repository. 
* Here is the URL for viewing and reporting a list of bugs: https://github.com/Pingumaniac/MasterSQL/issues
