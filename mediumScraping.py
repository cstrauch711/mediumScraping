import requests
import json
import time

#The username of the wanted person is put here
username = ""
#This is the URL that is dependent on the person wanted to be parsed through
url = 'https://medium.com/@'+username+'/latest'
headers = {'Accept':'application/json'}
#Request a json string of 'url' but asking for a JSON string to be received
response = requests.get( url, headers=headers )

#convert the returned JSON string into an actual JSON object
newtext = response.text[16:len(response.text)]
obj = json.loads( newtext )
#print( obj )

#name of the person for later use
name = obj['payload']['user']['name']

#latest articles will show the articles written in the past 'k' months
k = 3

#Shows titles of articles person has written in the last 'k' number of months
def latestArticles():
    articles = []#This is a list that wil be filled with article objects from the last 'k' number of months
    for key,value in obj['payload']['references']['Post'].items() : #this object is a dictionary of the latest posts
        trueCreation = value['createdAt'] * 1e-3 #object does not have correct date. This fixes it
        article = {} #Each article is a dictionary of different values, and each of these dictionaries will be stored in articles if it has been written recently
        #Initializing and Resetting the temporary article object each time
        article['article_name'] = ""
        article['id'] = ""
        article['url'] = ""
        article['date'] = ""
        article['subtitle'] = ""
        article['claps'] = 0
        article['tags'] = []
        article['image_url'] = ""
        if trueCreation >= (time.time() - 2.628e+6 * k): #Only will add to 'articles' if written recently
            article['article_name'] = value['title']
            article['id'] = value['id']
            article['url'] = 'https://medium.com/@'+username+'/'+value['uniqueSlug']
            article['date'] = time.ctime(value['createdAt'] * 1e-3)
            article['subtitle'] = value['content']['subtitle']
            article['claps'] = value['virtuals']['totalClapCount']
            for tag in value['virtuals']['tags']:
                article['tags'].append( tag['name'] )
            article['image_url'] = 'https://cdn-images-1.medium.com/'+value['virtuals']['previewImage']['imageId']
            articles.append( article )#add the completed article object to 'articles'
    print( name + " has written these articles in the past " + str(k) + " months:")
    for a in articles:
        print( str(a) + "\n")

#This will return a dictionary of different info for the latest post from person
#This function works similarly to the previous function, but only returns one article dictionary (the most recent)
def latestArticle():
    #'Article' is a dictionary that will contain all the values for the most recent article
    article = {}
    #Initialization of all the keys and values in the article object
    article['article_name'] = ""
    article['id'] = ""
    article['url'] = ""
    article['date'] = ""
    article['subtitle'] = ""
    article['claps'] = 0
    article['tags'] = []
    article['image_url'] = ""
    b = True #the while statement with b ensures that only one article will be used (the most recent one)
    print( name + "'s most recent article:")
    for key,value in obj['payload']['references']['Post'].items() : #this object is a dictionary of the latest posts
        while b:
            article['article_name'] = value['title']
            article['id'] = value['id']
            article['url'] = "https://medium.com/@"+username+"/"+value['uniqueSlug']
            article['date'] = time.ctime(value['createdAt'] * 1e-3)#need to fix date
            article['subtitle'] = value['content']['subtitle']
            article['claps'] = value['virtuals']['totalClapCount']
            for tag in value['virtuals']['tags']:
                article['tags'].append( tag['name'] )
            article['image_url'] = "https://cdn-images-1.medium.com/"+value['virtuals']['previewImage']['imageId']
            b = False
    print( article )

#Run the functions
latestArticles()
latestArticle()
