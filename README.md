# pyLSM

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24237179.svg)](https://doi.org/10.5281/zenodo.24237179)

**pyLSM** é um aplicativo desktop interativo desenvolvido em Python (PyQt5) para fins didáticos e de pesquisa, aplicando o **Lattice Strain Model (LSM)** de Blundy & Wood (1994) e Brice (1975) para modelar a partição de elementos traço entre minerais e líquidos e observar as variações dos parâmetros físico-químicos associados.

---

## Visão Geral

O pyLSM explora graficamente como parâmetros termodinâmicos ($T$), elásticos ($E_N$, módulo de Young) e cristaloquímicos ($r_0$, raio iônico ideal) afetam o comportamento parabólico dos coeficientes de partição de elementos traço em sítios cristalinos.

## Principais Funcionalidades

* **Simulação Interativa em Tempo Real:** Sliders dinâmicos para ajuste de $D_0$, $E_N$, $r_0$ e Temperatura ($T$).
* **Visualização Gráfica:** Curvas de partição em escala logarítmica geradas com Matplotlib e atualizadas instantaneamente.
* **Fundamentação Teórica Integrada:** Diálogo embutido com as referências clássicas da literatura geoquímica.
* **Interface Moderna:** Construída com PyQt5 para uso em salas de aula, laboratórios e suporte a pesquisas em petrologia ígnea.

## Instalação

Clone o repositório e instale as dependências necessárias:

```bash
git clone https://github.com/ocaminhodaspedras/pylsm.git
cd pylsm
pip install -r requirements.txt
```

### Dependências
* Python 3.8+
* NumPy
* Matplotlib
* PyQt5

## Uso

Para iniciar a aplicação desktop, execute o script principal:

```bash
python main.py
```

## Referências Principais

* **Brice, J. C. (1975).** Some thermodynamic aspects of the growth of strained crystals. *Journal of Crystal Growth*, 28(2), 249-253.
* **Blundy, J., & Wood, B. (1994).** Prediction of crystal-melt partition coefficients from elastic moduli. *Nature*, 372(6505), 452-454.

## Como Citar

Se você utilizar o pyLSM em suas pesquisas, aulas ou publicações, cite-o utilizando o DOI emitido pelo Zenodo:

> Leitzke, F. P. (2026). pyLSM: Explorador Didático do Modelo de Deformação de Rede (Version 1.0) [Computer software]. https://doi.org/10.5281/zenodo.XXXXXXX

Consulte o arquivo `CITATION.cff` para formatos de exportação direta (BibTeX, APA).

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
