Algoritmo "MatrizPar"
Var
    valores: vetor[1..3, 1..3] de Inteiro
    l, c: Inteiro
Inicio
    Para l <- 1 ate 3 faca
        Para c <- 1 ate 3 faca
            Se (l = c) entao
                Escreva(1)
                Leia(valores[l, c])
            Senao
                Escreva(0)
                Leia(valores[l, c])
            FimSe
        FimPara
    FimPara

    Escreval()
    Para l <- 1 ate 3 faca
        Para c <- 1 ate 3 faca
            Escreva(valores[l, c]:4)
        FimPara
        Escreval()
    FimPara
    Escreval()
FimAlgoritmo
