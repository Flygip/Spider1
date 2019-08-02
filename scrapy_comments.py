import pymongo
import requests
import json

#To get the host,post and database name
host = "127.0.0.1"
port = 27017
dbname = "Comments"

#Creat links to the database
client = pymongo.MongoClient(host = host, port = port)
#Confirm the database
mdb = client[dbname]
#To get data table name
post = mdb["Comment_items"]

def get_response(url):
    """
    To get response
    :param url: adress
    """
    User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    headers = {"User-Agent":User_Agent}
    response = requests.get(url=url,headers=headers)
    if response.status_code == 200:
        # print(response.text)
        get_single_comments(response.text)

def get_single_comments(text):
    """
    To get comments
    :param text: response.text
    :return:
    """
    temp_store = {}   #Temporarily store comments of one page
    # print(json.loads(text))
    data = (json.loads(text)).get("data")
    # print(data)
    comments = data.get('comments')
    for comment in comments:
        # print(comment)
        temp_store["nick"] = comment.get("nick")
        temp_store["gender"] = comment.get("gender")
        temp_store["score"] = comment.get("score")
        temp_store["comments"] = comment.get("content")
        temp_store["userLevel"] = comment.get("userLevel")
        store.append(temp_store)
        temp_store = {}

def store_comments(comment):
    """
    To store comments
    :param comments: comments
    :return:
    """
    post.insert(comment)    #To store data in MongoDB

num = 15   #To set the value of offset
store = []
for i in range(5):
    num *= i+1
    url = "http://m.maoyan.com/review/v2/comments.json?movieId=1211270&userId=-1&offset={}&limit=15&ts=1564738457916&type=3".format(num)
    get_response(url=url)
    num = 15

store_comments(store)
