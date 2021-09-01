# <p align="center">Testing

### W3C Validation

The following pages were passed through the official W3C validation site with no errors returning:

- index.html: No errors or warnings to show.
- products.html: No errors or warnings to show.
- product_detail.html: No errors or warnings to show.
- checkout.html: No errors or warnings to show.
- checkout-success.html: No errors or warnings to show.
- blog.html: No errors or warnings to show.
- blog_detail.html: No errors or warnings to show.

![HTML Validator Results](documents/images/readme_images/html_validator.png)

- base.css: Congratulations! No Error Found.

![Duplicate ID Error](documents/images/readme_images/css_validator.png)

Blog and Product editing pages:
- Edit-post.html
- Edit_product.html

Site validation on both these pages failed due to a Duplicate ID error:  

![Duplicate ID Error](documents/images/readme_images/dup-id-image-error.png)

This is explained more in the Fixed Bugs section.

- Bag.html: 

Site validation failed on this page also due a different Duplicate ID error: 

![Duplicate ID Error](documents/images/readme_images/dup-id-error-bag.png)

Resolution details contained in the fixed bugs section.


### JSHint

The following files were passed through JSHint with no warnings detected.

- blog_elements.js
- product_elemets.js
- strip_elements.js

stripe_elements.js threw up some errors which were resolved by adding `/*jshint esversion: 6 */` to the top of the file. One additional error remained which was a missing semi collon. 

![JShint Results](documents/images/readme_images/js-hint.png)

### PEP8 Python Validator

PEP8 was used to ensure that all Python code meets PEP8 requirements. All .py files in this project were passed through the PEP8 Python Validator successfully. 

### Browser Validation
- In addition to testing on google chrome, I tested the site fully on the Safari and Firefox browsers.
- Firefox: All tests successful.
- Safari: All tests successful.

### Manual Device Check:

I checked the site manually on the following devices - all pages check checked separately.
- Samsung S10
- Iphone X
- Macbook Pro 
- Dell Laptop
- Ipad Pro
- Samasung Tablet
- Monitor Screen 

#### Link And Hover Validation
I went through each page individually to manually check that all links & hover styling worked as intended. This test was performed on both mobile and desktop devices. 

index.html: 
> - First call to action link on the hero image.
> - Nav Bar: All product links.
> - My account when not logged in state: 
>   - Register, 
>   - Log in. 
> - My Account when logged in state: 
>   - Product Admin, 
>   - Blog Admin, 
>   - My Profile, 
>   - Log Out.

Products.html
> - Product image link 
> - Edit product link
> - Delete product modal

Product_detail.html
>  - Quantity selector
>  - Continue shopping link
>  - Add to bag link
>  - Bag Toast Pop Up
>  - Secure checkout link 

Bag.html
>  - Quantity selector
>  - Continue shopping link
>  - Secure checkout link

Checkout.html
> - Adjust bag link 
> - Complete order link 
> - Checkout_success.html: back to store link

Blog.html
> - Readmore link 

Blog_detail.html
> - Edit blog button
> - Delete blog button
> - Submit comment
> - Delete comment 

Product Admin
> - Add Product and image

Blog Admin
> - Add blog and image
> - Save blog and image

### Form Validation

- Sign in form: 
    - Checked on both mobile, ipad and desktop devices. 
    - Submit form without username added to ensure input field ‘required’ attribute was working correctly and alert displayed prompted customer to add input. 
    - Submit form without password added to ensure input field ‘required’ attribute was working correctly and alert displayed prompted customer to add input.

- Sign up form 
    - Checked on both mobile, ipad and desktop devices. 
    - Submit form without email address added to ensure input field ‘required’ attribute was working correctly and alert displayed prompted customer to input email address. 
    - Submit form without name added to ensure input field ‘required’ attribute was working correctly and alert displayed prompted customer to input email address.

- Add Product Form: 
    - Submitted fully filled in product and reviewed on main products page to ensure review displayed as intended. 
    - Tested adding images.
    - Checked Django Admin to ensure data captured correctly

- Add Blog Form: 
    - Submitted fully filled in blog post and reviewed on blog page to ensure new blog displayed as intended. 
    - Checked Django Admin to ensure data captured correctly
    - Tested adding images.

