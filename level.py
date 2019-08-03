```
    import pymongo
    import matplotlib.pyplot as plt
    
    #连接数据库
    client = pymongo.MongoClient(host="localhost",port=27017)
    db = client["Comments"]
    doc = db["Comment_items"]
    #查询全部的评论
    data = doc.find()
    
    all_level = []
    for item in data:
        all_level.append(item["userLevel"])

    level_length = len(all_level)

    x = [1,2,3,4,5]
    labels = ["1","2","3","4","5"]
    
    sizes = [0,0,0,0,0]
    
    for level in all_level:   #对等级分类
        sizes[level-1] += 1
    
    plt.bar(x,sizes,alpha=0.7,color=["red","yellow","blue","purple","orange"],tick_label=labels)
    #alpha表示透明度
    plt.title("User Level")
    plt.ylabel("Num")
    plt.xlabel("Level")
    plt.show()
```
