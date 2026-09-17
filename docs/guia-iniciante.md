# Guia para quem nunca usou LaTeX

Leia na ordem na primeira vez. Depois, use como consulta.

## 1. Entenda o projeto

No LaTeX você **não** formata o texto clicando em botões. Você escreve o texto
em arquivos comuns, marca o que cada trecho é (`\section{...}` é um título,
`\cite{...}` é uma citação) e o programa monta o PDF com a formatação certa.
A vantagem: numeração, sumário, citações e referências se ajustam sozinhos.

Vocabulário mínimo:

- **Arquivo `.tex`:** texto com comandos de formatação. É onde você escreve.
- **Arquivo `.bib`:** cadastro das obras que você pode citar.
- **Arquivo `.sty` / `.cls`:** definições técnicas de aparência. Não mexa.
- **Comando:** uma palavra iniciada por barra invertida, como `\textbf`.
  O que vem entre `{ }` logo depois é o conteúdo sobre o qual ele age.
- **Ambiente:** um par de comandos que delimita um bloco, sempre
  `\begin{nome}` … `\end{nome}`. Tabelas, figuras e citações longas são
  ambientes. Todo `\begin` precisa de um `\end` correspondente.
- **Preâmbulo:** a parte inicial do documento, antes do `\begin{document}`,
  onde os pacotes são carregados. Aqui fica em `estrutura/preambulo.tex`.
  Cuidado: existe também um comando chamado `\preambulo` em
  `configuracoes/metadados.tex`; é outra coisa (o texto da folha de rosto).
- **Pacote:** extensão que acrescenta recursos ao LaTeX, carregada com
  `\usepackage{nome}` no preâmbulo.
- **Compilar:** transformar esses arquivos em um PDF.
- **Log:** o relatório que a compilação produz, com avisos e erros. Todo
  editor tem um lugar para vê-lo; no computador, é o arquivo `main.log`.
- **UTF-8:** a codificação de texto que preserva acentos. Todos os arquivos
  deste modelo já estão em UTF-8; mantenha assim ao salvar.

Sempre compile `main.tex`, mesmo quando estiver editando outro arquivo: os
demais não são documentos independentes, são pedaços incluídos por ele.
Todos os caminhos partem da pasta de `main.tex` — escreva
`imagens/foto.png`, nunca `C:\Users\...\foto.png` nem `/home/voce/...`.

Faça uma cópia do modelo antes de começar e compile depois de cada alteração
pequena. Assim, quando algo quebrar, você sabe exatamente o que causou.

## 2. Compile antes de editar

Compile o modelo **como ele veio**, antes de mudar qualquer coisa. Você deve
obter um PDF de poucas páginas com: capa, folha de rosto, página do resumo,
o abstract, os capítulos de exemplo, as referências e um apêndice de exemplo.
Não há sumário — ele vem desativado na configuração de artigo (a Seção 8
explica como ativar).

| Onde você está | O que fazer |
| --- | --- |
| **OpenAI Prism** | Importe o ZIP do modelo, abra `main.tex` na lista de arquivos. A compilação é automática e o PDF aparece ao lado. |
| **Overleaf** | Upload Project com o ZIP. Menu → Compiler: **pdfLaTeX**; Main document: **main.tex**. Clique em **Recompile**. |
| **Seu computador** | Abra o terminal na pasta de `main.tex` e execute `latexmk`. O resultado é `main.pdf`. |

Se esse primeiro PDF sair, o ambiente está correto. Qualquer erro daí em
diante veio da sua edição — e você sabe a qual voltar.

## 3. Faça sua primeira alteração

Abra `configuracoes/metadados.tex`. Em `\autor{Nome do aluno}`, substitua
apenas `Nome do aluno` pelo seu nome. Mantenha o comando, a barra e as chaves.
Compile e confira a capa: seu nome deve aparecer automaticamente, e também na
folha de rosto e na página do resumo. É essa a ideia do arquivo — um dado
preenchido uma vez aparece em todos os lugares certos.

Repita com o título, o curso, o campus, a cidade, o ano e a orientação.
Preencha também as notas de rodapé com formação e e-mail: **não deixe os
endereços `example.com` no trabalho final**.

Três detalhes que costumam pegar:

- **`\coorientador{}` vazio faz a linha desaparecer** da folha de rosto. Se
  houver coorientação, escreva só o nome e a titulação; o rótulo
  "Coorientador:" é inserido automaticamente pelo modelo.
