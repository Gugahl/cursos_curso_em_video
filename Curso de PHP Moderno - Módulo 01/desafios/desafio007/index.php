<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 007 - Salário Mínimo</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <?php 
        $salario_minimo = 1518;

        $salario = (float) ($_POST["salario"] ?? 0);

        $qtd_salarios = intdiv($salario, $salario_minimo) ?? 0;

        $sobra = $qtd_salarios % $salario_minimo;

        $localizacao = "pt_BR";

        $formatacao = new NumberFormatter($localizacao, NumberFormatter::CURRENCY);

        $salario = $formatacao->formatCurrency($salario, "BRL",);

        $salario_minimo = $formatacao->formatCurrency($salario_minimo, "BRL");

        $sobra = $formatacao->formatCurrency($sobra, "BRL")
    ?>

    <main>
        <h1>Informe seu salário</h1>
        <form action="" method="post">
            <label for="salario">Salário (R$)</label>
            <input type="number" name="salario" id="idsalario" value="$salario">
            <input type="submit" value="Enviar">
        </form>
        <p><?="Considerando o salário mínimo de <strong>R$ $salario_minimo</strong>. Atualizado em 24/06/2025.</p>"?>
    </main>

    <section>
        <h2>Resultado Final</h2>
        <p><?= "Quem recebe um salário de R$$salario ganha <strong>$qtd_salarios salários mínimos</strong> + $sobra."?> </p>
    </section>
</body>
</html>