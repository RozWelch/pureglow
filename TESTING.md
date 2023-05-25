# Browser and Devices Tests
## Browsers: tested on Google Chrome and Safari browsers with no issues noted.
## Devices: viewed on the following devices to check responsiveness: iPhone 11 Pro, iPhone 14, Samsung Galaxy, iPad, iMac pro 15in screen, iMac 27in screen
## Chrome Developer tools: checked multiple device sizes to check responsiveness

# Manual Testing
## Site Navigation
| Page Element | Action | Expected Result | Pass/Fail  |
| -- | -- | -- | -- |
| Main header      |         |      |   |
| pure glow logo      | Click       | goes to homepage   | Pass |
| Search bar      | Enter text and click the search icon | Searches the title and description for the text   | Pass |
| 'My Account' Dropdown Menu      | Click       | Opens profile dropdown   | Pass |
| 'My Account' Register link      | Click       | Opens Sign up page   | Pass |
| 'My Account' Login link      | Click       | Opens Sign in page   | Pass |
| 'My Account' Login and Register only show to logged out users |         | Opens Sign in page   | Pass |
| 'My Account' (only shown if logged in user) My Profile link  | Click       | Opens My Profile page   | Pass |
| 'My Account' (only shown if logged in superuser) Add a product  | Click       | Opens Add product page   | Pass |
| 'Wishlist' (only show if logged in user)  | Click       | Opens Wishlist page   | Pass |
| 'My Account' (only show if logged in user) Logout link      | Click       | Opens Log out page   | Pass |
| 'Shopping bag icon'| Click       | Opens Shopping bag page   | Pass |
|Mobile Header Navigation |   |   |  
| Search icon | Click | Opens search box | Pass |
| Search bar Function | Enter text and click the search icon | Searches the title and description for the text | Pass |
| 'My Account' Dropdown | Click | Opens dropdown menu | Pass |
| 'My Account' (only show if logged out) Sign Up Link | Click | Opens to Sign Up page | Pass |
| 'My Account' (only show if logged out user) Login Link | Click | Opens to login page | Pass |
| 'My Account' (only show if logged in user) Product Management | Click | Opens to Product Management page | Pass |
| 'My Account' (only show if logged in user) My profile | Click | Opens My Profile page | Pass |
| 'My Account' (only show if logged in user) My wishlist | Click | Opens wishlist page | Pass |
| 'My Account' (only show if logged in user) Logout | Click | Opens logout page | Pass |
| 'Shopping bag icon'| Click | Opens Shopping bag page | Pass |
| Main Nav |   |   |  
| 'All products' dropdown-by price | Click | Opens Products sorted by price | Pass |
| 'All products' dropdown-by category | Click | Opens Products sorted by category | Pass |
| 'All products' dropdown-all products | Click | Opens all Products | Pass |
| 'Face' dropdown-moisturiser | Click | Opens Face-moisturisers products | Pass |
| 'Face' dropdown-cleansers | Click | Opens Face-cleansers products | Pass |
| 'Face' dropdown-Masks and treatments | Click | Opens Face-masks and treatments products | Pass |
| 'Face' dropdown-all face | Click | Opens all Face products | Pass |
| 'Body' dropdown-moisturiser | Click | Opens Body-moisturisers products | Pass |
| 'Body' dropdown-Bath and Shower | Click | Opens Body-Bath and shower products | Pass |
| 'Body' dropdown-All body | Click | Opens All Body products | Pass |
| 'Organic' dropdown-face | Click | Opens Organic-face products | Pass |
| 'Organic' dropdown-body | Click | Opens Organic-body products | Pass |
| 'Organic' dropdown-all organic | Click | Opens All Organic products | Pass |
| 'How To' | Click | Opens All 'How To' Articles | Pass |
| Hamburger Menu | Responsive | Displayed when screen size is smaller size devices | Pass |
| Home Link -only on smaller size devices | Click | Redirects to home | Pass |
| Footer |   |   |  
| Social Media Icons | Click | Open correct link in new tab | Pass |
| Newsletter Email field | Insert incorrect/empty format | On submit: form won't submit | Pass |
| Newsletter Email field | Insert incorrect/empty format | Error message displayed | Pass |
| Subscribe Button | Click | Form submit | Pass |
| Subscribe Button | Click | 'Thank You for subscribing!' message displayed | Pass |
| 'Our Products' link | Click | Opens products page | Pass |
| 'Terms & Conditions' Link | Click | Opens Terms & Conditions page | Pass |
| Privacy Policy Link | Click | Open privacy policy page in new tab | Pass |
| Home page |   |   |  
| 'Shop Now' button | Click | Opens Products page | Pass |
| Animated gradient on free delivery banner |  | Displays animated gradient | Pass |
| All Auth account pages |   |   |  
| Sign Up |   |   |  
| Sign in link | Click | Redirects to sign in page | Pass |
| Email field | Inserted incorrect format | Form doesn't submit when submit button clicked  | Pass |
| Email field | Inserted incorrect format | Error message displayed | Pass |
| Email field | Inserted correct format | On submit-form submitted | Pass |
| Email field | Left empty | On submit-form not submitted | Pass |
| Email field | Duplicate email inserted | On submit-form not submitted | Pass |
| Email field | Duplicate email inserted | Error message displayed | Pass |
| Email Confirmation field | Insert different email | On submit-form not submitted | Pass |
| Email Confirmation field | Insert different email | Error message displayed | Pass |
| Username field | Left empty or incorrect format | On submit-form not submitted | Pass |
| Username field | Left empty or incorrect format | Error message displayed | Pass |
| Username field | Insert correct format | On submit-form submitted | Pass |
| Username field | Insert duplicate username | On submit-form not submitted | Pass |
| Username field | Insert duplicate username | Error message displayed | Pass |
| Password field | Insert incorrect format or length | On submit-form not submitted | Pass |
| Password field | Insert incorrect format or length | Error message displayed | Pass |
| Password field | Passwords didn't match | On submit-form not submitted | Pass |
| Password field | Passwords didn't match | Error message displayed | Pass |
| Password field | Insert correct format and password matches | On submit-form submitted | Pass |
| Sign Up button(valid form) | Click | Form submits | Pass |
| Sign Up button(valid form) | Click | Redirect to Email verification page | Pass |
| Sign Up button(valid form) | Click | Alert message - confirming email sent | Pass |
| Confirmation Email confirm link | Click | Opens confirm Email address Page | Pass |
| Confirm Button | Click | Success message - confirming new users | Pass |
| Confirm Button | Click | Redirect to sign in page | Pass |
| Log in |   |   |  
| Sign up link | Click | Redirects to sign up page | Pass |
| Username field | Left empty | On submit-form not submitted | Pass |
| Username field | Left empty | Error message displayed | Pass |
| Username field | Insert wrong username | On submit-form not submitted | Pass |
| Username field | Insert wrong username | Error message displayed | Pass |
| Password field | Left empty | On submit-form not submitted | Pass |
| Password field | Left empty | Error message displayed | Pass |
| Password field | Wrong password entered | On submit-form not submitted | Pass |
| Password field | Wrong password entered | Error message displayed | Pass |
| Login button(form valid) | Click | Form submits | Pass |
| Login button(form valid) | Click | Redirects to home page | Pass |
| Login button(form valid) | Click | Success message - confirming login | Pass |
| Forgot password link | Click | Redirects to password reset page | Pass |
| Email field | Leave empty or incorrect format | On submit-form not submitted | Pass |
| Reset password button | Click | Confirmation message - email sent | Pass |
| Password reset Email link | Click | Opens change password page | Pass |
| Change Password button | Click | Success message - confirming Password changed | Pass |
| Sign out Confirmation |   |   |  
| Sign out button | Click | Redirects to homepage | Pass |
| Sign out button | Click | Success message -confirming signed out | Pass |
| All Products page |   |   |  
| 'Sort By' selector(price/name/category) | Click | Orders products correctly | Pass |
| Product selected by a category | Displayed | Category name(s) shown under heading | Pass |
| Number of products | Displayed | Displays the correct number of products on page | Pass |
| Product Image | Hover | Changes image opacity | Pass |
| Product Card | Click | Redirects to product's details page | Pass |
| If superuser: Edit link | Click | Redirects to edit product page | Pass |
| If superuser: Delete link | Click | Opens delete confirmation page | Pass |
| Delete cancel button | Click | Redirect to Products page | Pass |
| Delete - confirm button | Click | Deletes the product | Pass |
| Delete - confirm button | Click | Success message - 'Success, your product is deleted!' | Pass |
| Products Management |   |   |  
| Add a product | Superuser only | If a user that is logged out tries to add a product by changing the url, they are redirected to the  sign in page | Pass |
| Required text field | Left blank | On Submit-warning message - form won't submit | Pass |
| Required text field | Inputs whitespace | On Submit - form won't submit | Pass |
| SKU | Duplicate sku | On Submit-warning message - form won't submit | Pass |
| 'Select Image' button | Click | User can browse to image | Pass |
| 'Select Image' button | Display | Image name is displayed when selected | Pass |
| 'Select Image' button | Display | Placeholder image is used if no image selected | Pass |
| 'Cancel' button | Click | Redirect to Products page | Pass |
| 'Add Product' button | Click (valid form) | Form submits | Pass |
| 'Add Product' button | Click (valid form) | Redirects to Product detail page for new product with all information displayed | Pass |
| 'Add Product' button | Click | Success message appears informing the superuser that the product has been added | Pass |
| Edit Product |   |   |  
| Edit Product | Superuser only | If a user that is logged out tries to edit a product by changing the url, they are redirected to the sign in page | Pass |
| Edit Product Form | Display | Form has all fields pre-populated with the product details  | Pass |
| Edit Product Form | Image Field | Thumbnail of product image shown | Pass |
| Required text field | Left blank | On Submit -warning - form won't submit | Pass |
| Required text field | Input whitespace | On Submit- form won't submit | Pass |
| 'Cancel' button | Click | Redirects to Products page | Pass |
| 'Submit' | Click (valid form) | Form submit | Pass |
| 'Edit' button | Click(valid form) | Redirect to Product detail page for new product with product information | Pass |
| 'Edit' button | Click(valid form) | Success message- product has been updated | Pass |
| Confirm Delete Product |   |   |   |
| Delete Product | Superuser only | If a user that is logged out tries to delete a product by changing the url, they are redirected to the sign in page | Pass |
| 'Cancel' delete button | Click | Redirect to Products page | Pass |
| 'Cancel' delete button | Click | Deletes product | Pass |
| 'Cancel' delete button | Click | Success message - confirming product deleted successfully | Pass |
| Shopping Bag |   |   |   |
| 'Keep Shopping' button | Click | Displayed if no items are in bag | Pass |
| 'Qty' button | Click | Increase or decrease quantity | Pass |
| 'Qty' button  | Click | Minus button disabled if quantity is 1 | Pass |
| 'Qty' button  | Click | Plus button disabled if quantity is 99 | Pass |
| 'Qty' button  | Manually Input >99 | Error message appears when refresh button is clicked | Pass |
| 'Qty' button  | Manually Input <1 | Shopping bag is emptied when refresh button is clicked | Pass |
| 'Update' button | Click | Update bag item quantity | Pass |
| 'Update' button | Refresh Icon button | Updated confirmation message displayed | Pass |
| 'Remove' button | Click | Remove item from bag | Pass |
| 'Remove' button | Click | Removed confirmation toast appears | Pass |
| Subtotal, Bag total, Delivery cost (or free delivery spend), Grand Total | Calculated | All numbers are calculated correctly | Pass |
| 'Keep Shopping' button | Click | Redirect to products page | Pass |
| 'Secure Checkout' button | Click | Redirect to checkout page | Pass |
| Checkout page |   |   |   |
| Checkout Page | User inputs url (if bag is empty) | redirect to products page | Pass |
| Checkout Page | User inputs url (if bag is empty) | Bag is empty message displayed | Pass |
| Form fields(logged in user) | On load | Form pre-populated with user profile info(if already saved) | Pass |
| Required text fields | Left blank | On submit-form doesn't submit | Pass |
| Required text fields | Left blank | Error message on invalid field | Pass |
| Required text fields | Whitespace only entered | On submit - forms doesn't submit | Pass |
| Required text fields | Whitespace only entered | Error message on invalid field | Pass |
| Required text fields | Filled in correctly | On submit - forms submits | Pass |
| Phone number field | Left blank | On submit:form won't submit | Pass |
| Phone number field | Left blank | Error message on invalid field | Pass |
| Phone number field | Whitespace only entered | On submit - forms doesn't submit | Pass |
| Phone number field | Whitespace only entered | Error message on invalid field | Pass |
| Phone number field | Non-numeric characters entered | On submit - forms doesn't submit | Pass |
| Phone number field | Non-numeric characters entered | Error message on invalid field | Pass |
| Email field | Left blank | On submit - forms doesn't submit | Pass |
| Email field | Left blank | Error message on invalid field | Pass |
| Email field | Whitespace only entered | On submit - forms doesn't submit | Pass |
| Email field | Whitespace only entered | Error message on invalid field | Pass |
| Email field | Fill in correctly | On submit - forms submits | Pass |
| 'Save to my profile' checkbox | Shown if user logged in | Shown | Pass |
| 'Login to save this info' | Shown if user not logged in | Shown | Pass |
| 'Save to my profile' checkbox | Checked | On submit- information saved to user profile | Pass |
| 'Save to my profile' checkbox | Unchecked | On submit - information not saved to user profile | Pass |
| Payment card input | Input invalid card number | Error message on field | Pass |
| Payment card input | Input invalid date | Error message on field |  
| 'Adjust Bag' button | Click | Redirects to bag page | Pass |
| 'Complete Order' button(form invalid) | Click | Form doesn't submit | Pass |
| 'Complete Order' button(form invalid) | Click | Error message on invalid fields | Pass |
| 'Complete Order' button(form valid) | Payment successful | Loading screen displayed | Pass |
| 'Complete Order' button(form valid) | Payment successful | Form submits | Pass |
| 'Complete Order' button(form valid) | Payment successful | Redirect to order confirmation page | Pass |
| 'Complete Order' button(form valid) | Logged in user | Order saved to user profile | Pass |
| 'Complete Order' button(form valid) | Payment failed | Loading animation appears | Pass |
| 'Complete Order' button(form valid) | Payment failed | Form doesn't submit | Pass |
| 'Complete Order' button(form valid) | Payment failed | Error message | Pass |
| 'Complete Order' button(form valid) | Click | Success message appears - confirming order successful message | Pass |
| Checkout Success Page |   |   |  
| Order Confirmation info | Displayed | Displays order details | Pass |
| 'Back to our products' button | Click | Redirect to Products page | Pass |
| Profile Page |   |   |  
| Profile Page access | Access | If a user tries enter the profile page with out logged in, they are directed to the sign in page | Pass |
| Form fields | On load | Form is pre-populated with user info (if previously saved) | Pass |
| All profile fields | Leave blank | On submit - form submits | Pass |
| All profile fields | Whitespace entered | On submit - form submits | Pass |
| All profile fields | Filled in correctly | On submit - form submits | Pass |
| 'Update Information' button | Click | Form submits | Pass |
| 'Update Information' button | Click | Success message - confirming profile successfully updated | Pass |
| Past order number | Click | Redirect to previous order page | Pass |
| Past order page |   |   |  
| Information Displayed | Displayed | All previous order info displayed correctly | Pass |
| Message | On load | Past confirmation order info message appears | Pass |
| 'Back to Profile' button | Click | Redirect to profile page | Pass |