- **`\dataapresentacao{...}` define o valor; `\imprimirdataapresentacao`
  o exibe.** Você edita o primeiro. Essa data já aparece no PDF, no rodapé da
  página do abstract, mesmo com a folha de aprovação desativada — troque-a.
- **Dentro de `\instituicao{...}`, o `\\` no fim de cada linha é obrigatório**
  e força a quebra de linha do cabeçalho da capa. É a única exceção: no texto
  corrido dos capítulos, você não deve usar `\\` (veja a Seção 4).

## 4. Escreva parágrafos e títulos

Digite o texto normalmente. **Uma linha em branco separa dois parágrafos.**
Não use `\\` nem espaços repetidos para tentar alinhar o texto corrido: o
LaTeX cuida do espaçamento, e forçar quebras à mão estraga a justificação.
(`\\` tem uso legítimo em dois lugares: dentro de tabelas e dentro do
`\instituicao{...}` dos metadados.)

| Recurso | Exemplo |
| --- | --- |
| Seção principal | `\section{Metodologia}` |
| Subseção | `\subsection{Coleta de dados}` |
| Divisão da subseção | `\subsubsection{Instrumentos}` |
| Negrito | `\textbf{palavra}` |
| Ênfase (itálico) | `\emph{palavra}` |
| Código no meio da frase | `\codigo{git commit}` |
| Nota de rodapé | `\footnote{Explicação complementar.}` |

Não digite o número dos títulos: ele é automático. Embora os arquivos fiquem
em `capitulos/`, o modo artigo usa `\section` para os títulos principais;
`\chapter` fica reservado aos apêndices e anexos. Não mude a modalidade para
monografia sem revisar a estrutura e as exigências do curso.

Alguns caracteres têm significado próprio no LaTeX e precisam de uma barra
quando você quer que apareçam no texto:

| Você quer escrever | Digite |
| --- | --- |
| % & _ # $ | `\%` `\&` `\_` `\#` `\$` |
| um endereço da web | `\url{https://exemplo.org}` |

O caractere `%` **sem** barra inicia um comentário: tudo dali até o fim da
linha é ignorado e não aparece no PDF. É assim que o modelo desativa linhas
(veja a Seção 8) e é assim que você escreve lembretes para si mesmo.

## 5. Acrescente ou retire uma seção

1. Crie, por exemplo, `capitulos/07-consideracoes-adicionais.tex`.
2. Escreva `\section{Considerações adicionais}` e seu texto nesse arquivo.
3. Acrescente `\input{capitulos/07-consideracoes-adicionais}` no ponto
   desejado de `estrutura/textual.tex`. A ordem das linhas `\input` é a
   ordem em que as seções aparecem no PDF.

Para retirar uma parte, ponha `%` no início da linha de inclusão. Depois,
confira se nenhum outro trecho ainda cita a parte removida — em especial o
último parágrafo de `capitulos/01-introducao.tex`, que lista as seções.

`capitulos/06-trabalhos-futuros.tex` contém uma **subseção da conclusão**
(`\subsection`), não uma seção independente; a numeração no nome do arquivo
serve apenas para ordenar a pasta. Para transformá-la em seção própria, troque
`\subsection` por `\section` dentro do arquivo.

## 6. Cite uma obra

Cada obra em `bibliografia.bib` tem uma **chave** única, escrita logo depois de
`@article{`, `@book{` ou outro tipo de entrada. Uma chave que já existe no
modelo é `SilvaNeto2019Credibility`.

- `\cite{SilvaNeto2019Credibility}` → citação entre parênteses, no fim da frase.
- `\citeonline{SilvaNeto2019Credibility}` → autores integrados à frase.
- Para indicar a página, acrescente `[p.~24]` entre o comando e as chaves:
  `\cite[p.~24]{SilvaNeto2019Credibility}`. O `~` é um espaço que não deixa a
  linha quebrar entre "p." e o número.

A lista de referências no fim do PDF é montada sozinha, **só com as obras que
você citou**. Uma entrada cadastrada e nunca citada não aparece. Nunca digite a
lista à mão: `pos-textual/referencias.tex` a imprime automaticamente.

Para cadastrar outra obra, copie um dos modelos comentados no fim de
`bibliografia.bib` (as entradas com chave `exemplo-...`), cole no fim do
arquivo, troque a chave e preencha os campos com os dados conferidos da
publicação. Duas regras salvam a maioria dos casos:

- Separe autores por `and`, nunca por `e` nem por vírgula entre as pessoas:
  `author = {Sobrenome, Nome and Outro Sobrenome, Outro Nome}`.
  A vírgula dentro de um nome é o que separa sobrenome de nome.
