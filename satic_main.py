import argparse
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
#created argumet parser 
parser=argparse.ArgumentParser(description="scraping")
parser.add_argument("--url",required=True,help="enter the url ⛓️ ")#ask the user to enter the --url
args=parser.parse_args()#getting the url command line agruments in args .user input in command line
                       #This line actually reads and parses whatever you typed in the terminal.
                        #Think of it like a translator  that turns terminal input into Python variables.
page_url="/pages/"#just a containter or page link
all_data=[]#empty list to store data 
url=args.url #copies that value into a new variable called url.
           
while True:#using loop for untill condition it true

    #getting data from url
    response=requests.get(url)
    #so if the response is not equal to 200 which is page load sucessfully
    if response.status_code!=200:
        print(f"webpage not respond--->>{response.status_code}")
        break
    #using beautifulsoup to read that raw data from the html
    soup=BeautifulSoup(response.text,"html.parser")#html.parser tell to beautifulsoup how to read and understand html structure
   
    all_text=soup.find_all(True)#looping through every HTML tag found on the webpage and return them as list
    
    for tag in all_text:
        tag_name=tag.name # # gives h1, p, span
        tag_text=tag.get_text(separator='\n',strip=True) # gives text inside tag
        all_data.append({"url":url,"tag":tag_name,"text":tag_text}) ## store current page url, tag name, and tag text as one record (dictionary)                                                        
                                                                  # then add it to the all_data list for saving later

    next_button=soup.find("li",class_="next")#stores the <li> tag that has the class “next”.

    if next_button and next_button.find("a"):##next_button → makes sure the <li class="next"> tag exists.#next_button.find("a") → checks if there's an <a> (anchor tag) inside it.
        next_link=next_button.find('a')["href"]##.find('a') → finds the <a> tag inside <li class="next">.["href"] → extracts the value of the href attribute (the link to the next page).
        url=urljoin(url,next_link)#Combines the current page URL and the next page link into a complete URL.
    else:
        break

#saving to csv using pandas
df=pd.DataFrame(all_data)
df.to_csv("static_data.csv",index=False)
print("sucsussfully done")
