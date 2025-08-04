# 🧪 Projeto de Manipulação de Imagens com Python Puro

Este projeto foi desenvolvido como parte de um **desafio da plataforma de ensino DIO**, com o objetivo de explorar e entender, na prática, como funciona a manipulação de imagens digitais — tudo isso sem utilizar bibliotecas externas para aplicarmos em Machine Learning.

A proposta era simples, mas desafiadora: ler uma imagem, alterar suas cores manualmente e salvar uma nova versão, trabalhando pixel a pixel em Python puro. Mais do que mudar cores, a intenção foi mergulhar nos bastidores da representação visual digital.

---

## 🧠 O que foi explorado

### 🔍 Como uma imagem é lida

Imagens no formato `.ppm` (modo binário P6) são compostas por um cabeçalho e uma sequência de bytes, onde cada grupo de três representa um pixel: vermelho (R), verde (G) e azul (B). O desafio começou ao ler e interpretar esse conteúdo direto do arquivo, sem atalhos.

### 🌫️ Conversão para tons de cinza

Para deixar a imagem em escala de cinza, foi usada a fórmula de luminosidade percebida pelo olho humano:

`cinza = 0.299 * R + 0.587 * G + 0.114 * B`

Esse valor de cinza foi replicado nos três canais RGB, produzindo o efeito visual esperado.

### ⚫️⚪️ Conversão para imagem binária (preto ou branco)

Outra transformação aplicada foi a binarização: cada pixel foi analisado e comparado a um **limiar** (threshold), como 128.  
Se a intensidade fosse maior ou igual ao limiar, o pixel virava branco. Caso contrário, preto.

---

## 🚀 Por que fazer isso?

Mais do que obter uma imagem diferente, a ideia foi **aprender de verdade como imagens funcionam**, entendendo o que acontece por trás de bibliotecas prontas. Trabalhar com bytes diretamente dá uma nova perspectiva sobre pixels, formatos e cores.

---

## 🧰 O que foi usado?

- Python (sem bibliotecas externas)
- Formato de imagem `.ppm` (P6)
- Lógica pura e prática passo a passo
- Curiosidade, tentativa e erro

---

## ✨ Resultado

Ao final, duas imagens foram geradas: uma versão em tons de cinza e outra em preto e branco binário. Ambas produzidas a partir do processamento direto dos bytes da imagem original.

---

> Esse projeto foi uma ótima oportunidade para fortalecer o raciocínio lógico, treinar manipulação de arquivos binários e compreender melhor os fundamentos de processamento de imagem.

---

👤 Conecte-se comigo no [LinkedIn]([https://www.linkedin.com/in/SEULINKAQUI/](https://www.linkedin.com/in/pedro-rodrigues-salom%C3%A3o-55a0ab310/)
