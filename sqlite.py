import sqlite3


connect = sqlite3.connect('database.db')
cursor = connect.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS baget(number STR, count INT)")


bagets = {"1": 10, "2": 10, "3": 10, '4': 10, "5": 10, "6": 10, "7": 10,
          "8": 10, "9": 10, "10": 10, "11": 10, "12": 10, "13": 10, "14": 10,
          "15": 10, "16": 10, "17": 10, "18": 10, "19": 10, "20": 10, "21": 10,
          "22": 10, "23": 10, "24": 10, "25": 10, "26": 10, "27": 10,
          }


def add_bagets_and_start_value(list):
    for key, value in list.items():
        cursor.execute(f"INSERT INTO\
        baget(number, count) VALUES({key}, {value})")


# add_bagets_and_start_value(bagets)
# # # connect.commit()


def show_count_of_baget(id_number):
    cursor.execute(f"SELECT count FROM baget WHERE number={id_number}")
    number = cursor.fetchone()
    connect.commit()
    return number[0]


def count_minus_one(id_number, baget=1):
    '''ex_value = ex_value - 1'''
    cursor.execute(f"SELECT count FROM baget WHERE number={id_number}")
    number = cursor.fetchone()
    number = number[0] - baget 
    cursor.execute(f"UPDATE baget SET count={number} WHERE number={id_number}")
    connect.commit()
    return show_count_of_baget(id_number)


def count_plus_one(id_number, baget=1):
    '''ex_value = ex_value + 1'''
    cursor.execute(f"SELECT count FROM baget WHERE number={id_number}")
    number = cursor.fetchone()
    number = number[0] + baget 
    cursor.execute(f"UPDATE baget SET count={number} WHERE number={id_number}")
    connect.commit()
    return show_count_of_baget(id_number)
    

def show_all_items():
    cursor.execute("SELECT number, count FROM baget")
    full_info = cursor.fetchall()
    return full_info