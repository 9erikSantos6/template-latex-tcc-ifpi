# Como disponibilizar o modelo

Este guia é para quem **mantém** o modelo e vai entregá-lo a outras pessoas.
Se você só quer escrever seu TCC, leia o `README.md` e o `guia-iniciante.md`.

## Prepare a versão de distribuição

1. Compile o projeto (`latexmk`) e confira o log final, sem erros.
2. Leia o PDF inteiro e mantenha apenas dados de demonstração: nenhum contato
   pessoal de estudante, comentário de avaliação ou conteúdo confidencial.
3. Preserve o `LICENSE` e os avisos de autoria e licença dos estilos de
   terceiros, em especial o cabeçalho de `abntex-ifpi/tikz-uml.sty`.
4. Confira a procedência e as permissões das imagens. O empacotador inclui os
   arquivos que existem; ele não verifica direitos de uso nem normas.
5. Execute, na pasta que contém `main.tex`:

   ```
   python3 scripts/empacotar.py
   ```

O arquivo `dist/modelo-artigo-ifpi.zip` reúne os textos, a bibliografia, as
imagens, os estilos, a licença, os guias e os arquivos de configuração da raiz
(`.gitignore`, `.latexmkrc`, `Dockerfile` e `.dockerignore`). O script usa apenas a biblioteca padrão do
Python, sem instalar dependências. Uma execução posterior substitui o ZIP.

Ficam **fora** do pacote: o PDF compilado, os arquivos auxiliares da
compilação, a pasta `dist/`, o histórico Git, as configurações de editor, o
`_config.yml` (que só serve ao GitHub Pages) e o
`pre-textual/ficha-catalografica.pdf` — que costuma trazer os dados pessoais de
quem estava escrevendo. Se quiser oferecer um PDF de demonstração, distribua
`main.pdf` separadamente, depois de revisá-lo.

## Confira em uma pasta limpa

Extraia o ZIP em outra pasta e compile a partir dela:

```
cd pasta-do-zip
latexmk
```

Sem LaTeX instalado, o mesmo teste sai do ambiente em contêiner (o `Dockerfile`
também vai no pacote):

```
cd pasta-do-zip
docker build -t tcc-tex:full .
docker run --rm -u "$(id -u):$(id -g)" -v "$(pwd)":/work -w /work tcc-tex:full latexmk
```

O guia do ambiente é [`compilar-com-docker.md`](compilar-com-docker.md).

Esse teste mostra se a distribuição está completa, sem depender dos arquivos
auxiliares da sua cópia de trabalho. Faça o mesmo teste importando o ZIP no
Overleaf e no Prism antes de anunciar uma versão nova: são os ambientes em que
a maioria das pessoas vai abrir o modelo.

Não envie apenas `main.tex`: ele depende das outras pastas. Não remova os PDFs
de `imagens/` nem `abntex-ifpi/logo_ifpi.pdf` — são recursos do modelo, não
resultados temporários da compilação.

## Se usar Git

O `.gitignore` do projeto ignora os arquivos gerados pela compilação, o
`main.pdf` e a pasta `dist/`, mas **não** os PDFs e imagens que o modelo usa.
Antes de publicar, confirme que os recursos estão versionados, inclusive
`LICENSE`, `.latexmkrc` e `abntex-ifpi/logo_ifpi.pdf`:

```
git status --short --untracked-files=all
git check-ignore -v caminho/do/arquivo
```

Alguns editores acrescentam regras locais de exclusão. O empacotador lê os
arquivos direto do disco, independentemente dessas regras — então um arquivo
pode entrar no ZIP mesmo estando fora do Git, e vice-versa.

## Informe o alcance do modelo

Apresente-o como um **modelo de artigo baseado em abnTeX2 e abntex-ifpi**.
Não anuncie conformidade automática com todas as normas ou todos os cursos.
Informe o compilador testado (pdfLaTeX + BibTeX), preserve os créditos e diga
com clareza que textos, imagens e referências são exemplos a substituir.

Histórico de reorganização, caso alguém traga arquivos de uma versão anterior:

- `Desnecessarios/` passou a se chamar `opcionais/`, em `pre-textual/` e
  `pos-textual/`. Um elemento desativado não é dispensável para todos os cursos.
- `051-trabalhos-futuros.tex` passou a se chamar `06-trabalhos-futuros.tex`.
- Para exibir a data de aprovação use `\imprimirdataapresentacao`;
  `\dataapresentacao{...}` fica reservado à definição do valor nos metadados.
