with open("lena.ppm", "rb") as f:
    tipo = f.readline().strip()
    dimensoes = f.readline().strip()
    max_valor = f.readline().strip()

    print("Tipo:", tipo.decode())
    print("Dimensões:", dimensoes.decode())
    print("Valor máximo:", max_valor.decode())
    # converte dimensões para números
    largura, altura = map(int, dimensoes.decode().split())

    # total de pixels (cada pixel = 3 bytes)
    tamanho_total = largura * altura * 3

    # ler os dados binários dos pixels
    pixels = f.read(tamanho_total)

    # só por enquanto: mostrar os 10 primeiros bytes
    print("Primeiros bytes dos pixels:", list(pixels[:10]))
    pixels_modificados = []

    for i in range(0, len(pixels), 3):
        r = pixels[i]
        g = pixels[i + 1]
        b = pixels[i + 2]

        #transformando em cinza
        cinza = int(0.299 * r + 0.587 * g + 0.114 * b )
        
        pixels_modificados.extend([cinza, cinza, cinza])
    print(f"Primeiros pixels modificados:{pixels_modificados[:10]}")
with open("a.ppm", "wb") as f:
# escrever o cabeçalho
    f.write(f"P6\n{largura} {altura}\n255\n".encode())

# converter a lista de pixels para bytes e escrever
    f.write(bytearray(pixels_modificados))
