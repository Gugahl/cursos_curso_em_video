<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 005 - Analisador de número real</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <main>
        <h1>Analisador de Número Real</h1>
        <?php 
            // Captura e normaliza o número real
            $num = $_GET["num"] ?? 0;
            $num = str_replace(',', '.', $num); // garante que vírgula seja interpretada como decimal

            $parte_inteira = floor($num);
            $parte_decimal = $num - $parte_inteira;

            // Formatação apenas na exibição
            $num_formatado = number_format($num, 3, ',', '.');
            $parte_inteira_formatada = number_format($parte_inteira, 0, '', '.');
            $parte_decimal_formatada = number_format($parte_decimal, 3, ',', '.');

            echo <<<FRASE
            Analisando o número <strong>$num_formatado</strong> informado pelo usuário:
            <br><br>
            <ul>
                <li>A parte inteira do número é <strong>$parte_inteira_formatada</strong></li>
                <li>A parte fracionária do número é <strong>$parte_decimal_formatada</strong></li>
            </ul>
            FRASE;
        ?>
        <p><a href="javascript:history.go(-1)"><input type="button" value="&#x2B05; Voltar"></a></p>
        </main>
</body>
</html>