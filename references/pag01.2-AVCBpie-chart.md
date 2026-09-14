## 📂 Fonte dos Dados
- **Aba da Planilha**: `AVCB IA` da planilha `Big_Numbers_AVCB_-_planilha_IA.xlsx`

## Proporção do Painel: 

- Mantenha o cabeçalho, filtros, Cards e cabeçalho da tabela sempre visivel, independente do estado da barra de rolagem

<!-- - Colocar o total de prédios dessa página na mesma linha dos filtros, no lado extremo esquerdo, com borda elíptica e fundo em preto (#000000), texto em branco(#FAFAFA), para destaque -->

- As seções 'AVCB', 'Detalhamento AVCB', 'Detalhamento AVCB Descontinuado' devem estar uma abaixo da outra, em sequência. Sem botões para intercambiar as seções.

## **Filtros do Cabeçalho**:
  - Siga estritamente a ordem dos Filtros: Regional, UF, Município, Tipo de Prédio, Resp. Legal, Prioridade, Status do projeto PPCI
  - Posicionados na parte superior da página, abaixo do cabeçalho
  - OBRIGATÓRIO USAR Filtros com Padrão flutuante/horizontal recolhível com suporte a múltipla seleção e opção "Selecionar Todos"
  - OBRIGATÓRIO USAR Filtro [UF] e filtro [Município] com relacionamento em cascata (ao selecionar UF, exibe apenas os municípios correspondentes, seguindo o arquivo "municipios-incendio.csv")
  - Considere APENAS o total de prédios em que AVCB_IA[Status AVCB] == "Pendente"
  <!-- - Colocar o total de prédios dessa página na mesma linha dos filtros, no lado extremo esquerdo, com borda elíptica e fundo em preto (#C2C6D6), texto em branco(#FAFAFA), para destaque. -->

## texto de observação acima dos cards

- alinhado à direita, fonte de texto escreva: "Essa aba do painel não considera os prédios com AVCB descontinuado" 

## 🎴 Cards / KPIs Globais para as abas "AVCB" e "Detalhamento AVCB"
Formatados como `XX (XX,XX%)`:

- Utilize ícones que estejam de acordo com o contexto do painel, da aba da planilha e com o item do respectivo card. Ícone no canto extremo esquerdo do card.

total_predios = distinctcount(AVCB_IA[Prédio])

total_predios_pendentes = prédios em que AVCB_IA[Status AVCB] == "Pendente"

total_predios_descontinuados = prédios em que AVCB_IA[AVCB] == "Descontinuados"

total_predios_ativos = total_predios - total_predios_descontinuados

1. **Total de Prédios**: Contagem de registros `total_predios_ativos`. Ícone no canto extremo esquerdo do card na cor  #FFD919
2. **Prédios Descontinuados**:  Contagem de registros `total_predios_descontinuados`. Ícone no canto extremo esquerdo do card na cor  #FFD919
3. **AVCBs Válidos**: Contagem de registros válidos na coluna `AVCB` + % sobre `total_predios_ativos`. Ícone no canto extremo esquerdo do card: fa-check-circle  na cor  #FFD919
4. **AVCBs Vencidos**: Contagem de registros do tipo "Vencido" na coluna `AVCB` + % sobre `total_predios_ativos`. Ícone no canto extremo esquerdo do card:  fa-exclamation-circle na cor  #FFD919
5. **Status do Projeto PPCI Concluído**: Contagem de registros "Concluído" na coluna `Status do Projeto PPCI` + % sobre `total_predios_ativos`.Ícone no canto extremo esquerdo do card: fa-file-signature na cor  #FFD919
6. **Status PPCI Aprovado**: Contagem de registros "Aprovado" na coluna `Status PPCI` + % sobre `total_predios_ativos`.Ícone no canto extremo esquerdo do card: fa-file-signature na cor  #FFD919


## 📈 Gráficos da 1ª Seção ("AVCB")

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
   - garanta que o eixo Y/escala de valores possua margem de respiro superior (`max` do eixo calculado com margem de segurança de ~10% acima do maior valor)

3. **Padrão Visual SaaS (V.tal / UI Moderna):**
   - Paleta de cores limpa: fundo #F4F5F9, cartões em #FFFFFF, cor principal: amarelo corporativo (#FFD919), cor secundária1: CINZA ESCURO 1 #514F66, cor secundária2: CINZA MÉDIO #C2C6D6, cor secundária3 CINZA ESCURO 2: #2E2D39, cor secundária4 AMARELO ESCURO ('#694A00')
   - Tipografia limpa, sem elementos poluidos
   - Código limpo, componentizado e responsivo.

### Bloco AVCB (3 Gráficos Lado a Lado)

- OBRIGATÓRIO Excluir de todos os gráficos desta seção os registros em que AVCB_IA[Status AVCB] == "Descontinuado"

1. **AVCB**:
   - Gráfico pie chart (pizza), com valor absoluto e o percentual. Os rótulos de dados precisam estar visíveis nos gráficos.
   - Itens:  Projetos Vencidos, Protocolos Válidos. NÃO conter itens AVCB_IA[Status AVCB] == "Descontinuado"
   <!-- - Ordenação em ordem **decrescente**.
2. **Status AVCB**:
   - Gráfico pie chart (pizza), com valor absoluto e o percentual. Os rótulos de dados precisam estar visíveis nos gráficos.
   - Itens: Pendente, Válido, Aguardando vistoria do CBM, Aguardando emissão de AVCB, Vistoria comunicada. NÃO conter itens AVCB_IA[Status AVCB] == "Descontinuado"
   <!-- - Ordenação em ordem **decrescente**.
3. **Detalhes dos Prédios com AVCB Pendente**:
   - Gráfico pie chart (pizza), com valor absoluto e o percentual. Os rótulos de dados precisam estar visíveis nos gráficos.
   - Tratamento de Dados: Tratar células em branco, null, NaN, undefined ou "0" como a categoria "Sem detalhamento"
   - Considere APENAS o total de prédios em que AVCB_IA[Status AVCB] == "Pendente"
   - Itens: Aguardando conclusão de PPCI, Coletando Documentos, Aguardando Adequação, Sem detalhamento (células em branco, nan ou "0" devem ser consideradas "Sem Detalhamento").
   - Os itens "Sem detalhamento" devem ser mostrados apenas para os casos em que AVCB_IA[Status AVCB] == "Pendente".
   <!-- - Ordenação em ordem **decrescente**.

### Bloco PPCI (2 Gráficos Lado a Lado)
 
 - OBRIGATÓRIO Excluir de todos os gráficos desta seção os registros em que AVCB_IA[Status AVCB] == "Descontinuado"

1. **Status do Projeto PPCI**:
   - Gráfico de barras horizontal, com valor absoluto e o percentual.
   - Agrupamento pela coluna `Status do Projeto PPCI` - Categorias esperadas : Concluído, N/A, Condomínio, Descontinuado, Pendente, Proprietário.
   - Ordenação das barras em ordem **decrescente** pela somatória de ocorrências.
2. **Status PPCI**:
   - Gráfico de barras horizontal, com valor absoluto e o percentual.
   - Agrupamento pela coluna `Status PPCI` (Descontinuado, Em análise do CBM, Comunique-se, Aprovado, N/A, Terceiro, Pendente).
   - Ordenação das barras em ordem **decrescente** pela somatória.


## 📋 2ª Seção ("Detalhamento AVCB")
- **Tabela com Cabeçalho de fonte #000000**:
  - `Prédio (ID)`, `Nome Comum`, `UF`, `Status AVCB`, `Status PPCI`, `Laudos OP`.
- **Seletor de Ordenação**: Crie o seletor de ordenação no cabeçalho: Adicione a classe de ordenação ao código JavaScript da tabela, 
que seja possível filtrar cada uma das colunas através do seletor de ordenação Crescente/Decrescente em formato de botão. 
De acordo com o tutorial do link https://webdesign.tutsplus.com/how-to-create-a-sortable-html-table-with-javascript--cms-92993t
- **Busca de Texto Aberto**: Filtro pelo nome do prédio.
- **Campo de Busca**: Campo de pesquisa por texto aberto pelo nome do prédio no canto superior direito da área da tabela.
- **Aparência**: Tabela com rolagem interna, sem paginação e sem textos na parte superior além do título e campo de busca.

<!--
## 📋 3ª Seção ("Detalhamento AVCB Descontinuado")

### Título da Seção: Prédios com AVCB Descontinuado
- **Tabela com Cabeçalho de fonte #000000**:
  - `Prédio (ID)`, `Nome Comum`, `UF`, `Status AVCB`, `Status PPCI`, `Laudos OP`.

- **Seletor de Ordenação**: Crie o seletor de ordenação no cabeçalho: Adicione a classe de ordenação ao código JavaScript da tabela, 
que seja possível filtrar cada uma das colunas através do seletor de ordenação Crescente/Decrescente em formato de botão. 
De acordo com o tutorial do link https://webdesign.tutsplus.com/how-to-create-a-sortable-html-table-with-javascript--cms-92993t
- **Busca de Texto Aberto**: Filtro pelo nome do prédio.
- **Campo de Busca**: Campo de pesquisa por texto aberto pelo nome do prédio no canto superior direito da área da tabela.
- **Aparência**: Tabela com rolagem interna, sem paginação e sem textos na parte superior além do título e campo de busca.
-->