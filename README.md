<h1 align="center"><strong>🏳️‍🌈🏳️‍🌈🏳️‍🌈 Proud Coders: July 2024 Hackathon 🏳️‍🌈🏳️‍🌈🏳️‍🌈</strong>

</h1>

<img src="https://res.cloudinary.com/djdefbnij/image/upload/v1718956326/Untitled_design_1_rlpfyv.png" alt="Proud Coders Banner" width="1200"/>

## Table of Contents
- [Deployment](#deployment)
  * [ElephantSQL Database](#elephantsql-database)
  * [Cloudinary API](#cloudinary-api)
  * [Heroku](#heroku)
    + [Create a Heroku App:](#create-a-heroku-app-)
    + [Prepare the environment and settings.py file:](#prepare-the-environment-and-settingspy-file-)
    + [Create files & directories](#create-files---directories)
    + [Update Heroku Config Vars](#update-heroku-config-vars)
    + [Deploy](#deploy)
- [Criteria](#criteria)
- [Submission](#submission)
  * [Introduction](#introduction)
  * [Goal](#goal)
  * [Tech](#tech)
  * [Resources Used](#resources-used)
    + [Acknowledgements -- EVERYONE PLEASE ADD / CHANGE WHAT YOU WANT](#acknowledgements----everyone-please-add---change-what-you-want)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


# Deployment
Take a look at the live site [here](https://chronicles-of-pride-9a12d37ba4db.herokuapp.com/).

## ElephantSQL Database

The project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

- Click **Create New Instance** to start a new database and choose a name.
- Select the **(Free)** plan, **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

## Cloudinary API

The project uses the [Cloudinary API](https://cloudinary.com) to store media assets online.

To obtain your own Cloudinary API key, create an account and log in.

- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

## Heroku

### Create a Heroku App:

- Log into your [Heroku](https://dashboard.heroku.com/apps) account or create an account.
- On the main page click the **New** button at the top right corner and select **Create New App** from the dropdown menu. 
![Heroku Create App](/documentation/readme_images/heroku-create-new.png)
- Enter in a unique app name.
- Select your region.
- Click **Create App**.
![Heroku New App](/documentation/readme_images/heroku-create-app.png)

### Prepare the environment and settings.py file:
- In your workspace, create an `env.py` file in the main directory. 
- You should add following to the file:

```python
import os

os.environ['CLOUDINARY_CLOUD_NAME'] = '<your-cloudinary-cloud-name>'
os.environ['CLOUDINARY_API_KEY'] = '<your-cloudinary-api-key>'
os.environ['CLOUDINARY_API_SECRET'] = '<your-cloudinary-api-secret>'
os.environ['SECRET_KEY'] = '<your-secret-key>'
os.environ['ALLOWED_HOST'] = '<your-localhost-address>'
os.environ['DATABASE_URL'] = "<your-elephantsql-database-url-or-alternative>"
```

- Make sure the `settings.py` file has `env.py` imported.
- Comment out the default database configuration.
- Save all files and make migrations.
- Add the Cloudinary libraries to the list of installed apps.
- Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
- Link the file to the templates directory in Heroku.
- Change the templates directory to `TEMPLATES_DIR`.
- Add Heroku to the `ALLOWED_HOSTS` list the format ['app_name.heroku.com', 'localhost']

### Create files & directories
- Create a `requirements.txt` file using command:
```python
pip3 freeze > requirements.txt
```
or
```python
pip freeze > requirements.txt
```
- Create directories in the main directory, eg: static, templates.
- Create a **Procfile** in the main directory and add the following: web: gunicorn project_name.wsgi
- Make sure the Procfile is capitalized and only has one line.

### Update Heroku Config Vars
Add the following Config Vars in Heroku:
- SECRET_KEY: value
- DATABASE_URL: value
- CLOUDINARY_URL: value

### Deploy
- Make sure `DEBUG = False` in `settings.py`
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need to be re-deployed each time the GitHub repository is updated.
- Click **Open App** to view the deployed site live.

# Criteria

In this section, we will briefly discuss how our team addressed the following applicable criteria:

<details>
<summary>🏳️‍🌈 <strong>Impact on the LGBTQIA+ community</strong></summary>
Many of the members of the LGBTQIA+ community are often misunderstood and alienated from the general community. This often results in daily struggles and challenges. This platform tries to support our members throughout said journey. Our goal is to educate users about the community's history, pivotal milestones and important trailblazers while providing a safe space for people to communicate with others.
<br>
<br>
</details>

<details>
<summary>🏳️‍🌈 <strong>Realistic and real-world value</strong></summary>
The basis of the platform lies in the history of the LGBTQIA+ community, which is outlined in the history section. The website enriches society through education (Cards, News, Blog) and sharing stories (anonymous mode is available!) and experiences that bring users together, both within and outside the LGBTQIA+ community. At the same time, we offer an extensive list of helpful resources.
<br>
<br>
</details>
   
<details>
<summary>🏳️‍🌈 <strong>Excellent design and layout</strong></summary>
Responsiveness was a top priority in our design an layout as attempted to make all pages compatible on various devices. Our team's goal was to stay close to the different flags the LGBTQIA+ community has waved over the years, most of which are still in use today.
<br>
<br>
</details>

<details>
<summary>🏳️‍🌈 <strong>Professional presentation to the judging panel</strong></summary>
Video presentation.
<br>
<br>
</details>

<details>
<summary>🏳️‍🌈 <strong>Demonstrates innovation and creativity</strong></summary>
We have created a historic timeine for our newer members to learn about their own roots. To also add a bit of freshness, our website gathers the latest news from the community for the ease of access. 
<br>
Current features:
<ul>
<li>Interactive timeline</li>
<li>Interactive blog posts with comments</li>
<li>Easy access on both desktop and mobile devices</li>
<li>Interactive flash cards designed to educate</li>
<li>Contact form which allows anonymous outreach</li>
<li>[originally benched] Help section for community members in need</li>
<li>[benched] List of important media found online</li>
<li>[originally benched] Showcase of relevant current and recent news articles</li>
<li>Interactive team page</li>
</ul>
</details>
<br>

# Submission

## Introduction

Prideful Pixels unveils Chronicals of Pride, a walk through history of the LGBTQIA+ movement and a platform to bring people from the community as well as those outside it together. Chronicals of Pride is primarily educational platform that showcases more than a century of the important milestones for the LGBTQIA+ community.<br>
<br>
The interactive timeline provides a journey through the community's history enabling visitors to follow the development of the movement from the past decades to today. Users can access the blog section to share personal stories, support and comments, while the flashcards can answer pertinent questions inquiring minds might have. Site visitors can contact Prideful Pixels and share their own story or questions by submitting a contact form, anonymously if they so choose, to the admin team. At the same time, we make the latest global news regarding the community easily available.

## Goal

The main objective of Chronicals of Pride is to create a safe and supporting space for users in the LGBTQIA+ community. For those outside of it, we've created an interactive learning experience focused on the general history, important events and people of the movement. The Prideful Pixels team strived to provide a concise understanding of this month's hackathon theme by addressing the following aspects:
<br>
<details>
<summary>➡️ Problem Statement</summary>
Being misunderstood can be one of the main challenges for individuals in the LGBTQIA+ community and for the community as a whole. At times, this can be a product of misinformation or lack thereof. Our goal as the Prideful Pixels team was to bridge this knowledge gap and foster interaction among people within and outside of the LGBTQIA+ community.
</details>
<br>

<details>
<summary>➡️ Objectives</summary>
  <ul>
  <li>Responsiveness (easy accessibility on desktop and mobile devices)</li>
  <li>Provide relevant information and resources</li>
  <li>Ensure an interactive, fun environment</li>
  <li>Enable visitors to interact</li>
  </ul>
</details>
<br>

<details>
<summary>➡️ Target Audience</summary>
On one hand, Chronicles of Pride was designed to target a 'cold audience' who might not have much knowledge of LGBTQIA+ history but who are open to learning. Similarly, the site provides a platform for people in the LGBTQIA+ community to share their experiences and help educate others. Our target audience is a questioning teenager as much as a flamboyant retiree, a couple, a shut-in, person in Sweden wishing to share their story, a man in Central Europe who narrowly escaped an attack for being himself just days ago, a person not yet ready to label themselves, a lion, scarecrow and, finally, a tinman. 
</details>
<br>

<details>
<summary>➡️ Benefits</summary>
Chronicles of Pride shares an easy, accessable way to learn about the history of the LGBTQIA+ community, as well as fun facts about flags and noted trailblazers. Users can interact with people in their community in a low-key atmosphere, thus helping break any boundaries that may exist.
</details>

## Tech

The tech section provides information regarding the technology stack, dependencies, and other technical details related to the project and used in the implementation of the Chronicals of Pride website.

| Source | Notes |
| --- | --- |
| [Source name](https://www.google.com/) | What did it do |
| [ElephantSQL](https://www.elephantsql.com) | Used as the Postgres database |
| [Heroku](https://dashboard.heroku.com) | Used for deployment |
| [Cloudinary](https://cloudinary.com) | Used for media storage |




## Resources Used

| Source | Location | Notes |
| --- | --- | --- |
| [Source name](https://www.google.com/) | Where was it used | What did it do |
| [Human Rights Campaign](https://www.hrc.org/resources/lgbtq-pride-flags) | Rainbow cards | Provided flag info and context |
| [Django](https://docs.djangoproject.com/en/4.2/topics/db/models/) | Models | Created models |
| [Mailtrap.io](https://mailtrap.io/) | Contact form | Linked  contact form to receive emails |
| [YouTube](https://www.youtube.com/watch?v=dnhEnF7_RyM) | Contact form | Tutorial to troubleshoot contact form functionality |
| [Cloudconvert](https://cloudconvert.com/avif-to-jpg) | LGBTQIA+ flags | Converted images from AVIF to JPG |
| [SVG to PNG](https://svgtopng.com/) | Across website | Converted images from SVG to PNG |
| [JPG to PNG](https://jpg2png.com/) | Across website| Converted images from JPG to PNG |
| [TinyJPG](https://tinyjpg.com/) | Across website | Surpressed images |
| [Font Awesome](https://fontawesome.com/) | Across website | Inspiration for icons |
| [Voda](https://www.voda.co/) | Some of our favourite people | Support page |
| [Queer Chameleon](https://www.youtube.com/@queeeerchameleon) | Some of our favourite people | Support page |
| [Bicycle Adventure Club](https://bicycleadventureclub.co.uk/) | Some of our favourite people | Support page |
| [Fandom](https://lgbtqia.fandom.com/wiki/LGBTQIA%2B_Wiki) | History | Provided main events |
| [Fonts Google](https://fonts.google.com/ ) | A website | Font selection |
| [Coolors](https://coolors.co/) | Across website | Colour palette selection |
| [PFLAG](https://pflag.org/intlfamilygroups/) | Contact page | Help section |
| [PFLAG](https://freefrontend.com/css-timelines/) | History Page | Histoy Timeline section |

### Acknowledgements -- EVERYONE PLEASE ADD / CHANGE WHAT YOU WANT
Firstly, we would like to acknowledge XXXXX <strong>(Kiree, your contact / people you have personal stories from?)</strong> for their willingness to share their story as a LGBTQIA+ individual. By showcasing stories like these, we hope Chronicles of Pride can facilitate understanding, foster interpersonal compassion and quell misinformation and hatred in the media. 

Special mention is also deserved by our team as a whole; each of us was integral in bringing Chronicles of Pride to fruition. We learned a lot from each other, dove headfirst into new technologies and were helpful in times of need resolving coding issues.


We would like to acknowledge three amazing groups of people that have permitted us to link their sites, each of them has a direct link to the LGBTQIA+ community and we thank them for their permission:

* [Bicycle Adventure Club](https://bicycleadventureclub.co.uk/) - An LGBTQIA+ led bike club and Community Interest Company based in Birmingham, UK, with members around the world.

* [Queer Chameleon](https://www.youtube.com/@queeeerchameleon) -  Youtube channel with lots of interesting facts and information about the queer community.

* [Voda](https://www.voda.co/blog) - An amazing app made by the queer community for the queer community to support the mental mental health of members of the LGBTQIA+ community.
