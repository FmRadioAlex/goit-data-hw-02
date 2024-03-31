import random
from faker import Faker
import psycopg2
from tabulate import tabulate


conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="123456",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


               
            #  Fake заповнення таблиці випадковими данними

fake = Faker()
# Функція для вставки випадкових даних у таблицю users
def seed_users(n):
    for _ in range(n):
        fullname = fake.name()
        email = fake.email()
        cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))
        conn.commit()

# Функція для вставки випадкових даних у таблицю status
def seed_status():
    for _ in range(20):
        title = fake.sentence(nb_words=6)
        description = fake.text(max_nb_chars=20)
        status_id = random.randint(1, 3)
   
        user_id = random.randint(1, 10) 
        cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", (title, description, status_id, user_id))
        conn.commit()

# Виклик функцій для заповнення таблиць
seed_users(10)  # Заповнення таблиці users із 10 користувачами
seed_status()   # Заповнення таблиці status



# Закриття з'єднання з базою даних
cur.close()
conn.close()
