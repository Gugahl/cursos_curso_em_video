algoritmo "ContagemInteligente"
var
    inic, fim, contagem: Inteiro
inicio
    Escreval("--------------------")
    Escreval("CONTAGEM INTELIGENTE")
    Escreval("--------------------")
    Escreva("Início: ")
    Leia(inic)
    Escreva("Fim: ")
    Leia(fim)
    contagem <- 1
    Se (inic > fim) entao
        Escreval("--------------------")
        Escreval("  C O N T A N D O   ")
        Escreval("--------------------")
        contagem <- fim
        Enquanto (contagem < inic + 1) faca
            Escreva(contagem, "... ")
            contagem <- contagem + 1
        FimEnquanto
    FimSe
    Se (fim > inic) entao
        Escreval("--------------------")
        Escreval("  C O N T A N D O   ")
        Escreval("--------------------")
        contagem <- inic
        Enquanto (contagem < fim + 1) faca
            Escreva(contagem, "... ")
            contagem <- contagem + 1
        FimEnquanto
    FimSe
fimalgoritmo
