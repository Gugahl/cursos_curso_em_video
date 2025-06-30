<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 010 - Calculando a sua idade</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <?php 
        $ano_atual = date("Y");
        $ano_do_nascimento = (int) ($_POST["ano_do_nascimento"] ?? $ano_atual);
        $ano_do_destino = (int) ($_POST["ano_do_destino"] ?? '') ?: $ano_atual;

        $idade = $ano_do_destino - $ano_do_nascimento;
    ?>

    <main>
        <h2>Calculando a sua idade</h2>
        <form action="<?= $_SERVER['PHP_SELF']?>" method="post">
            <label for="ano_do_nascimento">Em que ano você nasceu?</label>
            <input type="number" name="ano_do_nascimento" id="ano_do_nascimento" value="<?= $ano_do_nascimento?>" min="1900" max="<?= $ano_atual?>">
            <label for="ano_do_destino">Quer saber sua idade em que ano? (atualmente estamos em <strong><?= $ano_atual?></strong>)</label>
            <input type="number" name="ano_do_destino" id="ano_do_destino" value="<?= $ano_do_destino?>">
            <input type="submit" value="Qual será a minha idade?">
        </form>
    </main>

    <section>
        <h2>Resultado</h2>
        <p><?= "Quem nasceu em $ano_do_nascimento, tem $idade anos em $ano_do_destino!"?></p>
    </section>
</body>
</html>