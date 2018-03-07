# mediumScraping
This program's purpose is to input the username of a Medium user, and the program will parse through their most recent articles in that person's https://medium.com/@username/latest page.
The program requires the username of the person's Medium account to function. It is entered as a string in line 10. The following modules are necessary to run the program: requests, json, and time.
The program contains two functions that parse the articles slightly differently.
1) The function 'latestArticles()' will print a list of dictionary objects (each object is an article) that has been written in the past k number of months
2) The other function, 'latestArticle()' will print only the latest article
