# 5. Se da un fisier de logging "login.txt" care contine date referitor la incercarile de autentificare ale utilizatorilor:
#    Sa se scrie un program care citeste fisierul "login.txt" si salveaza in fisierul "user_attempts.txt" numarul de incercari de autentificare
#    pentru fiecare utilizator si ora si data ultimei incercari de autentificare reusite in formatul:
#    # <user> | <numar_incercari> | <ultima_data_ora_reusita>


import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_FILE = os.path.join(BASE_DIR, "login.txt")
OUTPUT_FILE = os.path.join(BASE_DIR, "user_attempts.txt")

def analiza_login():
    user_data = {}
    
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for linie in f:
            linie = linie.strip()
            
            if not linie:
                continue 
            
            linie = linie.lstrip("$")
            
            data_text, user, status = linie.split(' | ')
            
            if user not in user_data:
                user_data[user] = {
                    'attempts': 0,
                    'last_succes': None
                }
            
            user_data[user]["attempts"] += 1
            
            if status == "login passed":
                
                if (user_data[user]['last_succes'] is None or data_text > user_data[user]['last_succes']):
                    user_data[user]["last_succes"] = data_text
                    
                    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for user in user_data:
            attempts = user_data[user]['attempts']
            last_succes = user_data[user]['last_succes']
            
            if last_succes is None:
                last_succes = "N/A"
                
                f.write(user + " | " + str(attempts) + " | " + last_succes + "\n")
                
                
    print("Fisierul user_attempts.txt a fost creat.")                         
    
analiza_login()    