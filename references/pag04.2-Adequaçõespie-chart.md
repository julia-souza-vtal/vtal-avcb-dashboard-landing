## 📂 Fonte dos Dados
- **Aba da Planilha**: `Adequações` da planilha `Big_Numbers_AVCB_-_planilha_IA.xlsx`

## Proporção do Painel: 

- Mantenha o cabeçalho, filtros, Cards e cabeçalho da tabela sempre visivel, independente do estado da barra de rolagem

## **Filtros do Cabeçalho**:
  - Siga estritamente a ordem dos Filtros: Regional, UF, Município, Tipo de Prédio, Resp. Legal
  - Posicionados na parte superior da página, abaixo do cabeçalho
  - OBRIGATÓRIO USAR Filtros com Padrão flutuante/horizontal recolhível com suporte a múltipla seleção e opção "Selecionar Todos"
  - OBRIGATÓRIO USAR Filtro [UF] e filtro [Município] com relacionamento em cascata (ao selecionar UF, exibe apenas os municípios correspondentes, seguindo o arquivo "municipios-incendio.csv")
   - As seções 'Adequações', 'Detalhamento Adequações', devem estar uma abaixo da outra, em sequência. Sem botões para intercambiar as seções.
  <-- - Colocar o total de prédios dessa página na mesma linha dos filtros, no lado extremo esquerdo, com borda elíptica e fundo em preto (#000000), texto em branco(#FAFAFA), para destaque -->


- filtros na parte superior, conforme a seguinte ordem: Regional | UF | Município | Tipo | Responsável Legal | Prioridade

## texto de observação acima dos cards

<!-- - alinhado à direita, fonte de texto escreva: "Essa aba do painel não considera os prédios com AVCB descontinuado" -->
-  alinhado à direita, fonte de texto escreva: "Atualizado em: " + data de envio da última planilha, seguindo o formato DD/MM/AAAA

### 🎴 Cards / KPIs Globais
Formatados como `XX (XX,XX%)`:

- **Total de Prédios**: Contagem de registros `total_predios_ativos` - SEM a porcentagem . Ícone no canto extremo esquerdo do card na cor  #FFD919

- **Total de Adequações**: Contagem de registros `total_adequações`. Ícone no canto extremo esquerdo do card na cor  #FFD919

- **Adequações Pendentes de Sistemas de Combate a Incêndio**: Contagem de registros pendentes nas colunas: "Bomba de Incêndio", "Extintor + suportes", "Hidrantes" - E a % sobre `total_predios_ativos`. Ícone no canto extremo esquerdo do card na cor  #FFD919

- **Adequações Pendentes de Adequação Civil**: Contagem de registros pendentes nas colunas "Escada", "Escada Enclausurada", "PCF" - E a % sobre `total_predios_ativos`. Ícone no canto extremo esquerdo do card na cor  #FFD919

- **Adequações Pendentes de Sistemas de Detecção e Alarme**: Contagem de registros pendentes nas colunas  "SDAI", "SDACI" - E a % sobre `total_predios_ativos`. Ícone no canto extremo esquerdo do card na cor  #FFD919

- **Adequações Pendentes de Sistemas Elétricos e Aterramento** - Contagem de registros pendentes nas colunas "Quadros Elétricos", "SPDA" E a % sobre `total_predios_ativos`. Ícone no canto extremo esquerdo do card na cor  #FFD919

- **Adequações Pendentes de Abandono de Área e Emergência** - Contagem de registros pendentes nas colunas "Sinalizações", "Iluminação de Emergência" E a % sobre `total_predios_ativos`. Ícone no canto extremo esquerdo do card na cor  #FFD919

### 1ª Seção ("Adequações")
#### Gráficos

- componente responsivo em HTML, CSS moderno e opcionalmente SVG ou Flexbox/CSS Grid puro (sem dependências externas pesadas tipo Chart.js, a menos que necessário), seguindo rigorosamente estas diretrizes técnicas e visuais: 

1. **Proporção e Limites (Escala Consistente):**
   - O tamanho das barras deve manter a proporção exata e matemática em relação aos valores dos dados (ex: uma barra de 100 deve ter exatamente o dobro do tamanho de uma barra de 50).
   - O contêiner do gráfico deve respeitar rigidamente os limites da área designada (largura máxima de 100% do painel), evitando transbordamentos (overflow) horizontais indesejados.

2. **Rótulos e Eixos Sempre Visíveis:**
   - Todos os rótulos (nomes das categorias) e os valores numéricos das barras (labels) DEVEM aparecer permanentemente legíveis, sem cortes, sobreposições ou truncamentos em qualquer largura de tela (mobile e desktop).
   - Para barras horizontais, posicione o valor numérico de forma clara (preferencialmente ao lado ou dentro da barra, com contraste adequado) e garanta que o eixo X/escala de valores possua margem de respiro superior (`max` do eixo calculado com margem de segurança de ~10% acima do maior valor).

3. **Padrão Visual SaaS (V.tal / UI Moderna):**
   - Paleta de cores limpa: fundo #F4F5F9, cartões em #FFFFFF, cor principal: amarelo corporativo (#FFD919), cor secundária1: CINZA ESCURO 1 #514F66, cor secundária2: CINZA MÉDIO #C2C6D6, cor secundária3 CINZA ESCURO 2: #2E2D39, cor secundária4 AMARELO ESCURO ('#694A00')
   - Tipografia limpa, sem elementos poluidos
   - Código limpo, componentizado e responsivo.

- **Valores e Percentuais**: Exibir valores absolutos e % diretamente em cada barra. 
- ** Rotulos de dados**: os rótulos serão colocados fora da barra, contanto que caibam na área do gráfico. Se o rótulo não puder ser colocado fora da barra, mas dentro da área de gráfico, o rótulo será colocado dentro da barra na posição mais próxima do final da barra.
- **Tooltips**: NÃO utilizar tooltips como forma de visualização das informações.
- **Eixos**: Não deixe os valores numéricos nos eixos X dos gráficos. Mantenha valores numéricos nos eixos Y dos gráficos

<!-- ####  Adequações pendentes gerais
1. Adequações Pendentes
    - Gráfico de barras verticais com valor absoluto e o percentual; 
    - Contagem de prédios com as adequações pendentes (colunas Elétrica, Bomba de incêndio,	Escada, Escada enclausurada, Extintor + suportes, FM200, Hidrantes, PCF, SDACI, SDAI, Sinalizações, Sistema de espuma, SPDA);
   - Ordenação em ordem **decrescente**.
-->

#### LINHA de gráficos 1 - Região 
1. Adequações Pendentes por Regional
    - Seletor suspenso que afeta APENAS os dados desse gráfico 2. Itens: Regional, UF, Município;
    - Gráfico de barras verticais com valor absoluto e o percentual; 
    - Contagem de prédios com as adequações pendentes(valor da célula "SIM") das colunas Elétrica, Bomba de incêndio,	Escada, Escada enclausurada, Extintor + suportes, FM200, Hidrantes, PCF, SDACI, SDAI, Sinalizações, Sistema de espuma, SPDA agregadas por regional (Coluna - itens NORDESTE, SUDESTE, CENTRO OESTE, SUL, NORTE);
   - Ordenação em ordem **decrescente**.

#### LINHA de gráficos 2 - por Categoria
<!-- | Categoria: Itens       
| Sistemas de Combate a Incêndio :  Bombas de incêndio, Extintores, Mangueiras, Hidrantes, SPK, LGE, Agente Limpo |
| Adequação Civil : Escada, Escada Enclausurada, PCF (porta corta-fogo)  |
| Sistemas de Detecção e Alarme: SDAI, SDACI  |
| Sistemas Elétricos e Aterramento : Quadros Elétricos, SPDA |
| Abandono de Área e Emergência: Sinalizações, Iluminação de Emergência   
-->

2. Adequações Pendentes de Sistemas de Combate a Incêndio 
    - Gráfico de barras horizontais com valor absoluto e o percentual. 
    - Contagem de prédios com as adequações pendentes (valor da célula "SIM") das colunas Bomba de Incêndio, Extintor + suportes, Hidrantes
   - Ordenação em ordem **decrescente**.

3. Adequações Pendentes de Adequação Civil
    - Gráfico de barras horizontais com valor absoluto e o percentual. 
    - Contagem de prédios com as adequações pendentes (valor da célula "SIM") das colunas Escada, Escada Enclausurada, PCF (porta corta-fogo); 
   - Ordenação em ordem **decrescente**.

4. Adequações Pendentes de Sistemas de Detecção e Alarme
    - Gráfico de barras horizontais com valor absoluto e o percentual. 
    - Contagem de prédios com as adequações pendentes (valor da célula "SIM") das colunas SDAI, SDACI 

5. Adequações Pendentes de Sistemas Elétricos e Aterramento
    - Gráfico de barras horizontais com valor absoluto e o percentual. 
    - Contagem de prédios com as adequações pendentes (valor da célula "SIM") das colunas Quadros Elétricos, SPDA

6. Adequações Pendentes de Abandono de Área e Emergência
    - Gráfico de barras horizontais com valor absoluto e o percentual. 
    - Contagem de prédios com as adequações pendentes (valor da célula "SIM") das colunas Sinalizações, Iluminação de Emergência

### 2ª Seção ("Detalhamento Adequações")
#### Tabela

- **Tabela com Cabeçalho de fonte #000000**:
Prédio | Nome Comum	| Tipo	| Próprio / Alugado	| Regional | UF |	Categoria de Adequações  |	Tipo de Adequações	| Descrição da adequação | Custo (OG)

- **Seletor de Ordenação**: Crie o seletor de ordenação no cabeçalho: Adicione a classe de ordenação ao código JavaScript da tabela, 
que seja possível filtrar cada uma das colunas através do seletor de ordenação Crescente/Decrescente em formato de botão. 
De acordo com o tutorial do link https://webdesign.tutsplus.com/how-to-create-a-sortable-html-table-with-javascript--cms-92993t

- **Busca de Texto Aberto**: Filtro pelo nome do prédio.

- **Campo de Busca**: Campo de pesquisa por texto aberto pelo nome do prédio no canto superior direito da área da tabela.

- **Aparência**: Tabela com rolagem interna, sem paginação e sem textos na parte superior além do título e campo de busca.

- **Valores monetários**: todos os valores monetários (coluna Custo (OG)) devem ter o ´R$´ na frente, conter o separador de milhar e a vírgula das casas decimais.