# **Validation**

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

### **Recommend a Movie Page**

> **Errors & Fix**
**No errors found.**

> **Result**
| <span style="color:green">Document checking completed. No errors or warnings to show. &check;</span>
---

### **Newsletter Page**

> **Errors & Fix**
1. Error: Duplicate ID div_id_email.

[Image of W3C newsletter page error](docs/validation/newsletter-error.png)

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

[Image of W3C signup page error](docs/validation/signup-error.png)

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

- [CI Python Linter](https://pep8ci.herokuapp.com/)

## **JS Validation**

- [JSHint](https://jshint.com/) 

## **CSS Validation**

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

## **Lighthouse**