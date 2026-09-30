// Valida a mensagem de cada commit (hook .husky/commit-msg e CI dos PRs).
// O semantic-release lê essas mensagens para decidir se sai uma versão:
// feat -> versão menor, fix/perf -> correção, "!" ou BREAKING CHANGE -> maior.
// docs, chore, refactor, style, test, build e ci não geram versão.
export default {
  extends: ["@commitlint/config-conventional"],
  rules: {
    // As mensagens são em português e podem começar com maiúscula.
    "subject-case": [0],
  },
};
