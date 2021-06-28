import pymongo
from pumongo import Mongoclient

def manipulaDadosMongoDB():
    cliente = pymongo.MongoClient("str de conexao onde o mongo esta instalado")
    db = cliente.conheca_python #o objeto é criado quando utilizado

    for i in range(1, 10):
        objDic = {'codigo' : i}
        db.conheca_mongodb.insert_one(objDic)

    db.conheca_mongodb.update_one({'codigo' : 2}, {'$set' : {'atributpNovo' : 789}})
    db.conheca_mongodb.delete_one({'codigo' : 1})

    resultadoConsulta = db.conheca_mongodb.find({})
    for doc in resultadoConsulta:
        print(doc)
manipulaDadosMongoDB()
