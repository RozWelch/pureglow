## Pure Glow
Pure Glow is a skincare range, selling products for the face, body and an organic range. Users can browse skincare products, and purchase them. There is a ‘how to’ section, with useful articles on how to use the products, users can view comments and signed-in users can add a comment. Signed-in users can add products to a wishlist, to purchase at a later date. 

The payment system uses Stripe. Please note this website is for educational purposes. Do not enter any personal credit/debit card details when using the site. To test this system, test card details can be used. These can be found in Stripe's documentation website: [stripe](https://stripe.com/docs/testing/) 

The live link can be found here - [pure glow skincare](https://pureglow.herokuapp.com/)

## Am I Responsive mockups
* Used Am I Responsive website to show the main pages on different devices:
    <details>
    <summary>Pure Glow mockups</summary>

    ![home](https://github.com/RozWelch/)
    ![list](https://github.com/RozWelch/)
    ![details](https://github.com/RozWelch/)

## Contents
* [Design and User Experience](#Design-and-User-Experience)
* [Features](#Features)
* [Marketing](#Marketing)
* [Technologies Used](#Technologies-Used)
* [Agile Methodology](#Agile)
* [Fixed and Unfixed Bugs](#Fixed-and-Unfixed-Bugs)
* [Validation](#Validation)
* [Testing](#Testing)
* [Project Deployment](#Project-Creation-and-Deployment)
* [Credits](#Credits)

## Design and User Experience
The site was aimed at purchasers of skin care products, main target audience is women age 18+.

* Colour pallet:
    * The main colours choosen gave the site a premium look, with warm accent colours to give an approchable feel.  
    ![Colour Pallett](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/colour_pallet.jpg)

* Wireframes:
    <details>
    <summary>Balsamiq wireframes</summary>
    
    * Home Page Wireframe
    ![Home Page](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/wireframes/wireframe1_homepage.jpg)

    * All Products list page 
    ![|All Products](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/wireframes/wireframe2_all_products.jpg)

    * Face Products list page
    ![Face Products](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/wireframes/wireframe3_face_products.jpg)
    
    * Body Products list page
    ![Body Products](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/wireframes/wireframe4_body_products.jpg)

    * Organic Products list page
    ![Organic Products](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/wireframes/wireframe5_organic_products.jpg)

    * My Profile page
    ![My Profile](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/wireframes/wireframe6_myprofile.jpg)

    * My Wishlist page
    ![Wishlist](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/wireframes/wireframe7_wishlist.jpg)

    * Shopping bag page
    ![Shopping bag](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/wireframes/wireframe8_shoppingbag.jpg)

    * Admin Products management page
    ![Products management](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/wireframes/wireframe9_productmgmt.jpg)

* Database Drawing:
    <details>
    <summary>Database schema</summary>

    * Database
    
    ![Database](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/database_schema_drawsql_diagram.jpg)

* User Stories:
* Epic: Viewing and Navigation
    * As a Site User, I can intuitively navigate around the site, so that I can find content.
    * As a Site User, I can view a list of products, so that I can select a product to view.
    * As a shopper, I can click on a product, so that I can read the full product details.
    * As a shopper, I can view a specific category of products, so I can browse the type of products I'm looking for.
    * As a shopper, I can search all products, so that I can find what I am looking for.
    * As a shopper, I can sort all products, so that I can view products based on price or title.
    * As a site user, I can read ‘how to’ articles, so I better understand how to use the products.
    * As a site user, I can read comments on ‘how to’ articles left by other customers, so I see what feedback and star rating they gave on the products they purchased.
    * As a shopper, I can add products to my wish list, so that I can go back and view them at a later date.
    * As a shopper, I can view my wish list, so I can find them easily in the one location.
 
* Epic: User Account and Profile
    * As a site user, I can register an account, so that I can have a personal account and keep track of my orders and wishlist.
    * As a site user, I can log in or log out of my account, so that I can keep my account secure.
    * As a site user, I can see my login status, so that I know if I'm logged in or out.
    * As a site user, I can save my personal details in my user profile, so that I do not have to fill them out for future orders.
    * As a site user, I can view my order history, so that I can remember what purchases I've made previously.
    * As a site user, I can recover my password in case I forget it, so that I can recover access to my account.

* Epic: Purchasing
    * As a shopper, I can add products with different quantities to my shopping bag, so that I can purchase them all together when I am ready.
    * As a shopper, I can view the current total of my shopping bag as I am shopping, so that I can see how much my purchases costs so far, so I can avoid spending too much.
    * As a shopper, I can view the contents of my shopping bag at any time, so I can see the products included and the total cost.
    * As a shopper, I can adjust the quantity, or delete products in my bag, so that I can easily make changes before I purchase.
    * As a shopper, I can see a summary of my shopping cart when I checkout so that I know what products are included and the total cost before I commit to purchasing.
    * As a shopper, I can easily enter my payment information securely, so that I can purchase my chosen products quickly with no issues.
    * As a shopper, I can checkout as a guest, so I don't have to sign up for an account.
    * As a shopper, I can view an order confirmation after checkout, so that I know my purchase was successful and see a summary of my purchases.
    * As a shopper, I can receive an email confirmation of my order, so that I have a record of my purchase.

* Epic: Admin & Store Management
    * As an Admin, I can easily add/edit/delete products through a front end interface, so that I can manage the store content.
    * As an Admin, I can add/edit/delete ‘how to’ articles, so that I can manage the store content.
    * As an Admin, I can approve comments on ‘how to’ articles, so I can manage the site content.

* Epic: User Interaction
    * As a site user, I can add comments on ‘how to’ articles, so that I can give my feedback.
    * As a site user, I can sign up for the website's newsletter, so that I can keep up to date with new products and promotions.

* Epic: Future Features
    * As a shopper, I can collect points for purchasing products, so I can use them as a discount on future purchases.
    * As a shopper, I can review products and rate them, so I can give my feedback on my purchases.
    * As a shopper, I can create an account using my Google or Facebook account.

## Features
* Header and footer
    ![header](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/header_logo_nav.jpg)
    * Logo: This logo is positioned in the top left of the navigation bar. The logo is linked to the home page so the user can easily navigate back to the home page.
    * Navigation Bar: The navigation bar is present at the top of every page and includes links to other pages.
When logged in, the user will see an icon and their user name. If not logged in they will see a link to sign up or log in.
The navigation bar is fully responsive, collapsing into a hamburger menu for smaller devices. The links show the user their current page by displaying a different colour and an underline, this is also used when the user hovers over a link so they can see what page they will navigate to.
    ![footer](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/footer.jpg)
    * Footer: The footer section has links to Carehub's Facebook, Instagram, Twitter and Youtube pages.
These open in a separate browser window to avoid taking the user away from the site.

* Home page
    * The call to action section
    ![cta_in](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/cta_section_loggedin.jpg)
    ![cta_out](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/cta_section_notloggedin.jpg)
    * The call to action section shows a relevant image, and a easy to locate call to action button: sign up button if not logged in, or find care button if already logged in.
    * The about section
    ![about](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/about_section.jpg)
    * The about section gives a brief description of who the site is for and what type of care a user can find there. 

* Account pages
    * Sign In
    ![signin](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/sign_in.jpg)
    * Sign up
    ![signup](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/sign_up.jpg)
    * Log out
    ![logout](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/sign_out.jpg)
    * Allauth was used to create the Sign up / Log in / Log out functions. A success message is displayed when the user has signed in / signed out / or created and account sucessfully.

* Care Providers' list view
    ![providerlist](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/providers_list.jpg)
    * Shows a list of Care Providers that have been approved by the site Admin, ordered by business name. The page paginates after every 6 providers are listed. Clicking on the 'Care providers Detail' button will bring the user to the full details for that provider.

* Care Provider Detail view
    ![providerdetail](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/provider_details.jpg)
    * Shows the full details for that provider
    * If the user is the author of the provider listing, they will see the buttons to edit or delete that provider
    ![editdeleteprovider](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/edit_delete_provider.jpg)

* Care Provider Detail - Comments section
    ![comments](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/comments.jpg)
    * Shows comments that have been approved by the site Admin for that Care Provider. If the user is signed in, a comment box is shown where they can leave a commnet. They are shown a message to show they have sucessfully left a comment, and it awaits approval by admin.

* Add a care provider page
    ![comments](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/add_provider.jpg)
    * If logged in, a user will see a form to add a care provider. A care provider can add an image, or a default placeholder image will be used. The user will receive a success message. The care provider details then await approval by the site Admin.

* Edit care provider page
    ![comments](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/edit_provider.jpg)
    * If logged in, and the user is the author of the Care Provider, they can see the edit button, which brings them to an edit provider page. The form is pre populated with all fields from the original provider details. When changes are submitted, the user will receive a message that the details have been sucessfully updated.

* Delete care provider page
    ![comments](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/featuresimages/delete_provider.jpg)
    * If logged in, and the user is the author of the Care Provider, they can see the delete button. If clicked, they will be asked to confirm they wish to delete the provider, or they can cancel. If they click delete, the user will receive a message to say the provider has successfully been deleted.

* Future Features
    * Logged in User can 'like' a Care Provider, number of likes can be displayed 
    * Have different user types for a care provider or a care seeker, so they can be restricted to certain areas of the website
    * Care providers can be filtered by county or by speciality
    * Bookmarks page, so logged in user can bookmark providers, and see a page of their bookmarked providers

## Marketing
* Business Model
    * pure glow is a Business to Consumer site (B2C). Products are sold directly online to the end user consumer. A pure glow customer is most likely to be a female adult interested in skincare. 
* SEO
    * Keywords were researched for the site    
* Social Media Marketing
    * A facebook page was created for social media marketing. The page has a 'Shop Now' button to take the user to the pure glow website. A link to the facebook page is on the pure glow website footer. 
    ![Facebook](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/facebookpage_pureglow.jpg)
* Email Marketing
    * An email signup is included in the footer of the website. Users can sign up for an email and do not need an account to do this. This allows the business to share new arrivals, offers and news with customers and potential customers. Mailchimp was used to create this feature.

## Technologies Used
* Languages: Python, HTML, CSS, Javascript
* Other technologies used:  
    * Django: Main python framework 
    * Django-allauth: authentication library used to create user accounts
    * Elephant PostgreSQL: database
    * Heroku: cloud based platform to deploy the site
    * Balsamiq: to draw wireframes
    * Chrome Dev Tools - for testing responsiveness, performance and for debugging
    * Font Awesome: icons used on the site
    * GitHub: version control and agile Kanban boards
    * Google Fonts: for fonts used on site
    * Favicon: to create a favicon for the site
    * Summernote: WYSIWYG editor - for users to create comments 
    * Crispy Forms: for Django forms
    * AWS: S3 bucket - image hosting service 
    * Bootstrap: CSS Framework for developing the site
    * Secret Key Generator: https://djecrety.ir/
    * Database schema drawing toool: https://drawsql.app
* Validators:
    * W3C: to validate html and css
    * PEP8: to validate Python code
    * Jshint: to validate Javascript
    * Python: Code Institute pep8 validator: https://pep8ci.herokuapp.com/

## Agile
* Github projects kanban boards were used, see link to final board here: https://github.com/users/RozWelch/projects/7
* The project was broken down into sprints, with a Github milestone for each Epic. A Github issue was added for each user story, and allocated to a milestone. Each user story had a defined acceptance criteria, which breaks it down into tasks. 
* The project was then divided into sprints:
* Sprint 1:
    <details>
    <summary>User authentication</summary>

    ![sprint1](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/agile/sprint1_userauth.jpg)

* Sprint 2:
    <details>
    <summary>Product and product details</summary>

    ![sprint2](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/agile/sprint2_products_and_details.jpg)

* Sprint 3:
    <details>
    <summary>The shopping bag</summary>

    ![sprint3](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/agile/sprint3_shopping_bag.jpg)

* Sprint 4:
    <details>
    <summary>Toasts and complete the shopping bag</summary>

    ![sprint4](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/agile/sprint4_toasts_finish_shoppingbag.jpg)

* Sprint 5:
    <details>
    <summary>The checkout app</summary>

    ![sprint5](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/agile/sprint5_checkout_app.jpg)

* Sprint 6:
    <details>
    <summary>User profiles</summary>

    ![sprint6](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/agile/sprint6_user_profiles.jpg)

* Sprint 7:
    <details>
    <summary>Wishlist</summary>

    ![sprint6](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/agile/sprint7_wishlist.jpg)

* Sprint 8:
    <details>
    <summary>‘How to’ Articles</summary>

    ![sprint6](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/agile/Sprint8_how_to_articles.jpg)

* Sprint 9:
    <details>
    <summary>Newsletter sign up</summary>

    ![sprint6](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/agile/sprint9_newslettr_signup.jpg)

* Final Sprint: Refactoring and tidy up styling. After a meeting with my mentor, some of the tasks were moved to future features, due to time constraints at this stage.


## Fixed and Unfixed Bugs

* Fixed bugs:
    * When first deployed to Heroku, the links were giving a ‘Server Error 500’. I fixed a couple of errors first: First I moved custom_storages.py to the correct location. I added gunicorn to the requirements.txt file. However these were not the cause of the error. I set DEBUT = True in settings to get a more accurate error message. On checking Heroku config vars, I had copied the "hidden" version of the database url from ElephantSQL: Some of the URL has been censored with **** symbols. From ElephantSQL, I copied the full DB url: I then updated the config var on heroku, and restart my app dynos: (the more button in the upper right, and select Restart All Dynos to rebuild my app.) Then the app was working correctly.

    * Product sorting was not working initially. The “ for the href was in the wrong place (before ?category). When “ moved to after category, the product sorting worked correctly.

    * A confirmation email was not being sent when I made a purchase, the purchase goes through ok and I get a success message, but I don't get an email. I checked on stripe and the payments were giving an error. I checked my heroku config vars, and noticed an extra line was on my STRIPE_WH_SECRET var - I removed that and tested again. Under the list of events in Strips, there was a 500 error - On checking the html with the error underneath, there was a BadHeader Error. There was a newline at the end of your email subject file. I removed this line and then the emails came through correctly.

* No known unfixed bugs

## Validation 

* CSS:
    <details>
    <summary>No errors when ran through the official W3C CSS Validator.</summary>

    ![css](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/css_valid.jpg)

* HTML:
    <details>
    <summary>All HTML files ran through the W3C HTML Validator with no errors</summary>

    ![homepage](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/homepage_noerrors.jpg)
    ![findcare](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/find_care_noerrors.jpg)
    ![providerdetails](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/provider_details_noerrors.jpg)
    ![forproviders](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/forproviders_noerrors.jpg)
    ![signup](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/signup_noerrors.jpg)
    ![login](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/login_noerrors.jpg)
    ![logout](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/logout_noerrors.jpg)

* Python:
    <details>
    <summary>Code Institites PEP8 Validator</summary>

    All Python files ran through Code Institites PEP8 Validator with no errors, except for 2 files. The env.py and settings.py files had 2 lines that were too long, but I kept them as long lines, as the code was more legible.

    ![admin](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/admin_clear.jpg)    
    ![apps](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/apps_clear.jpg) 
    ![env](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/env_2lines_left_long.jpg) 
    ![forms](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/forms_clear.jpg) 
    ![manage](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/manage_clear.jpg) 
    ![models](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/models_clear.jpg) 
    ![settings](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/settings_2lines_left_long.jpg) 
    ![urlscaresearch](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/urls_caresearch_clear.jpg) 
    ![urls](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/urls_clear.jpg) 
    ![views](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/views_clear.jpg) 
    ![wsgi](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/wsgi_clear.jpg) 

* Javascript:
    <details>
    <summary>No errors when ran through JShint.</summary>

    ![jshint](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/jshint_valid.jpg)

* Lighthouse:
    <details>
    <summary>Score was 100% for Accessibility</summary>

    Score was 100% for Accessibility, which was important for the site's target users. On first running through Lighthouse, the score was lower, but after adjusting the colour contrast on CTA buttons, the score was brought to 100%. Other scores were close to, or at 100%.
    ![homepage](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/homepage.jpg) 
    ![findcare](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/find_care.jpg) 
    ![addprovider](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/add_provider.jpg)    
    ![logout](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/logout.jpg) 
    ![providerdetails](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/provider_details.jpg) 
    ![signin](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/signin.jpg) 
    ![signup](https://github.com/RozWelch/CareHub-Project4-2023/blob/main/assets/readmeimages/validations/signup.jpg) 


## Testing

* Link to testing and results: https://github.com/RozWelch/CareHub-Project4-2023/blob/main/TESTING.md

## Project Creation and Deployment

The project was created in Git Hub using the Code Institute template.

* Deployment from Heroku:  
    * Login to Heroku (https://www.heroku.com/) or create an account
    * On the main page, click the 'New' button in the top right corner, select 'Create New App' from the menu
    * Choose a name and select your region, then click on the 'Create App' button
    * Choose Github as the deployment method, then select the correct repository, and click the connect button
    * Select the Settings tab
    * Click Reveal Config Vars
    * Add Config Vars settings with values: SECRET_KEY =(add value here), CLOUDINARY_URL, DATABASE_URL, PORT = 8000, DISABLE_COLLECTSTATIC = 1
    * Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
    * Scroll to the bottom of the deploy page and select the preferred deployment type
    * Click 'Enable Automatic Deploys' if you wish to automatically deploy when you push updates to Github

* Forking the repository
     * Locate the repository at this link https://github.com/RozWelch/CareHub-Project4-2023
     * At the top right of the repository, select 'Fork' from the menu
     * A copy of the repository is now created

* Cloning the repository
     * Locate the repository at this link https://github.com/RozWelch/CareHub-Project4-2023
     * Under 'Local', there is cloning options: HTTPS, SSH, GitHub CLI. Click the prefered cloning option, and then copy the link provided.
     * Open the terminal
     * In the terminal change the current working directory to where you wish to put the cloned directory
     * Type: 'git clone', then paste the URL already copied from GitHub earlier
     * Press Enter. Your local clone will be created.

## Credits
* Code Institue's 'Boutique Ado' tutorial
* All images used are from Freepix: www.freepix.com
* How To articles: https://www.nytimes.com/guides/tmagazine/skincare-routine
* W3Schools
* Django Documentation
* Bootstrap Documentation
* Stack Overflow

## Acknowledgements
Thanks to my mentor, my facilitator, my fellow students on Slack, tutoring support and to my friends for helping test the site.