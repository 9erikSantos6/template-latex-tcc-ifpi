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
(`.gitignore` e `.latexmkrc`). O script usa apenas a biblioteca padrão do
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

Esse teste mostra se a distribuição está completa, sem depender dos arquivos
auxiliares da sua cópia de trabalho. Faça o mesmo teste importando o ZIP no
Overleaf e no Prism antes de anunciar uma versão nova: são os ambientes em que
a maioria das pessoas vai abrir o modelo.

Não envie apenas `main.tex`: ele depende das outras pastas. Não remova os PDFs
de `imagens/` nem `abntex-ifpi/logo_ifpi.pdf` — são recursos do modelo, não
resultados temporários da compilação.

## Prepare o ambiente de manutenção

Só quem faz commits no modelo precisa disto. Quem escreve o TCC não precisa
de Node.js, pnpm nem de nada desta seção.

As ferramentas (husky, commitlint e semantic-release) são instaladas pelo
pnpm a partir do `package.json`. Nada disso é publicado no npm: o
`package.json` existe apenas para instalar essas ferramentas.

### Pré-requisitos

| Programa | Para quê | Versão |
| --- | --- | --- |
| Git | versionar o modelo | qualquer recente |
| Node.js | rodar as ferramentas | 22.14 ou mais recente (recomendado: 24 LTS, a mesma do CI) |
| Corepack | baixar a versão certa do pnpm | vem com o Node.js 22 e 24; no Node.js 25 ou mais recente, instale à parte |
| Python 3 | rodar `scripts/empacotar.py` | 3.8 ou mais recente, sem pacotes extras |
| LaTeX | compilar o modelo | veja "No seu computador" no `README.md` |

Instale o Node.js pelo site oficial (nodejs.org), pelo gerenciador de pacotes
do sistema ou por um gerenciador de versões como o nvm. Confira a versão:

```
node --version
```

Não instale o pnpm por conta própria: o Corepack baixa automaticamente a
versão fixada no campo `packageManager` do `package.json`, a mesma que o CI
usa.

### Instalação (uma vez por máquina e por cópia do repositório)

Na pasta do repositório:

```
corepack enable
pnpm install
```

- No Node.js 25 ou mais recente, o Corepack não vem mais junto. Instale-o
  antes com `npm install -g corepack`.
- Se o `corepack enable` falhar por falta de permissão (Node.js instalado no
  sistema, fora da sua pasta pessoal), rode-o com `sudo` ou use um Node.js
  instalado pelo nvm.
- Na primeira vez, o Corepack pode perguntar se deve baixar o pnpm. Responda
  que sim.

O `pnpm install` também ativa o hook do husky. Para conferir se ele está
ativo:

```
git config core.hooksPath
```

A resposta deve ser `.husky/_`. Se vier vazia, rode `pnpm install` de novo.
Sem o hook, o commit não é conferido na hora; os PRs continuam sendo conferidos
no CI.

### Manutenção das dependências

- Depois de um `git pull` que altere o `package.json` ou o `pnpm-lock.yaml`,
  rode `pnpm install` de novo.
- Para atualizar as ferramentas, use `pnpm update` e faça o commit do
  `pnpm-lock.yaml` junto. O CI instala exatamente o que está no lock
  (`pnpm install --frozen-lockfile`) e falha se ele estiver desatualizado.
- Não atualize o `conventional-changelog-conventionalcommits` para a versão 10:
  ela é incompatível com o gerador de notas do semantic-release e quebra a
  publicação. Mantenha a 9 até o semantic-release suportar a nova versão.
- Para mudar a versão do pnpm, use `corepack use pnpm@<versão>`, que atualiza o
  `packageManager` do `package.json`.

## Versões e publicação automática

Cada versão do modelo é uma **Release** no GitHub (tag `vX.Y.Z`) com o ZIP
anexado como `modelo-artigo-ifpi-vX.Y.Z.zip`. Quem cria a Release é o
semantic-release, rodando no GitHub Actions (`.github/workflows/release.yml`).
Nem todo commit gera versão: ela só sai quando o modelo está pronto para uso.

**Quando sai uma versão.** Só quando a `main` recebe commits destes tipos:

| Tipo do commit | Exemplo | Versão |
| --- | --- | --- |
| `fix:` ou `perf:` | `fix: corrige a margem da capa` | correção (1.0.0 → 1.0.1) |
| `feat:` | `feat: adiciona a folha de aprovação` | menor (1.0.1 → 1.1.0) |
| `feat!:` ou rodapé `BREAKING CHANGE:` | `feat!: renomeia os arquivos de capítulos` | maior (1.1.0 → 2.0.0) |

`docs:`, `chore:`, `refactor:`, `style:`, `test:`, `build:` e `ci:` **não**
geram versão. Use-os para trabalho em andamento ou que não muda o modelo
entregue. Trabalho incompleto fica numa branch própria e só chega à `main`
quando estiver usável.

**O que é verificado antes.** Em todo PR para a `main` e em todo push nela, o
CI gera o ZIP, extrai numa pasta limpa e compila com pdfLaTeX + BibTeX. Se a
compilação falhar, não sai versão. O PDF compilado fica disponível por 14 dias
como artefato da execução (`pdf-de-verificacao`), para você conferir. O CI
**não** substitui a revisão do PDF nem os testes no Overleaf e no Prism
descritos acima.

**Mensagens de commit.** O padrão é o *Conventional Commits*
(`tipo: descrição`). Depois de preparar o ambiente (seção anterior), o husky
confere cada mensagem na hora do commit e recusa as que estiverem fora do
padrão (por exemplo `fex: ...`). Nos PRs, o CI confere as mensagens de novo. Se o PR for integrado
com *squash*, o título do PR vira a mensagem do commit: escreva o título no
mesmo padrão.

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
