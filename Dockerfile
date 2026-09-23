# Ambiente de compilação deste modelo: TeX Live com os pacotes que ele usa.
# O passo a passo está em docs/compilar-com-docker.md.
#
# Construir a imagem (uma vez, na pasta que contém este arquivo):
#     docker build -t tcc-tex:full .
#
# Compilar o trabalho:
#     docker run --rm -u "$(id -u):$(id -g)" -v "$(pwd)":/work -w /work tcc-tex:full latexmk
#
# A base é a imagem TeX Live do Island of TeX, no esquema "medium" (cerca de
# 3,2 GB); a imagem final fica em torno de 3,3 GB. O esquema completo
# ("latest", sem o sufixo) dispensaria o tlmgr abaixo, mas é bem maior.
#
# Para fixar uma edição do TeX Live -- útil para reproduzir a compilação
# meses depois, quando "latest" já tiver mudado:
#     docker build --build-arg TEXLIVE_IMAGE=registry.gitlab.com/islandoftex/images/texlive:TL2025-historic -t tcc-tex:2025 .
ARG TEXLIVE_IMAGE=registry.gitlab.com/islandoftex/images/texlive:latest-medium
FROM ${TEXLIVE_IMAGE}

LABEL org.opencontainers.image.title="tcc-tex"
LABEL org.opencontainers.image.description="TeX Live com os pacotes do modelo de artigo do IFPI"

# Os pacotes que faltam no esquema "medium" -- a mesma lista do README, obtida
# compilando o modelo e instalando cada pacote que o log pediu:
#   abntex2 ................. classe e estilo de citação do abnTeX2
#   simplecd ................ capa de CD (pos-textual/opcionais/capa-cd.tex)
#   tcolorbox ............... ambiente "caixa" do estilo IFPI
#   tikzfill, pdfcol, environ, trimspaces ... exigidos pelo tcolorbox
#   multirow ................ células que ocupam várias linhas nas tabelas
#   ifmtarg ................. dependência interna dos anteriores
#
# As duas consultas ao kpsewhich fazem a construção falhar em vez de gerar uma
# imagem incompleta, caso algum pacote mude de nome no repositório do CTAN.
RUN tlmgr install \
      abntex2 simplecd tcolorbox tikzfill pdfcol environ trimspaces \
      multirow ifmtarg \
 && kpsewhich abntex2.cls > /dev/null \
 && kpsewhich tcolorbox.sty > /dev/null

# Pasta em que o projeto é montado na hora de compilar.
WORKDIR /work
