# mediumScraping
This program's purpose is to input the username of a Medium user, and the program will parse through their most recent articles.
The program requires the username of the person's Medium account to function. It is entered as a string in line 10. The modules requests, json, and time are necessary to run the program.
The program contains two functions that parse the articles differently
1) The function 'latestArticles()' will print a list of dictionary objects (each object is an article) that has been written in the past k number of months
2) The other function, 'latestArticle()' will print only the latest object
