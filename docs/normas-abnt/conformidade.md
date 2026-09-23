# Conformidade: regra do manual → arquivo do modelo

Mapa de onde cada regra do **Manual de Normalização de Trabalhos Acadêmicos do
IFPI (2024)** foi aplicada. As seções citadas são as do manual; o resumo delas
está em [`normas-ifpi-2024-formatacao.md`](normas-ifpi-2024-formatacao.md).

Use esta tabela para conferir uma exigência do seu curso ou para saber onde
mexer quando precisar adaptar o modelo.

> Mapeamento e aplicação das regras: Erik Santos
> ([@9erikSantos6](https://github.com/9erikSantos6), `9xerix6@gmail.com`),
> discente de Análise e Desenvolvimento de Sistemas, IFPI — Campus Pedro II.
> É uma leitura do manual oficial, sem revisão da biblioteca ou do curso.

## Apresentação geral

| Seção | Regra | Onde está |
| --- | --- | --- |
| 3.1 a | Fonte Arial ou Times New Roman | `configuracoes/tipografia.tex` (Times por padrão; Helvetica comentada) |
| 3.1 b | Texto em preto | `configuracoes/cores.tex` |
| 3.1 c | Tamanho 12 em todo o trabalho | opção `12pt` em `main.tex` |
| 3.1 d | Tamanho 10 em citações longas, notas, paginação, legendas e fontes | `\ABNTEXfontereduzida` em `abntex-ifpi/abntex-ifpi.sty` |
| 3.2 | Margens 3 cm (esq./sup.) e 2 cm (dir./inf.) | `\setulmarginsandblock` e `\setlrmarginsandblock` em `abntex-ifpi/abntex-ifpi.sty`; para anverso e verso, troque `oneside` por `twoside` em `main.tex` e as margens espelham sozinhas |
| 3.3 a-b | Entrelinhas 1,5; simples nas exceções | `configuracoes/espacamentos.tex` (o artigo é exceção: simples em todo o texto, seções 3.6.1 e 7.4) |
| 3.3 c | Referências separadas por uma linha em branco | `\bibitemsep` em `configuracoes/citacoes.tex` |
| 3.4 a | Corpo do texto justificado | padrão da classe |
| 3.4 c | Recuo de 1,25 cm e 0 pt entre parágrafos | `configuracoes/espacamentos.tex` |
| 3.4 d | Papel A4 | opção `a4paper` em `main.tex` |
| 3.5 | Paginação no canto superior direito, a 2 cm das bordas, tamanho 10, a partir da parte textual | estilo `abntifpi` em `abntex-ifpi/abntex-ifpi.sty`, aplicado por `estrutura/textual.tex` |
| 3.5 d | Paginação contínua, inclusive na folha de abertura dos apêndices e anexos | `\aliaspagestyle{part}{abntifpi}` em `abntex-ifpi/abntex-ifpi.sty` |
| 3.6 | Um espaço de caractere entre indicativo e título; título de mais de uma linha alinhado sob a primeira letra | `\@seccntformat` em `abntex-ifpi/abntex-ifpi.sty` |
| 3.6.1 | Títulos sem indicativo numérico, centralizados e com o destaque das seções primárias | opção `chapter=TITLE` em `main.tex`; nomes de apêndices e anexos em `abntex-ifpi/abntex-ifpi.sty` |
| 3.7 | Numeração progressiva com destaque hierárquico | blocos `\ABNTEXsection*` em `abntex-ifpi/abntex-ifpi.sty`. O abnTeX2 oferece quatro níveis numerados (`\section` a `\subsubsubsection`); a seção quinária é o limite máximo da norma, não uma exigência, e **não** existe como comando — veja *Limitações conhecidas* |
| 3.7.1-3.7.2 | Alíneas e subalíneas | ambientes `alineas` e `subalineas` do abnTeX2; exemplo em `capitulos/02-fundamentacao-teorica.tex` |
| 3.8 | Siglas com nome completo na primeira menção | responsabilidade do autor; lista em `pre-textual/opcionais/siglas.tex` |
| 3.10 | Equações centralizadas e numeradas à direita | ambiente `equation`; exemplo em `capitulos/04-resultados.tex` |
| 3.11 | Ilustração: título acima, centralizado, tamanho 12; fonte obrigatória abaixo, tamanho 10 | `\captionsetup` e `\fonte` em `abntex-ifpi/abntex-ifpi.sty` |
| 3.12 | Tabela (laterais abertas) × quadro (fechado) | ambiente `quadro` em `abntex-ifpi/abntex-ifpi.sty`; exemplo em `capitulos/03-metodologia.tex` |
| 3.13 | Notas de rodapé em tamanho 10, com filete de 5 cm, numeração contínua | `\setfootnoterule` em `abntex-ifpi/abntex-ifpi.sty` |

## Resumo e palavras-chave (seção 4)

| Regra | Onde está |
| --- | --- |
| Parágrafo único, sem recuo, justificado, tamanho 12 | `pre-textual/resumo.tex` |
| 150 a 250 palavras no artigo | orientação em `pre-textual/resumo.tex` |
| Resumo em língua estrangeira obrigatório | `pre-textual/resumo-lingua-estrangeira.tex` |
| `Palavras-chave:` em negrito, 3 a 5 descritores separados por ponto e vírgula | `pre-textual/resumo.tex` e `configuracoes/metadados.tex` |

## Estrutura (seções 5 e 7.2)

| Regra | Onde está |
| --- | --- |
| Ordem dos elementos pré-textuais | `estrutura/pre-textual.tex` |
| Ordem dos elementos pós-textuais (referências → glossário → apêndice → anexo) | `estrutura/pos-textual.tex` |
| Capa: instituição, autor, título, local, ano | `\imprimircapa` em `abntex-ifpi/abntex-ifpi.sty` |
| Folha de rosto com natureza do trabalho em espaço simples, do meio da mancha para a direita | `\folhaderostocontent` em `abntex-ifpi/abntex-ifpi.sty` (`\hspace*{.5\textwidth}` + `\SingleSpacing`) |
| Folha de aprovação com data de aprovação e natureza em espaço simples | `\imprimirfolhadeaprovacao` e `\imprimirfolhadeaprovacaoduascolunas` em `abntex-ifpi/abntex-ifpi.sty` |
| Ficha catalográfica: dispensada no artigo | `pre-textual/opcionais/ficha-catalografica.tex` |
| Sumário com os mesmos destaques do texto | blocos `\cft*font` em `abntex-ifpi/abntex-ifpi.sty` |
| Pré-textuais contados e não numerados | `\pretextual` do abnTeX2 |
| Apêndice e anexo com paginação contínua | `estrutura/pos-textual.tex` |
| Título e autoria do artigo, com notas de rodapé de identificação | `pre-textual/resumo.tex` e `configuracoes/metadados.tex` |
| Data de aprovação em DD/MM/AAAA abaixo das *keywords* | `pre-textual/resumo-lingua-estrangeira.tex` |

## Citações (seção 10 — NBR 10520:2023)

| Regra | Onde está |
| --- | --- |
| Chamada em maiúsculas e minúsculas: `(Silva, 2020)` | perfil `abnt-nbr10520=2023` em `abntex-ifpi/abntex-ifpi.bib`, acionado por `configuracoes/citacoes.tex` |
| Um único sistema de chamada no trabalho | opção `alf` em `configuracoes/citacoes.tex` |
| Dois autores ligados por "e" | mesmo perfil |
| `et al.` em itálico a partir de quatro autores | `abnt-etal-list` e `abnt-etal-text` em `configuracoes/citacoes.tex` |
| Citação direta de até 3 linhas entre aspas | exemplo em `capitulos/02-fundamentacao-teorica.tex` |
| Citação com mais de 3 linhas: recuo 4 cm, tamanho 10, espaço simples, sem aspas | ambiente `citacao` do abnTeX2, com `\ABNTEXcitacaorecuo` corrigido em `abntex-ifpi/abntex-ifpi.sty` (o valor original do abnTeX2 somava o recuo de lista e produzia 5 cm) |
| Citação de citação (`apud`) | comando `\apud`; exemplo em `capitulos/02-fundamentacao-teorica.tex` |

## Referências (seção 11 — NBR 6023:2018)

| Regra | Onde está |
| --- | --- |
| Entrada da referência em caixa alta | estilo `abntex2-alf` |
| Espaço simples, alinhadas à margem esquerda, separadas por linha em branco | `bibleftalign` e `\bibitemsep` em `configuracoes/citacoes.tex` |
| Destaque do título uniforme | `abnt-emphasize=bf` em `configuracoes/citacoes.tex` |
| Sobrenome composto, com prefixo ou grau de parentesco | `abnt-last-names=bibtex` em `abntex-ifpi/abntex-ifpi.bib`; instruções em `bibliografia.bib` |
| Ordenação alfabética em lista única | estilo `abntex2-alf` |
| Só entram as obras citadas | comportamento do BibTeX |
| Nenhum texto estranho à referência | pacote `backref` desativado em `estrutura/preambulo.tex` |
| Modelos por tipo de obra (livro, capítulo, artigo, evento, tese, legislação, rede social) | `bibliografia.bib` |

## Limitações conhecidas

Pontos em que o PDF gerado não reproduz exatamente o manual e a causa está
fora do modelo. Confira com o seu curso se algum deles for exigido:

- **Numeração até a seção quinária (3.7):** o abnTeX2 tem quatro níveis
  numerados — `\section`, `\subsection`, `\subsubsection` e
  `\subsubsubsection`. Não use `\paragraph` para tentar um quinto: ele
  ocupa o mesmo nível de `\subsubsubsection` e sai numerado como outra seção
  quaternária (`1.1.1.2`). A norma fixa a quinária como limite, não como
  exigência.
- **Endereços nas referências (11.4):** o estilo `abntex2-alf` imprime a URL
  entre `<` e `>` (`Disponível em: <https://...>`), forma da edição anterior
  da NBR 6023. Corrigir isso exige alterar o arquivo `.bst` do abnTeX2.
- **Travessão das legendas (3.11):** as legendas saem com o travessão curto
  (`Figura 1 – Título`), padrão do abnTeX2.
- **Tamanho das legendas:** o manual pede fonte 12 na identificação da
  ilustração (seção 3.11) e fonte 10 nas legendas (seção 3.1, alínea d). O
  modelo adota 12 no título e 10 na fonte consultada; se o seu curso exigir
  10 também no título, troque `font=normalsize` por
  `font=\ABNTEXfontereduzida` no `\captionsetup` do estilo.

## O que o modelo não resolve por você

Estas regras dependem da redação, não da formatação:

- resumo informativo, com verbo na voz ativa e na terceira pessoa do singular
  (seção 4);
- nome completo da sigla na primeira menção (seção 3.8);
- pontuação das alíneas: ponto e vírgula em todas, ponto final na última, dois
  pontos quando houver subalínea (seção 3.7.1);
- citar no texto toda ilustração, tabela e quadro (seções 3.11 e 3.12);
- não introduzir citações nem discussões novas na conclusão (seção 5.2.2);
- conferir os dados de cada referência com a publicação real (seção 11).

## Diferenças para monografia, dissertação e tese

Este modelo implementa a modalidade **artigo** (seção 7). Para as demais
modalidades, além de conferir as exigências do curso:

1. remova a opção `article` de `main.tex` e passe a usar `\chapter` nos títulos
   principais;
2. troque `\SingleSpacing` por `\OnehalfSpacing` em
   `configuracoes/espacamentos.tex` (a exceção do espaçamento simples vale só
   para o artigo);
3. ative a folha de aprovação, a ficha catalográfica e o sumário em
   `estrutura/pre-textual.tex` — os três passam a ser obrigatórios (a natureza
   do trabalho continua em espaço simples nas duas folhas, mesmo com o corpo
   do texto em 1,5);
4. lembre que as seções primárias devem começar em página ímpar (seção 3.6).
