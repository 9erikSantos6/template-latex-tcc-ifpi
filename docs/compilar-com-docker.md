# Compilar com Docker

Este guia mostra como gerar o `main.pdf` **sem instalar LaTeX no seu
computador**. Tudo o que a compilação precisa fica dentro de uma imagem
Docker: se um dia você não quiser mais o modelo, apaga a imagem e não sobra
nada espalhado pelo sistema.

Use este caminho se você compila na sua máquina e prefere não instalar o TeX
Live (que ocupa vários gigabytes e mexe no `PATH`), ou se precisa que a
compilação saia igual na sua máquina e na de outra pessoa. Quem escreve no
Overleaf ou no Prism **não precisa de nada disto**: lá a compilação já é feita
no servidor.

## Antes de começar

1. Instale o Docker: <https://docs.docker.com/get-started/get-docker/>.
   No Linux, prefira o pacote da sua distribuição (`docker` ou `docker-ce`) e
   confirme que o serviço está ativo.
2. Confira se ele responde:

   ```
   docker run --rm hello-world
   ```

   Se aparecer `Cannot connect to the Docker daemon`, veja a tabela de
   problemas no fim deste guia.
3. Reserve cerca de **3,5 GB** de espaço em disco para a imagem (o download
   é menor, perto de 1 GB, porque vem compactado).
4. Abra o terminal na pasta que contém o `main.tex` — é de lá que todos os
   comandos abaixo são executados.

## Passo 1 — construir a imagem (uma vez só)

O `Dockerfile` na raiz do projeto descreve o ambiente: TeX Live mais os
pacotes que o modelo usa. Para construí-lo:

```
docker build -t tcc-tex:full .
```

O `-t tcc-tex:full` é o nome que você dá à imagem; o `.` indica que o
`Dockerfile` está na pasta atual. A primeira execução baixa o TeX Live e
demora — de alguns minutos a mais de meia hora, conforme a sua internet; quase
todo esse tempo é o download da imagem base. Só é preciso repetir isto se o
`Dockerfile` mudar.

Conferindo o que foi criado:

```
docker images tcc-tex
```

Se você já tinha uma imagem com esse nome, o `-t` passa o nome para a imagem
recém-construída; a anterior continua no disco, sem nome, até você removê-la
(`docker image prune`).

## Passo 2 — compilar o trabalho

```
docker run --rm -u "$(id -u):$(id -g)" -v "$(pwd)":/work -w /work tcc-tex:full latexmk
```

No **Windows (PowerShell)**, o mesmo comando muda só o trecho do caminho e
dispensa o `-u`:

```
docker run --rm -v "${PWD}:/work" -w /work tcc-tex:full latexmk
```

O resultado é o `main.pdf`, na sua pasta, como se tivesse sido compilado
localmente. Abra-o no visualizador de PDF de sempre.

O que cada parte do comando faz:

| Parte | Para que serve |
| --- | --- |
| `docker run` | executa um contêiner a partir da imagem |
| `--rm` | descarta o contêiner ao terminar; a imagem continua |
| `-u "$(id -u):$(id -g)"` | roda com o **seu** usuário, para que `main.pdf` não saia pertencente ao `root` (no Linux e no macOS; no Windows não é preciso) |
| `-v "$(pwd)":/work` | monta a pasta atual dentro do contêiner, em `/work`. É por isso que o PDF aparece na sua pasta: o contêiner escreve direto nela |
| `-w /work` | entra nessa pasta antes de rodar o comando |
| `tcc-tex:full` | a imagem construída no passo 1 |
| `latexmk` | o comando executado lá dentro |

O `latexmk` lê o `.latexmkrc` do projeto, que já configura pdfLaTeX e BibTeX,
e repete a compilação quantas vezes for necessário para resolver sumário,
citações e referências cruzadas.

### Um atalho para o dia a dia

Digitar a linha inteira toda vez cansa. No Linux ou no macOS, acrescente ao
seu `~/.bashrc` ou `~/.zshrc`:

```
tcc() { docker run --rm -u "$(id -u):$(id -g)" -v "$(pwd)":/work -w /work tcc-tex:full "$@"; }
```

Depois de reabrir o terminal, dentro da pasta do trabalho basta:

```
tcc latexmk          # compila
tcc latexmk -c       # limpa os arquivos auxiliares
tcc pdflatex --version
```

