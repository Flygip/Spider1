```
    # -*- coding:utf-8 -*-
    import pymongo
    import matplotlib.pyplot as plt
    import jieba  #jieba分词
    from wordcloud import WordCloud,ImageColorGenerator
    import numpy as np
    import cv2   #用来读取图片
    import matplotlib as mpl
    
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    txt_path = "D:/test.txt"   #txt文件位置
    font_path = "C:/windows/fonts/simfang.ttf"   #字体位置
    img_path = "D:/beauty.jpg"   #背景图片位置
    background_image = np.array(cv2.imread(img_path))
    
    #Click MongoDB database
    client = pymongo.MongoClient(host="localhost",port=27017)
    db = client["Comments"]
    doc = db["Comment_items"]
    #Find all data(Cursor)
    data = doc.find()
    
    all_comments = []
    for item in data:
        all_comments.append(item["comments"])
        
    data = open("D:/test.txt","a",encoding="utf-8")
    print(all_comments)
    for comment in all_comments:
        data.write(comment)
    data.close()
    print("写入完毕！")
    
    t = open(txt_path,"r",encoding="utf-8").read()
    cut_text = " ".join(jieba.cut(t))
    wordcloud = WordCloud(font_path,mask=background_image,background_color="white").generate(cut_text)
    image_color = ImageColorGenerator(background_image)
    
    plt.imshow(wordcloud.recolor(color_func=image_color),interpolation="bilinear")
    plt.show()
```
