<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h2>Resultado do Processamento</h2>
    </header>
    <main>
        <?php 
        $nome = $_GET["nome"] ?? "Sem nome";
        $sobrenome = $_GET["sobrenome"] ?? "Sem sobrenome";
        echo "<p>É um prazer te conhecer <strong>$nome $sobrenome</strong>! Este é o meu site!</p>"
        ?>
        <p><a href="javascript:history.go(-1)">Voltar para a página anterior</a></p>
    </main>
</body>
</html>