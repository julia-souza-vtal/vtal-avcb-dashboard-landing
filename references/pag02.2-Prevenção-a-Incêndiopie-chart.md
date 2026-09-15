## 📂 Fonte dos Dados
- **Aba da Planilha**: `DIVERSOS` da planilha `Big_Numbers_AVCB_-_planilha_IA.xlsx`

## Proporção do Painel: 

- Mantenha o cabeçalho, filtros, Cards e cabeçalho da tabela sempre visivel, independente do estado da barra de rolagem

## **Filtros do Cabeçalho**:
  - Siga estritamente a ordem dos Filtros:  Brigada, SDAI, Regional, UF, Município, Tipo de Prédio, Resp. Legal, Prioridade
  - Posicionados na parte superior da página, abaixo do cabeçalho
  - OBRIGATÓRIO USAR Filtros com Padrão flutuante/horizontal recolhível com suporte a múltipla seleção e opção "Selecionar Todos"
  - OBRIGATÓRIO USAR Filtro [UF] e filtro [Município] com relacionamento em cascata (ao selecionar UF, exibe apenas os municípios correspondentes, seguindo o arquivo "municipios-incendio.csv")
  - As seções 'Prevenção a Incêndio', 'Detalhamento PI', devem estar uma abaixo da outra, em sequência. Sem botões para intercambiar as seções.
  <!-- - Colocar o total de prédios dessa página na mesma linha dos filtros, no lado extremo esquerdo, com borda elíptica e fundo em preto (#000000), texto em branco(#FAFAFA), para destaque -->

## texto de observação acima dos cards

<!-- - alinhado à direita, fonte de texto escreva: "Essa aba do painel não considera os prédios com AVCB descontinuado" -->
-  alinhado à direita, fonte de texto escreva: "Atualizado em: " + data de envio da última planilha, seguindo o formato DD/MM/AAAA

A partir dos dados da aba "DIVERSOS" da planilha em anexo, crie:

### 🎴 Cards / KPIs Globais
Formatados como `XX (XX,XX%)`:
 
1. **Total de Prédios**: Contagem de registros `total_predios_ativos`. Ícone no canto extremo esquerdo do card na cor  #FFD919

2. **Brigada**: Contagem de registros "12 Horas", "24 Horas", "12H - noturno", "12H - diurno" na coluna `Brigada Civil V.tal 2026` + % sobre `total_predios`. Ícone no canto extremo esquerdo do Card: user-shield na cor  #FFD919

3. **SDAI válido**: Contagem de registros "SIM" na coluna `SDAI` + % sobre `total_predios`. Ícone no canto extremo esquerdo do Card: alarm-smoke  na cor  #FFD919

4. **SDAI/SDACI sem falhas**: Contagem de registros "SIM" na coluna `Operacional sem falhas` + % sobre `total_predios`. Ícone no canto extremo esquerdo do Card: fa-check-circle na cor  #FFD919

5. **SDAI/SDACI com falhas**: Contagem de registros "Operacional com falhas - Alto", "Inoperante",
"Operacional com falhas - Médio", "Operacional com falhas - Baixo",
"Operacional com falhas - Muito alto" na coluna `SDAI/SDACI operante` + % sobre `total_predios`. Ícone no canto extremo esquerdo do Card: fa-exclamation-circle na cor  #FFD919


6. **FM200 válido**: Contagem de registros do tipo "SIM" na coluna `FM200` + % sobre `total_predios`. Ícone no canto extremo esquerdo do Card: cylinder na cor  #FFD919

7. **Extintor presente**: Contagem de registros "SIM" na coluna `Extintor` + % sobre `total_predios`. Ícone no canto extremo esquerdo do Card: fire-extinguisher na cor  #FFD919

## 📋 1ª Seção ("Prevenção a Incêndio (PI)")
### Gráficos
- gere os gráficos "Brigada Civil" e "SDAI/SDACI Operante" lado a lado. Ambos gráficos devem ter a mesma altura.
- O espaçamento das barras do gráfico "SDAI/SDACI Operante" deve ser de 12 px
- **Valores e Percentuais**: Exibir valores absolutos e % diretamente em cada barra.
- **Tooltips**: NÃO utilizar tooltips como forma de visualização das informações.
- **Eixos**: Não deixe os valores numéricos nos eixos X dos gráficos. Mantenha valores numéricos nos eixos Y dos gráficos

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

1. **Brigada Civil**:
   - Gráfico de barras horizontal, com valor absoluto e o percentual.
   - Cor da barra: na cor  #FFD919
   - Itens: SIM, NÃO, 12 Horas, 24 Horas.
   - Ordenação em ordem **decrescente**.

2. **SDAI/SDACI Operante**
   - Gráfico de barras horizontal,  com valor absoluto e o percentual.
   - Cor da barra: #FFD919
   - Itens: Operacional sem falhas, Operacional com falhas - Alto , Inoperante, Operacional com falhas - Médio, Condomínio, Operacional com falhas - Baixo, Operacional com falhas - Muito alto, Não Informado
   - Os itens " " e "-" na coluna devem ser tratados como "Não Informado" na contagem do gráfico
   - Ordenação em ordem **decrescente**.

3. **SDAI**:
   - Gráfico de barras horizontal, com valor absoluto e o percentual. Coloque os rótulos de "SIM" ou "NÃO" junto aos números. Não crie a legenda.
   - Cor da barra: #FFD919   
   - Itens: SIM, NÃO.
   - Ordenação em ordem **decrescente**.

4. **FM200**:
   - Gráfico de barras horizontal, com valor absoluto e o percentual. Coloque os rótulos de "SIM" ou "NÃO" junto aos números. Não crie a legenda.
   - Cor da barra: #FFD919   
   - Itens: SIM, NÃO.
   - Ordenação em ordem **decrescente**.

5. **Extintor**:
   - Gráfico de barras horizontal, com 4 barras ("Atenção", "Em recarga ", "Vencido", "OK"), contendo valor absoluto e o percentual. Coloque os rótulos de "Atenção" | "Em recarga "| "Vencido" | "OK" no eixo Y. Não crie a legenda.
   - Cor da barra: #FFD919   
   - Itens: Atenção | Em recarga | Vencido | OK
   - Ordenação em ordem **decrescente**.

## 2ª Seção ("Detalhamento PI")
A partir dos dados da aba "DIVERSOS" da planilha em anexo, crie:

- Tabela com Cabeçalho de fonte #000000:

(Prédio (ID) | Nome Comum | UF | Município | Tipo | Responsável | Brigada Civil | SDAI | FM200	| Status Extintor | Data de Vencimento Extintor | Data de Vencimento Mangueira | SDAI/SDACI operante)

- Permita que o usuário consiga ajustar o tamanho das colunas, com o cursor, semelhante a funcionalidade do Microsoft Excel;

- Para colunas com texto do cabeçalho muito grande, dê uma quebra de linha, para mostrar o texto dividido em 2 linhas (para garantir que todas as colunas estejam visíveis na página)

- **Seletor de Ordenação**: Crie o seletor de ordenação no cabeçalho: Adicione a classe de ordenação ao código JavaScript da tabela, 
que seja possível filtrar cada uma das colunas através do seletor de ordenação Crescente/Decrescente em formato de botão. 
De acordo com o tutorial do link https://webdesign.tutsplus.com/how-to-create-a-sortable-html-table-with-javascript--cms-92993t
- **Busca de Texto Aberto**: Filtro pelo nome do prédio.
- **Campo de Busca**: Campo de pesquisa por texto aberto pelo nome do prédio no canto superior direito da área da tabela.
- **Aparência**: Tabela com rolagem interna, sem paginação e sem textos na parte superior além do título e campo de busca.