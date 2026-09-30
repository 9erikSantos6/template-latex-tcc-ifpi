# Modelo de artigo acadêmico — IFPI

Um ponto de partida em LaTeX para escrever um artigo de conclusão de curso,
baseado no abnTeX2 e no abntex-ifpi. Você escreve em arquivos de texto comuns e
a compilação transforma esses arquivos em um PDF com a formatação do modelo.

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
   `scripts/empacotar.py`; quem recebeu o ZIP já pode usá-lo direto). A versão
   mais recente fica na página **Releases** do repositório no GitHub.
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

## O que normalmente não precisa ser alterado

- `main.tex`: reúne as partes do documento; não escreva o artigo dentro dele.
- `estrutura/preambulo.tex`: carrega os pacotes e as configurações.
- `configuracoes/compatibilidade.tex`: ajusta a convivência entre abnTeX2,
  memoir e os nomes em português do Babel. É carregado antes do
  `\documentclass`, de propósito.
- `abntex-ifpi/`: estilo institucional, logotipo e suporte a diagramas UML.
- `.latexmkrc`: configuração da compilação local.
- `.gitignore`: lista dos arquivos gerados, que não devem ser versionados.
- `scripts/empacotar.py`: gera o ZIP de distribuição (veja `docs/publicacao.md`).
- `_config.yml`: tema usado caso o repositório seja publicado no GitHub Pages.
- `package.json`, `pnpm-lock.yaml`, `.husky/`, `.github/`, `commitlint.config.mjs`
  e `release.config.mjs`: ferramentas de quem mantém o modelo (versões e
  publicação). Não entram no ZIP e não são necessárias para escrever o TCC.
  Para configurá-las, veja "Prepare o ambiente de manutenção" em
  `docs/publicacao.md`.
- `docs/`: os guias que você está lendo.

## Antes de entregar

- [ ] Troque todos os dados de `configuracoes/metadados.tex`, inclusive a data
      de apresentação — ela aparece no rodapé da página do abstract mesmo sem
      folha de aprovação.
- [ ] Apague os e-mails `example.com` das notas de rodapé dos autores.
- [ ] Substitua o resumo, o abstract e o texto de todos os capítulos.
- [ ] Remova as figuras e tabelas de demonstração. Procure por `EXEMPLO` nos
      arquivos: todo bloco de demonstração está marcado assim.
- [ ] Desative o apêndice de exemplo em `estrutura/pos-textual.tex` se você não
      tiver apêndice, ou substitua o conteúdo dele.
- [ ] Apague de `bibliografia.bib` as entradas de exemplo (chaves começadas por
      `exemplo-`) e as obras que você não citou.
- [ ] Ative os elementos exigidos pelo seu curso. Sumário e listas vêm
      desativados na configuração inicial de artigo.
- [ ] Revise o PDF inteiro: legendas, numeração, referências e apêndices.
- [ ] Confirme com o curso ou a biblioteca as exigências de apresentação.

**Este projeto não certifica conformidade com as normas vigentes.** Ele preserva
a base visual e o estilo de citações do modelo recebido. A modalidade inicial é
**artigo**, não um modelo completo de monografia.

## Créditos e licença

Modelo derivado do abntex-ifpi, criado por Rafael Madureira Lins de Araújo, com
adaptações descritas na versão recebida por Tulio Vidal, IFPI — Campus Corrente
(`tulio.vidal@ifpi.edu.br`). A documentação original informa como bases um
modelo de monografia do IFPI e o Manual de Normalização de Trabalhos Acadêmicos
do IFPI de 2022.

O `LICENSE` (MIT) cobre o código e a documentação deste repositório. Ele **não**
se estende a:

- `abntex-ifpi/tikz-uml.sty`, de terceiros, com licença própria declarada no
  próprio arquivo;
- o abnTeX2 e os demais pacotes LaTeX, distribuídos sob LPPL pelo TeX Live;
- as imagens de `imagens/`, que são exemplos herdados do modelo original —
  confira a procedência e as permissões antes de republicá-las.