A função serve para comandos que apenas rodam e terminam. Para abrir um
terminal **interativo** dentro do ambiente, use a forma completa da seção
*Investigar um erro*, que acrescenta o `-it`.

## Compilar passo a passo

O `latexmk` resolve tudo sozinho. Se quiser acompanhar a sequência completa,
os comandos são estes, na ordem:

```
tcc pdflatex -interaction=nonstopmode main.tex
tcc bibtex main
tcc pdflatex -interaction=nonstopmode main.tex
tcc pdflatex -interaction=nonstopmode main.tex
```

O `bibtex` no meio é o que monta as referências; as duas passadas seguintes
existem para que citações, sumário e referências cruzadas parem de aparecer
como `??`.

Se você tiver ativado o índice remissivo (`\makeindex` em
`estrutura/preambulo.tex` e `pos-textual/opcionais/indices.tex`), acrescente o
`makeindex` logo depois do `bibtex`:

```
tcc makeindex main.idx
```

## Limpar os arquivos auxiliares

```
tcc latexmk -c    # apaga os auxiliares e mantém o main.pdf
tcc latexmk -C    # apaga também o main.pdf
```

## Investigar um erro dentro do ambiente

Para olhar o ambiente por dentro — conferir se um pacote existe, testar uma
instalação — abra um terminal no contêiner. O `-it` é o que o torna
interativo:

```
docker run --rm -it -u "$(id -u):$(id -g)" -v "$(pwd)":/work -w /work tcc-tex:full bash
```

Lá dentro:

```
kpsewhich abntex2.cls      # mostra onde a classe está; vazio = não instalada
tlmgr install nome-do-pacote
exit
```

Atenção: o que você instalar assim **some quando o contêiner fecha**. Para
valer sempre, acrescente o pacote à linha `tlmgr install` do `Dockerfile` e
reconstrua a imagem (passo 1).

## Atualizar ou remover a imagem

```
docker build --no-cache -t tcc-tex:full .   # reconstrói do zero, com o TeX Live mais recente
docker image rm tcc-tex:full                # remove a imagem
docker system df                            # mostra quanto espaço o Docker ocupa
```

Se precisar reproduzir a compilação meses depois, com a mesma edição do TeX
Live, fixe a imagem base na construção:

```
docker build --build-arg TEXLIVE_IMAGE=registry.gitlab.com/islandoftex/images/texlive:TL2025-historic -t tcc-tex:2025 .
```

## Problemas comuns

| Mensagem ou sintoma | O que fazer |
| --- | --- |
| `Cannot connect to the Docker daemon` | O serviço não está rodando (`sudo systemctl start docker`) ou seu usuário não está no grupo `docker` (`sudo usermod -aG docker $USER` e refazer o login). No Windows e no macOS, abra o Docker Desktop e espere ficar verde |
| `Unable to find image 'tcc-tex:full' locally` | A imagem ainda não foi construída: refaça o passo 1, na pasta que contém o `Dockerfile` |
| `permission denied` ao compilar, ou arquivos pertencentes ao `root` | Faltou o `-u "$(id -u):$(id -g)"`. Para consertar os arquivos já criados: `sudo chown -R "$(id -u):$(id -g)" .` |
| A pasta aparece vazia dentro do contêiner | O caminho do `-v` está errado. Use o comando exatamente como está aqui, a partir da pasta do `main.tex`. Caminhos com espaço ou acento precisam das aspas |
| No Windows, `error during connect` ou a montagem não funciona | Confirme que o Docker Desktop está aberto e que o disco do projeto está compartilhado (Settings → Resources → File sharing) |
| `main.pdf` não foi gerado | Procure a **primeira** mensagem iniciada por `!` no `main.log` — as seguintes costumam ser consequência dela. A tabela de erros comuns está em [`guia-iniciante.md`](guia-iniciante.md) |
| `abntex2.cls not found` depois de mexer no `Dockerfile` | Reconstrua a imagem: `docker build -t tcc-tex:full .` |
| A construção da imagem demorou muito | Normal na primeira vez: o TeX Live está sendo baixado. As compilações seguintes levam segundos, porque a imagem já está no disco |

## Para quem mantém o modelo

O mesmo ambiente serve para conferir a distribuição antes de publicar:
extraia o `dist/modelo-artigo-ifpi.zip` em uma pasta limpa e compile lá dentro
com o mesmo comando do passo 2. É o teste descrito em
[`publicacao.md`](publicacao.md), sem depender dos arquivos auxiliares da sua
cópia de trabalho.
