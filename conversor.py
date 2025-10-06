<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Portfólio Pedro Henrique Brunner Souza</title>
  <style>
    /* ===== ESTILO GERAL ===== */
    body {
      margin: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(270deg, #00ff00, #004d00, #000000);
      background-size: 600% 600%;
      animation: moveBg 8s ease infinite;
      color: white;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      line-height: 1.5;
    }

    /* ===== ANIMAÇÕES ===== */
    @keyframes moveBg {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }

    @keyframes glow {
      from { text-shadow: 0 0 5px #00ff00; }
      to { text-shadow: 0 0 20px #00ff00; }
    }

    @keyframes floatRotate {
      0% { transform: translateY(0px) rotate(0deg); }
      50% { transform: translateY(-10px) rotate(15deg); }
      100% { transform: translateY(0px) rotate(0deg); }
    }

    /* ===== CONTAINER ===== */
    .container {
      background-color: rgba(0, 50, 0, 0.85);
      padding: 25px 35px;
      border-radius: 12px;
      max-width: 600px;
      box-sizing: border-box;
      box-shadow: 0 0 15px #00cc00;
      text-align: center;
      animation: fadeIn 1.2s ease-in-out;
    }

    /* ===== GIF DO ALIEN X ===== */
    .alienx {
      width: 150px;
      height: auto;
      border-radius: 50%;
      box-shadow: 0 0 20px #00ff00;
      margin-bottom: 15px;
      animation: floatRotate 3s ease-in-out infinite, glow 2s infinite alternate;
    }

    /* ===== TÍTULOS ===== */
    h1 {
      color: #00ff00;
      text-shadow: 0 0 10px #00ff00;
      animation: glow 2s ease-in-out infinite alternate;
      font-size: 28px;
      margin-bottom: 5px;
    }

    h3 {
      margin-top: 5px;
      font-weight: 700;
    }

    /* ===== SEÇÃO SOBRE MIM ===== */
    .sobre-mim p {
      font-weight: 600;
      font-size: 14px;
      margin-bottom: 20px;
    }

    /* ===== INFORMAÇÕES ===== */
    .info {
      border-left: 4px solid #00cc00;
      padding-left: 12px;
      margin-bottom: 25px;
      font-size: 14px;
      line-height: 1.4;
      text-align: left;
    }

    .info p {
      margin: 6px 0;
    }

    /* ===== HABILIDADES ===== */
    .skills {
      border-left: 4px solid #00cc00;
      padding-left: 12px;
      margin-bottom: 20px;
      text-align: left;
    }

    .skills span {
      background-color: #004d00;
      padding: 8px 16px;
      margin-right: 15px;
      margin-bottom: 12px;
      border-radius: 8px;
      font-size: 15px;
      font-weight: 600;
      display: inline-block;
      cursor: default;
      transition: background-color 0.3s ease, transform 0.3s ease;
    }

    .skills span:hover {
      background-color: #00cc00;
      transform: scale(1.1);
      color: #000000;
    }

    .skills a {
      color: #00ff00;
      text-decoration: none;
    }

    .skills a:hover {
      text-decoration: underline;
    }

    /* ===== BOTÃO DE DOWNLOAD ===== */
    .btn-download {
      display: inline-block;
      background: #00cc00;
      color: #000000;
      padding: 10px 20px;
      border-radius: 8px;
      text-decoration: none;
      font-weight: bold;
      transition: background-color 0.3s ease, transform 0.3s ease;
    }

    .btn-download:hover {
      background-color: #00ff00;
      transform: scale(1.05);
    }

    /* ===== RESPONSIVIDADE ===== */
    @media (max-width: 480px) {
      .container {
        padding: 20px;
        font-size: 14px;
      }
      .skills span {
        display: block;
        margin-bottom: 10px;
      }
      .alienx {
        width: 120px;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <!-- GIF DO ALIEN X -->
    <img class="alienx" src="https://assets.goal.com/images/v3/bltf6aee452c5dd6d3e/44e1c620aeb8347dc5b7fd7ef68a56c988b0856d.jpg?auto=webp&format=pjpg&width=1080&quality=60" alt="Alien X" />

    <h1>Pedro Henrique Brunner Souza</h1>
    <h3>Portfólio Pessoal</h3>

    <section class="sobre-mim">
      <h3>Sobre Mim</h3>
      <p>Desde cedo, descobri minha paixão pela programação ao explorar computadores e a internet. Programar para mim é criar e resolver problemas com lógica e criatividade. Cada desafio me motiva a aprender, experimentar e encontrar soluções inovadoras. A programação me ensinou paciência, persistência e a valorizar cada conquista. Meu sonho é crescer como programador e transformar ideias em experiências digitais.</p>
    </section>

    <section class="info">
      <p><strong>Nome:</strong> Pedro Henrique Brunner Souza</p>
      <p><strong>Idade:</strong> 15 anos</p>
      <p><strong>Escola:</strong> Colégio Municipal Tenente General Gaspar de Godoi Colaço</p>
      <p><strong>Bairro:</strong> Sítio do Rosário</p>
      <p><strong>Email:</strong> Pedrosouza8@gmail.com</p>
      <p><strong>Telefone:</strong> +55 11 97303-5788</p>
      <p><strong>Série:</strong> 1º Ano do Ensino Médio</p>
    </section>

    <section class="skills">
      <h3>Habilidades</h3>
      <span>
        <a href="https://github.com/PedrosouzaB/Frontend-basico/blob/main/frontend.html" target="_blank">
          Frontend Básico (GitHub)
        </a>
      </span>
      <span>
        <a href="https://github.com/PedrosouzaB/Repositorio_Base_Pedro/blob/main/Modulo%202/APIs/Flask" target="_blank">
          Backend Básico (GitHub)
        </a>
      </span>
      <span>
        <a href="https://github.com/PedrosouzaB/Repositorio_Base_Pedro/blob/main/Modulo%202/Banco%20de%20Dados/tabela%20de%20alunos" target="_blank">
          Banco de Dados (GitHub)
        </a>
      </span>
      <span>
        <a href="https://github.com/PedrosouzaB/Repositorio_Base_Pedro/blob/main/Modulo%202/Manipula%C3%A7%C3%A3o%20de%20Arquivos%20e%20Automa%C3%A7%C3%A3o/criar(pasta%20e%20arquivo)remover(pasta%20e%20arquivo)lista" 
           target="_blank">
          Criação de Aplicativos (GitHub)
        </a>
      </span>
    </section>


  </div>
</body>
</html>
