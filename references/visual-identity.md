# Guia de Identidade Visual e Layout - Dashboard V.tal

## 🎨 Estilo e Paleta de Cores (Padrão V.tal Oficial)
- **Estilo**: Corporativo Premium + Data Analytics
- **Fundo da Página (Page Background)**: `#F4F5F9` (Cinza claro suave, limpo e corporativo)
- **Fundo dos Cards**: `#FFFFFF` (Branco puro para destaque dos KPIs)
- **Menu Lateral (Sidebar Background)**: `#2E2D39` (Cinza-escuro slate corporativo)
- **Bordas e Divisores**: `#BCC1D6` ou `#E2E2EC` (Azul-acinzentado sutil)
- **Texto Principal**: `#1E1D24` (Alta legibilidade em fundo claro)
- **Destaque Principal (Active Accent)**: `#FFD919` (Amarelo vibrante V.tal)
- **Gráficos**: Cor principal `#FFD919`
- **Gráficos**: Cor secundária `#C2C6D6`

## 🔤 Tipografia
- **Fonte Principal**: Inter (Google Fonts)
- **Títulos**: SemiBold (600)
- **Conteúdo**: Regular (400)
- **Números / KPIs**: Bold (700)

## 📐 Proporção e Layout Geral
- **Proporção do Painel**: Aspect Ratio 16:9 (com design responsivo para telas menores). Evite o uso da barra de rolagem principal, para toda a tela. Diminua o espaçamento e/ou a altura dos gráficos se necessário.
- **Cabeçalho**:
  - Título do painel: `"Painel de Monitoramento de AVCB"`
  - Logo da empresa (`logo-vtal-footer.png`) posicionado à esquerda, fora da barra de navegação
  - Proibido incluir outros textos ou sub-títulos no cabeçalho
  
- **Sidebar Esquerda**:
  - Padrão SaaS drawer: Recolhível por botão e flutuante sobreposta ao abrir
  - Navegação entre as abas: detalhado no arquivo navegação.md
  
- **Filtros do Cabeçalho**:
  - Filtros de Regional, UF, Município, Tipo de Prédio, Resp. Legal, Prioridade
  - Posicionados na parte superior da página, abaixo do cabeçalho
  - OBRIGATÓRIO USAR Filtros com Padrão flutuante/horizontal com suporte a múltipla seleção, botão "Selecionar Todos" para cada gráfico, botão "Limpar" para cada gráfico, botão "Limpar Todos"
  - OBRIGATÓRIO USAR Filtro [UF] e filtro [Município] com relacionamento em cascata (ao selecionar UF, exibe apenas os municípios correspondentes, seguindo o arquivo "municipios-incendio.csv")

## 📊 Regras dos Rótulos nos Gráficos
- **Valores e Percentuais**: Exibir valores absolutos e % diretamente em cada barra. Os valores devem estar visíveis no espaço delimitado para o gráfico. Mantenha espaçamento de 5 px em cada borda.
- **Tooltips**: NÃO utilizar tooltips como forma de visualização das informações.
- **Fonte do Eixo/Rótulos**: Tamanho `9px`. <!-- Se o texto não couber no espaço delimitado, realizar quebra de linha em 2 linhas.-->

# Regras nos Gráficos

- componente responsivo em HTML, CSS moderno e opcionalmente SVG ou Flexbox/CSS Grid puro (sem dependências externas pesadas tipo Chart.js, a menos que necessário), seguindo rigorosamente estas diretrizes técnicas e visuais: 

1. **Proporção e Limites (Escala Consistente):**
   - O tamanho das barras deve manter a proporção exata e matemática em relação aos valores dos dados (ex: uma barra de 100 deve ter exatamente o dobro do tamanho de uma barra de 50).
   - O contêiner do gráfico deve respeitar rigidamente os limites da área designada (largura máxima de 100% do painel), evitando transbordamentos (overflow) horizontais indesejados.

2. **Rótulos e Eixos Sempre Visíveis:**
   - Todos os rótulos (nomes das categorias) e os valores numéricos das barras (labels) DEVEM aparecer permanentemente legíveis, sem cortes, sobreposições ou truncamentos em qualquer largura de tela (mobile e desktop).
   - Para barras horizontais, posicione o valor numérico de forma clara (preferencialmente ao lado ou dentro da barra, com contraste adequado) e garanta que o eixo X/escala de valores possua margem de respiro superior (`max` do eixo calculado com margem de segurança de ~10% acima do maior valor).

3. **Padrão Visual SaaS (V.tal / UI Moderna):**
   - Paleta de cores limpa: fundo `#F4F5F9`, cartões em `#FFFFFF`, amarelo corporativo (`#FFD919`) para as barras horizontais.
   - Tipografia limpa, sem elementos poluidos, sem gráficos de pizza ou rosca (utilize estritamente barras horizontais com rótulos de valor absoluto e percentual quando aplicável).
   - Código limpo, componentizado e responsivo.

<!-- 
- mantenha um espaçamento de 20 px nas bordas laterais dos gráficos. Preciso que os textos dos rótulos estejam visíveis.

- mantenha os rótulos das barras na parte interior da barra, com possibilidade de estourar o texto para parte externa da barra, o valor NÃO pode ultrapassar a área do gráfico.

- os rótulos de dados precisam estar sempre visíveis.

- tamanho da barra + rótulo de dados, PRECISAM ser sempre menores do que o tamanho do eixo X.
-->