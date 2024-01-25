# Grain Free Friend
Your baking buddy for alternative breads and more

![Mockup on different devices, created with Techsini.]()

Grain Free Friend is a recipe sharing web app that allows users to ...
<!-- Add content here -->
It has full CRUD functionality; a user can
- Create a new recipe
- Read posted recipes
- Update recipes they have posted
- Delete recipes they have posted

## Table of Contents
- [Intro](#grain-free-friend)
- [Table of Contents](#table-of-contents)
- [UX](#ux)
  - [User Personas](#user-personas)
  - [User Stories](#user-stories)
  - [Structure](#structure)
  - [Features](#features)
  - [Surface](#surface)
- [Testing](#testing)
- [Future Implementations](#future-implementations)
- [Languages, Libraries, and Software](#languages-libraries-and-software)
- [Deployment](#deployment)
- [Credits](#credits)

## UX
### User Personas
- A home cook who enjoys experimenting and wants to learn more about grain-free baking.
- A person with overlapping dietary restrictions (low-carb + kosher, vegan + celiac, etc).
- A person with new grain-free dietary restrictions who wants to find tasty substitute recipes efficiently.

### User Stories
### Structure
#### Landing Page
#### All Recipes
#### Recipe Detail
#### Add Recipe
#### Update Recipe
#### Delete Recipe
#### About
#### Contact
#### 403 & 404
### Features
#### Header and Navigation
#### Footer
- Social media icons were created with [UXWing](https://uxwing.com/).
#### Account
#### Create an Account
#### Login
#### Logout

### Surface
#### Colors
The color palette is from [Lilybug Design](https://www.lilybugdesign.co.nz/colour-wall). I saw one of these designs used in a [PP4 project by Roshna Vakkee](https://github.com/RoshnaVakkeel/Little_Learners_Lab_Logs?tab=readme-ov-file), and found a beautiful one for my project. This palette is fresh and lively, as well as warm. It supports the Grain Free Friend branding: accessible, fun, supportive. <br>
![Color palette](static/images/readme-images/color-palette.png)
I used colorpicker to get the HEX tags for each color. <br>
Colors were picked with [imagecolorpicker.com](https://imagecolorpicker.com/en).

#### Fonts
The fonts used in this project are from [Google Fonts](https://fonts.google.com/). <br>
The title font is [Montserrat](https://fonts.google.com/specimen/Montserrat). This is a bold, modern font with a rounded shape that's friendly and accessible. It was an option in the logo maker, and I decided to use it for the titles as well. <br>
![Montserrat font](static/images/readme-images/font-montserrat.png)
The main font is [Raleway](https://fonts.google.com/specimen/Raleway). This is a friendly, readable font in a modern style. It makes the recipe ingredients and instructions very clear and accessible. <br>
![Raleway font](static/images/readme-images/font-raleway.png)
#### Logo
The logo represents <br>
<!-- Add content about logo and how it was made -->
It was created using the [wix.com logo maker](https://www.wix.com/logo/maker). <br>
![Logo](static/images/logo.png)
#### Favicon
The favicon was created from the logo image using the [favico.io favicon converter](https://favicon.io/favicon-converter/). <br>
![Favicon](static/images/readme-images/favicon-image.png)
#### Images
The recipe images are either my personal photos or from [Unsplash](https://unsplash.com/).
<!-- Add content about images -->
<br>

They are stored in and accessed through [Cloudinary](https://cloudinary.com).

#### Background

## Testing
#### Lighthouse
### Code Validation
#### HTML
#### CSS
#### Javascript
#### Python
### User Stories Testing
### Manual Testing
### Bugs
- Missing imports <br>
The installed libraries would not run. The error message was: <i>Import "django_resized" could not be resolved.</i> The solution really was [to turn it off and on](https://stackoverflow.com/questions/65933570/import-boto3-could-not-be-resolved-python-vs-code). I restarted VS Code, and this fixed the bug.
- Add input field for levels <br>
The first time I tried to add an input field, the site would not run. I realized I needed to make migrations, which fixed the bug. I ran: <br>
`python3 manage.py makemigrations` <br>
`python3 manage.py migrate`
- Multi-select field <br>
I wanted to add something like tags to show the attributes of each recipe. It seemed like this would be possible with CheckboxSelectMultiple. I created the code but it did not work. I searched Stack Overflow, asked my fellow students, asked ChatGPT, and finally found out that I needed a later version of Django to run crispy forms, but only an earlier version could implement CheckboxSelectMultiple. Unfortunately I had to abandon the idea of a multi-select field. Instead I used 3 dropdown menus to list up to 3 attributes of the recipe. It is not the best UX, but they are searchable, and visible on each recipe card as if they are tags.
- Loading static files on the deployed site <br>
The static files wouldn't load, so I did some research and found [from Stack Overflow](https://stackoverflow.com/questions/28961177/heroku-static-files-not-loading-django) that I needed to install whitenoise. I installed whitenoise per [these instructions](https://devmaesters.com/blog/34). After I updated my requirements.txt, the files loaded.

## Future Implementations

## Languages, Libraries, and Software
### Languages
- HTML
- CSS
- Javascript
- Python
### Modules and Packages
- black (code formatter)
- cloudinary (image hosting)
- crispy-bootstrap5
- dj-database-url
- django-allauth (authorization package)
- django-cloudinary-storage
- django-crispy-forms (styles forms)
- django-resized (resizes a photo submitted in the form)
- django-richtextfield (allows markdown styling in input fields)
- gunicorn (server for WSGI applications)
- psycopg2
- whitenoise (allows static files to load in deployed app)
### Frameworks and Websites
- Bootstrap5
- Django
- Github
- Cloudinary
- PostgreSQL (ElephantSQL)
- Heroku
- VS Code
- Google Chrome Dev Tools
- Google Fonts
- Colorpicker
- UXWing
- Unsplash
- PEP8
- W3C - HTML
- W3C - CSS

## Deployment
### Heroku
- Create accounts in Heroku and ElephantSQL
- 
### Github

## Credits
### Content
### Media
### Thank you
- This project was developed using the [Django Recipe Sharing tutorial by Dee Mc](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=1). I am indebted to her for the basic styling of the header, footer, and forms, the CRUD functionality of the recipes, class-based views, and querying.
- The project was also inspired by Code Institute's Django Blog Walkthrough. I used this to help create the success alerts.
- Inspiration for this readme came from [gStarhigh](https://github.com/gStarhigh/pro4).

<!-- ## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so. You will need to explain what value each of the features provides for the user, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

### Existing Features

- __Navigation Bar__

  - Featured on all three pages, the full responsive navigation bar includes links to the Logo, Home page, Gallery and Sign Up page and is identical in each page to allow for easy navigation.
  - This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button. 

![Nav Bar](https://github.com/lucyrush/readme-template/blob/master/media/love_running_nav.png)

- __The landing page image__

  - The landing includes a photograph with text overlay to allow the user to see exactly which location this site would be applicable to. 
  - This section introduces the user to Love Running with an eye catching animation to grab their attention

![Landing Page](https://github.com/lucyrush/readme-template/blob/master/media/love_running_landing.png)

- __Club Ethos Section__

  - The club ethos section will allow the user to see the benefits of joining the Love Running meetups, as well as the benefits of running overall. 
  - This user will see the value of signing up for the Love Running meetups. This should encourage the user to consider running as their form of exercise. 

![Club Ethos](https://github.com/lucyrush/readme-template/blob/master/media/love_running_ethos.png)

- __Meetup Times section__

  - This section will allow the user to see exactly when the meetups will happen, where they will be located and how long the run will be in kilometers. 
  - This section will be updated as these times change to keep the user up to date. 

![Meetup Times](https://github.com/lucyrush/readme-template/blob/master/media/love_running_times.png)

- __The Footer__ 

  - The footer section includes links to the relevant social media sites for Love Running. The links will open to a new tab to allow easy navigation for the user. 
  - The footer is valuable to the user as it encourages them to keep connected via social media

![Footer](https://github.com/lucyrush/readme-template/blob/master/media/love_running_footer.png)

- __Gallery__

  - The gallery will provide the user with supporting images to see what the meet ups look like. 
  - This section is valuable to the user as they will be able to easily identify the types of events the organisation puts together. 

![Gallery](https://github.com/lucyrush/readme-template/blob/master/media/love_running_gallery.png)

- __The Sign Up Page__

  - This page will allow the user to get signed up to Love Running to start their running journey with the community. The user will be able specify if they would like to take part in road, trail or both types of running. The user will be asked to submit their full name and email address. 

![Sign Up](https://github.com/lucyrush/readme-template/blob/master/media/love_running_signup.png)

For some/all of your features, you may choose to reference the specific project files that implement them.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement

- Another feature idea

## Testing 

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.


### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css)

### Unfixed Bugs

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-running-2.0/index.html 


## Credits 

In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 

You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site


Congratulations on completing your Readme, you have made another big stride in the direction of being a developer! 

## Other General Project Advice

Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 

- Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
  - [Writing Your Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  - [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
  - [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#General) -->
