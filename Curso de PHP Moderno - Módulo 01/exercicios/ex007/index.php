<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Funções Aritméticas</title>
</head>
<body>
    <?php 
    $numero = "-297";
    echo "O valor absoluto do número $numero é: " . abs($numero) . "<br>";

    $numero = "254";
    echo "<br>O número $numero convertido em base binária é: " . base_convert($numero, 10, 2);

    $numero = "254";
    echo "<br>O número $numero convertido em base octal é: " . base_convert($numero, 10, 8);

    $numero = "254";
    echo "<br>O número $numero convertido em base hexadecimal é: " . base_convert($numero, 10, 16);

    $resposta = intdiv(5, 2);
    echo "<br><br>A resposta da divisão de 5 por 2 é: $resposta";

    $resposta = min(5, 2);
    echo "<br><br>O valor mínimo entre 5 e 2 é: $resposta";

    $resposta = max(5, 2);
    echo "<br>O valor máximo entre 5 e 2 é: $resposta";
    ?>
</body>
</html>