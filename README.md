# eis-plugins

Marketplace de plugins do Claude Code do Diego Eis. Este repo só lista os plugins; o código de cada um vive no próprio repositório.

## Instalar

No Claude Code:

```
/plugin marketplace add diegoeis/eis-plugins
/plugin install eis-manager-assistant@eis-plugins
/plugin install eis-content-builder@eis-plugins
```

Para receber versões novas:

```
/plugin marketplace update eis-plugins
```

## Plugins

| Plugin | O que faz | Repositório |
| --- | --- | --- |
| `eis-manager-assistant` | Status reports com fontes verificáveis para líderes acompanharem times, fóruns e pessoas. | [diegoeis/eis-manager-plugin](https://github.com/diegoeis/eis-manager-plugin) |
| `eis-content-builder` | Assistente de escrita que aprende sua voz e produz conteúdo para vários canais. | [diegoeis/eis-content-builder](https://github.com/diegoeis/eis-content-builder) |

## Adicionar um plugin

1. O plugin precisa estar num repo público do GitHub, com `.claude-plugin/plugin.json` na pasta do plugin.
2. Acrescente uma entrada em `.claude-plugin/marketplace.json` com `source` do tipo `git-subdir` (`url` do repo e `path` da pasta do plugin; use `github` com `repo` quando o plugin estiver na raiz).
3. A versão fica só no `plugin.json` de cada plugin. Não coloque `version` na entrada do marketplace, senão o plugin fica preso nela.
4. Rode `claude plugin validate .` e faça o push.
