# Modelo de artigo acadêmico — IFPI

Um ponto de partida em LaTeX para escrever um artigo de conclusão de curso,
baseado no abnTeX2 e no abntex-ifpi. Você escreve em arquivos de texto comuns e
a compilação transforma esses arquivos em um PDF com a formatação do modelo.

A formatação segue o **Manual de Normalização de Trabalhos Acadêmicos do IFPI,
edição de 2024** (ISBN 978-65-86592-96-2), que consolida as normas ABNT NBR
6022, 6023:2018, 6024:2012, 6027:2012, 6028:2021, 10520:2023, 14724:2011 e
15287:2011. O resumo das regras usadas está em
[`docs/normas-abnt/`](docs/normas-abnt/), e
[`docs/normas-abnt/conformidade.md`](docs/normas-abnt/conformidade.md) diz,
regra por regra, em que arquivo cada uma foi aplicada.

> **Se você usava a versão anterior deste modelo**, a mudança mais visível é a
> das citações: a NBR 10520:2023 acabou com a caixa alta na chamada. Onde saía
> `(SILVA, 2020)` agora sai `(Silva, 2020)`. A entrada da referência, no fim do
> trabalho, continua em caixa alta. Veja a seção
> [O que mudou na atualização de 2024](#o-que-mudou-na-atualização-de-2024).

**Nunca usou LaTeX? Siga os cinco passos abaixo.** Não é preciso entender os
arquivos de estilo para escrever seu trabalho. Se travar em algum ponto, o
`docs/guia-iniciante.md` explica cada tarefa com mais calma.

## Comece em cinco passos

1. **Abra o projeto inteiro** no editor que você vai usar (veja
   "[Onde escrever](#onde-escrever)" logo abaixo). O modelo só funciona
   completo: `main.tex` sozinho não compila, porque depende das outras pastas.
2. **Compile uma vez, antes de editar qualquer coisa.** Se o PDF sair, o
   ambiente está certo e qualquer erro daqui em diante veio da sua edição.
   O documento principal é `main.tex`, o compilador é **pdfLaTeX** e a
   bibliografia usa **BibTeX** (não Biber).
3. **Preencha `configuracoes/metadados.tex`:** título, seu nome, curso, campus,
   cidade, ano, orientação, banca, data de apresentação, notas de rodapé dos
   autores e palavras-chave. É o único arquivo com dados pessoais.
4. **Escreva seu texto** nos arquivos de `capitulos/` e substitua o resumo e o
   abstract em `pre-textual/`. Os textos que vêm no modelo são exemplos de
   preenchimento: apague-os.
5. **Cadastre suas referências em `bibliografia.bib`** e compile de novo.
   Troque também as imagens e as tabelas de demonstração.

## Onde escrever

O modelo funciona nos três ambientes abaixo. Escolha um.

### OpenAI Prism (prism.openai.com)

1. Gere ou baixe o ZIP do modelo (`dist/modelo-artigo-ifpi.zip`, criado por
   `scripts/empacotar.py`; quem recebeu o ZIP já pode usá-lo direto).
2. No Prism, crie um projeto e **importe o ZIP**.
3. Abra `main.tex` na lista de arquivos à esquerda. O Prism compila sozinho e
   mostra o PDF ao lado; não há botão de compilar a cada alteração.
4. Se o PDF não aparecer, abra o painel de erros/log e procure a **primeira**
   mensagem — as seguintes costumam ser consequência dela.

### Overleaf (overleaf.com)

1. **New Project → Upload Project** e envie o ZIP do modelo.
2. **Menu** (canto superior esquerdo) → **Compiler: pdfLaTeX** e
   **Main document: main.tex**.
3. Clique em **Recompile**. O Overleaf executa o BibTeX automaticamente.
4. Deu erro? Clique em **Logs and output files** e leia o primeiro erro.
   Todos os pacotes usados aqui já vêm instalados no Overleaf.

### No seu computador

Você precisa de uma distribuição LaTeX com os pacotes que o modelo usa.
A instalação completa (TeX Live `scheme-full`, MacTeX, ou MiKTeX instalando
pacotes sob demanda) já traz tudo. Instalações menores falham com
`abntex2.cls not found` ou `... .sty not found`; nesse caso instale:

```
tlmgr install abntex2 simplecd tcolorbox tikzfill pdfcol environ trimspaces multirow ifmtarg
```

Essa é a lista exata do que falta em um TeX Live `scheme-medium` — foi obtida
compilando este modelo e instalando cada pacote que o log pediu.

Na pasta que contém `main.tex`, execute:

```
latexmk
```

O arquivo `.latexmkrc` já configura pdfLaTeX e BibTeX, então não são precisas
opções extras. O resultado é `main.pdf`. O latexmk repete a compilação quantas
vezes for necessário para resolver sumário, citações e referências cruzadas.

Se aparecer `??` no lugar de uma citação ou de um número de figura, deixe o
ciclo completo terminar. Se persistir, veja a tabela de problemas no
`docs/guia-iniciante.md`.

## Onde editar cada coisa

| Quero alterar… | Arquivo ou pasta |
| --- | --- |
| Título, autoria, curso, campus, orientação, banca e palavras-chave | `configuracoes/metadados.tex` |
| Resumo em português | `pre-textual/resumo.tex` |
| Abstract em inglês | `pre-textual/resumo-lingua-estrangeira.tex` |
| Introdução, fundamentação, metodologia, resultados, conclusão e trabalhos futuros | `capitulos/` (seis arquivos) |
| Ordem das seções ou inclusão de outra seção | `estrutura/textual.tex` |
| Capa, folha de rosto, folha de aprovação, listas e sumário | `estrutura/pre-textual.tex` |
| Agradecimentos, dedicatória, epígrafe, errata e outros opcionais | `pre-textual/opcionais/` |
| Referências bibliográficas | `bibliografia.bib` |
| Apêndices, anexos, glossário e índice | `pos-textual/` e `estrutura/pos-textual.tex` |
| Figuras e gráficos | `imagens/` |
| Fonte tipográfica, espaçamentos, cores e estilo de citação | `configuracoes/` |
| Regras de formatação da norma (títulos, paginação, quadros, legendas) | `abntex-ifpi/abntex-ifpi.sty` |

## O que normalmente não precisa ser alterado

- `main.tex`: reúne as partes do documento; não escreva o artigo dentro dele.
- `estrutura/preambulo.tex`: carrega os pacotes e as configurações.
- `configuracoes/compatibilidade.tex`: ajusta a convivência entre abnTeX2,
  memoir e os nomes em português do Babel. É carregado antes do
  `\documentclass`, de propósito.
- `abntex-ifpi/`: estilo institucional, logotipo e suporte a diagramas UML.
  O `abntex-ifpi.sty` concentra as regras de formatação do manual de 2024;
  o `abntex-ifpi.bib` só carrega o perfil de citação da NBR 10520:2023 — não
  cadastre obras nele.
- `.latexmkrc`: configuração da compilação local.
- `.gitignore`: lista dos arquivos gerados, que não devem ser versionados.
- `scripts/empacotar.py`: gera o ZIP de distribuição (veja `docs/publicacao.md`).
- `_config.yml`: tema usado caso o repositório seja publicado no GitHub Pages.
- `docs/`: os guias que você está lendo.

## Antes de entregar

- [ ] Troque todos os dados de `configuracoes/metadados.tex`, inclusive a data
      de apresentação — ela aparece no rodapé da página do abstract mesmo sem
      folha de aprovação, e vai no formato `DD/MM/AAAA`.
- [ ] Apague os e-mails `example.com` das notas de rodapé dos autores.
- [ ] Substitua o resumo, o abstract e o texto de todos os capítulos. O resumo
      do artigo tem de 150 a 250 palavras, em parágrafo único.
- [ ] Confira as palavras-chave: de 3 a 5, separadas por ponto e vírgula,
      terminadas em ponto e com iniciais minúsculas.
- [ ] Remova as figuras, tabelas e quadros de demonstração. Procure por
      `EXEMPLO` nos arquivos: todo bloco de demonstração está marcado assim.
- [ ] Confirme que toda ilustração, tabela e quadro é citado no texto e tem
      indicação de fonte — obrigatória mesmo quando o material é seu.
- [ ] Desative o apêndice de exemplo em `estrutura/pos-textual.tex` se você não
      tiver apêndice, ou substitua o conteúdo dele.
- [ ] Apague de `bibliografia.bib` as entradas de exemplo (chaves começadas por
      `exemplo-`) e as obras que você não citou. Só entram nas referências as
      obras efetivamente citadas.
- [ ] Ative os elementos exigidos pelo seu curso. Sumário e listas vêm
      desativados na configuração inicial de artigo, porque a estrutura do
      artigo (seção 7.2 do manual) não os exige.
- [ ] Revise o PDF inteiro: legendas, numeração, referências e apêndices.
- [ ] Confirme com o curso ou a biblioteca as exigências de apresentação.

## O que mudou na atualização de 2024

| Item | Antes | Agora | Regra |
| --- | --- | --- | --- |
| Chamada da citação | `(SILVA, 2020)` em versalete | `(Silva, 2020)` | NBR 10520:2023; manual, seção 10 |
| Ligação entre dois autores | `Silva & Souza (2020)` | `Silva e Souza (2020)` | manual, seção 10.2 |
| Sobrenome composto ou com grau de parentesco | `NETO, M. S.` | `SILVA NETO, M.` | manual, seção 11.4 |
| Recuo de parágrafo | 1,5 cm | 1,25 cm | manual, seção 3.4, alínea c |
| Entrelinhas do artigo | 1,5 | simples | manual, seções 3.6.1 e 7.4 |
| Indicativo de seção | `1&nbsp;&nbsp;&nbsp;&nbsp;INTRODUÇÃO` | `1 INTRODUÇÃO` | manual, seções 3.6 e 3.7 |
| Paginação | tamanho 12, sem posição definida | tamanho 10, a 2 cm do topo e da borda direita | manual, seção 3.5 |
| Filete da nota de rodapé | ~6,4 cm | 5 cm | manual, seção 3.13 |
| Título de tabela | tamanho 10 | tamanho 12 (a fonte continua em 10) | manual, seções 3.1 e 3.12 |
| Legendas longas | alinhadas à esquerda | centralizadas | manual, seção 3.11 |
| Títulos pós-textuais | `Referências`, `Apêndices` | `REFERÊNCIAS`, `APÊNDICES` | manual, seções 3.6.1 e 5.2.3 |
| Sumário | sem destaque por nível | mesmos destaques do texto | manual, seção 5.1.2.14 |
| Quadro | não existia (só tabela) | ambiente `quadro`, com numeração e lista próprias | manual, seção 3.12 |
| Referências | justificadas | alinhadas à margem esquerda | manual, seção 11.3 |
| "Citado na página X" nas referências | ligado | desligado (é apoio à revisão, não elemento da referência) | manual, seção 11.3 |

Recursos que passaram a ter exemplo pronto no modelo: alíneas e subalíneas
(`alineas`/`subalineas`), citação direta curta, citação indireta, citação de
citação (`\apud`), quadro e equação numerada.

## Créditos e licença

Modelo derivado do abntex-ifpi, criado por Rafael Madureira Lins de Araújo, com
adaptações descritas na versão recebida por Tulio Vidal, IFPI — Campus Corrente
(`tulio.vidal@ifpi.edu.br`). A documentação original informa como bases um
modelo de monografia do IFPI e o Manual de Normalização de Trabalhos Acadêmicos
do IFPI de 2022; esta versão atualiza a formatação para a **edição de 2024** do
mesmo manual.

A atualização da formatação para a edição de 2024 do Manual de Normalização de
Trabalhos Acadêmicos do IFPI, feita a partir do documento oficial, e a
documentação de `docs/normas-abnt/` são de Erik Santos
([@9erikSantos6](https://github.com/9erikSantos6), `9xerix6@gmail.com`),
discente do curso de Análise e Desenvolvimento de Sistemas, IFPI — Campus
Pedro II.

**Este projeto não é uma publicação oficial do IFPI e não certifica
conformidade.** A modalidade implementada é **artigo**, não um modelo completo
de monografia. Confirme sempre as exigências com o seu curso e com a
biblioteca.

O `LICENSE` (MIT) cobre o código e a documentação deste repositório. Ele **não**
se estende a:

- `abntex-ifpi/tikz-uml.sty`, de terceiros, com licença própria declarada no
  próprio arquivo;
- o abnTeX2 e os demais pacotes LaTeX, distribuídos sob LPPL pelo TeX Live;
- as imagens de `imagens/`, que são exemplos herdados do modelo original —
  confira a procedência e as permissões antes de republicá-las.