- Não use duas entradas com a mesma chave.

As entradas que vêm no modelo são exemplos. Não basta trocar a chave: autores,
título, ano e veículo também precisam corresponder à obra consultada.

Uma citação direta longa vai no ambiente `citacao` (há um exemplo em
`capitulos/02-fundamentacao-teorica.tex`) e exige a transcrição exata da obra
e a indicação da fonte. O texto que está lá é uma instrução de preenchimento,
não uma citação publicável: substitua-o ou remova-o.

## 7. Insira imagens e tabelas

Coloque as imagens (PNG, JPG ou PDF) em `imagens/`. Prefira nomes simples, sem
espaços e sem acentos, como `resultado-experimento.png`. Maiúsculas e
minúsculas importam: `Foto.PNG` e `foto.png` são arquivos diferentes.

Copie um ambiente `figure` já existente em `capitulos/04-resultados.tex` e
altere quatro coisas:

1. O texto de `\caption{...}`: o título da figura, sem número — ele é automático.
2. O identificador de `\label{...}`: único, por exemplo `fig:resultado`.
3. O caminho em `\includegraphics[width=0.7\linewidth]{imagens/arquivo.png}`.
   `\linewidth` é a largura disponível na linha, então `0.7\linewidth` são 70%
   dela.
4. A fonte em `\fonte{...}`: autoria ou referência verdadeira. Use
   `\fonte{Elaboração própria.}` quando a figura for sua.

Mantenha o `\label` **depois** do `\caption`: é a legenda que cria o número.
Depois, mencione a figura no texto com `\autoref{fig:resultado}`, que escreve
"Figura 3" sozinho e vira um link no PDF.

Figuras e tabelas são **flutuantes**: o LaTeX as move para onde couberem
melhor, para não deixar buracos na página. A opção `[htb]` é uma sugestão de
posição — `h` aqui mesmo, `t` no topo da página, `b` no rodapé — e o LaTeX
tenta nessa ordem. Não force posição com espaços negativos ou quebras de
página; deixe o texto se referir à figura pelo `\autoref`, não por "a figura
abaixo".

As tabelas da introdução, da metodologia e do apêndice podem ser copiadas.
Dentro de uma tabela, `&` separa colunas e `\\` termina uma linha. A coluna `X`
do ambiente `tabularx` estica para ocupar a largura que sobra — use-a na coluna
de texto mais longo. Para escrever um `&` como conteúdo de uma célula, use `\&`.

## 8. Ative as partes opcionais

Abra `estrutura/pre-textual.tex` ou `estrutura/pos-textual.tex`. As linhas que
começam com `%` estão desativadas. Para incluir agradecimentos, por exemplo,
retire o `%` de `\input{pre-textual/opcionais/agradecimentos}` e edite o
arquivo correspondente em `pre-textual/opcionais/`.

- **Sumário:** ative **juntas** as quatro linhas indicadas no fim de
  `estrutura/pre-textual.tex`. Ele é construído a partir dos títulos das seções.
- **Listas de figuras e de tabelas:** recebem as legendas automaticamente.
- **Siglas e símbolos:** listas escritas à mão; mantenha apenas os itens que
  você realmente usa e apague os cinco exemplos que vêm no arquivo.
- **Dedicatória, agradecimentos, epígrafe e errata:** textos livres, cada um em
  seu arquivo em `pre-textual/opcionais/`.
- **Folha de aprovação:** escolha **apenas uma** das duas versões —
  `\imprimirfolhadeaprovacao` (orientador e dois membros) ou
  `\imprimirfolhadeaprovacaoduascolunas` (quatro nomes, em duas colunas).
  Preencha a banca em `configuracoes/metadados.tex`.
- **Ficha catalográfica:** adicione primeiro o PDF oficial emitido pela
  biblioteca em `pre-textual/ficha-catalografica.pdf`. Ele **não** acompanha o
  modelo; ativar a linha sem o arquivo dá `File ... not found`.
- **Apêndices:** materiais produzidos por você. Vem um exemplo **ativo**;
  desative-o ou substitua o conteúdo.
- **Anexos:** documentos de terceiros; há um exemplo desativado.
- **Glossário:** lista manual de termos e definições.
- **Capa de CD:** recurso legado; só ative se a entrega exigir.
- **Diagramas UML:** o pacote vem desativado em `estrutura/preambulo.tex`
  porque é grande e poucos trabalhos o usam. Retire o `%` da linha
  `\usepackage{abntex-ifpi/tikz-uml}` para usá-lo.

