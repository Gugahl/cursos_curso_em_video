<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manipulação de strings em PHP</title>
</head>
<body>
    <h2>Manipulando strings</h2>
    <?php 
        $nome = "Gustavo";
        $sobrenome = "Lima";
        echo "$nome $sobrenome \u{1F60E}<br>";
        echo '$nome $sobrenome \u{1F60E}<br>';

        const CANAL = "Gustavo Lima";
        echo "<br>Meu canal do YouTube é CANAL <br>";
        echo "<br>Meu canal do YouTube é " . CANAL . "<br>";

        const ESTADO = "Alagoas";
        echo "<br>Moro em " . ESTADO . "<br>";

        echo "<br>Estamos no ano date('Y')";
        echo "<br>Estamos no ano " . date('Y'). "<br>";

        $nome = "Gustavo";
        $apelido = "Guga";
        $sobrenome = "Lima";
        echo "<br>$nome $apelido $sobrenome";
        echo "<br>$nome '$apelido' $sobrenome";
        echo "<br>$nome \"$apelido\" $sobrenome<br>";


        $curso = "PHP";
        $ano = date('Y');
        echo <<< FRASE
        <br>Estou estudando
            $curso em $ano<br>
        FRASE;

        echo <<< FRASE
        <br>Fala moleques e
                    molecas
                belezaaaaa? <br>
        $nome aqui dessa vez
        no ano de $ano<br> 
        trazendo mais um vídeo
        para vocês! \u{1F60E}<br>
        FRASE;

        echo <<< 'FRASE'
        <br>Fala moleques e
                    molecas
                belezaaaaa? <br>
        $nome aqui dessa vez
        no ano de $ano<br> 
        trazendo mais um vídeo
        para vocês! \u{1F60E}
        FRASE;
    ?>
</body>
</html>