# Pure Glow
Pure Glow is a skincare range, selling products for the face, body and an organic range. Users can browse skincare products, and purchase them. There is a ‘how to’ section, with useful articles on how to use the products, users can view comments and signed-in users can add a comment. Signed-in users can add products to a wishlist, to purchase at a later date. 

The payment system uses Stripe. Please note this website is for educational purposes. Do not enter any personal credit/debit card details when using the site. To test this system, test card details can be used. These can be found in Stripe's documentation website: [stripe](https://stripe.com/docs/testing/) 

The live link can be found here - [pure glow skincare](https://pureglow.herokuapp.com/)

# Am I Responsive mockups
* Used Am I Responsive website to show the main pages on different devices:
    <details>
    <summary>Pure Glow mockups</summary>

    ![home](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/amiresponsive/homepage.jpg)
    ![list](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/amiresponsive/allproducts.jpg)
    ![details](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/amiresponsive/skincare_articels.jpg)

# Contents
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

# Design and User Experience
The site was aimed at purchasers of skin care products, main target audience is women age 18+.

* Colour pallet:
    * The main colours choosen gave the site a premium look, with warm accent colours to give an approachable feel.  
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

* Sitemap Drawing:
    <details>
    <summary>Sitemap drawing</summary>

    * Sitemap
    
    ![Sitemap](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/sitemap.jpg)

## User Stories:
* Epic: Viewing and Navigation
    * As a Site User, I can intuitively navigate around the site, so that I can find content.
    * As a Site User, I can view a list of products, so that I can select a product to view.
    * As a shopper, I can click on a product, so that I can read the full product details.
    * As a shopper, I can view a specific category of products, so I can browse the type of products I'm looking for.
    * As a shopper, I can search all products, so that I can find what I am looking for.
    * As a shopper, I can sort all products, so that I can view products based on price or title.
    * As a site user, I can read ‘how to’ articles, so I better understand how to use the products.
    * As a site user, I can read comments on ‘how to’ articles left by other customers, so I see what feedback they gave on the products they purchased.
    * As a shopper, I can add products to my wish list, so that I can go back and view them at a later date.
    * As a shopper, I can view my wish list, so I can find them easily in the one location.
 
* Epic: User Account and Profile
    * As a site user, I can register an account, so that I can have a personal account and keep track of my orders and wishlist.
    * As a site user, I can log in or log out of my account, so that I can keep my account secure.
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

# Features
* Header
    * The site logo is positing at the top left and is linked to the home page to make it easy for a user to navigate back to the home page.
    ![Header](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature1_header.jpg)

* Navigation Bar
    * The navigation bar is at the top of every pages and includes links to the main pages.
    * It is fully responsive, and collapses to a hamburger menu on mobile size devices

* Search bar
    ![Searchbar](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature2_searchbar.jpg)
    * The search bar is located at the top centre of the page.
    * On mobile size devices, it becomes a search icon, which opens up as a bar when clicked.
    * When a search word is entered, the product’s name and description is searched for the word, and a list of results are displayed to the user.
    

* The User Icon
    ![usericon](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature3_account_nav.jpg)
    * This is displayed on the top right. 
    * When logged out a Sign up or Log in dropdown is displayed
    * If logged in, My Profile is available as well
    * If logged in and an Admin, the Product management option is available

* The bag icon
    ![Bagicon](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature4_bag_nav.jpg)
    * This is displayed on the top right. 
    * Once a product is added to the bag, the number of items in the bag is displayed
    * When the user adds products to their bag, a toast message appears in the top right-hand corner of the screen. The bag contents and the total cost of the bag are shown
    * Clicking the icon brings the user to the shopping bag page

* Footer
    ![Footer](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature6_footer.jpg)
    * The footer is at the bottom of every page
    * The newsletter signup allows a user opt to sign up for a newsletter - this is powered by Mailchimp
    * The next section has links to the products page, a site map, and the sites privacy policy
    * The final section has social media links, including a link to the pure glow Facebook page, created for this project
    * All external links open in a new tab, to avoid taking the user away from the pure glow site 

* The home page
    ![Home](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature7_homepage_cta.jpg)
    * A brief introduction to the site is included
    * A CTA ‘Shop now’ button in included to encourage the user to browse the products

* User’s Accounts pages
    * Sign Up
    ![Signup](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature8_sign_up.jpg)

    * Sign In
    ![Signin](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature9_sign_in.jpg)

    * Log out
    ![Logout](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature10_sign_out.jpg)

    * Allauth was used to create the Sign up, Sign in and Log out functionality
    * The user receives a success message on successfully login/logout
    * When signing up for an account, the user must verify their email address provided
    * The user can reset their password if forgotten,  by clicking the 'Forgot Password' on the login page

* Profile
    ![Profile](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature11_my_profile.jpg)
    * The profile page contains the user’s saved delivery and contact information, so they don’t have to enter it each time they checkout
    * Order history - The user can view their previous orders

* All products
    ![Products](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature12_all_products.jpg)
    * When clicked the products navigation link shows a drop down menu where all products can be shown sorted by price or by category
    ![ProductsMenu](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature13_all_products_dropdown.jpg)
    * The products are displayed, with a sort by button where the products can be sorted by price (ascending or descending), name or category (A-Z or Z-A)
    * Each product card shows the product image, name, price 
    * If an authenticated user is a superuser, they will see a button to Edit or Delete a product

* All Face products
    ![Face](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature14_face_products.jpg)
    * When clicked the Face navigation link shows a drop down menu where the user can select: Moisturiser, Cleansers, Masks and treatment or all face care
    * The Category of Face Care product is shown under the Products heading
    * The products are displayed, with a sort by button where the products can be sorted by price (ascending or descending), name or category (A-Z or Z-A)
    * Each product card shows the product image, name, price 
    * If an authenticated user is a superuser, they will see a button to Edit or Delete a product

* All Body Products
    ![Body](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature15_body_products.jpg)
    * When clicked the Face navigation link shows a drop down menu where the user can select: Body Moisturiser, Body Bath and shower or all body
    * The Category of Body Care product is shown under the Products heading
    * The products are displayed, with a sort by button where the products can be sorted by price (ascending or descending), name or category (A-Z or Z-A)
    * Each product card shows the product image, name, price 
    * If an authenticated user is a superuser, they will see a button to Edit or Delete a product

* All Organic Products
    ![Organic](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature16_organic_products.jpg)
    * When clicked the Face navigation link shows a drop down menu where the user can select: face, body or all organic
    * The Category of Organic Care product is shown under the Products heading
    * The products are displayed, with a sort by button where the products can be sorted by price (ascending or descending), name or category (A-Z or Z-A)
    * Each product card shows the product image, name, price 
    * If an authenticated user is a superuser, they will see a button to Edit or Delete a product

* Product Detail page
    ![Details](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature17_product_details.jpg)
    * The product image is shown, with a brief description, the category
    * A Quantity button with + - is show so a user can add the item to their shopping bag
    * A Wishlist icon is shown so a user can add the item to a wishlist
    * If an authenticated user is a superuser, they will see a button to Edit or Delete a product

* Add Product page
    ![Add product](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature18_add_product.jpg)
    * If an authenticated user is a superuser, they can see a Product Management, where they can add a product
    * Fields with an Astrix are required, the user will get an error message if they are not filled out and the form submit button is clicked
    * The sku must be unique, the user will get an error message if they try submit a sku that already exists
    * If a user tries to add a product by changing the url, without being a superuser they are redirected to a custom 403 page.
    * If a price is added with more than 6 digits the form will not be submitted and the user will receive an error message
    * The user can upload a photo, or if no photo is submitted  a placeholder image is used
    * Clicking the 'Add Product' button at the bottom of the form will create the product if the form is valid
    * The user will receive a success message notifying them that the product has been successfully added

* Edit a Product
    ![Edit](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature19_edit_product.jpg)
    * A logged in superuser will see an edit button on the product list, or the product detail page.
    * When clicked, a form opens with the product details repopulated
    * If edited, and updated button is clicked, the user will receive a success message

* Delete a Product
    * A logged in superuser will see a delete button on the product list, or the product detail page.
    * When clicked, the user will receive a message asking if they are sure they wish to delete.
    * If deleted and confirmed the user wants to delete,  the user will receive a success message.

* ‘How To’ Articles list page
    ![How to](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature23_how_to_articles.jpg)
    * A list of articles are displayed showing the title and the author

* ‘How To’ Articles details page
    ![How to detail](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature24_how_to_detail.jpg)
    * The articles are written by an admin user. 
    * The article is shown with a list of any comments displayed below
    * A signed in user can make a comment.
    * On clicking submit, they will be show a success message telling them their comment is awaiting approval
    * An admin user can approve comments.

* Wishlist
    ![Wishlist](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature25_wishlist.jpg)
    * A logged-in user can add items to their wishlist by clicking on the icon on the product details page
    * On their wishlist page, they can see details of items in their list, and click on the shop now icon to purchase them, or click on the bin icon to remove them

* Shopping Bag
    ![Shopping bag](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/features_low_res/feature20_shopping_bag.jpg)
    * If there are items in the shopping bag they are displayed
    * Next to the item is a + and - button to update the quantities.
    * If the quantity is 0, the - button is disables to prevent a negative quantity
    * The total of the bag is displayed, with delivery cost if applicable, and how much extra to spend for free delivery.
    * Under the grand total are two buttons - one to return shopping to products, or the other to checkout.

* Checkout
    * The user can see a summary of their purchases, and the cost.
    * A form will be displayed for the user to fill out with contact details, delivery address, and card details
    * If the user is a guest, a link for them to create an account or login will be shown
    * If the user is already signed in, a checkbox will be shown to save the delivery information
    * If the user is signed in, and had delivery information on their profile, the details will be shown
    * If a user leaves a required field empty, or puts in an incorrect format, they will be shown an error message
    * Order summary section
    * The order summary shows the user what they are purchasing, details and cost.
    * The order summary shows an image of the product, which links back to that product’s details.

* Payment
    * If an incorrect number is entered, the user is shown an error message to show invalid card number
    * A warning message is displayed at the bottom of the screen to show the user how much their card will be charged
    * When the form is submitted, a loading screen is displayed to prevent the user clicking away from the page
    * The web hook ensures the order will be created in the database, even if the user’s form didn’t submit correctly, or if the user closed the browser 
    * The web hook will also search the database to confirm the order exists. If not found, it will create one using the payment information 

* Payment confirmation
    * When the user’s payment is processed, they are taken to the checkout success page, with a summary of the order
    * The user will receive an order confirmation email

* Future Features
    * Points can be collected for purchasing products, so they can be used as a discount on future purchases.
    * Signed in users can review products and rate them, to give feedback on their purchases.
    * A user can create an account using their Google or Facebook account.

# Marketing
## Business Model
* pure glow is a Business to Consumer site (B2C). Products are sold directly online to the end user consumer. A pure glow customer is most likely to be a female adult interested in skincare. 
## SEO
SEO techniques were used to ensure the site ranks highly in search engine results
## Keywords
Both short tail and long tail keywords were carefully selected for the site. Keywords were selected by researching data available on keyword volume and competition using [wordtracker.com](https://www.wordtracker.com/)
The most relevant keywords have been added to the site's meta-keywords and meta-description. These keywords have also been included in site content across the site:
Pure Glow, skincare, moisturiser, face moisturiser, body moisturiser, skin cleanser, skin care products, organic skin care products
Pure skin care, Kind to your skin, natural skin care range, nourish your skin

## Sitemap and robots.txt 
Using xml-sitemaps.com, a site map of the site was made. This ensures search engines are able to easily navigate the site and understand the site's structure.

A robots.txt file was added to the project to tell search engines what directories not to search on the website. This improves SEO by increasing the quality of the site.

Content marketing
A 'How To' section was added, to show the expertise of the company and to engage and give users a reason to return to the site.   
## Social Media Marketing
* A facebook page was created for social media marketing. The page has a 'Shop Now' button to take the user to the pure glow website. A link to the facebook page is on the pure glow website footer. 
![Facebook](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/facebookpage_pureglow.jpg)
## Email Marketing
* An email signup is included in the footer of the website. Users can sign up for an email and do not need an account to do this. This allows the business to share new arrivals, offers and news with customers and potential customers. Mailchimp was used to create this feature.

# Technologies Used
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

# Agile
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


# Fixed and Unfixed Bugs

* Fixed bugs:
    * When first deployed to Heroku, the links were giving a ‘Server Error 500’. I fixed a couple of errors first: First I moved custom_storages.py to the correct location. I added gunicorn to the requirements.txt file. However these were not the cause of the error. I set DEBUT = True in settings to get a more accurate error message. On checking Heroku config vars, I had copied the "hidden" version of the database url from ElephantSQL: Some of the URL has been censored with **** symbols. From ElephantSQL, I copied the full DB url: I then updated the config var on heroku, and restart my app dynos: (the more button in the upper right, and select Restart All Dynos to rebuild my app.) Then the app was working correctly.

    * Product sorting was not working initially. The “ for the href was in the wrong place (before ?category). When “ moved to after category, the product sorting worked correctly.

    * A confirmation email was not being sent when I made a purchase, the purchase goes through ok and I get a success message, but I don't get an email. I checked on stripe and the payments were giving an error. I checked my heroku config vars, and noticed an extra line was on my STRIPE_WH_SECRET var - I removed that and tested again. Under the list of events in Strips, there was a 500 error - On checking the html with the error underneath, there was a BadHeader Error. There was a newline at the end of your email subject file. I removed this line and then the emails came through correctly.

    * The 'back to top' arrow was not working properly when you scrolled down to the footer section. I added and id, and gave the arrow a z-index of 99, so that it was always on top. The arrow then worked correctly when over the footer section.

* No known unfixed bugs

# Validation 

## CSS - no errors when run through W3 validator:
* Base css file
    <details>
    <summary>Base Css</summary>
    
    ![base css](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/validation/css/base_css.jpg)

* Checkout css file
    <details>
    <summary>Checkout Css</summary>

    ![checkout css](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/validation/css/checkout_css.jpg)

* Profile css file
    <details>
    <summary>Profile Css</summary>

    ![profile css](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/validation/css/profile_css.jpg)

* HTML:
    <details>
    <summary>All HTML files ran through the W3C HTML Validator</summary>

    ![all html valid](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/validation/all_files_html_valid.jpg)

    All files were valid, with the exception of a duplicate ID where a product image is added. This could not be fixed, as it would break the code.


## Python:

    All Python files ran through Code Institites PEP8 Validator with no errors.

| File name | CI Linter Results | link to screenshot | 
| -- | -- | -- | 
| bag/apps.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/bag/bag_apps.jpg) |
| bag/contexts.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/bag/bag_contexts.jpg)   |
| bag/urls.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/bag/bag_urls.jpg) |
| bag/views.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/bag/bag_views.jpg) |
| checkout/admin.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/checkout/checkout_admin.jpg) |
| checkout/apps.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/checkout/checkout_apps.jpg) |
| checkout/forms.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/checkout/checkout_forms.jpg) |
| checkout/models.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/checkout/checkout_models.jpg) |
| checkout/signals.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/checkout/checkout_signals.jpg) |
| checkout/urls.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/checkout/checkout_urls.jpg) |
| checkout/views.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/checkout/checkout_views.jpg) |
| checkout/webhookhandler.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/checkout/checkout_webhookhandler.jpg) |
| checkout/webhooks.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/checkout/checkout_webhooks.jpg) |
| home/apps.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/home/home_apps.jpg) |
| home/urls.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/home/home_urls.jpg) |
| home/views.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/home/home_views.jpg) |
| how_to/apps.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/how_to/howto_adds.jpg) |
| how_to/admin.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/how_to/howto_admin.jpg) |
| how_to/forms.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/how_to/howto_forms.jpg) |
| how_to/models.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/how_to/howto_models.jpg) |
| how_to/urls.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/how_to/howto_urls.jpg) |
| how_to/views.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/how_to/howto_views.jpg) |
| products/admin | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/products/products_admin.jpg) |
| products/apps | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/products/products_apps.jpg) |
| products/forms | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/products/products_forms.jpg) |
| products/models | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/products/products_models.jpg) |
| products/urls | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/products/products_urls.jpg) |
| products/views | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/products/products_views.jpg) |
| products/widgets | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/products/products_widgets.jpg) |
| profiles/apps.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/profiles/profiles_apps.jpg) |
| profiles/forms.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/profiles/profiles_forms.jpg) |
| profiles/models.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/profiles/profiles_models.jpg) |
| profiles/urls.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/profiles/profiles_urls.jpg) |
| profiles/views.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/profiles/profiles_views.jpg) |
| pure_glow/asgi.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/pure_glow/pureglow_asgi.jpg) |
| pure_glow/settings.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/pure_glow/pureglow_settings.jpg) |
| pure_glow/urls.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/pure_glow/pureglow_urls.jpg) |
| pure_glow/wsgi.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/pure_glow/pureglow_wsgi.jpg) |
| wishlist/apps.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/wishlist/wishlist_apps.jpg) |
| wishlist/models.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/wishlist/wishlist_models.jpg) |
| wishlist/urls.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/wishlist/wishlist_urls.jpg) |
| wishlist/views.py | All clear, no errors found | [screenshot](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/python_jpgs/wishlist/wishlist_views.jpg) |
  

