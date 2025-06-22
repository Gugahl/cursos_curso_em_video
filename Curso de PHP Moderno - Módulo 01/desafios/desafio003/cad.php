<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 003 - Conversor de moedas simples</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <main>
        <h1>Conversor de Moedas v1.0</h1>
        <?php 
            $real = $_GET["real"];
            $real = str_replace(['.', ','], ['', '.'], $real);
            $cotacao_dolar = 5.51;
            $dolar = $real / $cotacao_dolar;
            
            // Formatação por number_format()
            // $dolar_formatado = number_format($dolar, 2, ',', '.');
            // $real_formatado = number_format($real, 2, ',', '.');
            
            // Formatação por internacionalização

            $padrão = numfmt_create("pt_BR", NumberFormatter::CURRENCY);

            echo "Seus " . numfmt_format_currency($padrão, $real, "BRL") . 
                " equivalem a <strong>" . numfmt_format_currency($padrão, $dolar, "USD") . "</strong>";

            echo "<br><br><strong>*Cotação fixa de R$5,22</strong>. Informada diretamente no código.";
        ?>
    </main>
</body>
</html>