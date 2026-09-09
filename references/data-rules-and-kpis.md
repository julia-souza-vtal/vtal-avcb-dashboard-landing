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

- **Base de Cálculo (`total_predios`)**:
  - Variável que armazena a contagem total de prédios na base filtrada.
- **Fórmula do Percentual**:
  $$\text{Percentual} = \left(\frac{\text{Quantidade}}{\text{total\_predios}}\right) \times 100$$

  - Todos os percentuais devem ser calculados dinamicamente e arredondados para **2 casas decimais**.
  - Proibido hardcoding ou valores fixados manualmente.
  - Desconsidere dos cálculos das abas (Exceto a aba "Detalhamento AVCB Descontinuado"), todos os prédios com coluna AVCB_IA[AVCB] == "Descontinuado"
  - Os cálculos da aba "Detalhamento AVCB Descontinuado", deve considerar todos os prédios com coluna AVCB_IA[AVCB] == "Descontinuado"

### Aba 01-AVCB

- Utilize ícones que estejam de acordo com o contexto do painel, da aba da planilha e com o item do respectivo card. Ícone no canto extremo esquerdo do card.

total_predios = distinctcount(AVCB_IA[Prédio])

total_predios_pendentes = prédios em que AVCB_IA[Status AVCB] == "Pendente"

total_predios_descontinuados = prédios em que AVCB_IA[AVCB] == "Descontinuados"

total_predios_ativos = total_predios - total_predios_descontinuados


#### **Total de Prédios**: Contagem de registros  `total_predios`. Ícone no canto extremo esquerdo do card: fa-check-circle  na cor  #FFD919


#### **AVCBs Válidos**: Contagem de registros válidos na coluna `AVCB` + % sobre `total_predios_ativos`. Ícone no canto extremo esquerdo do card: fa-check-circle  na cor  #FFD919

#### **AVCBs Vencidos**: Contagem de registros do tipo "Vencido" na coluna `AVCB` + % sobre `total_predios_ativos`. Ícone no canto extremo esquerdo do card:  fa-exclamation-circle na cor  #FFD919

#### **Status do Projeto PPCI Concluído**: Contagem de registros "Concluído" na coluna `Status do Projeto PPCI` + % sobre `total_predios_ativos`.Ícone no canto extremo esquerdo do card: fa-file-signature na cor  #FFD919

#### **Status PPCI Aprovado**: Contagem de registros "Aprovado" na coluna `Status PPCI` + % sobre `total_predios_ativos`.Ícone no canto extremo esquerdo do card: fa-file-signature na cor  #FFD919

### Aba 02-Prevenção-a-Incêndio

####  Card **Total Prédios**: Contagem de registros  `total_predios`. Ícone no canto extremo esquerdo do card: fa-check-circle  na cor #FFD919

####  Card **Brigada**: Contagem de registros "12 Horas", "24 Horas", "12H - noturno", "12H - diurno" na coluna `Brigada Civil V.tal 2026` + % sobre `total_predios`. Ícone no canto extremo esquerdo do Card: user-shield na cor #FFD919

#### **SDAI válido**: Contagem de registros "SIM" na coluna `SDAI` + % sobre `total_predios`. Ícone no canto extremo esquerdo do Card: alarm-smoke  na cor  #FFD919

#### **SDAI/SDACI sem falhas**: Contagem de registros "SIM" na coluna `Operacional sem falhas` + % sobre `total_predios`. Ícone no canto extremo esquerdo do Card: fa-check-circle na cor  #FFD919

#### **SDAI/SDACI com falhas**: Contagem de registros "Operacional com falhas - Alto", "Inoperante",
"Operacional com falhas - Médio", "Operacional com falhas - Baixo",
"Operacional com falhas - Muito alto" na coluna `SDAI/SDACI operante` + % sobre `total_predios`. Ícone no canto extremo esquerdo do Card: fa-exclamation-circle na cor  #FFD919

#### **FM200 válido**: Contagem de registros do tipo "SIM" na coluna `FM200` + % sobre `total_predios`. Ícone no canto extremo esquerdo do Card: cylinder na cor  #FFD919

#### **Extintor presente**: Contagem de registros "SIM" na coluna `Extintor` + % sobre `total_predios`. Ícone no canto extremo esquerdo do Card: fire-extinguisher na cor  #FFD919

### Aba 03-Laudos

####  Card **Total Prédios**: Contagem de registros  `total_predios`. Ícone no canto extremo esquerdo do card: fa-check-circle  na cor #FFD919

####  Card **Total de Laudos Pendentes**: Contagem de registros  `total_laudos_pendentes`. Ícone no canto extremo esquerdo do card: fa-exclamation-circle  na cor #FFD919

#### **ART Elétrica Pendentes**: Faça uma contagem de registros 'SIM' na coluna 'ART ELÉTRICA' (no estilo da função INDICE-CORRESP do excel, buscando o valor SIM) E a porcentagem sobre `total_predios`. Ícone no canto extremo esquerdo do Card: zap, na cor  #FFD919	

#### **ART SPDA Pendentes**: Contagem de registros 'SIM' na coluna `ART SPDA` (no estilo da função INDICE-CORRESP do excel, buscando o valor SIM) E a porcentagem sobre `total_predios`. Ícone no canto extremo esquerdo do Card: fa-bolt na cor  #FFD919	 

#### **ART GMG Pendentes**: Contagem de registros 'SIM' na coluna `ART GMG` (no estilo da função INDICE-CORRESP do excel, buscando o valor SIM) E a porcentagem sobre`total_predios`. Ícone no canto extremo esquerdo do Card: fa-charging-station  na cor  #FFD919

#### **ART Tanques Pendentes**: Contagem de registros 'SIM' na coluna  `ART TANQUES` (no estilo da função INDICE-CORRESP do excel, buscando o valor SIM) E a porcentagem sobresobre `total_predios`.	Ícone no canto extremo esquerdo do Card: cylinder, na cor  #FFD919

### Aba 04-Adequações

####  Card **Total Prédios**: Contagem de registros  `total_predios`. Ícone no canto extremo esquerdo do card: fa-check-circle  na cor #FFD919

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