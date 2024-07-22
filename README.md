<h1 align="center"><strong>🏳️‍🌈🏳️‍🌈🏳️‍🌈 Proud Coders: July 2024 Hackathon 🏳️‍🌈🏳️‍🌈🏳️‍🌈</strong>

</h1>

<img src="https://res.cloudinary.com/djdefbnij/image/upload/v1718956326/Untitled_design_1_rlpfyv.png" alt="Proud Coders Banner" width="1200"/>

## Table of Contents
  * [Deployment](#deployment)
    + [Create a Heroku App:](#create-a-heroku-app-)
    + [Prepare the environment and settings.py file:](#prepare-the-environment-and-settingspy-file-)
    + [Create files & directories](#create-files---directories)
    + [Update Heroku Config Vars -- JOSIP CAN YOU LOOK AT THIS?](#update-heroku-config-vars----josip-can-you-look-at-this-)
    + [Deploy](#deploy)
  * [Criteria](#criteria)
- [SUBMISSION](#submission)
  * [Introduction](#introduction)
  * [Goal](#goal)
  * [Tech](#tech)
  * [Resources Used](#resources-used)
    + [Acknowledgements -- EVERYONE PLEASE ADD / CHANGE WHAT YOU WANT](#acknowledgements----everyone-please-add---change-what-you-want)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>



# Deployment
Take a look at the live site [here](https://chronicles-of-pride-9a12d37ba4db.herokuapp.com/).

The following steps were taken to deploy the live website to Heroku from the GitHub repository:

### Create a Heroku App:
- Log into your [Heroku](https://dashboard.heroku.com/apps) account or create an account.
- On the main page click the 'New' button at the top right corner and select 'Create New App' from the dropdown menu. 
![Heroku Create App](/documentation/readme_images/heroku-create-new.png)
- Enter in a unique app name
- Select your region
- Click 'Create App'
![Heroku New App](/documentation/readme_images/heroku-create-app.png)

### Prepare the environment and settings.py file:
- In your workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file. 
- Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
- Comment out the default database configuration.
- Save all files and make migrations.
- Add the Cloudinary URL to env.py
- Add the Cloudinary libraries to the list of installed apps.
- Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
- Link the file to the templates directory in Heroku.
- Change the templates directory to TEMPLATES_DIR
- Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

### Create files & directories
- Create a requirements.txt file
- Create directories in the main directory, eg: static, templates.
- Create a "Procfile" in the main directory and add the following: web: gunicorn project_name.wsgi
- Make sure the Procfile is capitalized and only has one line.

### Update Heroku Config Vars -- JOSIP CAN YOU LOOK AT THIS?
Add the following Config Vars in Heroku:
- SECRET_KEY value 
- CLOUDINARY_URL
- PORT = 8000
- DISABLE_COLLECTSTATIC = 1
- DATABASE_URL value

### Deploy
- Make sure DEBUG = False in settings.py
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need to be re-deployed each time the GitHub repository is updated.
- Click 'Open App' to view the deployed site live.

# Criteria

In this section, we will briefly discuss how our team addressed the following applicable criteria:

<details>
<summary>🏳️‍🌈 <strong>Impact on the LGBTQIA+ community</strong></summary>
Many of the challenges faced by the LGBTQIA+ community are misunderstood, which this platform tries to remedy. Our goal is to educate users about the community's history, pivotal milestones and important trailblazers while providing a safe space for people to communicate with others.
<br>
<br>
</details>

<details>
<summary>🏳️‍🌈 <strong>Realistic and real-world value</strong></summary>
The basis of the platform lies in the history of the LGBTQIA+ community, which is outlined on the history page with a timeline. The website enriches society through education and sharing stories and experiences that bring users together, both within and outside the LGBTQIA+ community.
<br>
<br>
</details>
   
<details>
<summary>🏳️‍🌈 <strong>Excellent design and layout</strong></summary>
Our team's goal was to stay close to the different flags the LGBTQIA+ community has waved over the years, some of which are still in use today. Responsiveness was a top priority in our design an layout and attempted to make all pages compatible on various devices.
<br>
<br>
</details>

<details>
<summary>🏳️‍🌈 <strong>Professional presentation to the judging panel - EDIT!!</strong></summary>
TBD
<br>
<br>
</details>

<details>
<summary>🏳️‍🌈 <strong>Demonstrates innovation and creativity -- LOOK AT 'BENCHED' FEATURES</strong></summary>
<br>
Current features:
<ul>
<li>Interactive timeline (with clickable entries)</li>
<li>Interactive blog posts</li>
<li>Easy access on both desktop and mobile devices</li>
<li>[benched] Help section for community members in need</li>
<li>[benched] List of important media found online</li>
<li>[benched] Showcase of relevant current and recent news articles</li>
</ul>
</details>
<br>

# Submission

## Introduction

Prideful Pixels unveils Chronicals of Pride, a walk through history of the LGBTQIA+ movement and a platform to bring people together within the community as well as those outside it. Chronicals of Pride is an educational platform that showcases more than a century of the important milestones for the LGBTQIA+ community.<br>
<br>
The interactive timeline provides a journey through the community's history enabling visitors to follow the development of the movement from the past decades to today. Users can access the blog section to share personal stories, support and comments, while the flashcards can answer pertinent questions inquiring minds might have. Site visitors can contact Prideful Pixels and share their own story or questions by submitting a contact form, anonymously if they so choose, to the admin team.

## Goal

The main objective of Chronicals of Pride is to be a safe space for users in the LGBTQIA+ community and outside of it to learn some of the history and important events and people of the movement in a safe environment. The Prideful Pixels team strived to provide a concise understanding of this month's hackathon theme by addressing the following aspects:
<br>
<details>
<summary>➡️ Problem Statement</summary>
Being misunderstood is can be one of the main challenges for individuals in the LGBTQIA+ community and for the community as a whole. At times, this can be a product of misinformation or lack thereof. Our goal as the Prideful Pixels team was to bridge this knowledge gap and foster interaction among people within and outside of the LGBTQIA+ community.
</details>
<br>

<details>
<summary>➡️ Objectives</summary>
  <ul>
  <li>Responsiveness (easy accessibility on desktop and mobile devices)</li>
  <li>Provide relevant information</li>
  <li>Ensure an interactive, fun environment</li>
  <li>Enable visitors to interact</li>
  </ul>
</details>
<br>

<details>
<summary>➡️ Target Audience</summary>
On one hand, Chronicles of Pride was designed to target a 'cold audience' who might not have much knowledge of LGBTQIA+ history but who are open to learning. Similarly, the site provides a platform for people in the LGBTQIA+ community to share their experiences and help educate others.
</details>
<br>

<details>
<summary>➡️ Benefits</summary>
Chronicles of Pride shares an easy, accessable way to learn about the history of the LGBTQIA+ community, as well as fun facts about flags and noted trailblazers. Users can interact with people in their community in a low-key atmosphere, thus helping break any boundaries that may exist.
</details>

## Tech

The tech section provides information regarding the technology stack, dependencies, and other technical details related to the project and used in the implementation of the Chronicals of Pride website.

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

### Acknowledgements -- EVERYONE PLEASE ADD / CHANGE WHAT YOU WANT
Firstly, we would like to acknowledge XXXXX <strong>(Kiree, your contact / people you have personal stories from?)</strong> for their willingness to share their story as a LGBTQIA+ individual. By showcasing stories like these, we hope Chronicles of Pride can facilitate understanding, foster interpersonal compassion and quell misinformation and hatred in the media. 

Special mention is also deserved by our team as a whole; each of us was integral in bringing Chronicles of Pride to fruition. We learned a lot from each other, dove headfirst into new technologies and were helpful in times of need resolving coding issues.

