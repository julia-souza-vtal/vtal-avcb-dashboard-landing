## 📂 Fonte dos Dados
- **Aba da Planilha**: `Laudos` da planilha `Big_Numbers_AVCB_-_planilha_IA.xlsx`

## Proporção do Painel: 

- Mantenha o cabeçalho, filtros, Cards e cabeçalho da tabela sempre visivel, independente do estado da barra de rolagem

## **Filtros do Cabeçalho**:
  - Siga estritamente a ordem dos Filtros: Regional, UF, Município, Tipo de Prédio, Responsável Legal, Prioridade
  - Posicionados na parte superior da página, abaixo do cabeçalho
  - OBRIGATÓRIO USAR Filtros com Padrão flutuante/horizontal recolhível com suporte a múltipla seleção e opção "Selecionar Todos"
  - OBRIGATÓRIO USAR Filtro [UF] e filtro [Município] com relacionamento em cascata (ao selecionar UF, exibe apenas os municípios correspondentes, seguindo o arquivo "municipios-incendio.csv")
   - As seções 'Laudos', 'Detalhamento Laudos', devem estar uma abaixo da outra, em sequência. Sem botões para intercambiar as seções.
  - NÃO colocar o total de prédios na mesma linha dos filtros
  <!-- - Colocar o total de prédios dessa página na mesma linha dos filtros, no lado extremo esquerdo, com borda elíptica e fundo em preto (#000000), texto em branco(#FAFAFA), para destaque -->

- Aba a partir dos dados da aba "Laudos" da planilha "Big Numbers AVCB - planilha IA.xlsx"
- filtros na parte superior, conforme a seguinte ordem: Regional | UF | Município | Tipo | Responsável Legal | Prioridade

## texto de observação acima dos cards

<!-- - alinhado à direita, fonte de texto escreva: "Essa aba do painel não considera os prédios com AVCB descontinuado" -->
-  alinhado à direita, fonte de texto escreva: "Atualizado em: " + data de envio da última planilha, seguindo o formato DD/MM/AAAA


### 🎴 Cards / KPIs Globais
Formatados como `XX (XX,XX%)`:

- **Total de Prédios**: Contagem de registros `total_predios_ativos`. Ícone no canto extremo esquerdo do card na cor  #FFD919

- **Total de Laudos Pendentes**: Contagem de registros `total_laudos_pendentes`. Ícone no canto extremo esquerdo do card na cor  #FFD919
 
1. **ART ELÉTRICA Pendentes**: Faça uma contagem de registros 'SIM' na coluna 'ART ELÉTRICA' (no estilo da função INDICE-CORRESP do excel, buscando o valor SIM) E a porcentagem sobre `total_predios`. Ícone no canto extremo esquerdo do Card: zap, na cor  #FFD919	

2. **ART SPDA Pendentes**: Contagem de registros 'SIM' na coluna `ART SPDA` (no estilo da função INDICE-CORRESP do excel, buscando o valor SIM) E a porcentagem sobre `total_predios`. Ícone no canto extremo esquerdo do Card: fa-bolt na cor  #FFD919	 

3. **ART GMG Pendentes**: Contagem de registros 'SIM' na coluna `ART GMG` (no estilo da função INDICE-CORRESP do excel, buscando o valor SIM) E a porcentagem sobre`total_predios`. Ícone no canto extremo esquerdo do Card: fa-charging-station  na cor  #FFD919

4. **ART TANQUES Pendentes**: Contagem de registros 'SIM' na coluna  `ART TANQUES` (no estilo da função INDICE-CORRESP do excel, buscando o valor SIM) E a porcentagem sobresobre `total_predios`.	Ícone no canto extremo esquerdo do Card: cylinder, na cor  #FFD919


## 1ª Sessão ("Laudos")
### Gráficos (a partir dos dados da aba "Laudos" da planilha "Big Numbers AVCB - planilha IA.xlsx")
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

- **Valores e Percentuais**: Exibir valores absolutos e % diretamente em cada barra.
- **Tooltips**: NÃO utilizar tooltips como forma de visualização das informações.
- **Eixos**: 
   - gráfico de barras verticais "Laudos Pendentes por Estado (UF)":   mantem eixo X e remove eixo Y
   - gráfico de barras horizontais "Laudos "ART ELÉTRICA" Pendentes":    mantem eixo Y e remove eixo X
   - gráfico de barras horizontais "Laudos "ART SPDA" Pendentes":        mantem eixo Y e remove eixo X
   - gráfico de barras horizontais "Laudos "ART GMG" Pendentes":         mantem eixo Y e remove eixo X
   - gráfico de barras horizontais "Laudos "ART TANQUES" Pendentes":     mantem eixo Y e remove eixo X

#### Linha 1:
1. Laudos Pendentes por estado: Gráfico de barras VERTICAL com Contagem de registros "SIM" da coluna "Pendências de Laudos", agrupado por estado (UF).

#### Linha 2

Gráficos lado a lado, seguindo a ordem:
1. Laudos "ART ELÉTRICA" Pendentes: Gráfico de barras horizontal com Contagem de registros "SIM", da coluna "ART ELÉTRICA", E % sobre total_predios.

2. Laudos "ART SPDA" Pendentes: Gráfico de barras horizontal com Contagem de registros "SIM", da coluna "ART SPDA", E % sobre total_predios.

3. Laudos "ART GMG" Pendentes: Gráfico de barras horizontal com Contagem de registros "SIM", da coluna "ART GMG",  E % sobre total_predios.

4. Laudos "ART TANQUES" Pendentes: Gráfico de barras horizontal com Contagem de registros "SIM", da colunas "ART TANQUES" E % sobre total_predios.


## 2ª Seção ("Detalhamento Laudos") <!-- Laudos[Pendências de Laudos (Sim / Não / N/A)] == 'Não' OU 'N/A' OU '0' -->

- **Tabela com Cabeçalho de fonte #000000**:
Prédio | Nome | Regional | UF | Município | Pendências de Laudos |	ART ELÉTRICA |	ART SPDA	| ART GMG	| ART TANQUES

- **Seletor de Ordenação**: Crie o seletor de ordenação no cabeçalho: Adicione a classe de ordenação ao código JavaScript da tabela, 
que seja possível filtrar cada uma das colunas através do seletor de ordenação Crescente/Decrescente em formato de botão. 
De acordo com o tutorial do link https://webdesign.tutsplus.com/how-to-create-a-sortable-html-table-with-javascript--cms-92993t
- **Busca de Texto Aberto**: Filtro pelo nome do prédio.
- **Campo de Busca**: Campo de pesquisa por texto aberto pelo nome do prédio no canto superior direito da área da tabela.
- **Aparência**: Tabela com rolagem interna, sem paginação e sem textos na parte superior além do título e campo de busca.

<!--
## 3ª Seção ("Detalhamento Laudos Pendentes")

- A TABELA DEVE CONTER APENAS OS DADOS DE Laudos[Pendências de Laudos (Sim / Não / N/A)] == 'SIM'

- **Tabela com Cabeçalho de fonte #000000**:
Prédio | Nome | Regional | UF | Município | Pendências de Laudos |	ART ELÉTRICA |	ART SPDA	| ART GMG	| ART TANQUES

- **Seletor de Ordenação**: Crie o seletor de ordenação no cabeçalho: Adicione a classe de ordenação ao código JavaScript da tabela, 
que seja possível filtrar cada uma das colunas através do seletor de ordenação Crescente/Decrescente em formato de botão. 
De acordo com o tutorial do link https://webdesign.tutsplus.com/how-to-create-a-sortable-html-table-with-javascript--cms-92993t
- **Busca de Texto Aberto**: Filtro pelo nome do prédio.
- **Campo de Busca**: Campo de pesquisa por texto aberto pelo nome do prédio no canto superior direito da área da tabela.
- **Aparência**: Tabela com rolagem interna, sem paginação e sem textos na parte superior além do título e campo de busca.

-->