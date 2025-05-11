# Captador de Temperatura de São Paulo

Este projeto automatiza a coleta de informações de clima (temperatura, umidade, etc) da cidade de São Paulo utilizando Python, Selenium e Tkinter.

## Funcionalidades

- Acesso automático à previsão do tempo via navegador
- Coleta de:
  - Temperatura atual
  - Clima (ensolarado, nublado, etc)
  - Umidade do ar
  - Velocidade do vento
- Armazenamento dos dados em uma planilha Excel
- Interface gráfica para acionar a coleta com um clique

## Tecnologias Utilizadas

- Python 3.11+
- Selenium
- Tkinter
- OpenPyXL
- ChromeDriver

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Yuri-Melo123/Portfolio-Development-with-Python.git
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Baixe o ChromeDriver compatível com sua versão do Google Chrome.

## Como Usar

```bash
python interface.py
```

Clique no botão "Buscar previsão" para coletar os dados.

## Fluxograma

Veja o funcionamento no arquivo `fluxograma.pdf`.

## Aprendizados

Este projeto proporcionou uma experiência prática de automação com Python, incluindo:
- Web scraping com Selenium
- Manipulação de arquivos Excel
- Criação de interfaces com Tkinter

Desenvolvido por Yuri de Oliveira Melo
