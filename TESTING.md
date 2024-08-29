# **Testing**

## **Manual Testing**
> **All Testings are done both on mobile and desktop devices.**
---

| Category | Feature | Expected Behaviour | Testing Method | Actual Behaviour | Result |
| :------- | :------ | :----------------- | :--------------- | :------------- | :----- |
| **Navigation bar** | Logo | Take user to home page when clicked | Clicked on logo | Takes to home page | **PASS &check;** |
| **Navigation bar** | Home link | Take user to home page when clicked | Clicked on home link | Takes to home page | **PASS &check;** |
| **Navigation bar** | Films link | Take user to films page when clicked | Clicked on films link | Takes to films page  | **PASS &check;** |
| **Navigation bar** | Signup link | Take user to Signup form when clicked | Clicked on Signup link | Takes to Signup page | **PASS &check;** |
| **Navigation bar** | Login link | Take user to Login form when clicked | Clicked on Login link | Takes to Login page | **PASS &check;** |
| **Navigation bar** | Recommend a movie link | Take user to Recommendation form when clicked | Clicked on Recommendation link | Takes to Recommend a movie page | **PASS &check;** |
| **Navigation bar** | Newsletter link | Take user to Newsletter form when clicked | Clicked on Newsletter link | Takes to Newsletter page | **PASS &check;** |

- Navigation bar is fully functional on mobile devices.

![Mobile nav-bar image](docs/features/nav-mobile.png)
![Mobile Dropdown nav-bar image](docs/features/nav-mobile-drop.png)
---

| Category | Feature | Expected Behaviour | Testing Method | Actual Behaviour | Result |
| :------- | :------ | :----------------- | :--------------- | :------------- | :----- |
| **Home Page** | Movie Carousel | The slide function should work without distortion, showing the latest movie posts. | Went to home page | The carousel slide works without any errors or image distortions. | **PASS &check;** |
| **Home Page**  | Carousel Movie Title & Genre link  | Take the user to the relevant movie post.(desktop only) | Clicked on title & genre | Takes to relevant movie post. | **PASS &check;** |
| **Home Page**  | Carousel Indicators | Control slides post to view.  | Clicked on indicators. | Changes which movie post is shown. | **PASS &check;** |

![Carousel image heading hover effect](docs/features/carousel-heading-img.png)
---

| Category | Feature | Expected Behaviour | Testing Method | Actual Behaviour | Result |
| :------- | :------ | :----------------- | :--------------- | :------------- | :----- |
| **Signup Page** | Username | Warn if username is already taken | Tried to signup with the superusername. | Warns that username is taken. | **PASS &check;** |
| **Signup Page** | Password | Warn if password doesnt contain at least 8 characters. | Tried to signup with password shorter than 8 characters. | Warns that password is too short. | **PASS &check;** |
| **Signup Page** | Password | Warn if password is a commonly used password. | Tried to signup with password "12345678" | Warns that password is commonly used. | **PASS &check;** |
| **Signup Page** | Password | Warn of password is entirely numeric. | Tried to signup with password "12345678"  | Warns that password is entirely numeric. | **PASS &check;** |
| **Signup Page** | Email    | Accept form submitton without a provided email. | Created an account without providing email adress. | Accepted the signup form without provided email adress. | **PASS &check;** |
| **Signup Page** | Signup form | Accept form submitton if if user data provided is suiting to above requirements. | Created a new account. | Accepted signup form. | **PASS &check;** |

![Password warning](docs/testing/password-common.png)
![Password warning](docs/testing/password-short.png)
![Username warning](docs/testing/username-taken.png)
---

| Category | Feature | Expected Behaviour | Testing Method | Actual Behaviour | Result |
| :------- | :------ | :----------------- | :--------------- | :------------- | :----- |
| **Login Page** |  |  |  |  | **PASS &check;** |
| **Login Page** |  |  |  |  | **PASS &check;** |
| **Login Page** |  |  |  |  | **PASS &check;** |
| **Login Page** |  |  |  |  | **PASS &check;** |
| **Login Page** |  |  |  |  | **PASS &check;** |
| **Login Page** |  |  |  |  | **PASS &check;** |
| **Login Page** |  |  |  |  | **PASS &check;** |

---
| Category | Feature | Expected Behaviour | Testing Method | Actual Behaviour | Result |
| :------- | :------ | :----------------- | :--------------- | :------------- | :----- |
| **Recommend a movie Page** |  |  |  |  | **PASS &check;** |
| **Recommend a movie Page** |  |  |  |  | **PASS &check;** |
| **Recommend a movie Page** |  |  |  |  | **PASS &check;** |
| **Recommend a movie Page** |  |  |  |  | **PASS &check;** |
| **Recommend a movie Page** |  |  |  |  | **PASS &check;** |
| **Recommend a movie Page** |  |  |  |  | **PASS &check;** |
| **Recommend a movie Page** |  |  |  |  | **PASS &check;** |


---
| Category | Feature | Expected Behaviour | Testing Method | Actual Behaviour | Result |
| :------- | :------ | :----------------- | :--------------- | :------------- | :----- |
| **Newsletter Page** |  |  |  |  | **PASS &check;** |
| **Newsletter Page** |  |  |  |  | **PASS &check;** |
| **Newsletter Page** |  |  |  |  | **PASS &check;** |
| **Newsletter Page** |  |  |  |  | **PASS &check;** |
| **Newsletter Page** |  |  |  |  | **PASS &check;** |
| **Newsletter Page** |  |  |  |  | **PASS &check;** |
| **Newsletter Page** |  |  |  |  | **PASS &check;** |

---
| Category | Feature | Expected Behaviour | Testing Method | Actual Behaviour | Result |
| :------- | :------ | :----------------- | :--------------- | :------------- | :----- |
| **Admin** |  |  |  |  | **PASS &check;** |
| **Admin** |  |  |  |  | **PASS &check;** |
| **Admin** |  |  |  |  | **PASS &check;** |
| **Admin** |  |  |  |  | **PASS &check;** |
| **Admin** |  |  |  |  | **PASS &check;** |
| **Admin** |  |  |  |  | **PASS &check;** |
| **Admin** |  |  |  |  | **PASS &check;** |
