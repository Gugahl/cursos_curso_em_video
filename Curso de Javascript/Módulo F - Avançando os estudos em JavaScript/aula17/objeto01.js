let amigo = []
let jose = {nome: 'José', sexo: 'M', peso: 85.4, engordar(p){
    console.log('Engordou')
    this.peso += p
}}

jose.engordar(2)

console.log(typeof amigo)
console.log(jose)
console.log(`${jose.nome} pesa ${jose.peso} kg.`)
console.log(typeof jose)