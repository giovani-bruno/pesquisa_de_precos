# Google Shopping Price Scraper

## Descrição

Este é um projeto em Python que realiza a pesquisa de preços de produtos no Google Shopping, coleta informações sobre os produtos e envia os resultados por e-mail. Ele permite que os usuários especifiquem o produto, os preços mínimo e máximo, e o seu endereço de e-mail para receber os resultados. O script utiliza Selenium para automação do navegador e coleta de dados.

## Funcionalidades

- Pesquisa de produtos no Google Shopping.
- Filtragem de resultados com base em preços mínimos e máximos.
- Geração de uma tabela HTML com os resultados.
- Envio da tabela por e-mail para o usuário com o menor preço destacado.

## Como Funciona

1. O usuário insere o nome do produto, preço mínimo e máximo, e um endereço de e-mail.
2. O script utiliza o [Selenium](https://selenium-python.readthedocs.io/) para realizar a pesquisa no Google Shopping e filtrar os resultados.
3. Os dados coletados (nomes dos produtos, preços e links) são armazenados em um DataFrame.
4. Uma tabela HTML é gerada a partir do DataFrame, destacando o produto com o menor preço.
5. A tabela é enviada por e-mail para o endereço especificado pelo usuário utilizando o [smtplib](https://docs.python.org/3/library/smtplib.html).

Obs: o script que contém a função de enviar o e-mail não foi incluído no repositório por motivos de segurança

## Executando

Para executar este projeto, tudo o que você precisa fazer é baixar a pasta `dist` e executar o arquivo `pesquisaPreco.exe`. Preencha as informações solicitadas e aguarde o recebimento do e-mail.
O executável foi feito usando o [PyInstaller](https://pyinstaller.org/en/stable/).

É necessário ter o Google Chrome instalado no seu computador para que o Selenium possa automatizar o navegador.

Clique [aqui](https://github.com/Numl8ck/pesquisa_preco/raw/main/dist) para baixar a pasta.
