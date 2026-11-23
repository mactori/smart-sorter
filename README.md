# Smart Sorter

Simulador de triagem de pacotes feito em Python. O programa lê o código de barras de um pacote pela webcam, consulta as informações dele em um banco de dados e mostra para qual área o pacote deve ser encaminhado.

> **Vídeo de demonstração:** [(https://drive.google.com/file/d/15ynDOiazvpRNuuiz8VqW2Mda8Dq6EsVL/view?usp=sharing)]

## Como funciona

1. A webcam fica aberta aguardando um código de barras.
2. Quando um código é lido, o programa procura o pacote no banco de dados (SQLite).
3. Com as informações do pacote, ele decide a rota e mostra o resultado.
4. Em seguida, a câmera é reaberta para o próximo pacote. Para encerrar, é só apertar **ESC**.

## Regras de classificação

As regras são verificadas nesta ordem:

| Condição | Destino |
|---|---|
| Pacote frágil | ÁREA DE FRÁGEIS |
| Tamanho "grande" **ou** peso maior que 5 | ÁREA DE CARGAS |
| Qualquer outro caso | ÁREA DE COMUNS |

Se o código lido não existir no banco, o programa avisa que o pacote não foi encontrado.

## Tecnologias

- **Python 3.14**
- **OpenCV** para acessar a webcam e mostrar a imagem
- **zxing-cpp** para ler os códigos de barras
- **SQLite** para guardar os dados dos pacotes

## Formato dos códigos de barras

Os códigos usam o padrão **Code 128**, que aceita letras, números e hífen. Exemplo: `BR-RIO-NIT-001`.

## Estrutura do projeto

```
smart-sorter/
├── main.py            # programa principal (leitura + classificação)
├── database.db        # banco de dados com os pacotes
```

## Banco de dados

O banco `database.db` tem uma tabela chamada `pacotes`, com as colunas:

| Coluna | Tipo | Descrição |
|---|---|---|
| `codigo_barras` | TEXT | Código do pacote lido pela câmera (chave primária). Ex.: `BR-RIO-NIT-001` |
| `peso` | KG | Peso do pacote |
| `tamanho` | TEXT | Tamanho do pacote (`pequeno` ou `grande`) |
| `fragil` | INTEGER | `1` = frágil, `0` = não frágil |

## Como instalar

1. Instale o Python 3.14.
2. Na pasta do projeto, instale as bibliotecas:

```
py -m pip install opencv-python zxing-cpp 
```

## Como usar

**1. Gerar as imagens dos códigos de barras** no formato Code 128, com os códigos cadastrados no banco (por exemplo, usando um gerador online). Imprima ou abra a imagem na tela do celular.

**2. Rodar o programa:**

```
py main.py
```

Aponte um código para a câmera. O resultado aparece no terminal. Aperte **ESC** para sair.


## Dicas para uma boa leitura

- Use boa iluminação e evite reflexos.
- Deixe uma margem branca em volta do código.
- Mantenha o código reto e a uma distância em que ele fique nítido.

## Problemas comuns

- **Erro "DLL load failed" ao importar o NumPy (Windows):** instale o *Microsoft Visual C++ Redistributable* e, se continuar, use uma versão um pouco mais antiga do NumPy: `py -m pip install "numpy<2.4"`.
- **A câmera não abre:** feche outros programas que estejam usando a webcam.

## Autora
mactori

[LinkedIn](www.linkedin.com/in/mactori) · [GitHub](https://github.com/mactori)
