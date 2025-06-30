<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 011 - Reajustador de Preços</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <?php 
        // Declaração de variáveis
        $preco_nao_formatado = (float) ($_POST["preco_nao_formatado"] ?? 0);

        $porcentagem = (float) ($_POST["minhaPorcentagem"] ?? 0);

        // Formatação
        $localizacao = "pt_BR";
        
        $formatacao = new NumberFormatter($localizacao, NumberFormatter::CURRENCY);
        
        $preco_formatado = $formatacao->formatCurrency($preco_nao_formatado, 'BRL');
        
        $preco_pos_reajuste = $preco_nao_formatado + ($preco_nao_formatado * ($porcentagem/100));
        
        $preco_pos_reajuste_formatado = $formatacao->formatCurrency($preco_pos_reajuste, 'BRL');
    ?>

    <main>
        <h2>Resultado do Reajuste</h2>
        <form action="<?= $_SERVER['PHP_SELF']?>" method="post">
            <label for="preco_nao_formatado">Preço do produto (R$)</label>
            <input type="text" name="preco_nao_formatado" value="<?= $preco_nao_formatado?>">

            <label for="porcentagem">Qual será o percentual de reajuste? (<span id="valorPorcentagem"><?= $porcentagem?></span
            >%)</label>
            <input type="range" name="minhaPorcentagem" id="minhaPorcentagem" min="0" max="100" step="1" value="<?= $porcentagem?>">
            <input type="submit" value="Reajustar">
        </form>
    </main>

    <section>
        <h2>Resultado do Reajuste</h2>
        <p><?= "O produto que custava $preco_formatado,  com <strong>$porcentagem% de aumento</strong> vai passar a custar <strong>$preco_pos_reajuste_formatado</strong> a partir de agora."?></p>
    </section>

    <script>
        const porcentagem = document.getElementById("minhaPorcentagem");
        const valorPorcentagem = document.getElementById("valorPorcentagem");

        porcentagem.addEventListener('input', function() {
            valorPorcentagem.textContent = this.value;
        })
    </script>
</body>
</html>