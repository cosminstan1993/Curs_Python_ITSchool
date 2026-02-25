# 4. Se da un fisier de logging "log.txt" care contine date referitor la evenimentele dintr-un sistem:
#    Sa se scrie un program care citeste fisierul "log.txt" si afiseaza numarul de evenimente de fiecare tip (INFO, WARNING, ERROR)
#    si afiseaza ora si evenimentul de tip ERROR care a avut loc cel mai recent.


from datetime import datetime


FILE = "TEME\exerxitii_fisiere\4\log.txt"

def analiza_log():
    info_count = 0
    warning_count = 0
    error_count = 0 
    
    ultimul_error = None
    ultimul_data_error = None
    
    with open(FILE, "r", encoding='utf-8') as f:
        for line in f:
            linie = linie.strip() 
            
            if not line:
                continue
            
            
            data_text, tip, mesaj = linie.split(' - ')
            
            if tip == "INFO":
                info_count += 1
            elif tip == "WARNING":
                warning_count += 1
            elif tip == "ERROR":
                 error_count += 1
                  
                  
                 data_curenta = datetime.strtime(data_text, "%Y-%m-%d %H:%M:%S") 
                 
                 if ultimul_data_error is None or data_curenta > ultimul_data_error:
                     ultimul_data_error = data_curenta
                     ultimul_error = linie
                     
                     
    print("Numar INFO: ", info_count)
    print("Numar WARNING: ", warning_count)
    print("Numar ERROR: ", error_count)
    
    if ultimul_error:
        print("\nCel mai recent ERROR: ")
        print(ultimul_error)
                            
analiza_log()                   
                