- Edit Product Form: 
    - Submitted fully filled in product edit and reviewed on product page to ensure new product displayed as intended. 
    - Tested adding new images.
    - Checked Django Admin to ensure data captured correctly

- Edit blog Form: 
    - Submitted fully filled in blog edit and reviewed on blog page to ensure new updated blog displayed as intended. 
    - Tested adding new images.
    - Checked Django Admin to ensure data captured correctly

- Delete Modal: 
  - Fully tested delete model for both product, blog and comments items to ensure modal pop up was presented as intended, and that product/blog/comment was deleted on confirmation. 
  - Checked Django Admin to ensure product/blog removed.

- Password Reset form
  - Checked on both mobile, ipad and desktop devices. 

### Additional Manual Testing:
Super user/admin user has access to the:
- Access to the django admin panel.
- Ability to add and edit products on the main products and individual products pages.
- Product admin page to add products directly to store.
- Superuser only profile page which shows unpublished blogs.
- Blog admin page to add blogs directly to store, or create drafts with ability to save for later. 
- Ability to delete all user comments on blog posts

Toast pop ups display when:
- a site user creates and account, signs in or logs out of their account
- a user adds a product to their bag
- a user updates a product in their bag.
- A user updates information in their profile
- A user makes a purchase
- A user adds or deletes a comment
- An Admin edits or deletes a product 
- An Admin edits or deletes a blog post
- A user attempts to access or use an site owner only page
- An Admin deletes a blog post or comment

### Email Validation

Email verification sent succesfull when account created with link tested:

![email verification](documents/images/readme_images/email-verification.png)

Email order confirmation sent succesfully after payment succesful with link tested:

![order confirmation email](documents/images/readme_images/email-subject.png)

![order confirmation email](documents/images/readme_images/email-body.png)

### Image Validation

-   I went through each page to ensure all images displayed correctly. 
-   I went through each file to ensure all Alt Text had been applied correctly to each image url to validate accessibility requirements.
- the image rendered on the edit product/blog form was squashed. I will look to improve this in a future release as this is not displayed on the customer facing part of the site, so less of a priority.

### Site Performance Validation

#### First Test

![Lighthouse Report](documents/images/readme_images/lighthouse_image-1.png)

The first report from lighthouse returned poor scores for best practice. Reasons outlined below. 

- Best Practices: Failing elements where:
  - Content Best PracticesFormat your HTML in a way that enables crawlers to better understand your app’s content.
  - Document does not have a meta description

To reseove this I added a meta description tag: `<meta name="description" content="Animal products and services - The Dog Shop"/>`

#### Second Test

With this issues fixed, the site now returns a stronger lighthouse performance score across all key measures:

![Lighthouse Report](documents/images/readme_images/lighthouse_image-2.png)

lighthouse perfromance testing was then carried out on all othersite pages. 

### Stripe Testing

I tested Stripe payments by sending test webhooks: All tests successful.

![Stripe Tests](documents/images/readme_images/stripe-wh.png)

### Error Handling 

To ensure that any site error is handled gracefully, a 404 and 505 error handler function was added to the page. The site was tested on all pages to generate the 404 message, which displays a simple message to the user, with a redirect to the home page.

![404](documents/images/readme_images/404_505_error.png)

### Deployment Version 

All testing was completed in both the development version of the site and the deployed version of the site. 

## User Story Testing

## <p align="center"> AS A SITE USER


> I WANT TO BE ABLE TO: Navigate through the site easily<br>
SO THAT I CAN: Purchase quickly and efficiently<br>

![User-story-1](documents/images/readme_images/user-story-1.png)

> I WANT TO BE ABLE TO: View individual products details<br>
SO THAT I CAN: Decide if the product is what I need<br>

![User-story-2](documents/images/readme_images/user-story-2.png)

> I WANT TO BE ABLE TO: Search for products on the site <br>
SO THAT I CAN: Find what I need quickly <br>

![User-story-3](documents/images/readme_images/user-story-3.png)

> I WANT TO BE ABLE TO: Understand why I need to create and account <br>
SO THAT I CAN: Make a decision on where to share my personal details <br>

