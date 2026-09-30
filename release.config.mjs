// Configuração do semantic-release para o modelo LaTeX.
//
// Isto não é um pacote npm: não há publicação no registro nem versão no
// package.json. O que se publica é o ZIP gerado por scripts/empacotar.py,
// anexado a uma Release do GitHub com a tag vX.Y.Z.
//
// Só sai versão quando a main recebe commits feat, fix ou perf (ou uma
// mudança incompatível). O workflow .github/workflows/release.yml compila o
// ZIP extraído numa pasta limpa antes de chegar aqui; se a compilação
// falhar, o semantic-release nem é executado.
export default {
  branches: ["main"],
  tagFormat: "v${version}",
  plugins: [
    ["@semantic-release/commit-analyzer", { preset: "conventionalcommits" }],
    ["@semantic-release/release-notes-generator", { preset: "conventionalcommits" }],
    ["@semantic-release/exec", { prepareCmd: "python3 scripts/empacotar.py" }],
    [
      "@semantic-release/github",
      {
        assets: [
          {
            path: "dist/modelo-artigo-ifpi.zip",
            name: "modelo-artigo-ifpi-v${nextRelease.version}.zip",
            label: "Modelo de artigo IFPI v${nextRelease.version} (ZIP para Overleaf, Prism ou uso local)",
          },
        ],
      },
    ],
  ],
};
