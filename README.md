# Platform Game

Jogo desenvolvido com o intuito de ensinar lógica de programação para aspirantes à programação. O jogo conta com uma opção de "piloto automático" em que o jogador pode adicionar no código do jogo algo como "ande", "pule" dentro de laços de repetições e expressões condicionais. 

![Main Image](https://github.com/KalvinAlbuquerque/game/blob/main/.imgGit/mainImage.png)

# REQUISITOS
Essa aplicação foi desenvolvida em ambiente Linux e não testada em Windows ou MacOS. 

Para rodar essa aplicação é necessária a instalação da biblioteca pygame. Para tal basta seguir os seguintes comandos:

```bash

sudo apt install python3-pip #Instalando o Pip3 - caso não esteja instalado
pip3 install pygame #Instalando a biblioteca pygame

```

# EXECUTANDO
![Tela inicial do jogo](https://github.com/KalvinAlbuquerque/game/blob/main/.imgGit/telaImage.png)

## IDE
Para executar o jogo basta clicar em "run", na sua IDE no arquivo main.py. 

## TERMINAL
No terminal , acesse a pasta do game e rode o código:

```bash
python3 main.py

```
Dentro do jogo, há um boneco 2D que pode ser controlado pelas setas do teclado e pular um bloco com a barra de espaço. Há moedas que podem ser coletadas ao passar por elas, monstros e lava que fazem com que o jogador vire um fantasminha ao tocá-los (morra =*( ). As fases são ultrapassadas quando o jogador alcança o portão.


#AUTO PLAYER MODE
O intuito principal dessa aplicação foi ensinar lógica de programação para alunos interessados em iniciar os estudos no mundo da programação. Para tal, criamos um "auto player mode" que basicamente é um script digitado pelo player - alunos. Dentro do main.py há uma função chamada ***"comandos()"***, nela podemos chamar funções que criamos para movimentar o jogador. 


![Auto Player Mode](https://github.com/KalvinAlbuquerque/game/blob/main/.imgGit/autoPlayerMode.png)

Entre as funções criadas para tal fim, há:
1.***andar_para_direita(), andar_para_esquerda():*** como o nome diz, faz com que o jogador ande um bloco para esquerda/direita.
2.***pular_para_esquerda(), pular_para_direita():*** como o nome diz, faz com que o jogador pule um bloco para esquerda/direita.
3.***esperar():*** faz com que o jogador fique parado.
4.***temBlocoNaFrente(), temLavaNaFrente(), temInimigoNaFrente(), temBuracoNaFrente():*** retorna "true" ou "false" caso haja o respectivo obstáculo um bloco a frente do jogador. Isso possibilita que o usuário possa praticar expressões condicionais. Como por exemplo: if temLavaNaFrente(): pular_para_direita(). 

Novamente, como o intuito é ensinar, a lógica do auto player mode foi pensada para se utilizar laços de repetições e expressões condicionais. Portanto, pode-se e deve criar expressões como: while(!temLavaNaFrente()): andar_para_direita(). 

## HABILITANDO O AUTO PLAYER MODE
![Tela inicial do jogo](https://github.com/KalvinAlbuquerque/game/blob/main/.imgGit/telaImage.png)

Uma vez digitado o código script, rode o game e na tela inicial clique no botão "OFF" no canto superior direito para que ele habilite esse modo.

#AUTORES
A aplicação foi pensada e desenvolvida também pelos desenvolvedores e pesquisadores:
[snttsz](https://github.com/snttsz)
[AlnnvN](https://github.com/AlnnvN)

#CONTRIBUIÇÃO
Esse código foi baseado no código do Coding With Russ, disponível em seu site: [Coding_With_Russ](http://www.codingwithruss.com/gamepage/Platformer/).




 
