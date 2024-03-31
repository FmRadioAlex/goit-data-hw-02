from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
uri = "mongodb+srv://fmradioalex:53e2rG6001E3JJz9@ifmradio.6zcczaa.mongodb.net/?retryWrites=true&w=majority&appName=IFmRadio"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.dc02
# Send a ping to confirm a successful connection

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def update_cat_age():
    db.cats.update_one(
        {"name":input("Name: ")},
        {
            "$set": {"age": input("New age cat: ")} 
        }
    )
    print(f"Оновлено вік кота")

def add_cat_feature():
    db.cats.update_one(
        {'name': input("Name: ")},

        {       
            '$push': {'features': (input("Features: ")).split()}
        })
    print(f"Додано нову характеристику до списку features кота.")

def creat_cats():
    db.cats.insert_one({
            "name": input("Name: "),
            "age": input("age: "),
            "features": (input("Features: ")).split(),
        })
    print("Create new cat 😻")

def all_cats():
    print(list(db.cats.find()))

def find_cats_name():
    find_name_cat=input("Find cats, Name: ")
    print(list(db.cats.find({"Name": find_name_cat})))

def delete_in_name_cat():
    db.cats.delete_one({"name":input("Name: ")})
    print("delete cats 😿")

try:
    def main():
        os.system('cls')
        print("Hello pls input comamnd help")
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command == "all":
                # Вивести усіх котів
                all_cats()


            elif command in["find name",'find','1']:
                # Знайти кота за name 
                find_cats_name()


            elif command in ['change age','2']:
                #Створіть функцію, яка дозволяє користувачеві оновити вік кота за ім'ям.    
                update_cat_age()


            elif command in ['add features','3']:
                #Створіть функцію, яка дозволяє додати нову характеристику до списку features кота за ім'ям
                add_cat_feature()


            elif command in ["delete",'4']:
                # Реалізуйте функцію для видалення запису з колекції за ім'ям тварини
                delete_in_name_cat()
            elif command =='add':
                creat_cats()

            elif command == 'delete all':
                db.cats.delete_many({})
            elif command =='cls':
                os.system('cls')
            elif command=='help':
                print(f'All commands:\nall\nchange age |2\nadd features |3\ndelete |4\nadd\ndelete all')
            elif command=='exit':
                print("close app")
                break
            
except Exception as e:
    print(e)

if __name__=="__main__":
    main()
