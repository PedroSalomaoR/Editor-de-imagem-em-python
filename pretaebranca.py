with open("a.ppm", "rb") as f:
    tipo = f.readline().strip()
    dimensoes = f.readline().strip()
    max_valor = f.readline().strip()
    largura, altura = map(int, dimensoes.decode().split())

    tamanho_total = largura * altura * 3

    pixels = f.read(tamanho_total)

    print("maior:", max(pixels))
    print("menor:", min(pixels))
    print("média:", sum(pixels)/len(pixels))
    
    pixels_modificados = []
    
    for i in range(0, len(pixels), 3):
        r = pixels[i]
        g = pixels[i + 1]
        b = pixels[i + 2]
        
        #verificando a intensidade
        intensidade = 0.299 * r + 0.587 * g + 0.114 * b
        
        #trocando para preto ou branco
        if intensidade >= 128:
            #branco
            pixels_modificados.extend([255 , 255 , 255])
        else:
            #preto
            pixels_modificados.extend([0 , 0 , 0])
with open("b.ppm", "wb") as f:
    f.write(f"P6\n{largura} {altura}\n255\n".encode())
    f.write(bytearray(pixels_modificados))
