with open('nginx_logs.txt') as f:
    data = []
    top_spamer = {}
    for line in f:
        splitted = line.split()
        data.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
        top_spamer.setdefault(splitted[0], 0)
        top_spamer[splitted[0]] += 1
top_spamer = sorted(top_spamer.items(), key=lambda x: x[1], reverse=True)
print(top_spamer[:3])