import mysql.connector
from faker import Faker
import random
import time
from datetime import datetime

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'narutio6590',
    'database': 'laravel'
}

TOTAL_RECORDS = 1_000_000
BATCH_SIZE = 1000

fake = Faker('pt_BR')
account_types = ['personal', 'business', 'free']

def generate_random_user(loop_index):
    name = fake.name()
    email = f'{fake.user_name().lower().replace(" ", "_")}_{loop_index}@example.com'
    now = datetime.now()
    password_hash = fake.sha256()
    acc_type = random.choice(account_types)
    plan_id = random.choice([1, 2, 3, None])

    return (name, email, now, password_hash, acc_type, plan_id, now, now)

def main():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        print(f"Iniciando a inserção de {TOTAL_RECORDS:,} usuários...")
        start_time = time.time()

        records_to_insert = []
        sql_insert_query = """
        INSERT INTO users (
            name, email, email_verified_at, password, type_account,
            subscription_plan_id, created_at, updated_at
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        for i in range(1, TOTAL_RECORDS + 1):

            records_to_insert.append(generate_random_user(i))

            if i % BATCH_SIZE == 0:
                cursor.executemany(sql_insert_query, records_to_insert)
                connection.commit()
                records_to_insert = []
                print(f"  -> {i:,} usuários inseridos...")
                fake.unique.clear()


        if records_to_insert:
            cursor.executemany(sql_insert_query, records_to_insert)
            connection.commit()

        end_time = time.time()
        print("\nInserção de usuários concluída com sucesso!")
        print(f"Tempo total: {end_time - start_time:.2f} segundos.")

    except mysql.connector.Error as e:
        print(f"Erro ao conectar ou inserir no MySQL: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão com o MySQL foi fechada.")

if __name__ == '__main__':
    main()