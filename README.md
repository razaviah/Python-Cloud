# Python Cloud Project -- Mini Project

Python Cloud Project, Data Engineering Diploma Program, WeCloudData

Content developed by: WeCloudData Academy


## 1. Scenario

You are going to get the job data from an API. Please go to the API web page first (https://www.themuse.com/developers/api/v2), and take a look at the page. We need 50 pages of jobs. So, let’s go to Job, and input 50 in the “page” field, and leave other fields blank.

<p align="center">
  <img src="https://user-images.githubusercontent.com/108837052/192638584-d491199d-587c-4a90-aecb-1d3b0255ad97.jpg" alt="API_50"/>
</p>



Then, Press “Run Example Request” button.

<p align="center">
  <img src="https://user-images.githubusercontent.com/108837052/192638500-149ea416-d5aa-41ff-9942-a05c09af7556.jpg" alt="API_button"/>
</p>


You will see the JSON result. This is the result you are going to use.

<p align="center">
  <img src="https://user-images.githubusercontent.com/108837052/192638756-9bf889ee-0aba-40da-896c-988bc7fe5398.jpg" alt="API_result"/>
</p>


And in your lab you will use https://www.themuse.com/api/public/jobs?page=50 **as your API url**. Only focus on the “Response body”, be careful about the JSON nested level.


The data we need from the result is from the “Response body”. The data we need from the body are: ***publication date***, ***job name***, ***job type***, ***job location***, ***company name*** (Please find them from the body).


Then you will convert the result into a csv file, and save to S3 bucket.

## 2. Detail Steps

1. Create an EC2 Instance on AWS.
2. Build your python Project on EC2 via VSCode. (You need VSCode remotely SSH connect to EC2)
3. Use the python script to read the API (use **requests library)**

4. Get the data we want:
        - “company name”
        - “locations”,
        - “job name”,
        - “job type”,
        - “publication date”, 

5. Convert the json data into a dataframe (use pandas library)

6. Manipulate data: create a table include:
        - company_name
        - country (cut the string of “locations”, keep the country part)
        - city (cut the string of “locations”, keep the city part)
        - Job_name
        - Job_type
        - Date (cut string of “publication date” only keep date part) 

7. This is the result sample:
    Untitled

8. Save the data into S3 bucket.
    
    You have two ways in your python script to save the csv data to S3:
    1. Use boto3 and AWS credentials.
    2. Attach an IAM Role to EC2, so that your EC2 doesn't need credentials and boto3 to upload csv files. All you need to do is save the csv to your local EC2 and use aws cli (aws s3 cp ….)to upload the file to S3. The way to set IAM Role in EC2 as below:

<p align="center">
  <img src="https://user-images.githubusercontent.com/108837052/192640061-d090482b-d5bf-4328-aaf4-567a0ef65f45.jpg" alt="EC2_ADD_ROLE"/>
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/108837052/192640170-d092a16d-269c-4c9b-8831-463ffaac3cff.jpg" alt="ROLE"/>
</p>




## 3. Requirements

In the project (one-off project), the files include:

- A shell script to set your virtual environment
- .gitignore file
- A python run script
- A toml file if you need to config parameters
- A separate file to save your secrets
- Better to initiate your project environment with a shell script.
- Better to use a shell script to control the python script. 


## 4. Diagram

The project diagram is as below:

<p align="center">
  <img src="https://user-images.githubusercontent.com/108837052/192905682-28b6f3b9-0dee-4782-8902-a0a1e4efcf4c.png" alt="Python_project_1_lab_1"/>
</p>
