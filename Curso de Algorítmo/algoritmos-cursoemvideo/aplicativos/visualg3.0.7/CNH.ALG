algoritmo "CNH"
var
    ano, nasc, idade: Inteiro
inicio
    Escreva("--------------------------")
    Escreva(" DEPARTAMENTO DE TRÂNSITO ")
    Escreva("--------------------------")
    Escreva("Ano Atual (yyyy): ")
    Leia(ano)
    EscrevaL("Ano de Nascimento (yyyy): ")
    Leia(nasc)
    idade <- ano - nasc
    Escreva("--------", " STATUS ", "--------")
    Escreva("Idade: ", idade, "anos.")
    Se (idade >= 18) entao
        Escreva("APTO A TIRAR A CARTEIRA")
    senao
        Escreva("INAPTO A TIRAR CARTEIRA")
    Escreva("------------------------")