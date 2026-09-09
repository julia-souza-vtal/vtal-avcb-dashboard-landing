---
name: vtal-avcb-dashboard-landing
description: Criação, atualização e publicação de painéis de monitoramento de AVCB/PPCI no padrão V.tal em HTML5 a partir de planilhas Excel. Use quando for solicitado criar o painel AVCB V.tal, gerar o relatório de monitoramento de AVCB/PPCI, processar a planilha Big_Numbers_AVCB_-_planilha_IA__1_.xlsx ou publicar o dashboard no MinIO S3.
---
## Progressive disclosure of reference files
Use the skill creator skill to update this skill so it uses progressive disclosure for reference files. Map each reference file to the specific step where it's actually needed, and instruct the skill to read a reference file only at that step, not all of them upfront. In the SKILL.md, name the exact file to read inside the step that uses it, so the context window only ever loads what the current step requires.

## Human-in-the-loop with multiple options

 Use the skill creator skill to update this skill so every human-in-the-loop step gives me multiple options to choose from. At each decision point in the process, before moving to the next step, have the skill present 5 to 10 variations or options and then wait for me to pick one. Don't move forward on a single suggestion, and don't make me re-prompt for alternatives. Present the options immediately at each step.

## Add a self-improvement rule
Add a self-improvement rule to this skill. Any time I correct your output during the process, or I get an output I explicitly like, ask me whether that should become a permanent update to the skill. If I say yes use the skill-creator to update the relevant SKILL.md step or reference file with the correction, new rule, or saved example. Always ask the confirmation question first, never update the skill silently.
---

# Painel de Monitoramento de AVCB V.tal

Este guia fornece o procedimento completo e automatizado para gerar e publicar o painel executivo interativo de monitoramento de AVCB e PPCI no padrão de identidade visual oficial da V.tal.

## 📌 Regras de Publicação e Infraestrutura
- **Caminho de Destino Local**: `/workspace/public/index_V2.html`
- **Link de Publicação S3**: `https://10.119.80.120/minio/tt831467/public/AVCB/`
- **Proibições**:
  - NÃO publicar no `pcorhx01` nem em `public/public`.
  - NÃO incluir textos que não foram explicitados nas especificações.

---

## 🚀 Fluxo de Execução em 5 Passos

### Passo 1: Validação dos Arquivos de Entrada
Antes de iniciar o processamento, execute o script de verificação dos arquivos obrigatórios:

```bash
/app/venv/bin/python3 /home/hermeswebui/.hermes/skills/vtal-avcb-dashboard/scripts/check_inputs.py /workspace
```

Se algum arquivo estiver ausente (`logo-vtal-footer.png` ou `Big_Numbers_AVCB_-_planilha_IA__1_.xlsx`), interrompa a execução e solicite os arquivos ao usuário.

### Passo 2: Extração e Tratamento dos Dados
1. Carregar a aba `AVCB IA(2)` da planilha Excel usando **Pandas** (`/app/venv/bin/python3`).
2. Consultar as regras detalhadas de cálculo e mapeamento em [data-rules-and-kpis.md](references/data-rules-and-kpis.md).
3. Calcular a variável `total_predios` e extrair os KPIs globais e agrupamentos dos gráficos.
4. Exportar o dataset tratado e consolidado em formato JSON para ser embutido diretamente no HTML.

### Passo 3: Geração do Painel HTML Interativo
Construir o arquivo `index.html` seguindo as diretrizes estritas de UI/UX descritas em [visual-identity.md](references/visual-identity.md) e de navegação descritas em [navegação](references/navegação.md):
- **Layout**: Proporção 16:9, responsivo, fundo `#F4F5F9`, cards `#FFFFFF`, destaque `#FFD919`.
- **Sidebar**: Drawer flutuante recolhível
- **Filtros**:
  - Filtros flutuantes no topo com opção "Selecionar Todos".
  - Cascata ativa entre **UF** e **Município**.
- **Gráficos**:
  - Usar bibliotecas interativas (Chart.js / Plotly).
  - Exibir valores absolutos e percentuais diretamente em cada barra (eixo Y tamanho `9px` com quebra de linha).
- **Tabela de Detalhamento**:
  - Campo de busca por nome do prédio.
  - Ordenação clicável por coluna (crescente/decrescente).

### Passo 4: Gravação do HTML
Salvar o arquivo gerado no caminho:
`/workspace/public/index.html`

### Passo 5: Publicação no MinIO S3
Execute o script oficial de publicação para expor o painel no S3 da V.tal:

```bash
/app/venv/bin/python3 /home/hermeswebui/.hermes/publish.py --public /workspace/public/index_V2.html
```

Forneça ao usuário a URL gerada pelo script de publicação para acesso direto via navegador. 
