# eis-plugins

Marketplace de plugins do Claude Code do Diego Eis. Este repo só lista os plugins; o código de cada um vive no próprio repositório.

## Instalar

No Claude Code:

```
/plugin marketplace add diegoeis/eis-plugins
/plugin install eis-manager-assistant@eis-plugins
/plugin install eis-content-builder@eis-plugins
/plugin install eis-setup-plugin@eis-plugins
```

Para receber versões novas:

```
/plugin marketplace update eis-plugins
```

Ou ligue a atualização automática em `/plugin` → Marketplaces → `eis-plugins` → Enable auto-update. Ela vem desligada por padrão em marketplaces de terceiros.

## Plugins

| Plugin | O que faz | Repositório |
| --- | --- | --- |
| `eis-manager-assistant` | Status reports com fontes verificáveis para líderes acompanharem times, fóruns e pessoas. | [diegoeis/eis-manager-plugin](https://github.com/diegoeis/eis-manager-plugin) |
| `eis-content-builder` | Assistente de escrita que aprende sua voz e produz conteúdo para vários canais. | [diegoeis/eis-content-builder](https://github.com/diegoeis/eis-content-builder) |
| `eis-setup-plugin` | Cria a estrutura de pastas de um projeto de plugin para Claude Code e Cowork: src/ como raiz do plugin, docs/, scripts/pack.sh e builds versionados em dist/. | [diegoeis/eis-setup-plugin](https://github.com/diegoeis/eis-setup-plugin) |

### eis-manager-assistant

Repositório: [diegoeis/eis-manager-plugin](https://github.com/diegoeis/eis-manager-plugin)

| Skill | O que faz |
| --- | --- |
| [`mgr-setup`](https://github.com/diegoeis/eis-manager-plugin/tree/master/plugin/skills/mgr-setup) | Cria ou amplia o workspace: times, fóruns, pessoas, tópicos e fontes. |
| [`mgr-status-report`](https://github.com/diegoeis/eis-manager-plugin/tree/master/plugin/skills/mgr-status-report) | Gera o status report de um time, fórum ou pessoa a partir do tracker, do messenger e das reuniões, com cada fato citado. |
| [`mgr-topic`](https://github.com/diegoeis/eis-manager-plugin/tree/master/plugin/skills/mgr-topic) | Cria, lista, remove e arquiva tópicos do workspace. |

### eis-content-builder

Repositório: [diegoeis/eis-content-builder](https://github.com/diegoeis/eis-content-builder)

| Skill | O que faz |
| --- | --- |
| [`writer-setup`](https://github.com/diegoeis/eis-content-builder/tree/main/plugin/skills/writer-setup) | Cria o workspace de escrita e o perfil de voz do autor. |
| [`writer-create`](https://github.com/diegoeis/eis-content-builder/tree/main/plugin/skills/writer-create) | Escreve um texto na voz do autor para um canal e um tema. |
| [`writer-ideate`](https://github.com/diegoeis/eis-content-builder/tree/main/plugin/skills/writer-ideate) | Ajuda a encontrar tema e ângulo, sem escrever o texto. |
| [`writer-calibrate`](https://github.com/diegoeis/eis-content-builder/tree/main/plugin/skills/writer-calibrate) | Ajusta as regras de voz a partir de um texto que o autor corrigiu. |
| [`writer-opinion-mine`](https://github.com/diegoeis/eis-content-builder/tree/main/plugin/skills/writer-opinion-mine) | Entrevista o autor para montar ou refinar o mapa de opiniões. |
| [`writer-index`](https://github.com/diegoeis/eis-content-builder/tree/main/plugin/skills/writer-index) | Cria ou atualiza o índice de artigos do workspace. |
| [`writer-save`](https://github.com/diegoeis/eis-content-builder/tree/main/plugin/skills/writer-save) | Move um rascunho para o destino final: pasta, CMS ou agendamento. |

### eis-setup-plugin

Repositório: [diegoeis/eis-setup-plugin](https://github.com/diegoeis/eis-setup-plugin)

| Skill | O que faz |
| --- | --- |
| [`skel-init`](https://github.com/diegoeis/eis-setup-plugin/tree/main/src/skills/skel-init) | Cria um projeto de plugin novo com `src/`, `docs/`, `scripts/pack.sh`, README, AGENTS.md e CLAUDE.md, pronto para receber as skills. |
| [`skel-migrate`](https://github.com/diegoeis/eis-setup-plugin/tree/main/src/skills/skel-migrate) | Move um plugin que já existe para essa estrutura: mostra o plano, espera aprovação, só move arquivos existentes e cria os que faltam. |
| [`skel-build`](https://github.com/diegoeis/eis-setup-plugin/tree/main/src/skills/skel-build) | Sobe a versão do plugin (patch por padrão) e roda o `pack.sh` para gerar `dist/vX.Y.Z/` e o zip. |

## Adicionar um plugin

1. O plugin precisa estar num repo público do GitHub, com `.claude-plugin/plugin.json` na pasta do plugin.
2. Acrescente uma entrada em `.claude-plugin/marketplace.json` com `source` do tipo `git-subdir` (`url` do repo e `path` da pasta do plugin; use `github` com `repo` quando o plugin estiver na raiz).
3. Não coloque `version` na entrada do marketplace. Se o `plugin.json` tiver `version`, os usuários só recebem atualização quando esse número mudar; sem `version`, cada commit no branch padrão vira uma versão nova.
4. Atualize este README: uma linha na tabela **Plugins** (nome, descrição, link do repo) e uma seção com as skills do plugin, cada uma com link para a pasta dela no GitHub. Detalhes em `AGENTS.md`.
5. Rode `claude plugin validate .` e faça o push.
