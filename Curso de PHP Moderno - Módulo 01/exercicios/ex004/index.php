<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tipos Primitivos no PHP</title>
</head>
<body>
    <h2>Teste de Tipos Primitivos</h2>
    <?php 
        // 0x hexadecimal, 0b binário e 0 octal
        $num = 300;
        echo "O valor da variável é: $num <br>";
        $num = 0x1A;
        echo "O valor da variável é: $num <br>";
        $num = 010;
        echo "O valor da variável é: $num <br>";

        echo "<br>";

        $v = 300;
        var_dump($v);
        echo "<br>";

        $v = 45.2;
        var_dump($v);
        echo "<br>";
        
        $v = true;
        var_dump($v);
        echo "<br>";
        
        $v = "Gustavo";
        var_dump($v);
        echo "<br>";

        echo "<br>";

        $num = 3e2;
        echo "O valor é $num <br>";
        var_dump($num);
        echo "<br>";

        echo "<br>";

        $num = (int) 3e2;
        echo "O valor é $num <br>";
        var_dump($num);
        echo "<br>";

        echo "<br>";

        $casado = false;
        var_dump($casado);
        echo "<br>";
        echo "O valor para casado é $casado";
        echo "<br>";

        echo "<br>";

        $casado = true;
        var_dump($casado);
        echo "<br>";
        echo "O valor para casado é $casado";
        echo "<br>";

        echo "<br>";

        $vet = [6, 2.5, "Maria", 3, false];
        var_dump($vet);
        echo "<br>";
        echo "O vetor é $vet";
        echo "<br>";

        echo "<br>";

        class Pessoa {
            private string $nome;
        };
        $p = new Pessoa;
        var_dump($p);
    ?>
</body>
</html>