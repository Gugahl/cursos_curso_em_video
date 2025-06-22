<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teste com Variáveis</title>
</head>
<body>
    <h2>
        <?php 
            echo "Teste com variáveis"
        ?>
    </h2>
    <?php 
        const PAIS = "Brasil";

        $nome = "Gustavo";
        $sobrenome = "Henrique";
        echo "Prazer em te conhecer $nome $sobrenome! Você mora no " . PAIS . "<br>";

        // PAIS = "Estados Unidos";

        $nome = "Gleyce";
        $sobrenome = "Lima";
        echo "<br>Prazer em te conhecer $nome $sobrenome! Você mora no " . PAIS . "<br>";

        $nome = "Djenanny";
        $sobrenome = "Christine";
        echo "<br>Prazer em te conhecer $nome $sobrenome! Você mora no " . PAIS . "<br>";

        $nome = "Francisco";
        $sobrenome = "José";
        echo "<br>Prazer em te conhecer $nome $sobrenome! Você mora no " . PAIS . "<br>";

        $nome = "Gustavo";
        $Nome = "Gabriela";
        $salário = 2500.75;
        echo "<br>É verdade que seu nome é $nome?<br>";
        
        echo "<br>É verdade que seu nome é $Nome?<br>";

        echo "<br>É verdade que seu nome é $NOME?<br>";

        echo "<br>Seu salário é de R$$salário<br>";
    ?>
</body>
</html>