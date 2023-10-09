import time
nomes = ["Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe"]
for i in range(0, len(nomes), 3):
    print(nomes[i], nomes[i+1], nomes[i+2])
    time.sleep(5)
