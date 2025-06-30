<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 08 - Raízes de um número</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <?php 
        $numero = (float) ($_POST["numero"] ?? 0);
        $raiz_quadrada = sqrt($numero);
        $raiz_cubica = pow($numero, (1/3));

        $raiz_quadrada_formatada = number_format($raiz_quadrada, 3);
        $raiz_cubica_formatada = number_format($raiz_cubica, 3);
    ?>

    <main>
        <h1>Informe o número</h1>
        <form action="<?= $_SERVER['PHP_SELF']?>" method="post">
            <label for="numero">Número:</label>
            <input type="number" name="numero" id="idnumero" value="<?= $numero?>">
            <input type="submit" value="Calcular Raízes">
        </form>
    </main>

    <section>
        <h2>Resultado final</h2>
        <p><?= "Analisando o <strong>número $numero</strong>, temos:<br>
        
        <ul>
        <li>A sua raiz quadrada é <strong> $raiz_quadrada_formatada</strong>
        
        <li>A sua raiz cúbica é <strong> $raiz_cubica_formatada</strong>
        </ul>" ?></p>
    </section>
</body>
</html>