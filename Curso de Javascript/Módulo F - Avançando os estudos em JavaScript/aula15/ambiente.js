let num = [5, 8, 2, 9, 3]

num.push(1)
num.sort()
num.push(1)
console.log(`Nosso vetor é o ${num}`)
console.log(`O vetor tem ${num.length} posições`)
console.log(`O primeiro valor do vetor é ${num[0]}`)

let valores = [8, 1, 7, 4, 2, 9]

for(let pos = 0; pos < valores.length; pos++){
    console.log(`A posição ${pos} tem o valor ${valores[pos]}`)
}

for(let pos in num) {
    console.log(num[pos])
}

let pos = num.indexOf(4)
if (pos == -1) {
    console.log(`O valor não foi encontrado!`)
} else {
    console.log(`O valor está na posição ${pos}`)
}
