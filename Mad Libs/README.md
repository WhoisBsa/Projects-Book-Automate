# Welcome

Suppose you have the tedious task of filling out various forms on a web page or in software with multiple text fields. The clipboard prevents you from having to type the same text repeatedly. But only one text can be on the clipboard at any moment. If you have several different portions of text that need to be copied and pasted, you will need to mark and copy the same data repeatedly.

This program is done exactly for this, controlling several portions of text. This "multiclipboard" will be called `mcb.pyw`. The `.pyw` extension means that Python will not show a terminal window when running this program.

The program will save each piece of text from the clipboard with one keyword. For example, when you run `python3 mcb.pyw save spam`, the current contents of the clipboard will be saved with the keyword `spam`. This text may later be uploaded to the clipboard again if `python3 mcb.pyw spam` is executed. If the user wants to delete `spam` from the list he should use the ` python3 mcb.pyw delete spam` command, which will delete `spam` from the `shelf`. If the user forgets the existing keywords, he can execute `python3 mcb.pyw list` so that a list of all keywords is copied to the clipboard.

**Here's what the program does:**
1. The command-line argument for the keyword is checked.
2. If the argument is `save`, the contents of the clipboard will be saved with the keyword.
3. If the argument is `delete`, all content is deleted (including the file itself)
4. If the argument is `list`, all keywords will be copied to the clipboard.
5. Otherwise, the text of the keyword will be copied to the clipboard.

**This means that the code should do the following:**
* Read command-line arguments in `sys.argv`.
* Read and write on the clipboard.
* Save and load a shelf file.

---
All thanks go to [Al Sweigart](https://www.amazon.com/Al-Sweigart/e/B007716TEG/ref=dp_byline_cont_book_1) for creating a book with such vast content.