## Javascript: No errors when ran through JShint.
* The shopping bag JS
    <details>
    <summary>Bag JS</summary>

    ![bag js](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/validation/css/jshint/bag_js.jpg)

* Base JS
    <details>
    <summary>Base JS</summary>

    ![bag js](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/validation/css/jshint/base_js.jpg)

* Checkout JS
    <details>
    <summary>Checkout JS</summary>

    ![bag js](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/validation/css/jshint/checkout_stripe_js.jpg)

* Image selector JS
    <details>
    <summary>Image Selector JS</summary>

    ![bag js](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/validation/css/jshint/image_selector_js.jpg)

* Products JS
    <details>
    <summary>Products JS</summary>

    ![bag js](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/validation/css/jshint/products_js.jpg)

* Profile JS
    <details>
    <summary>Profile JS</summary>

    ![bag js](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/validation/css/jshint/profile_js.jpg)

* Quantity Input JS
    <details>
    <summary>Quantity Input JS</summary>

    ![bag js](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/validation/css/jshint/quantity_input_js.jpg)

## Lighthouse:
* Scores were close to, or at 100%.

    <details>
    <summary>Lighhouse results</summary>
    
    ![homepage](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/lighthouse_scores/lighthouse1_homepage.jpg) 
    ![all_products](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/lighthouse_scores/lighthouse2_all_products.jpg) 
    ![all_face](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/lighthouse_scores/lighthouse3_all_face.jpg) 
    ![all_body](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/lighthouse_scores/lighthouse4_all_body.jpg)
    ![organics](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/lighthouse_scores/lighthouse5_organics.jpg)
    ![Product Detail](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/lighthouse_scores/lighthouse6_product_detail.jpg)
    ![How to Articles](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/lighthouse_scores/lighthouse7_howto_articles.jpg)
    ![How to Detail](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/lighthouse_scores/lighthouse8_howto_detail.jpg)
    ![Profile](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/lighthouse_scores/lighthouse8_howto_detail.jpg)
    ![Wishlist](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/lighthouse_scores/lighthouse10_wishlist.jpg)
    ![Bag](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/lighthouse_scores/lighthouse11_bag.jpg)
    ![Checkout](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/lighthouse_scores/lighthouse12_checkout.jpg)
    ![Checkout success](https://github.com/RozWelch/pureglow/blob/main/documentation/readme_images/lighthouse_scores/lighthouse13_checkout_success.jpg)



# Testing

* Link to testing and results: [Testing](https://github.com/RozWelch/pureglow/blob/main/TESTING.md)

# Project Creation and Deployment

The project was created in Git Hub using the Code Institute template.
The project was deployed using Heroku.
Deployment setup can be viewed here: [Deployment](https://github.com/RozWelch/pureglow/blob/main/DEPLOY.md)

# Credits
* Code Institue's 'Boutique Ado' tutorial
* All images used are from Freepix: www.freepix.com
* How To articles: https://www.nytimes.com/guides/tmagazine/skincare-routine
* W3Schools
* Django Documentation
* Bootstrap Documentation
* Stack Overflow
* Animated Background tutorial: https://codepen.io/P1N2O/pen/pyBNzX
* Terms & Conditions generatior: https://app.websitepolicies.com/

# Acknowledgements
Thanks to my mentor, my facilitator, my fellow students on Slack, tutoring support and to my friends for helping test the site.
