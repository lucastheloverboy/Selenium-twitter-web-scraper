from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

driver = uc.Chrome(version_main=143)
time.sleep(5)
driver.get("https://x.com/login") 
input()
time.sleep(10)

hashtag = "city115"
start_date = "2025-10-01"
end_date = "2025-12-31"

url = f"https://x.com/search?q=(%23{hashtag})%20until%3A{end_date}%20since%3A{start_date}&src=typed_query&f=live"
driver.get(url)

time.sleep(8)
tweet_data = []
tweetusers = []
date_of_creation = []
user_posts = []
hashtag_use = []
length = 0
new_length = 1

while length != new_length:
 time.sleep(3)
 driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 time.sleep(3)
 tweets = driver.find_elements(By.CSS_SELECTOR , '[data-testid="tweet"]') 
 length = len(tweets)
 driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 time.sleep(3)
 tweets = driver.find_elements(By.CSS_SELECTOR , '[data-testid="tweet"]')   
 new_length = len(tweets)
 
     
tweets = driver.find_elements(By.CSS_SELECTOR , '[data-testid="tweet"]')
    

    

 
    
for tweet in tweets:
    try:
            text = tweet.find_element(By.CSS_SELECTOR, '[data-testid="tweetText"]').text
            tweet_data.append({"text": text})
    except:
        pass
for tweet in tweets:
    try:
           username = tweet.find_element(By.XPATH, ".//span[starts-with(text(), '@')]").text[1:]
           tweetusers.append({"user handle": username})

    except:
         print("aint work")
        
         pass

for i in tweetusers:
 driver.get(f"https://x.com/{i['user handle']}")
 time.sleep(6)
 doc = driver.find_element(By.XPATH, ".//span[starts-with(text(), 'Joined')]").text
 date_of_creation.append({"date of account creation": doc})
 time.sleep(2)
 postamount = driver.find_element(By.XPATH, ".//div[contains(text(), 'posts')]").text
 user_posts.append({'user posts': postamount})
 time.sleep(1)
 driver.get(f"https://x.com/search?q=(from%3A{i['user handle']})%20(%23{hashtag})&src=typed_query&f=live")
 length = 0
 new_length = 1
 while length != new_length:
  time.sleep(3)
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  time.sleep(3)
  tweets = driver.find_elements(By.CSS_SELECTOR , '[data-testid="tweet"]') 
  length = len(tweets)
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  time.sleep(3)
  tweets = driver.find_elements(By.CSS_SELECTOR , '[data-testid="tweet"]')   
  new_length = len(tweets)
 
 hashtag_tweets = driver.find_elements(By.XPATH, f".//a[contains(text(), '#{hashtag}')]")
 hashtag_amount = str(len(hashtag_tweets))
 hashtag_use.append({"hashtag frequency" : hashtag_amount})


with open('tweets.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['user handle', 'date of account creation', 'user posts', 'hashtag frequency'])
    writer.writeheader()
    writer.writerows(tweetusers)
    writer.writerows(date_of_creation)
    writer.writerows(user_posts)
    writer.writerows(hashtag_use)
    

print(f"saved {len(tweetusers)} tweets to tweets.csv")


driver.quit()