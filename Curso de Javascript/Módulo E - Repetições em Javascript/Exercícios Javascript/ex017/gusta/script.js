function contar() {
    var inicio = document.getElementById('inicio').value
    var fim = document.getElementById('fim').value
    var passo = document.getElementById('passo').value
    var res = document.getElementById('res')

    if (inicio === "" || fim === "" || passo === "" || fim == 0) {
        res.innerHTML = `<p>Por favor, insira valores válidos!</p>`
        return
    }
    if (passo == 0) {
        alert("Passo inválido! Considerando passo = 1.")
        passo = 1
    }

    inicio = Number(inicio)
    fim = Number(fim)
    passo = Number(passo)

    if (isNaN(inicio) || isNaN(fim) || isNaN(passo) || fim == null || fim == 0 || passo == 0) {
        res.innerHTML = `<p>Por favor, insira valores válidos!</p>`
    } else {
        res.innerHTML = `<p id="paragrafo">Contando...</p>`
        for(var c = inicio; c <= fim; c += passo) {
            if (c < fim) {
                res.innerHTML += `${c} 👉 `
            } else if (c == fim) {
                res.innerHTML += ` ${c}.`
            }
        }
    }
}
