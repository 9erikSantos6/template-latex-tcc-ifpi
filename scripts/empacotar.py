"""Cria o ZIP de distribuição do modelo.

Execute na pasta que contém main.tex:

    python3 scripts/empacotar.py

O resultado fica em dist/modelo-artigo-ifpi.zip e contém tudo o que um
colega precisa para compilar: textos, bibliografia, imagens, estilos,
licença, guias e os arquivos de configuração da raiz, inclusive o
Dockerfile do ambiente de compilação. Não entram no
pacote o PDF compilado, os arquivos auxiliares da compilação nem o PDF
da ficha catalográfica (que costuma trazer dados pessoais).
"""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

# Arquivos da raiz que fazem parte do modelo. Se algum sumir, o pacote
# gerado ficaria incompleto, então a execução é interrompida.
ARQUIVOS_DA_RAIZ = [
    Path("main.tex"),
    Path("README.md"),
    Path("LICENSE"),
    Path("bibliografia.bib"),
    Path(".gitignore"),
    Path(".latexmkrc"),
    Path("Dockerfile"),
    Path(".dockerignore"),
]

# Recursos que o modelo usa na compilação.
RECURSOS = [
    Path("abntex-ifpi/abntex-ifpi.sty"),
    Path("abntex-ifpi/abntex-ifpi.bib"),
    Path("abntex-ifpi/logo_ifpi.pdf"),
    Path("imagens/abntex2-modelo-img-grafico.pdf"),
    Path("imagens/carta_pero_vaz.png"),
    Path("imagens/fig_exemplo.png"),
    Path("imagens/grafs_1.png"),
    Path("imagens/grafs_2.png"),
]

# Pasta -> extensões que devem ser empacotadas.
PASTAS = {
    "abntex-ifpi": {".sty", ".bib", ".pdf"},
    "capitulos": {".tex"},
    "configuracoes": {".tex"},
    "estrutura": {".tex"},
    "pre-textual": {".tex"},
    "pos-textual": {".tex"},
    "imagens": {".png", ".jpg", ".jpeg", ".pdf"},
    "docs": {".md"},
    "scripts": {".py"},
}

# Arquivos que nunca entram no pacote, mesmo que existam. A ficha
# catalográfica é emitida pela biblioteca com os dados do aluno.
NUNCA_EMPACOTAR = {
    Path("pre-textual/ficha-catalografica.pdf"),
}


def main():
    obrigatorios = ARQUIVOS_DA_RAIZ + RECURSOS
    ausentes = [str(caminho) for caminho in obrigatorios if not caminho.is_file()]
    if ausentes:
        raise SystemExit(
            "Não foi possível empacotar. Verifique se você está na pasta que "
            "contém main.tex e se estes arquivos do modelo existem:\n  - "
            + "\n  - ".join(ausentes)
        )

    arquivos = set(obrigatorios)
    for pasta, extensoes in PASTAS.items():
        diretorio = Path(pasta)
        if not diretorio.is_dir():
            raise SystemExit(f"Pasta obrigatória ausente: {pasta}")
        arquivos.update(
            caminho
            for caminho in diretorio.rglob("*")
            if caminho.is_file()
            and caminho.suffix.lower() in extensoes
            and caminho not in NUNCA_EMPACOTAR
        )

    destino = Path("dist/modelo-artigo-ifpi.zip")
    destino.parent.mkdir(exist_ok=True)
    with ZipFile(destino, "w", compression=ZIP_DEFLATED) as pacote:
        for caminho in sorted(arquivos):
            pacote.write(caminho, arcname=caminho.as_posix())

    print(f"Pacote criado: {destino} ({len(arquivos)} arquivos)")
    print("Antes de publicar, revise os dados pessoais e as permissões das imagens.")


if __name__ == "__main__":
    main()
