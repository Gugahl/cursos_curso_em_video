<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 006 - Anatomia de uma divisão</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <?php 
        $dividendo = $_POST["dividendo"] ?? 0;
        $divisor = $_POST["divisor"] ?? 1;

        $divisao_real = $dividendo/$divisor;
        $divisao_real = number_format($divisao_real, 2, ',', '.');
        
        $divisao_inteira = intdiv($dividendo, $divisor);

        $resto_da_divisao = $dividendo % $divisor;
    ?>
    <main>
        <h1>Anatomia de uma Divisão</h1>
        <form action="" method="post">
            <label for="dividendo">Digite aqui o número a ser dividido:</label>
            <input type="number" name="dividendo" id="iddividendo" value="<?= $dividendo?>">

            <label for="divisor">Digite aqui o número divisor:</label>
            <input type="number" name="divisor" id="iddivisor" value="<?= $divisor?>">

            <input type="submit" value="Analisar">
        </form>
    </main>

    <section>
        <h2>Estrutura da Divisão</h2>
        <div>
            <p> 
                <?=
                "O resultado da divisão real: $dividendo / $divisor é igual a $divisao_real e o resto dessa operação é igual a $resto_da_divisao<br>" .
            
                "<ul>
                <li>Dividendo: $dividendo
                <li>Divisor: $divisor
                <li>Quociente: $divisao_real
                <li>Resto da divisao: $resto_da_divisao
                <li>Divisão inteira: $divisao_inteira
                </ul><br>" .

                "
                <table class=\"divisao\">
                    <tr>
                        <td>$dividendo</td>
                        <td>$divisor</td>
                    </tr>
                    <tr>
                        <td>$resto_da_divisao</td>
                        <td>$divisao_real</td>
                    </tr>
                </table>
                "
            ?>
            </p>
        </div>
    </section>
</body>
</html>