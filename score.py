```
    import pymongo
    import matplotlib.pyplot as plt
    
    #连接数据库
    client = pymongo.MongoClient(host="localhost",port=27017)
    db = client["Comments"]
    doc = db["Comment_items"]
    #找到全部的评论
    data = doc.find()
    
    all_score = []

    for item in data:
        #获取全部的分数
        all_score.append(item["score"])
        
    length = len(all_score)
    
    #三个类别
    labels = ["10-9","8-6","5-1"]
    label_one = 0
    label_two = 0
    label_three = 0
    sizes = []
    
    for score in all_score:
        if score >= 9:
            label_one += 1
        if score >= 6 and score <= 8:
            label_two += 1
        if score <= 5:
            label_three += 1
    
    sizes.append(label_one/ length)
    sizes.append(label_two/ length)
    sizes.append(label_three/ length)
    
    plt.pie(sizes, labels=labels, explode=(0.1, 0, 0), shadow=True, autopct="%1.3f%%")
    plt.title("Score Pie",loc='center')
    plt.axis("equal")   #画成圆
    plt.legend()
    plt.show()
```
