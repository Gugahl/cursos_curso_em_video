<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP</title>
</head>
<body>
    <h2>Exemplo de PHP</h2>
    <?php 
        date_default_timezone_set("America/Sao_Paulo");
        echo "Hoje é dia " . date("d") . " de " . date("M") . " de " . date("Y") . " e a hora atual é " . date("G:i:s") . " UTC" . date("T");
    ?>
</body>
</html>