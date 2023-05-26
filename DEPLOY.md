The project was created in Git Hub using the Code Institute template.
# DEPLOYMENT PROCESS

## To Fork the site
Locate the repository at this link LINK
* At the top right of the repository, select 'Fork' from the menu
* A copy of the repository is now created

## Cloning the repository
* Locate the repository at this LINK
* Under 'Local', there is cloning options: HTTPS, SSH, GitHub CLI. Click the prefered cloning option, and then copy the link provided.
* Open the terminal
* In the terminal change the current working directory to where you wish to put the cloned directory
* Type: 'git clone', then paste the URL already copied from GitHub earlier
* Press Enter. Your local clone will be created.

# Deployment from Heroku:
* Login to Heroku (https://www.heroku.com/) or create an account
* On the main page, click the 'New' button in the top right corner, select 'Create New App' from the menu
* Choose a name and select your region, then click on the 'Create App' button
* Choose Github as the deployment method, then select the correct repository, and click the connect button
* Select the Settings tab
* Click Reveal Config Vars SCREENSHOT
* Add Config Vars settings and values as below:
* AWS_ACCESS_KEY_ID From: AWS - CSV file - see AWS section below
* AWS_SECRET_ACCESS_KEY From: AWS - CSV file - see AWS section below
* DATABASE_URL From: ElephantSQL Postgres - see ElephantSQL section
* EMAIL_HOST_PASS From: Password from email client
* EMAIL_HOST_USER From: Site's email address
* SECRET_KEY From: Random key generated with secret key generator LINK
* STRIPE_PUBLIC_KEY From the Developers tab on Stripe - API Keys /Publishable key
* STRIPE_SECRET_KEY From the Developers tab on Stripe - API Keys /Secret key
* STRIPE_WH_SECRET From the Developers tab on Stripe - Webhooks /site endpoint /Signing secret
* USE_AWS Set to: True when AWS is set up

* Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
* Scroll to the bottom of the deploy page and select the preferred deployment type
* NB: Ensure in Django settings, DEBUG is False
* Click 'Enable Automatic Deploys' if you wish to automatically deploy when you push updates to Github

# Setting up your ElephantSQL database
* Login or create and account on https://www.elephantsql.com/
* Click 'Create new instance' green button on top right
* Give your project a name
* Select the 'Tiny Turtle (free)' plan
* Click the green button on bottom right
* Select your region
* Click the 'Review' green button on bottom right
* If all details are correct, click green 'Create instance' button on bottom right
* Go to your 'Details' tab to find the URL for your database LINK

# Setting up your AWS S3 Bucket (Image storage)
* Login or create an AWS account
* On the AWS Management Console, Services tab - search 'S3' and select
* Click 'Create a new bucket', give it a name(use Heroku app name if possible), and choose your region
* Under 'Object Ownership' select 'ACLs enabled' - leave the Object Ownership as Bucket owner preferred
* Uncheck block all public access and acknowledge that the bucket will be public
* Click 'Create bucket'
* Open your created bucket, go to the 'Properties' tab. Scroll to the bottom and under 'Static website hosting' click 'edit' and change the Static website hosting option to 'enabled'
* Copy the default values for the index and error documents and click 'save changes'
* Open the 'Permissions' tab, locate the CORS configuration section and add the following code:
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
* In the 'Bucket Policy' section and select 'Policy Generator'
* Choose 'S3 Bucket Policy' from the type dropdown
* In 'Step 2: Add Statements' add the following settings:
Effect: Allow
Principal: *
Actions: GetObject
ARN: Bucket ARN (copied from S3 Bucket page)
* Click 'Add Statement'
* Click 'Generate Policy'
* Copy the policy from the popup
* Paste the generated policy into the Permissions > Bucket Policy area
* Add '/*' at the end of the 'Resource' key, and save
* Go to the 'Access Control List' section click edit and enable List for Everyone (public access) and accept the warning