Para um **índice remissivo** (lista de termos com as páginas em que aparecem,
diferente do sumário, que lista títulos): ative `\makeindex` no fim de
`estrutura/preambulo.tex`, marque palavras no texto com `\index{termo}` e ative
`\input{pos-textual/opcionais/indices}` na estrutura pós-textual. O latexmk e
o Overleaf executam o MakeIndex sozinhos; em outros editores, confira no log se
a etapa rodou antes de concluir que o índice não funciona.

## 9. Entenda a compilação

Compilar não é um passo só. O LaTeX lê o documento inteiro, anota numerações e
citações em arquivos auxiliares e **precisa passar de novo** para usar o que
anotou. É por isso que uma citação pode aparecer como `??` na primeira passada.

A sequência completa deste modelo é: `pdflatex` → `bibtex` → `pdflatex` →
`pdflatex`. Você não precisa fazer isso à mão:

- **No computador:** `latexmk` repete o que for necessário sozinho.
- **No Overleaf e no Prism:** o ciclo é executado automaticamente a cada
  recompilação.

A bibliografia deste projeto usa **BibTeX**, não Biber.

Os arquivos `.aux`, `.log`, `.bbl`, `.blg`, `.brf`, `.toc`, `.lof`, `.lot`,
`.out` e `.fls` são gerados a cada compilação. Nunca escreva nada neles — são
apagados e recriados. O `.gitignore` do projeto já os mantém fora do controle
de versão. Para limpar a pasta manualmente: `latexmk -c` remove os auxiliares e
preserva o PDF; `latexmk -C` remove também o PDF.

## 10. Resolva problemas comuns

**Comece sempre pelo primeiro erro do log.** As mensagens seguintes costumam
ser consequência dele, e corrigir a primeira geralmente resolve várias.

| Mensagem ou sintoma | O que conferir |
| --- | --- |
| `File ... not found` | O projeto foi aberto inteiro? O caminho, o nome e a extensão estão certos? Maiúsculas importam. |
| `abntex2.cls not found` | Sua instalação LaTeX é mínima. Instale o pacote: `tlmgr install abntex2`. No Overleaf e no Prism isso não acontece. |
| `... .sty not found` | Falta um pacote na instalação; o nome do arquivo no log é o nome a instalar. |
| `Undefined control sequence` | Comando escrito errado, sem a barra inicial, ou de um pacote que não foi carregado. |
| `Missing $ inserted` | Um `_`, `^` ou `&` solto no texto; escreva `\_`, `\^{}` ou `\&`. |
| `Runaway argument` ou `Missing }` | Uma chave `{` aberta e não fechada no trecho recém-editado. |
| `\begin{...} ended by \end{...}` | Um ambiente foi fechado com o nome errado, ou um `\end` está faltando. |
| Citação aparece como `??` | A chave existe no `.bib`? O ciclo completo terminou? Se persistir, force uma recompilação limpa. |
| Figura ou seção aparece como `??` | O `\label` existe, está depois do `\caption` e está escrito igual na referência? |
| `Label ... multiply defined` | Dois `\label` com o mesmo identificador; renomeie um e atualize quem o cita. |
| `Overfull \hbox` | Algo passou da margem: uma palavra muito longa, um endereço sem quebra (use `\url{}`), uma imagem ou tabela larga demais. |
| `Underfull \hbox` | Linha com espaçamento esticado. Costuma ser cosmético; revise só se estiver visível no PDF. |
| O PDF não atualiza | A compilação falhou e o PDF mostrado é o anterior. Procure o erro no log. |

Corrigiu? Compile e confira o PDF antes de seguir.

## 11. Faça a revisão final

Use a lista "Antes de entregar" do `README.md` e, além dela:

- Procure a palavra `EXEMPLO` em todos os arquivos: cada ocorrência marca um
  bloco de demonstração que precisa sair ou ser substituído.
- Procure `example.com` — não deve sobrar nenhum.
- Confira o idioma do abstract e se ele traduz o resumo final, não uma versão
  antiga.
- Leia as páginas de referências e de apêndices, que são fáceis de esquecer.

A configuração preserva fonte Times, corpo de 12 pontos e recuo de parágrafo de
1,5 cm do modelo recebido; o estilo de página do texto exibe a numeração sem
títulos no cabeçalho. Esses valores **não** substituem a conferência das
exigências do seu curso, da biblioteca ou da orientação.