> I WANT TO BE ABLE TO: Make a purchase without having to create an account <br>
SO THAT I CAN: Do not need to share my personal details <br>

![User-story-4](documents/images/readme_images/user-story-4.png)

> I WANT TO BE ABLE TO: Create an account <br>
SO THAT I CAN: Save my personal information<br>

![User-story-5](documents/images/readme_images/user-story-5.png)

> I WANT TO BE ABLE TO: Create an account <br>
SO THAT I CAN: Comment on and share opinions on recent blog posts<br>

![User-story-6](documents/images/readme_images/user-story-6.png)

> I WANT TO BE ABLE TO: Receive email confirmation when creating an account <br>
SO THAT I CAN: Have confirmation that it was successful<br>

![email verification](documents/images/readme_images/email-verification.png)

> I WANT TO BE ABLE TO: Reset my password <br>
SO THAT I CAN: Access my account if I forget my password<br>

![User-story-7](documents/images/readme_images/user-story-7.png)

> I WANT TO BE ABLE TO: Have a personal profile page <br>
SO THAT I CAN: View my order history <br>

![User-story-8](documents/images/readme_images/user-story-8.png)

> I WANT TO BE ABLE TO: Select quantity of individual products <br>
SO THAT I CAN: Purchase the right quantity I require <br>

![User-story-9](documents/images/readme_images/user-story-9.png)

> I WANT TO BE ABLE TO: Be able to delete any personal comments posted <br>
SO THAT I CAN: Full control over my content <br>

![User-story-10](documents/images/readme_images/user-story-10.png)

> I WANT TO BE ABLE TO: Be notified when I add a product to my shopping bag <br>
SO THAT I CAN: I can easily see what I am buying<br>

![User-story-12](documents/images/readme_images/user-story-12.png)

> I WANT TO BE ABLE TO: See the total cost of my purchase before paying <br>
SO THAT I CAN: Know how my will be charged to be debit/credit card<br>

![User-story-13.1](documents/images/readme_images/user-story-13.1.png)
![User-story-13](documents/images/readme_images/user-story-13.png)

> I WANT TO BE ABLE TO: See a payment success or failure message<br>
SO THAT I CAN: Verify that my purchase has been successful<br>

![User-story-14](documents/images/readme_images/user-story-14.png)

> I WANT TO BE ABLE TO: Receive a confirmation email after making a purchase<br>
SO THAT I CAN: Have a receipt and record of my purchase<br>

![order confirmation email](documents/images/readme_images/email-subject.png)

![order confirmation email](documents/images/readme_images/email-body.png)

## <p align="center"> AS A SITE OWNER

> I WANT TO BE ABLE TO: Add products to the store from the front end <br>
SO THAT I CAN: Quickly add new products to the site <br>

![User-story-15](documents/images/readme_images/user-story-15.png)

> I WANT TO BE ABLE TO: Edit products on the front end <br>
SO THAT I CAN: Update products details on the site <br>

![User-story-16](documents/images/readme_images/user-story-16.png)

> I WANT TO BE ABLE TO: Delete products from the front end <br>
SO THAT I CAN: Remove products from the site <br>

![User-story-17](documents/images/readme_images/user-story-18.1.png)

> I WANT TO BE ABLE TO: Add blog posts to the site <br>
SO THAT I CAN: Share relevant information with the site user <br>

![User-story-19](documents/images/readme_images/user-story-17.png)

> I WANT TO BE ABLE TO: Edit blog posts on the site <br>
SO THAT I CAN: Update the content easily <br>

![User-story-20](documents/images/readme_images/user-story-18.png)

> I WANT TO BE ABLE TO: Save draft blog posts in my profile <br>
SO THAT I CAN: Access and finish at a later time before posting to the site <br>

> I WANT TO BE ABLE TO: View all saved draft blog posts in my admin profile <br>
SO THAT I CAN: Easily see all unpublished blog posts<br>

![User-story-4](documents/images/readme_images/user-story-19.1.png)
![User-story-4](documents/images/readme_images/user-story-19.png)

> I WANT TO BE ABLE TO: Delete blog posts from site<br>
SO THAT I CAN: Remove content from the site <br>

![User-story-4](documents/images/readme_images/user-story-20.png)