```
    import pymongo
    import matplotlib.pyplot as plt
    
    #连接数据库
    client = pymongo.MongoClient(host="localhost",port=27017)
    db = client["Comments"]
    doc = db["Comment_items"]
    #查找评论
    data = doc.find()
    
    all_gender = []
    for item in data:
        all_gender.append(item["gender"])

    gender_length = len(all_gender)

    labels = ["man","women","unknow"]
    
    man = 0
    women = 0
    unknow = 0
    sizes = []
    
    for gender in all_gender:
        if gender == 0:
            man += 1
        if gender == 1:
            women += 1
        if gender == 2:
            unknow += 1
    
    sizes.append(man/gender_length)
    sizes.append(women/gender_length)
    sizes.append(unknow/gender_length)
    
    plt.pie(sizes,explode=(0.1,0.1,0),labels=labels,autopct="%1.3f%%",shadow=True)
    plt.title("Gender Pie",loc="center")
    plt.axis("equal")
    plt.legend()
    plt.show()
```
