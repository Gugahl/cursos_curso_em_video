<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 09 - Médias Aritméticas</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <?php 
        $numero1 = (float) ($_POST["numero1"] ?? 0);
        $peso1 = (float) ($_POST["peso1"] ?? 1);
        $numero2 = (float) ($_POST["numero2"] ?? 0);
        $peso2 = (float) ($_POST["peso2"] ?? 1);

        $media_simples = ($numero1 + $numero2) / 2;
        $media_ponderada = (($numero1 * $peso1) + ($numero2 * $peso2)) / ($peso1 + $peso2);

        $numero1 = number_format($numero1, 2);
        $numero2 = number_format($numero2, 2);
        $media_simples = number_format($media_simples, 2);
        $media_ponderada = number_format($media_ponderada, 2);
    ?>

    <main>
        <h2>Médias Aritméticas</h2>
        <form action="<?= $_SERVER['PHP_SELF']?>" method="post">
            <label for="numero1">Primeiro valor</label>
            <input type="number" name="numero1" id="idnumero1"
            value="<?= $numero1?>" required>

            <label for="peso1">Primeiro peso</label>
            <input type="number" name="peso1"  id="idpeso1" value="<?= $peso1?>">

            <label for="numero2">Segundo valor</label>
            <input type="number" name="numero2" id="idnumero2" value="<?= $numero2?>" required>

            <label for="peso2">Segundo peso</label>
            <input type="number" name="peso2" id="idpeso2" value="<?= $peso2?>">

            <input type="submit" value="Calcular Médias">
        </form>
    </main>

    <section>
        <h2>Cálculo das Médias</h2>
        <p>
            <?= "
                Analisando os valores <strong>$numero1</strong> e <strong>$numero2</strong>
                
                <br><br>
                
                <ul>
                    
                    <li>A <strong>Média Aritmética Simples</strong> entre os valores $numero1 e $numero2 é igual a <strong>$media_simples;</strong>
                    
                    <br><br>
                    
                    <li>A <strong>Média Aritmética Ponderada</strong> entre os valores $numero1, com peso $peso1, e $numero2, com peso $peso2, é igual a <strong>$media_ponderada</strong>;
                </ul>
            " ?>
        </p>
    </section>
</body>
</html>