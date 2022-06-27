
# LinkedIn-Webscrapper

LinkedIn Webscrapper for Jobs and Candidate profile.

## About Project

LinkedIn Webscrapper is part of Hiring Vista project developed at AUR Consultants. The programs scrape data from LinkedIn and export them to CSV sheet.

## Requirements

1. Python 3.9.7
2. Selenium
3. webdriver_manager
4. Pandas
5. Time

## Program Flow

1. _For Jobs Profiles_

    a. Login to Linkedin.

    b. Redirecting to Jobs page.

    c. Search using Job or Location or Both.

    d. Apply any filters required.

    e. Program scraps Position, Company name, Location, Details and Apply link.

    f. All scrapped details exported to CSV.

2. _For Candidate Profile_

    a. Login to Linkedin

    b. Redirecting to Candidate's profile.

    c. Program scraps Name, Current Designation, Current Location, About, Education, Experiences, Skills.

    d. All scrapped details exported to CSV.

## How to Use

1. Clone Repository to local machine.

2. Open JD_WS (For Jobs Scrapping)/Candidate_WS (For Candidate Profile scrapping) folder in your local terminal (CMD) or in VS Code terminal.

3. Run main.py file in either directory with command ```python main.py```.

4. The program will ask for Email ID and password to Login or the details can be edited in the program accordingly.

5. The Job Title, Location, Candidate Profile link and any filter to be appiled can be edited in the program's files.

6. After scrapping is done the output is exported to CSV which can be later viewed or used by the user.
