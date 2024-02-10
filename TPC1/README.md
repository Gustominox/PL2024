# TPC1: Análise de um Dataset

- Proibido usar o módulo CSV;
- Ler o dataset, processá-lo e criar os seguintes resultados:
    1. Lista ordenada alfabeticamente das modalidades desportivas.
    2. Percentagens de atletas aptos e inaptos para a prática desportiva.
    3. Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos).

## Estrutura do Repositório

- `emd.csv`: O arquivo CSV contendo os dados do dataset.
- `solution.py`: O script Python para realizar a análise do dataset.
- `resultados/`: Pasta onde os resultados da análise serão armazenados.
  - `modalidades.txt`: Arquivo contendo a lista ordenada alfabeticamente das modalidades desportivas.
  - `aptos_inaptos.txt`: Arquivo contendo as percentagens de atletas aptos e inaptos.
  - `distribuicao_idades.txt`: Arquivo contendo a distribuição de atletas por escalão etário.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Abra um terminal ou prompt de comando.
3. Navegue até o diretório onde este repositório está clonado.
4. Execute o seguinte comando para rodar a análise do dataset:

   ```
   python solution.py
   ```

5. Os resultados serão gerados na pasta `resultados/`.

## Requisitos

- Python 3.x
- Um editor de texto ou IDE para revisar o código (opcional)

## Observações

- Este projeto foi desenvolvido como parte de um trabalho acadêmico.
- O dataset utilizado neste projeto está armazenado no arquivo `emd.csv`.
- O script Python `solution.py` contém o código para processar o dataset e gerar os resultados solicitados.
- Este projeto segue as diretrizes do enunciado do TPC1.
