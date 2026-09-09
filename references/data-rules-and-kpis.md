# Regras de Negócio, Cálculo e Estrutura de Dados - AVCB V.tal

## 📂 Fonte dos Dados
- **Aba da Planilha**: `AVCB IA` da planilha `Big_Numbers_AVCB_-_planilha_IA.xlsx`
- **Colunas Obrigatórias**:
  - `AVCB`
  - `Status do Projeto PPCI`
  - `Status PPCI`
  - `Status AVCB`
  - `Detalhes AVCB`
  - `Validade AVCB`
  - `UF`
  - `Município`
  - `Tipo de Prédio`
  - `Resp. Legal`
  - `Prioridade`


## 🔢 Regras Gerais de Cálculo
<!--
- **Base de Cálculo (`total_predios`)**:
  - Variável que armazena a contagem total de prédios na base filtrada.
- **Fórmula do Percentual**:
  $$\text{Percentual} = \left(\frac{\text{Quantidade}}{\text{total\_predios}}\right) \times 100$$
-->
  - Todos os percentuais devem ser calculados dinamicamente e arredondados para **2 casas decimais**.
  - Proibido hardcoding ou valores fixados manualmente.
  - Desconsidere dos cálculos das abas (Exceto a aba "Detalhamento AVCB Descontinuado"), todos os prédios com coluna AVCB_IA[AVCB] == "Descontinuado"
  - Os cálculos da aba "Detalhamento AVCB Descontinuado", deve considerar todos os prédios com coluna AVCB_IA[AVCB] == "Descontinuado"

### Aba 09-Adequações
####  Card Sistemas de Combate a Incêndio : 
Implemente o cálculo do indicador de **Percentual de AVCB Válidos** considerando as seguintes especificações:

 1. **Denominador - Base do Universo Considerado (`total_adequacoes`):**
 * Contabilize o total de registros da coluna `"AVCB"` da tabela/aba `Adequações revisada` cujo valor seja exatamente igual a **`"Sistemas de Combate a Incêndio"`** (ignorando os demais status na base).
  
  * total_adequacoes_sistemas = SUM(Adequações_revisada["Categoria"] == "Sistemas de Combate a Incêndio")

 
 2. **Numerador (`adequacoes_sistemas`):**
 * Contabilize o total de registros da coluna `"AVCB"` da tabela/aba `AVCB_IA` cujo valor seja exatamente igual a **`"VÁLIDO"`**.
  
  * adequacoes_sistemas = SUM(Adequações_revisada["Categoria"] == "Sistemas de Combate a Incêndio")
 
 
 3. **Fórmula de Cálculo:**
 
  * Valor Absoluto = total_adequacoes_sistemas
  * Percentual = (adequacoes_sistemas / total_adequacoes_sistemas) * 100

####  Card Adequação Civil : 
Implemente o cálculo do indicador de **Percentual de AVCB Válidos** considerando as seguintes especificações:

 1. **Denominador - Base do Universo Considerado (`total_adequacoes`):**
 * Contabilize o total de registros da coluna `"AVCB"` da tabela/aba `Adequações revisada` cujo valor seja exatamente igual a **`"Sistemas de Combate a Incêndio"`** (ignorando os demais status na base).
  
  * total_adequacoes = SUM(Adequações_revisada["Categoria"] == "Sistemas de Combate a Incêndio")

 
 2. **Numerador (`adequacoes_sistemas`):**
 * Contabilize o total de registros da coluna `"AVCB"` da tabela/aba `AVCB_IA` cujo valor seja exatamente igual a **`"VÁLIDO"`**.
  
  * adequacoes_sistemas = SUM(Adequações_revisada["Categoria"] == "Sistemas de Combate a Incêndio")
 
 
 3. **Fórmula de Cálculo:**
 
  * Percentual = (adequacoes_sistemas / total_adequacoes) * 100
<!--
### Aba 01 - AVCB
  ####  Card AVCBs Válidos : 
Implemente o cálculo do indicador de **Percentual de AVCB Válidos** considerando as seguintes especificações:

 1. **Denominador - Base do Universo Considerado (`total_AVCB`):**
 * Contabilize o total de registros da coluna `"AVCB"` da tabela/aba `AVCB_IA` cujo valor seja exatamente igual a **`"VÁLIDO"`** OU **`"VENCIDO"`** (ignorando os demais status na base).
  
  * total_AVCB = AVCB_IA["AVCB"] == "VÁLIDO" OU AVCB_IA["AVCB"] == "VENCIDO"
 
 
 2. **Numerador (`AVCB_vencido`):**
 * Contabilize o total de registros da coluna `"AVCB"` da tabela/aba `AVCB_IA` cujo valor seja exatamente igual a **`"VÁLIDO"`**.
  
  * AVCB_valido =  AVCB_IA["AVCB"] == "VÁLIDO"
 
 
 3. **Fórmula de Cálculo:**
 
 $$\text{Percentual} = \left( \frac{\text{AVCB\_valido}}{\text{total\_AVCB}} \right) \times 100$$



 ####  Card AVCB Vencido**
 Implemente o cálculo do indicador de **Percentual de AVCB Vencido** considerando as seguintes especificações:

 1. **Denominador - Base do Universo Considerado (`total_AVCB`):**
 * Contabilize o total de registros da coluna `"AVCB"` da tabela/aba `AVCB_IA` cujo valor seja exatamente igual a **`"VÁLIDO"`** OU **`"VENCIDO"`** (ignorando os demais status na base).
  
  * total_AVCB = AVCB_IA["AVCB"] == "VÁLIDO" OU AVCB_IA["AVCB"] == "VENCIDO"
 
 
 2. **Numerador (`AVCB_vencido`):**
 * Contabilize o total de registros da coluna `"AVCB"` da tabela/aba `AVCB_IA` cujo valor seja exatamente igual a **`"VENCIDO"`**.
  
  * AVCB_vencido =  AVCB_IA["AVCB"] == "VENCIDO"
 
 
 3. **Fórmula de Cálculo:**
 
 $$\text{Percentual} = \left( \frac{\text{AVCB\_vencido}}{\text{total\_AVCB}} \right) \times 100$$


  #### Card Projeto PPCI Concluído : 
  Considerar no cálculo 
  
      total_AVCB = AVCB_IA["AVCB"] == "VÁLIDO" OU AVCB_IA["AVCB"] == "VENCIDO" 

      AVCB_vencido =  AVCB_IA["AVCB"] == "VENCIDO" 

  $$\text{Percentual} = \left(\frac{\text{AVCB_vencido}}{\text{total_AVCB}}\right) \times 100$$

### Aba 02 - Detalhamento AVCB
  - Card AVCBs Vencidos : Considerar no cálculo 
  
  total_AVCB = AVCB_IA["AVCB"] == "VÁLIDO" OU AVCB_IA["AVCB"] == "VENCIDO" 

  AVCB_vencido =  AVCB_IA["AVCB"] == "VENCIDO" 

    $$\text{Percentual} = \left(\frac{\text{AVCB_vencido}}{\text{total_AVCB}}\right) \times 100$$

### Aba 03 - Prevenção a Incêndio

### Aba 04 - Detalhamento PI

### Aba 05 - Detalhamento PI

### Aba 06 - Detalhamento Laudos

-->