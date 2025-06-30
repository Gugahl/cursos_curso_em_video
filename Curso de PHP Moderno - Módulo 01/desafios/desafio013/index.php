<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 013 - Caixa Eletrônico</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <?php 
        $valor = $_POST["valor"] ?? 0;
        
        $cedulas_de_duzentos = (float) (floor($valor / 200) ?? 0);
        
        $cedulas_de_cem = (float) (floor(($valor % 200) / 100) ?? 0);
        
        $cedulas_de_cinquenta = (float) (floor((($valor % 200) % 100) / 50) ?? 0);
        
        $cedulas_de_vinte = (float) (floor(((($valor % 200) % 100) % 50) / 20) ?? 0);
        
        $cedulas_de_dez = (float) (floor((((($valor % 200) % 100) % 50) % 20) / 10) ?? 0);
        
        $cedulas_de_cinco = (float) (floor(((((($valor % 200) % 100) % 50) % 20) % 10) / 5) ?? 0);
        
        $cedulas_de_dois = (float) (floor((((((($valor % 200) % 100) % 50) % 20) % 10) % 5) / 2) ?? 0);

        $localizacao = "pt_BR";
        $formatacao = new NumberFormatter($localizacao, NumberFormatter::CURRENCY);
        $valor = $formatacao->formatCurrency($valor, "BRL");
    ?>

    <main>
        <h2>Caixa Eletrônico</h2>
        <form action="<?= $_SERVER['PHP_SELF']?>" method="post">
            <label for="valor">Qual valor você deseja sacar? (R$)*</label>
            <input type="number" name="valor" id="valor" value="<?=(int) ($valor)?>" min="2" required>
            <input type="submit" value="Sacar">
        </form>
        <p><strong>Cédulas disponíveis:</strong> R$200,00; R$100,00; R$50,00; R$20,00; R$10,00; R$5,00; R$2,00.</p>
    </main>
    
    <section>
        <h2>Saque de <?= $valor?> realizado</h2>
        <p><?= "
        O caixa eletrônico vai te devolver as seguintes notas:
        <br><br>
        <ul>
        <li><img src=\"dinheiro/200.jpg\" width=\"200\">x$cedulas_de_duzentos<br>
        
        <li><img src=\"dinheiro/100.jpg\" width=\"200\">x$cedulas_de_cem<br>
        
        <li><img src=\"dinheiro/50.jpg\" width=\"200\">x$cedulas_de_cinquenta<br>
        
        <li><img src=\"dinheiro/20.jpg\" width=\"200\">x$cedulas_de_vinte<br>
        
        <li><img src=\"dinheiro/10.jpg\" width=\"200\">x$cedulas_de_dez<br>
        
        <li><img src=\"dinheiro/5.jpg\" width=\"200\">x$cedulas_de_cinco<br>
        
        <li><img src=\"dinheiro/2.jpg\" width=\"200\">x$cedulas_de_dois<br>
        </ul>"?></p>
    </section>
</body>
</html>