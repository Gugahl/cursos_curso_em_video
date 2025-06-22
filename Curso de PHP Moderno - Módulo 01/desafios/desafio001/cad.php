<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 001 - Antecessor e sucessor</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <main>
        <h1>Resultado Final</h1>
        <?php 
        $numero = (int) ($_GET["numero"] ?? 0);
        echo "<p>O número escolhido foi <strong>$numero</strong></p>";
        echo "<p>O número antecessor de $numero é " . ($numero-1) . "</p>";
        echo "<p>O número sucessor de $numero é " . ($numero + 1) . "</p>"
        ?>
        <p><a href="javascript:history.go(-1)"><input type="button" value="&#x2B05; Voltar"></a></p>
    </main>
</body>
</html>