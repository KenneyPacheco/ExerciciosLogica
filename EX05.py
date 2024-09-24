'''
Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

Resposta:
    Para simplificar o raciocínio vamos numerar os itens da seguinte forma:
    salas/Lâmpadas 1,2,3
    Interruptores 1,2,3


    Começo ligando o interruptor 1 e o deixo assim por 5 ou 10min, após esse tempo desligo o interruptor 1 e ligo o 2.
    Vou até a sala da lâmpada 1 e se ela estiver ligada, significa que o interruptor 2 é o correto, caso esteja apagada e quente, significa que o interruptor 1 é o correto, se não será o interruptor 3.
    Volto a sala dos interruptores e repito o procedimento com a proxima sala utilizando os 2 interruptores que faltam.
'''

