from pymongo import MongoClient

import datetime

stockDB = 'mydb'
dbname = 'test-good1'

def constructor_stock():
    client = MongoClient('mongodb://a8602016:a21678762@ac-k8ls6b3-shard-00-00.h4ayndf.mongodb.net:27017,ac-k8ls6b3-shard-00-01.h4ayndf.mongodb.net:27017,ac-k8ls6b3-shard-00-02.h4ayndf.mongodb.net:27017/?ssl=true&replicaSet=atlas-zohb7q-shard-0&authSource=admin&retryWrites=true&w=majority')
    db = client[stockDB]
    return db

#——————————————————————————————— 更新暫存的股票名稱 —————————————————————————————
def update_my_stock(user_name,  stockNumber, condition , target_price):
    db = constructor_stock()
    collect = db[user_name]
    collect.update_many({"favorite_stock": stockNumber }, {'$set': {'condition':condition , "price": target_price}})
    content = f"股票{stockNumber}更新成功"
    return content
#——————————————————————————————— 新增使用者的股票 ——————————————————————————————
def write_my_stock(userID, user_name, stockNumber, condition , target_price):
    db = constructor_stock()
    collect = db[user_name]
    is_exit = collect.find_one({"favorite_stock": stockNumber})
    if is_exit != None :
        content = update_my_stock(user_name, stockNumber, condition , target_price)
        return content
    else:
        collect.insert_one({
                "userID": userID,
                "favorite_stock": stockNumber,
                "condition" :  condition,
                "price" : target_price,
                "tag": "stock",
                "date_info": datetime.datetime.now()
            })
        return f"{stockNumber}已新增至您的股票清單"
    
#——————————————————————————————— 新增使用者的股票 ——————————————————————————————
def show_stock_setting(user_name,userID):
    db=constructor_stock()
    collect=db[user_name]
    dataList=list(collect.find({'userID':userID}))
    if dataList==[]:return '您的股票清單為空，請透過指令新增股票至清單中'
    content='您情單中的選股條件為: \n'
    for i in range(len(dataList)):
        content+=f"{dataList[i]['favorite_stock']}{dataList[i]['condition']}{dataList[i]['price']}\n"
    return content