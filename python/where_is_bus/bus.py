"""A simple model to find best routes between 2 bus stops"""


bus_1 = ["Kadikoy", "Moda", "Rasim", "Fener", "Goztepe", "Erenkoy", "Bostanci", "Kucukyali", "Maltepe", "Kartal", "Sabiha"]
bus_2 = ["Taksim", "Sisli", "Osmanbey", "Besiktas", "Ortakoy", "Arnavut", "Bebek", "Etiler", "Levent", "Maslak", "Eyup"]
bus_3 = ["Uskudar", "Salacak", "Harem", "Acibadem", "Altunizade", "Capitol", "Kisikli", "Umraniye", "Cekmekoy", "Sancaktepe"]
bus_4 = ["Eminonu", "Karakoy","Sabiha" ,"Galata", "Tophane", "Findikli", "Kabatas", "Dolmabahce", "Besiktas", "Yildiz", "Ortakoy"]
bus_5 = ["Bakirkoy", "Atakoy", "Salacak", "Yesilkoy", "Florya", "Avcilar", "Cihangir", "Beylik", "Esenyurt", "Bahcesehir", "Hadim"]
bus_6 = ["Esenler", "Davutpasa", "Topkapi", "Merter", "Zeytin", "Gungoren", "Bagcilar", "Kirazli", "Mahmut", "Ikitelli"]
bus_7 = ["Eyup", "Pierre", "Alibey", "Kagithane", "Seyrantepe", "Ayazaga", "Tarabya", "Sariyer", "Rumeli", "Kilyos", "Eminonu"]
bus_8 = ["Pendik", "Tuzla", "Aydinli", "Orhanli", "Sabiha", "Kurtkoy", "Yeni", "Cevizli", "Dragos", "Yali"]
#the list of buses

start = "Tarabya"
finish =  "Atakoy"
#two random bus stops

all_bus = [bus_1, bus_2, bus_3, bus_4, bus_5, bus_6, bus_7, bus_8]
for bus in all_bus:
    mesage = ''
    if start  in bus and finish in bus:
        start_index = bus.index(start)
        finish_index = bus.index(finish)
        if start_index < finish_index:
            mesage = bus[start_index:finish_index + 1]
        if start_index > finish_index:
            mesage = bus[start_index :finish_index - 1: -1]
        break
    else:
        mesage = f" {start} and {finish} are not in the same line! "
#finds the best path between two stops|

print(mesage)
