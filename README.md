# <p align="center"> The Dog Shop: Milestone Project 4

![Responsive Designs](static/images/readme_images/readme-image-main.png)

### <p align="center">The image above is a visual of the site displayed on different devices using [I Am Responsive](http://ami.responsivedesign.is/#)

### <p align="center">You can view the live site here: [www.the-dog-shop.com](https://the-dog-shop.herokuapp.com//)

--- 

## <p align="center"> Introduction

Welcome to The Dog Shop - a dedicated store for site users to purchase dog related products. The site also has a dedicated blog section where our dog experts post relevant articles related to dog’s health and wellbeing. Site users can interact with blog posts by adding comments on posts and interacting with other site users. The store is of course fictional and for educational purposes only. 

I built this e-commerce site for my 4th and final milestone project he Code Institutes Full Stack Software Development Course. The overall goal of the project was to design, build and launch a full stack django based software app, that allows users to create an account, be authenticated, store and manipulate data, and purchase products using the stripe payment platform. Due to the nature of the site, additional authentication and validation protocols have been used to prevent unintended use of the site.  

--- 

## Contents

- [**User Experience (UX)**](#ux)
  - [User Stories](#user-stories)
  - [Strategy](#strategy)
    - [_External user’s goal_](#external-user’s-goal)
    - [_Site owner's goal_](#external-user’s-goal)
  - [Scope](#scope)
    - [_Scope In_](#scope-in)
    - [_Scope Out_](#scope-out)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
    - [_Wireframes_](#mobile-wireframes)
  - [Surface](#surface)
    - [_Design_](#design)
    - [_Colour_](#colour)
    - [_Typography_](#typography)
- [**Data Set Up**](#data-set-up)
    - [_Database Design_](#cdata-base-design)
- [**Features**](#features)
  - [_Existing Features_](#existing-features)
  - [_Features Left to Implement_](#features-left-to-implement)
- [**Technologies Used**](#technologies-used)
  - [_Languages_](#languages)
  - [_Frameworks & Libraries_](#frameworks-and-libraries)
- [**Testing**](#testing)
- [**Version Control Management**](#version-control-management)
- [**Deployment**](#deployment)
  - [_Deployment Steps_](#deployment-steps)
  - [_How To run this Project Locally_](#how-to-run-this-project-locally)
- [**Credits**](#credits)
  - [_Content_](#content)
  - [_Media_](#media)
  - [_Code_](#code)
- [**Resources**](#resources)
- [**Acknowledgements**](#acknowledgements)

---

## <p align="center"> UX

### User Stories

|   As A       |  I want to be able to...                                |   So that I can...                                       |
| :----------  | :-------------------------------------------------------|----------------------------------------------------------|
| Site User    | Navigate through the site easily                        | Purchase quickly and efficiently                         |
| Site User    | View individual products details                        | Decide if the product is what I need                     |
| Site User    | Search for products on the site                         | Find what I need quickly                                 |
| Site User    | Understand why I need to create and account             | Make a decision on where to share my personal details    |
| Site User    | Make a purchase without having to create an account     | Do not need to share my personal details                 |
| Site User    | Create an account                                       | Save my personal information                             |
| Site User    | Create an account                                       | Comment on and share opinions on recent blog posts       |
| Site User    | Receive email confirmation when creating an account     | Have confirmation that it was successful                 |
| Site User    | Reset my password                                       | Access my account if I forget my password                |
| Site User    | Have a personal profile page                            | View my order history                                    |
| Site User    | Select quantity of individual products                  | Purchase the right quantity I require                    |
| Site User    | Be able to delete any personal comments posted          | Full control over my content                             |
| Site User    | Be notified when I add a product to my shopping bag     | I can easily see what I am buying                        |
| Site User    | See the total cost of my purchase before paying         | Know how my will be charged to be debit/credit card      |
| Site User    | See a payment success or failure message                | Verify that my purchase has been successful              |
| Site User    | Receive a confirmation email after making a purchase    | Have a receipt and record of my purchase                 |
| Site Owner   | Add products to the store from the front end            | Quickly add new products to the site                     |
| Site Owner   | Edit products on the front end                          | Update products details on the site                      |
| Site Owner   | Delete products from the front end                      | Remove products from the site                            |
| Site Owner   | Add blog posts to the site                              | Share relevant information and engage with the site user |
| Site Owner   | Edit blog posts on the site                             | Update the content easily                                |
| Site Owner   | Save draft blog posts in my profile                     | Access and finish at a later time before posting to the site |
| Site Owner   | View all saved draft blog posts in my admin profile     | Easily see all unpublished blog posts                    |
| Site Owner   | Delete blog posts from site                             | Remove content from the site                             |
| Site Owner   | Delete site user comments                               | So that I can remove comments that are not appropriate   |

--- 

### Strategy

#### External user’s goal

> - Easily navigate a consumer website to find the products that I’m interested in. 
> - Creating an account should be seamless and not require too much personal information or questions. 
> - Checking out should be simple and easy to understand, I should know exactly what is in my basket and how much I am going to pay. 
> - Adding comments and interacting with blog posts should be simple, and I should have control over my content by being able to delete posts whenever I decide to do so. 


#### Site owner's goal

> - Create a site that provides specific information to a targeted audience. 
> - Create a site that allows site users to easily navigate products, having the ability to search and sort different product types and view individual product details - price, ratings etc. 
> - Create a site that allows users to create an account, enabling them to store their information for quicker checkout. 
> - reate a site that is user friendly and visually indicates when the user has actioned a specific event - like a pop up when adding a product to their shopping bag.
> - Share content to engage site users. Allows users to read and interact with relevant content (Blog Posts) by having the ability to post comments / share opinions on individual articles. 
> -  Create a business revenue stream by targeting a specific market with relevant products.


### Scope

#### Scope In

- A homepage that instantly and visually demonstrates what the site’s overall purpose is.
- A one page home page that provides a link to the site product page.
- A nav bar that provides easy navigation to different product ranges. 
- A search bar within the navbar throughout the site to allow users to quickly find relevant products. 
- Product page that visually shows price, ratings and an image. 
- Product details page that shows individual product information with quantity selector. 
- Sorting functionality to allow the site user to sort by price, rating, name or category. 
- Shopping bag icon in the navbar throughout the site, with visual indication of the users total spend. 
- My account section that allows customers to create an account, as well as logging in and out of existing accounts. 
- Dedicate profile page where site users can save their delivery information and view their order history. 
- Active email receipts for account creation verification, password reset, and purchase receipts. 
- Dedicated Blog Page that allows the site owner to post, edit and delete content. 
- Comments structure that allows site users to comment on individual blog posts when signed into their account.
- Site owner ability to add, edit and remove products from the store.
- Site owner admin privileges to remove site user comments.
- Site owner only ability to add, edit and delete blog posts.
- Site owner ability to save draft blog posts in their user profile.
- Stripe payments integration.

#### Scope out

- Ability to create an account or sign in using social media accounts.
- Ability to add ratings to products.
- Ability for site users to add blog posts.
- Mandatory account creation - account creation only required to save personal information, shopping bag items between sessions or post comments to published blog posts. 
- Site user ability to reply directly to other site user comments. 
- Ability to like, up, or downvote other site user comments. 
- Ability to save payment information. 
- Ability to use google, android or alternative payment payment methods. 
- Requirement for site owners to approve site users comments before being published. 

--- 


