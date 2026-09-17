# Configuração do latexmk para este modelo.
# Com este arquivo, basta executar `latexmk` na pasta de main.tex.
#
# O modelo usa pdfLaTeX (por causa de inputenc/fontenc) e BibTeX (não Biber).

$pdf_mode = 1;        # gerar PDF com pdflatex
$bibtex_use = 2;      # sempre executar o BibTeX e limpar o .bbl no -C
$default_files = ('main.tex');

# Mostra os erros com "arquivo:linha:", que é mais fácil de localizar.
$pdflatex = 'pdflatex -interaction=nonstopmode -file-line-error %O %S';
