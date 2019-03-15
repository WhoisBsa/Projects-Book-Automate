# Welcome

CheckingPasswords is a simple project that has the only functionality to detect strong passwords.

---
### The program is composed of four functions:

- stripRegex:  Return the password pure, without spaces  
- checkPassw:  Checks the strength of the password and asks, if it is weak, if it wants to generate a new  
- mkPass:         If the password is weak, and the user agree in generate, returns the new password  
- main:           The known main function  

### And it works basically like this:

1.  The user type the password  
2.  The `stripPassword` function is triggered  
3.  With the `re` module the programm compile the password  
4.  With the `match` function, the program check the result
5.  Validate the password with the conditions
6.  If it does not respond to all aspects (uppercase, lowercase, digits)
7.  Asks the user if he wants generate a new password (`mkPass`)  
8.  If the answer is yes, the new password is generated, if is no, well, good lucky :)

### Here is a preview of how the program works:  

![demo](https://user-images.githubusercontent.com/36895235/54222651-93817080-44d4-11e9-8f92-4f72508ffcf3.gif)

---
All thanks go to [Al Sweigart](https://www.amazon.com/Al-Sweigart/e/B007716TEG/ref=dp_byline_cont_book_1) for creating a book with such vast content.
