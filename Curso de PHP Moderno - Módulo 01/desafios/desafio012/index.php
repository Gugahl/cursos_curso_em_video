<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 012 - Calculadora de tempo</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <?php 
        $segundos_usuario = (float) (($_POST["segundos"]) ?? 0);
        
        $segundos = (floor($segundos_usuario % 60) ?? 0);

        $minutos = (floor(($segundos_usuario % (60 * 60)) / 60) ?? 0);
        
        $horas = (floor(($segundos_usuario % (60 * 60 * 24)) / (60 * 60)) ?? 0);

        $dias = (floor(($segundos_usuario % (60 * 60 * 24 * 7)) / (60 * 60 * 24)) ?? 0);

        $semanas = floor($segundos_usuario / (60 * 60 * 24 * 7));

        $segundos_usuario = number_format($segundos_usuario, 0, ',', '.');
    ?>

    <main>
        <h2>Calculadora de Tempo</h2>
        <form action="<?= $_SERVER['PHP_SELF']?>" method="post">
            <label for="segundos">Qual é o total de segundos?</label>
            <input type="number" name="segundos" id="">
            <input type="submit" value="Calcular">
        </form>
    </main>

    <section>
        <h2>Totalizando tudo</h2>
        <p>
            <?= "Analisando o valor que você digitou, <strong>$segundos_usuario segundos</strong> equivalem a um total de:<br>
            
            <ul>
                <li>$semanas semanas<br>
                <li>$dias dias<br>
                <li>$horas horas<br>
                <li>$minutos minutos<br>
                <li>$segundos segundos<br>
            </ul>"?>
        </p>
    </section>
</body>
</html>