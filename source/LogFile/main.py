def GravarLog(conteudo):
    logFile = open("log.txt", 'a+')
    logFile.write(f"{conteudo} \n")
    logFile.close()

def ExibeLog():
    logFile = open("log.txt", 'r')
    print(logFile.read())
    logFile.close()

for num in range(1, 101):
    GravarLog(f"Esta é a linha número {num} do arquivo log.txt")

ExibeLog()


