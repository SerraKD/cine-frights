# ***Cine-Frights***

- **Description :** **Cine Frights** Is a horror movie review blog created for Portfolio Project 4. This website includes the latest horror movies with various popular movie pages ratings, website's ratings, a chance to create a user account, comment on movies to share users' opinions, join to website newsletter, and recommend a movie to be featured on the website.
- **Project goal :** To create a platform for horror movie lovers to review the latest horror movies, and engage with other users by commenting and sharing opinions about movies.
- **Audience :**  The target audience is adults who like horror movies and are in search of new movie recommendations.
- **Live website :** [https://cine-frights-ed31240ece67.herokuapp.com/](https://cine-frights-ed31240ece67.herokuapp.com/)
- **Github Page :** [https://github.com/SerraKD/cine-frights](https://github.com/SerraKD/cine-frights)
- **Github Projects :**[https://github.com/users/SerraKD/projects/4](https://github.com/users/SerraKD/projects/4)

![Mockup Image](/docs/design/amiresponsive-img.png)

---

## **User Experience (UX)**

### **Site Goals**

The goal of the Cine-Frights site is to attract users who like horror movies and are on the lookout for what to watch next. Even though there are multiple platforms for movie reviews, this site focuses on one genre that is quite popular and not much shown.

- Easy to navigate, user-friendly website structure.
- Design that suits to horror theme.
- A place to let users share their opinions about movies.
- A place where users can find multiple ratings regarding movie posts.
- Option the read movie summary, genre and release that all in one page.
- A place where users can interact further by recommending a movie to the site to be featured.
- A newsletter option that keeps users updated about the newest horror flicks.

### **Target Audiance**

The target audience is users looking for new horror movies, seeing multiple ratings on one platform, seeing other people's opinions about the movies, and sharing their opinions in one place. 

- Individuals who are interested in horror movies.
- Individuals who are looking for a new movie to watch.
- Individuals who want to share their opinion about the latest horror movie they watched.
- Individuals who are interested in other like-minded individuals' opinions about horror movies.

### **Epics**

As the site developer, I used Epics as the main frame to build the site and keep the work ordered.

![Kanban Board image](docs/design/kanban-board.png)

- **[Epic 1. Create the project & Set up the Environment](https://github.com/users/SerraKD/projects/4/views/1?pane=issue&itemId=71533834) <kbd>[Must Have](https://github.com/SerraKD/cine-frights/labels/Must%20Have)</kbd>** &check;
> Epic Description : Set up the project repository and manage the Heroku deployment.

- **[Epic 2. Create Database & Models](https://github.com/users/SerraKD/projects/4/views/1?pane=issue&itemId=71536163) <kbd>[Must Have](https://github.com/SerraKD/cine-frights/labels/Must%20Have)</kbd>** &check;
> Epic Description : configure database, manage environment variables, create models.

- **[Epic 3. Admin Panel & Functions](https://github.com/users/SerraKD/projects/4/views/1?pane=issue&itemId=71563124) <kbd>[Must Have](https://github.com/SerraKD/cine-frights/labels/Must%20Have)</kbd>** &check;
> Epic Description : Site admins competence & tasks.

- **[Epic 4. Validation & Testing](https://github.com/users/SerraKD/projects/4/views/1?pane=issue&itemId=71564008) <kbd>[Must Have](https://github.com/SerraKD/cine-frights/labels/Must%20Have)</kbd>** &check;
> Epic Description : All testing and validation required for the project.

- **[Epic 5. Automated testing with Django](https://github.com/users/SerraKD/projects/4/views/1?pane=issue&itemId=71564953) <kbd>[Could Have](https://github.com/SerraKD/cine-frights/labels/Could%20Have)</kbd>**
> Epic Description: Automated testing to check projects functionality.


### **User stories**

I created 12 user stories with MoSCoW prioritization technique. Every user story includes the acceptance criteria.

- **[1.User Story: User Account registration](https://github.com/SerraKD/cine-frights/issues/3) <kbd>[Must Have](https://github.com/SerraKD/cine-frights/labels/Must%20Have)</kbd>**  &check;

> As a site user I can create an account so that i can use the site as logged in user .

> Acceptance Criteria
> 1. With a username & password user can register an account.
> 2. After creation user can log in.
> 3. Logged in user can view and create a comment.

- **[2.User Story: User Login](https://github.com/SerraKD/cine-frights/issues/4) <kbd>[Must Have](https://github.com/SerraKD/cine-frights/labels/Must%20Have)</kbd>** &check;

> As a site user I can login into my account so that i can write a comment on a movie post and suggest movies to the site.

> Acceptance Criteria
> 1. I can log in into account using my user name and password with log in link.

- **[3.User Story: View the details of movie posts](https://github.com/SerraKD/cine-frights/issues/5) <kbd>[Must Have](https://github.com/SerraKD/cine-frights/labels/Must%20Have)</kbd>** &check;

> As a Site User, I can click on a post so that I can read the movie details, view ratings and comments.

> Acceptance Criteria
> 1. When a movie post title is clicked on movie name, info, ratings and user comment is seen.

- **[4.User Story: Log out](https://github.com/SerraKD/cine-frights/issues/6) <kbd>[Must Have](https://github.com/SerraKD/cine-frights/labels/Must%20Have)</kbd>**  &check;

> As a site user I can log out of my account.

> Acceptance Criteria
> 1. Any logged in user has the functionality to log out.

- **[5.User Story: Comment on a movie post](https://github.com/SerraKD/cine-frights/issues/7) <kbd>[Must Have](https://github.com/SerraKD/cine-frights/labels/Must%20Have)</kbd>** &check;

> As a site user I can write comments so that i can engage with other users and share my opinion about movies.

> Acceptance Criteria
> 1. Comments has to be approved my admin before other users view.
> 2. Users can read, update and delete their comments.

- **[6.User Story: Change or delete a comment](https://github.com/SerraKD/cine-frights/issues/9) <kbd>[Must Have](https://github.com/SerraKD/cine-frights/labels/Must%20Have)</kbd>** &check;

> As a Site User I can change or delete my comment on a movie post.

> Acceptance Criteria
> 1. A logged in user can change &/or delete their comment.

- **[7.User Story: View all Movie posts](https://github.com/SerraKD/cine-frights/issues/10) <kbd>[Must Have](https://github.com/SerraKD/cine-frights/labels/Must%20Have)</kbd>** &check;

>  As a site user I can view all movies so that i can choose which movie post i want to see more detailed.

> Acceptance Criteria
> 1. All movie posts should be listed with their poster.
> 2. When a user opens movies page all posts can be seen.
> 3. Page pagination required if there is multiple posts. 

- **[8.User Story: Search Movies](https://github.com/SerraKD/cine-frights/issues/11) <kbd>[Could Have](https://github.com/SerraKD/cine-frights/labels/Could%20Have)</kbd>** &cross;

> As a site user i can search movie names so that i can find specific movie post i am interested in.

> Acceptance Criteria
> 1. Search bar should be at the top of the home page. 

- **[9.User Story: Delete user account](https://github.com/SerraKD/cine-frights/issues/12) <kbd>[Could Have](https://github.com/SerraKD/cine-frights/labels/Could%20Have)</kbd>** &cross;

> As a user I can delete my account if i want to.

> Acceptance Criteria
> 1. When i go to my account page i can delete my account. https://github.com/SerraKD/cine-frights/labels/Should%20Have

- **[10.User Story: View Recommended movies](https://github.com/SerraKD/cine-frights/issues/13) <kbd>[Should Have](https://github.com/SerraKD/cine-frights/labels/Should%20Have)</kbd>** &check;

> As a site user I can view recommended movies on a slide at the home page.

> Acceptance Criteria
> 1. The slides must include movie posters and names.
> 2. When clicked on, the slide picture should take user to the linked movie post.

- **[11.User Story: Recommend a movie](https://github.com/SerraKD/cine-frights/issues/14) <kbd>[Could Have](https://github.com/SerraKD/cine-frights/labels/Could%20Have)</kbd>** &check;

> As a logged in user i would like to recommend a movie to the site admin for it to be featured.

> Acceptance Criteria
> 1. Logged in users can fill out a form to recommend a movie.

- **[12.User Story: Subscribe to Newsletter](https://github.com/SerraKD/cine-frights/issues/28) <kbd>[Could Have](https://github.com/SerraKD/cine-frights/labels/Could%20Have)</kbd>** &check;

> As a user, I can subscribe to the newsletter to stay updated about the newest movies.

> Acceptance Criteria
> 1. I can subscribe to the newsletter easily as a logged in user by providing my email address.
> 2. A confirmation message is shown if the subscription is completed successfully.

---
> **[Kanban Board @SerraKD's PP4 Cine-Frights](https://github.com/users/SerraKD/projects/4/views/1)**
---

## **Design**

### **Colour Scheme**

 I kept the color scheme minimalistic and fitting to the horror theme of the site. I realized that many horror movie posters use these colors.

![Color scheme image](docs/design/color-scheme.png)

### **Typography**

I selected Pathway Gothic One and Bebas Neue fonts from Google fonts. The dramatic feel of Bebas Neue font fits the site headings and movie titles perfectly.

![Fonts image](docs/design/fonts-image.png)

### **Wire-frames**

In the planning stage, I used Balsamiq wireframes to create the basic layout of the website. Views of the pages change depending on if the user is signed in. The final design evolved more to fit to horror theme.

| Page  | Wireframe |
| :----: | :----: |
| Home | ![Home Page wireframe image](docs/wireframes/home-wireframe.png) |
| Home Signed in | ![Home Page signed in user wireframe image](docs/wireframes/signedin-home-wireframe.png) |
| Films | ![Films Page wireframe image](docs/wireframes/films-wireframe.png) |
| Films Signed in | ![Films Page signed in user wireframe image](docs/wireframes/signedin-films-wireframe.png) |
| Movie Detail | ![Movie Detail Page wireframe image](docs/wireframes/movie-detail-wireframe.png) |
| Movie Detail Signed in | ![Movie Detail signed in user wireframe image](docs/wireframes/signedin-movie-detail-wireframe.png) |
| Sign In | ![Sign In Page wireframe image](docs/wireframes/sign-wireframe.png) |
| Login | ![Login Page wireframe image](docs/wireframes/login-wireframe.png) |

## **Features**

## **Validation, Testing & Bugs**

I documented validation, testing, and bugs in all separate files. Links to the relative files are located below.

### **Validation**

> **[VALIDATION.md](/docs/VALIDATION.md)**

### **Testing**

> **[TESTING.md](/docs/TESTING.md)**

### **Bugs**

> **[BUGS.md](/docs/BUGS.md)**

## **Deployment**

### **CI Database Maker**

- Input your email to [CI Database Maker](https://dbs.ci-dbs.net/)
- Go to your email and open the latest mail you recieved from Code Institute.
- Click on the on the provided link to manage databases. 
- Copy database URL provided you in selected database **info**.
- Update your settings.py in your project directory.

### **Cloudinary**

- Go to [Cloudinary](https://console.cloudinary.com/) and register a new account.
- Login to Cloudinary with your account credentials.
- Navigate to Add a new environment.
- Confirm your selection.
- In your dashboard,under Product Environment, click on Go to API Keys.
- Copy Cloudinary URL in format **cloudinary://<your_api_key>:<your_api_secret>**
- Update settings.py in the your project directory.

### **Environment & Settings**

- In your IDE open your env.py file or create one in the main directory if it hasn't been created.
- Add the DATABASE_URL value and a SECRET_KEY value to the env.py file.
- Open the settings.py file and import the env.py file and the DATABASE_URL and SECRETKEY file paths.
- Install Django and add to requirements.txt.
- Create your project.
- Add the STATIC files settings.
- Create a file called **Procfile** in the main directory,
- Add Cloudinary URL to env.py for cloud-based image storage.
- Add Cloudinary to INSTALLED APPS.
- Add your IDE workspace and Heroku to ALLOWED_HOSTS.
- Make migrations and migrate.
- Before you add, commit & push your files to GitHub, ensure **DEBUG** is set to **False** in your settings.py file.

### **Deploying to Heroku**

- Log in or create an account on Heroku.com. Click 'New' and then 'Create New App'.
- Give your project a unique name, select a region, and click 'Create App'.
- Connect your Heroku project to your GitHub repository. Under deployment, you can choose GitHub, select the appropriate one, and - select 'Connect'.
- When you are connected, go to the Settings tab and click on 'Reveal Config Vars'. Add the environment key & value variables used in your env.py file **(CLOUDINARY_URL, DATABASE_URL & SECRET_KEY)**.
- Next, add **'DISABLE_COLLECTSTATIC'** and add '1' if this is for disabling to prevent errors, or 0 if the app is in a state where errors will not be generated.
- Click on Buildpack further down and click Add Buildpack.
- Go to the Deploy section, click on Github for the deployment method, and confirm.
- Search for your repository name and click connect.
- At the bottom of the deploy section, make sure you are connected to the main branch and then click Deploy Branch.
- Now you can view your live site.

## **Local Deployment**

**Fork**:

1. Log in to Github and go to projects' repository.
2. On the top right side of the page, click on _fork_ button.

**Clone**:

1. Log in to Github and go to projects' repository.
2. On the top of the file lists, click on _Code_ button.
3. Whether you want to use HTTPS, SSH key or Github CLI select it, and then click on copy.
4. Open the terminal, type **git clone** and paste the URL copied.
5. Press enter and local clone is now created.

## **Technologies & Frameworks**

### **Main Technologies**

- HTML - templates language of the project 
- CSS - styling of the project with external CSS file
- Python - BackEnd programming language of the project
- JavaScript - for functionality.

### **Frameworks, Libraries & Programs Used**

- [Django](https://docs.djangoproject.com/) Python based framework for backend development.
- [Bootstrap v.5.2.3](https://getbootstrap.com/docs/5.2/) styling framework used for the project.
- [CI Database Maker](https://dbs.ci-dbs.net/)  Postgres database to store data.
- [Cloudinary](https://console.cloudinary.com/) - used to store static files.
- [Heroku](https://id.heroku.com/login)  to deploy the project.
- [GitHub](https://github.com/)  for version control and kanban board.
- [Gitpod](https://www.gitpod.io/)  cloud IDE to deploy workspace environment to Github.
- [Google Fonts](https://fonts.google.com/) to import fonts used on the site.
- [Balsamiq](https://balsamiq.com/) to create Wireframes.
- [V3C HTML](https://validator.w3.org/) used for HTML validator testing.
- [V3C CSS](https://jigsaw.w3.org/css-validator/) used for CSS validator testing.
- [JShint](https://jshint.com/) used for JavaScript testing.
- [CI Python Linter](https://pep8ci.herokuapp.com/) used for Python validator testing.
- [Dev Tools](https://developer.chrome.com/docs/devtools/) used throughout the project for testing, troubleshooting, and styling.
- [Grammarly](https://app.grammarly.com/) To check the grammar of all text content.

## **Credits**

- [favicon](https://favicon.io/) for site logo
- [Am I responsive?](https://ui.dev/amiresponsive) for responsive mockup.
- [Adobe Color Wheel](https://color.adobe.com/) for color scheme
- Code Institute Slack Channel
- Code Institute Tutor Support
- Markdown labels [https://github.com/isaacs/github/issues/305](https://github.com/isaacs/github/issues/305#issuecomment-308790044)

 > **Below documents and sites were used as study and reference material.**

 - https://docs.djangoproject.com/en/4.2/ref/models/fields/#model-field-types
 - https://developer.mozilla.org/en-US/docs/Learn/Forms/Sending_and_retrieving_form_data
 - https://getbootstrap.com/docs/5.2/layout/utilities/
 - https://getbootstrap.com/docs/5.2/examples/grid/#containers
 - https://stackoverflow.com/questions/53594745/what-is-the-use-of-cleaned-data-in-django
 - [CI I Think Therefore I Blog](https://learn.codeinstitute.net/) walkthrough project to help and assist with setup and coding.

### **Image Credits**

- [default image | Photo by Dmitry Demidov: https://www.pexels.com/photo/bobbin-on-heap-of-film-3921045/s](https://www.pexels.com/photo/bobbin-on-heap-of-film-3921045/)

<details>
<summary>
Click to View movie poster credits
</summary>

- https://images.app.goo.gl/syrCJZXRvUD3TkE7A
- https://images.app.goo.gl/U3ryWUDco1Y6iZys6
- https://images.app.goo.gl/RwXNJaPHtyfkWV1r7
- https://images.app.goo.gl/8GFH9YTMELj1xC4e9
- https://www.filmweb.pl/film/Terrifier-2011-692670/posters
- https://images.app.goo.gl/CYuQGkvnK7sPfxoy7
- https://www.imdb.com/title/tt4972582/mediaviewer/rm1913600000/?ref_=tt_ov_i
- https://images.app.goo.gl/g9Xqhd124AHAqhYK9
- https://images.app.goo.gl/7X2J43dzSeG98hEYA
- https://images.app.goo.gl/yrUmrDneD1u1nsKM6
- https://images.app.goo.gl/ktf6JmwERbWoNfF69
- https://images.app.goo.gl/3qBw4pu2UQosNBVi9
- https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSPkv49y0UYywLik-CVtV5TnAl5KXKwf9W0nqOrw7HCl-pqow5k
- https://images.app.goo.gl/6tEm4TTEdV14AdVg8
- https://images.app.goo.gl/c3mNhZDPHJc3QxQd6
- https://images.app.goo.gl/D8Gn2iQikTyJkPA66
- https://images.app.goo.gl/WM453Peq485jGfTJA
- https://images.app.goo.gl/yUwnvUZnXGH5Xumn8
- https://images.app.goo.gl/KrA2qZstDoBALP3d7
- https://images.app.goo.gl/s81iKDuGpayFYLzNA

</details>

## **Acknowledgments**