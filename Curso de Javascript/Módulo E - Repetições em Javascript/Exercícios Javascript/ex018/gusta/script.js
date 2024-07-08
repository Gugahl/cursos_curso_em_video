function gerarTabuada() {
    var num = Number(window.document.getElementById('numero').value)
    var select = document.getElementById('select')
    select.innerHTML = ""
    for (i = 1; i <= 10; i++) {
        select.innerHTML += ('<option>' + `${num} x ${i} = ${(num * i)}` + '</option>');
    }
}