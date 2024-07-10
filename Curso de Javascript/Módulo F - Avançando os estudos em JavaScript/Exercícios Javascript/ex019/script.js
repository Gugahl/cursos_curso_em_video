var lista = [];
var maior = null;
var menor = null;
var soma = 0;

function adicionarItem() {
    var num = document.getElementById('numero').value;
    var select = document.getElementById('select');
    
    if (isNaN(num) || num === "") {
        alert('Digite um número válido!');
    } else {
        var num = Number(num);

        if (lista.indexOf(num) !== -1) {
            alert('Valor já encontrado na lista!');
        } else { 
            lista.push(num);

            if (num < 1 || num > 100) {
                alert('O valor é inválido!');
            } else {
                select.innerHTML += (`<option>Valor ${num} adicionado com sucesso!</option>`);

                if (maior === null || num > maior) {
                    maior = num;
                }
                if (menor === null || num < menor) {
                    menor = num;
                }

                soma += num;

                document.getElementById('numero').value = '';
                document.getElementById('numero').focus();
            }
        }
    }
}

function finalizarOperacao() {
    var res = document.getElementById('res');
    res.innerHTML = '';

    if (lista.length == 0) {
        alert('Adicione valores antes de finalizar!');
    } else {
        var media = soma / lista.length;
        res.innerHTML += (`<p>Ao todo, temos ${lista.length} números cadastrados;</p>`);
        res.innerHTML += (`<p>O maior valor informado foi ${maior};</p>`);
        res.innerHTML += (`<p>O menor valor informado foi ${menor};</p>`);
        res.innerHTML += (`<p>Somando todos os valores temos ${soma};</p>`);
        res.innerHTML += (`<p>A média dos valores digitados é ${media.toFixed(2)};</p>`);
    }
}