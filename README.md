# eis-plugins

Marketplace de plugins do Claude Code do Diego Eis. Este repo só lista os plugins; o código de cada um vive no próprio repositório.

## Instalar

No Claude Code:

```
/plugin marketplace add diegoeis/eis-plugins
/plugin install eis-manager-assistant@eis-plugins
/plugin install eis-content-builder@eis-plugins
/plugin install eis-plugin-skeleton@eis-plugins
/plugin install eis-task-manager@eis-plugins
```

Para receber versões novas:

```
/plugin marketplace update eis-plugins
```

Ou ligue a atualização automática em `/plugin` → Marketplaces → `eis-plugins` → Enable auto-update. Ela vem desligada por padrão em marketplaces de terceiros.

## Plugins

| Plugin | O que faz | Repositório |
| --- | --- | --- |
| `eis-manager-assistant` | Status reports with verifiable sources for leaders who follow teams, forums and people. | [diegoeis/eis-manager-assistant](https://github.com/diegoeis/eis-manager-assistant) |
| `eis-content-builder` | Writing assistant that learns your voice and produces content for blogs, LinkedIn, newsletters and other channels. | [diegoeis/eis-content-builder](https://github.com/diegoeis/eis-content-builder) |
| `eis-plugin-skeleton` | Creates the folder structure of a plugin project for Claude Code and Cowork: src/ as the plugin root, docs/, scripts/pack.sh and versioned builds in dist/. | [diegoeis/eis-plugin-skeleton](https://github.com/diegoeis/eis-plugin-skeleton) |
| `eis-task-manager` | Task manager for your tasks and obligations, built on a daily note from calendar, messenger, e-mail, meeting notes and reports: tasks sorted by due date, pending issues by person and important topics, with tasks closed automatically when any source shows they were done. Runs again during the day to update the note, plus a local page to work the tasks. | [diegoeis/eis-task-manager](https://github.com/diegoeis/eis-task-manager) |

### eis-manager-assistant

Repositório: [diegoeis/eis-manager-assistant](https://github.com/diegoeis/eis-manager-assistant)

| Skill | O que faz |
| --- | --- |
| [`mgr-setup`](https://github.com/diegoeis/eis-manager-assistant/tree/master/src/skills/mgr-setup) | Cria ou amplia o workspace: times, fóruns, pessoas, tópicos e fontes. |
| [`mgr-status-report`](https://github.com/diegoeis/eis-manager-assistant/tree/master/src/skills/mgr-status-report) | Gera o status report de um time, fórum ou pessoa a partir do tracker, do messenger e das reuniões, com cada fato citado. |
| [`mgr-topic`](https://github.com/diegoeis/eis-manager-assistant/tree/master/src/skills/mgr-topic) | Cria, lista, remove e arquiva tópicos do workspace. |

Também roda no Hermes: `hermes plugins install diegoeis/eis-manager-assistant/src --enable`.

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

### eis-plugin-skeleton

Repositório: [diegoeis/eis-plugin-skeleton](https://github.com/diegoeis/eis-plugin-skeleton)

| Skill | O que faz |
| --- | --- |
| [`skel-init`](https://github.com/diegoeis/eis-plugin-skeleton/tree/main/src/skills/skel-init) | Cria um projeto de plugin novo com `src/`, `docs/`, `scripts/pack.sh`, README, AGENTS.md e CLAUDE.md, pronto para receber as skills. |
| [`skel-migrate`](https://github.com/diegoeis/eis-plugin-skeleton/tree/main/src/skills/skel-migrate) | Move uma pasta que já existe (plugin, skill ou scripts) para essa estrutura: mostra um plano curto, espera aprovação, só move arquivos e cria os que faltam, inclusive o `plugin.json`. |
| [`skel-build`](https://github.com/diegoeis/eis-plugin-skeleton/tree/main/src/skills/skel-build) | Sobe a versão do plugin (patch por padrão) e roda o `pack.sh` para gerar `dist/vX.Y.Z/` e o zip. |

### eis-task-manager

Repositório: [diegoeis/eis-task-manager](https://github.com/diegoeis/eis-task-manager)

| Skill | O que faz |
| --- | --- |
| [`tasks-setup`](https://github.com/diegoeis/eis-task-manager/tree/main/src/skills/tasks-setup) | Cria, mostra ou edita o workspace `.eis-task-manager/` na pasta que o usuário escolhe: `config.json` (quem é o usuário, idioma, pasta das notas, fontes ligadas, pessoas e canais prioritários, pastas de reuniões e reports), formato das tarefas e a cópia da página da daily. |
| [`tasks-update`](https://github.com/diegoeis/eis-task-manager/tree/main/src/skills/tasks-update) | Gera a nota do dia com agenda, tarefas (novas e migradas, ordenadas por prazo, criação e prioridade), pendências por pessoa, tópicos importantes e concluídos. Quando a nota já existe, atualiza no lugar sem perder edições. Põe prioridade só quando a fonte pede; tarefa cancelada não volta. Fecha tarefas com evidência na fonte ou numa busca dirigida (série da reunião, notas e DMs das pessoas, issues citadas), lendo só o que mudou desde a última execução. Roda sem perguntas, pode ser agendada. |
| [`tasks-view`](https://github.com/diegoeis/eis-task-manager/tree/main/src/skills/tasks-view) | Abre a página local da daily: painel de tarefas (abertas, novas na semana, vencendo, atrasadas; filtros e ordenação) com abas de abertas, vencendo hoje, feitas e canceladas, com busca, onde se marca, cancela (`[-]`) e cria tarefas, deixa ações para a IA (🤖) e edita com duplo clique texto, prioridade, prazo e comentários; fontes que são notas viram links (Obsidian e Granola); cada mudança vai direto para a nota. Antes de abrir, roda o `tasks-update` (cria ou atualiza a nota do dia); `--no-generate` só abre. |
| [`tasks-act`](https://github.com/diegoeis/eis-task-manager/tree/main/src/skills/tasks-act) | Executa as ações que o usuário deixou para a IA nos comentários das tarefas (marcados com 🤖), com qualquer skill, plugin, connector ou agendamento que a sessão tenha. Trava cada ação (🤖⏳) antes de executar, marca 🤖✅ ou 🤖⚠️ e anota o resultado com links logo abaixo. Um script lista as pendentes sem LLM, para rodar agendada. |

## Adicionar um plugin

1. O plugin precisa estar num repo público do GitHub, com `.claude-plugin/plugin.json` na pasta do plugin.
2. Acrescente uma entrada em `.claude-plugin/marketplace.json` com `source` do tipo `git-subdir` (`url` do repo e `path` da pasta do plugin; use `github` com `repo` quando o plugin estiver na raiz).
3. Não coloque `version` na entrada do marketplace. Se o `plugin.json` tiver `version`, os usuários só recebem atualização quando esse número mudar; sem `version`, cada commit no branch padrão vira uma versão nova.
4. Atualize este README: uma linha na tabela **Plugins** (nome, descrição, link do repo) e uma seção com as skills do plugin, cada uma com link para a pasta dela no GitHub. Detalhes em `AGENTS.md`.
5. Rode `claude plugin validate .` e faça o push.
