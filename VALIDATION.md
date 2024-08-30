# **Validation**

# **Table of contents**

1. [**HTML Validation**](#html-validation)
    - [**Home Page**](#home-page)
    - [ **Films Page**](#films-page)
    - [**Recommend a Movie Page**](#recommend-a-movie-page)
    - [**Newsletter Page**](#newsletter-page)
    - [**Log out Page**](#log-out-page)
    - [**Sign Up Page**](#sign-up-page)
    - [**Login Page**](#login-page)
2. [**PEP8 Validation**](#pep8-validation)
3. [**JS Validation**](#js-validation)
4. [**CSS Validation**](#css-validation)
5. [**Lighthouse**](#lighthouse)



## **HTML Validation**

 - [W3C HTML Validator](https://validator.w3.org/) - is used to validate each pages source code.

### **Home Page**

> **Errors & Fix**
1. Error: Duplicate ID nav-item. | **Fix: Removed the redundant nav-item id's from list elements in base.html**
2. Error: Duplicate ID carousel-caption. | **Fix: Removed the redundant carousel-caption id's and added as class in index.html**
3. Error: Duplicate ID carousel-title. | **Fix: Removed the redundant carousel-title id's  and added as class in index.html**

> **Result**
| <span style="color:green">Document checking completed. No errors or warnings to show. &check;</span>
---

### **Films Page**

> **Errors & Fix**
1. Error: Duplicate ID card-title.| **Fix: Removed the redundant card-title id's from post link in films.html**
2. Error: Duplicate ID movie-summary| **Fix: Removed the redundant movie-summary id's from post link in films.html**

> **Result**
| <span style="color:green">Document checking completed. No errors or warnings to show. &check;</span>
---

### **Movie Detail Page**

> **Errors & Fix**
1. Error: Attribute comment_is ID not allowed on element button. | **Fix: Added data attibute to comment id in movie_detail.html**


> **Result**
| <span style="color:green">Document checking completed. No errors or warnings to show. &check;</span>
---

### **Recommend a Movie Page**

> **Errors & Fix**
**No errors found.**

> **Result**
| <span style="color:green">Document checking completed. No errors or warnings to show. &check;</span>
---

### **Newsletter Page**

> **Errors & Fix**
1. Error: Duplicate ID div_id_email.

![Image of W3C newsletter page error](docs/validation/newsletter-error.png)

> <span style="color:red">Error description:</span> This error is caused by the crispy subscription form I created. Because for subscribing and unsubscribing the server is using the same form, it's automatically creating the above error. Unfortunately, I couldn't fix this issue.

> **Result**
| <span style="color:red">Error remains &cross;</span>
---

### **Log out Page**

> **Errors & Fix**
**No errors found.**

> **Result**
| <span style="color:green">Document checking completed. No errors or warnings to show. &check;</span>
---

### **Sign Up Page**

> **Errors & Fix**
1. Error:  End tag p implied, but there were open elements. 
2. Error: Unclosed element span. 
3. Error: No p element in scope but a p end tag seen. 

![Image of W3C signup page error](docs/validation/signup-error.png)

> <span style="color:red">Error description:</span> This error is caused by Django's sign-up form. The part of the code that I wrote does not return any errors.

> **Result**
| <span style="color:red">Error remains &cross;</span>
---

### **Login Page**

> **Errors & Fix**
**No errors found.** 

> **Result**
| <span style="color:green">Document checking completed. No errors or warnings to show. &check;</span>
---

## **PEP8 Validation**

- [CI Python Linter](https://pep8ci.herokuapp.com/) used for all .py files.

All the errors besides the ones specified below was about indentation, trailing whitespace and blank lines and all of them are fixed.

| Directory    | File    | Result    |
| :------: | :--------: | :--------: |
| films  | admin.py  | PASS |
| films | urls.py    | PASS  |
| films | views.py   | PASS |
| films | apps.py   | PASS  |
| films | models.py  | PASS |
| films  | forms.py  | PASS |
| movies | admin.py  | PASS |
| movies | urls.py   | PASS |
| movies | views.py  | PASS  |
| movies | apps.py   | PASS   |
| movies | models.py   | PASS |
| movies  | forms.py   | PASS   |
| cinefrights | asgi.py    | PASS |
| cinefrights  | settings.py | FAIL |
| cinefrights  | urls.py     | PASS   |
| cinefrights  | wsgi.py     | PASS  |

> After fixing the [Newsletter Unsubscribe Bug](https://github.com/SerraKD/cine-frights/issues/29) in films/views.py i ran PEP8 validation again.
![CI Python Linter films/views.py](docs/validation/pep8-films-views.png)

---
> **All below files' Fail Reason was Line too long**

**settings.py**

![CI Python Linter settings.py](docs/validation/pep8-settings.png)

**movies/models.py**

![CI Python Linter movies/models.py](docs/validation/pep8-movies-models.png)

**movies/urls.py**

![CI Python Linter movies/urs.py](docs/validation/pep8-movies-url.png)

**movies/views.py**

![CI Python Linter movies/views.py](docs/validation/pep8-movies-views.png)
---

**Fix**

> **I broke down all long lines in below files and did PEP8 validation again**

**movies/models.py**

![CI Python Linter movies/models.py](docs/validation/pep8-movies-models-new.png)

**movies/urls.py**

![CI Python Linter movies/urs.py](docs/validation/pep8-movies-url-new.png)

**movies/views.py**

![CI Python Linter movies/views.py](docs/validation/pep8-movies-views-new.png)
---

## **JS Validation**

- [JSHint](https://jshint.com/) is used for custom Js file validation.

**comments.js**

![JSHint comments.js](docs/validation/jshint-comments.png)

## **CSS Validation**

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) is used for custom css file validation.

**style.css**

![W3C CSS Validator style.css](docs/validation/w3c-css.png)

## **Lighthouse**

 - [Chrome Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) is used in incognito mode to test the performance, accessibility, best practices, and SEO of the site.

**Home Page**

 ![Lighthouse home page](docs/validation/lighthouse-home.png)

**Films Page**

 ![Lighthouse films page](docs/validation/lighthouse-films.png)

**Movie Detail Page**

 ![Lighthouse movie detail page](docs/validation/lighthouse-movie-detail.png)

**Sign up Page**

 ![Lighthouse Sign up page](docs/validation/lighthouse-signup.png)

**Login Page**

 ![Lighthouse Login Page](docs/validation/lighthouse-login.png)

**Newsletter Page**

 ![Lighthouse Newsletter Page](docs/validation/lighthouse-newsletter.png)

**Recommend a movie Page**

![Lighthouse Recommend a movie Page](docs/validation/lighthouse-recommend.png)

**Logout Page**

![Lighthouse Logout Page](docs/validation/lighthouse-logout.png)

**[Go back to README.md](https://github.com/SerraKD/cine-frights#cine-frights)**