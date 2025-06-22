<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Operadores Aritméticos do PHP</title>
</head>
<body>
    <h2>Operadores Aritméticos do PHP</h2>
    <?php 
        $num1 = 5;
        $num2 = 2;
        
        echo "A resposta da operação $num1 + $num2 é igual a " . $num1+$num2 . "<br>";
        
        echo "A resposta da operação $num1 - $num2 é igual a " . $num1-$num2 . "<br>";

        echo "A resposta da operação $num1 x $num2 é igual a " . $num1*$num2 . "<br>";

        echo "A resposta da operação $num1 / $num2 é igual a " . $num1/$num2 . "<br>";

        echo "O resto da operação $num1 / $num2 é igual a " . $num1%$num2 . "<br>";

        echo "A resposta da operação $num1^($num2) é igual a " . $num1**$num2 . "<br>";
    ?>
</body>
</html>