# **📰 Newspaper Management System**

A Django-based web application for managing newspapers, topics, and publishers/editors.
## You can see the project on the site:
https://news-agency-pzrj.onrender.com

You can use this account:

##### username: `admin`

##### password: `s30HzR0MLs`

<br>

### **_BUT IF YOU WHANT TO START PROJECT IN_**
### _**YOUR LOCAL MACHINE FOLLOW THIS INSTRUCTIONS:**_

**1. Clone the repository and create a virtual environment:**

`git clone https://github.com/MaksVakulenko/News-agency/pull/1`

`python -m venv venv`
 
On Windows:

`venv\Scripts\activate`

On macOS/Linux:

`source venv/bin/activate`

**2. Install the required packages:**

`pip install -r requirements.txt`

**3.Migrate the database:**

   `python manage.py makemigrations`

   `python manage.py migrate`

**4. Load initial data (topics and sample content):**

   `python manage.py loaddata newspaper_db_data.json`


**5. Create a superuser (admin) account:**
   
   `python manage.py shell`
   
    from newspaper.models import Redactor
      Redactor.objects.create_user(
          username='admin',
          password='1234',
          years_of_experience=1,
      )

**6. Run the development server:**

   `python manage.py runserver`

## Features

- Manage newspapers with titles, content, and publication dates
- Create and manage topics for categorizing news
- Handle publishers/editors with experience tracking
- Search functionality for newspapers and publishers
- Date-based filtering for newspapers
- Topic-based filtering

## Project Structure

- `newspaper/` - Main application directory
- `templates/` - HTML templates
- `static/` - CSS and static files
- `News_agency/` - Project settings and configuration





##### if you want to clear the database:

`python manage.py flush`