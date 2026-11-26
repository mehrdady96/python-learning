"""A simple model to find best routes between 2 bus stops"""



bus_1 = ["Kadikoy", "Moda", "Rasim", "Fener", "Goztepe", "Erenkoy", "Bostanci", "Kucukyali", "Maltepe", "Kartal", "Sabiha"]
bus_2 = ["Taksim", "Sisli", "Osmanbey", "Besiktas", "Ortakoy", "Arnavut", "Bebek", "Etiler", "Levent", "Maslak", "Eyup"]
bus_3 = ["Uskudar", "Salacak", "Harem", "Acibadem", "Altunizade", "Capitol", "Kisikli", "Umraniye", "Cekmekoy", "Sancaktepe"]
bus_4 = ["Eminonu", "Karakoy","Sabiha" ,"Galata", "Tophane", "Findikli", "Kabatas", "Dolmabahce", "Besiktas", "Yildiz", "Ortakoy"]
bus_5 = ["Bakirkoy", "Atakoy", "Salacak", "Yesilkoy", "Florya", "Avcilar", "Cihangir", "Beylik", "Esenyurt", "Bahcesehir", "Hadim"]
bus_6 = ["Esenler", "Davutpasa", "Topkapi", "Merter", "Kagithane", "Zeytin", "Gungoren", "Bagcilar", "Kirazli", "Mahmut", "Ikitelli"]
bus_7 = ["Eyup", "Pierre", "Alibey", "Kagithane", "Seyrantepe", "Ayazaga", "Tarabya", "Sariyer", "Rumeli", "Kilyos", "Eminonu"]
bus_8 = ["Pendik", "Tuzla", "Aydinli", "Orhanli", "Sabiha", "Kurtkoy", "Yeni", "Cevizli", "Dragos", "Yali"]

def segment(line , station_1 , station_2):
    if line.index(station_1) < line.index(station_2):
        print(line[line.index(station_1):line.index(station_2) + 1])
    if line.index(station_1) > line.index(station_2):
        print(line[line.index(station_1):line.index(station_2) - 1 : -1])
    

     
all_buses = [bus_1 , bus_2 , bus_3 , bus_4 , bus_5 , bus_6 , bus_7 , bus_8]
buses_names = {
    "bus_1": bus_1,
    "bus_2": bus_2,
    "bus_3": bus_3,
    "bus_4": bus_4,
    "bus_5": bus_5,
    "bus_6": bus_6,
    "bus_7": bus_7,
    "bus_8": bus_8,
}
start = "Kabatas"  # bus_4
finish = "Tarabya"   # bus_7
com = ''
for bus  in all_buses:
    if start in bus:
            start_bus_line = bus
    if finish in bus:
            finish_bus_line = bus
comoun_stations = list(set(start_bus_line) & set(finish_bus_line))
for com in comoun_stations:
     com = com



if start_bus_line == finish_bus_line:  
    if start_bus_line.index(start) < finish_bus_line.index(finish):
        print(start_bus_line[start_bus_line.index(start):finish_bus_line.index(finish) + 1])
    if start_bus_line.index(start) > finish_bus_line.index(finish):
        print(start_bus_line[start_bus_line.index(start):finish_bus_line.index(finish) - 1 : -1])
    # For special ocasions
if start_bus_line.index(start) < start_bus_line.index(com):
    print(start_bus_line[start_bus_line.index(start):start_bus_line.index(com) + 1])
    if finish_bus_line.index(com) < finish_bus_line.index(finish):
        print(finish_bus_line[finish_bus_line.index(com):finish_bus_line.index(finish) + 1])
    if finish_bus_line.index(com) > finish_bus_line.index(finish):
        print(finish_bus_line[finish_bus_line.index(com):finish_bus_line.index(finish) - 1 : -1])
if start_bus_line.index(start) > start_bus_line.index(com):
    print(start_bus_line[start_bus_line.index(start):start_bus_line.index(com) - 1 : -1])
    if finish_bus_line.index(com) < finish_bus_line.index(finish):
        print(finish_bus_line[finish_bus_line.index(com):finish_bus_line.index(finish) + 1])
    if finish_bus_line.index(com) > finish_bus_line.index(finish):
        print(finish_bus_line[finish_bus_line.index(com):finish_bus_line.index(finish) - 1 : -1]) 

