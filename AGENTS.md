# AGENTS.md

Este repo é só o marketplace `eis-plugins`. Ele lista plugins cujo código vive em outros repositórios. Não há código de plugin aqui.

## Ao adicionar, remover ou renomear um plugin

Toda mudança em `.claude-plugin/marketplace.json` exige atualizar o `README.md` no mesmo commit.

### Adicionar

1. Acrescente a entrada em `.claude-plugin/marketplace.json` (regras na seção "Adicionar um plugin" do README). Não use `version` na entrada.
2. No `README.md`:
   - Em **Instalar**, acrescente `/plugin install <nome>@eis-plugins`.
   - Na tabela **Plugins**, acrescente uma linha: nome da entrada, a mesma `description` do marketplace, e o link do repositório (`[owner/repo](https://github.com/owner/repo)`).
   - Crie uma seção `### <nome>` com o link do repositório e uma tabela das skills do plugin.
3. Para a tabela de skills, leia as skills reais do repositório do plugin (pasta `skills/` dentro do `path` da entrada). Uma linha por skill:
   - Nome com link para a pasta da skill: `https://github.com/<owner>/<repo>/tree/<branch padrão>/<path>/skills/<skill>`. Confira o branch padrão do repo; não assuma `main`.
   - Uma frase em português resumindo o `description` do `SKILL.md`. Não invente funcionalidade que o `SKILL.md` não descreve.
4. Rode `claude plugin validate .` antes do push.

### Remover ou renomear

- Remova ou renomeie a linha da tabela, a seção de skills e o comando em **Instalar**.
- Para renomear, use `renames` no `marketplace.json` para não quebrar quem já instalou.

### Quando um plugin ganhar ou perder skills

O README não se atualiza sozinho. Se souber que o repositório de um plugin mudou as skills, atualize a seção dele aqui.
