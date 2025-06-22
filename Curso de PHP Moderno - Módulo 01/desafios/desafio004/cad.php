<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 004 - Conversor de moedas consultando api</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <main>
        <h1>Conversor de Moedas v2.0</h1>
        <?php 
            // 1. Consumindo a API do Banco Central (cotação PTAX do dólar - venda)
            $link_da_api = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados/ultimos/1?formato=json";
            $json_api = file_get_contents($link_da_api); // Pega o JSON da API
            $array = json_decode($json_api, true);       // Converte o JSON para array associativo

            $cotacao_dolar = $array[0]["valor"];         // Valor do dólar comercial
            $data_cotacao = $array[0]["data"];           // Data da cotação

            // 2. Captura e tratamento do valor recebido via GET
            $real = $_GET["real"] ?? 0;
            $real = str_replace(['.', ','], ['', '.'], $real); // Transforma "1.234,56" em "1234.56"

            $dolar = $real / $cotacao_dolar;

            // 3. Formatação com internacionalização (NumberFormatter - extensão intl)
            $padrão = numfmt_create("pt_BR", NumberFormatter::CURRENCY);

            $real_formatado = numfmt_format_currency($padrão, $real, "BRL");
            $dolar_formatado = numfmt_format_currency($padrão, $dolar, "USD");
            $cotacao_formatada = number_format($cotacao_dolar, 4, ',', '.'); // só para mostrar a cotação como texto

            echo "Seus $real_formatado equivalem a <strong>$dolar_formatado</strong>";
            echo "<br><br>*Cotação de <strong>R$$cotacao_formatada</strong> em $data_cotacao, segundo o Banco Central do Brasil.";

            /* Alternativa com number_format():

            $real_formatado = number_format($real, 2, ',', '.');   // R$ formatado manualmente
            $dolar_formatado = number_format($dolar, 2, ',', '.'); // US$ formatado manualmente
            $cotacao_formatada = number_format($cotacao_dolar, 4, ',', '.'); // Cotação formatada

            echo "Seus R$$real_formatado equivalem a <strong>US$$dolar_formatado</strong>";
            echo "<br><br>*Cotação de <strong>R$$cotacao_formatada</strong> em $data_cotacao, segundo o Banco Central do Brasil.";
            */
        ?>
    </main>
</body>
</html>