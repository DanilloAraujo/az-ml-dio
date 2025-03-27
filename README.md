# Atividades Realizadas com AutoML e Pipeline Designer no Azure ML

## AutoML (Auto Machine Learning)

O **AutoML** no Azure ML automatiza várias etapas do fluxo de trabalho de machine learning. Aqui estão as atividades realizadas:

### 1. Importação e Preparação de Dados
- Carregar conjuntos de dados de diferentes fontes, como arquivos CSV, bancos de dados SQL ou serviços do Azure (Azure Blob Storage, Azure Data Lake, etc.).
- Limpeza e pré-processamento dos dados, incluindo tratamento de valores ausentes, normalização, transformação de variáveis categóricas, etc.

### 2. Divisão de Dados
- O AutoML divide automaticamente os dados em conjuntos de treinamento, validação e teste para garantir uma boa generalização do modelo.

### 3. Seleção Automática de Algoritmos
- O AutoML avalia diferentes algoritmos e seleciona automaticamente o mais adequado para o tipo de problema (classificação, regressão, detecção de anomalias, etc.).

### 4. Ajuste Automático de Hiperparâmetros
- O AutoML ajusta os hiperparâmetros automaticamente para melhorar o desempenho do modelo, utilizando técnicas como **Grid Search** e **Bayesian Optimization**.

### 5. Treinamento e Avaliação do Modelo
- O AutoML treina múltiplos modelos e avalia seu desempenho com métricas específicas (precisão, F1-score, AUC, etc.).
- O melhor modelo é selecionado com base no desempenho nas métricas de avaliação.

### 6. Implantação do Modelo
- O modelo final pode ser implantado como um serviço de predição no Azure ML, expondo-o como uma API REST para predições em tempo real.

### 7. Monitoramento e Manutenção
- Após a implantação, o AutoML permite monitorar o desempenho do modelo em produção e realizar ajustes ou re-treinamento quando necessário.

---

## Pipeline Designer

O **Pipeline Designer** no Azure ML oferece uma interface visual para a criação, automação e execução de fluxos de trabalho de machine learning. As atividades realizadas incluem:

### 1. Criação do Pipeline
- O Pipeline Designer permite criar pipelines visualmente, arrastando e soltando módulos para representar diferentes etapas do fluxo de trabalho, como importação de dados, pré-processamento, treinamento, avaliação e implantação.

### 2. Importação de Dados
- Carregar dados de diversas fontes (arquivos, bancos de dados, serviços de armazenamento na nuvem) utilizando módulos específicos.

### 3. Pré-processamento de Dados
- Incluir módulos para limpar e transformar os dados, como normalização, codificação de variáveis categóricas, imputação de valores ausentes e divisão dos dados em conjuntos de treinamento, validação e teste.

### 4. Treinamento de Modelos
- Adicionar módulos para treinar modelos com diferentes algoritmos de machine learning (como árvores de decisão, redes neurais, etc.) ou integrar o AutoML para automação no treinamento.

### 5. Avaliação de Modelos
- Incluir módulos de avaliação para medir a performance do modelo com métricas como precisão, recall, F1-score, AUC, etc.
- Comparar múltiplos modelos e escolher o melhor.

### 6. Ajuste de Hiperparâmetros
- Utilizar módulos de ajuste de hiperparâmetros (como **HyperDrive**) para otimizar os parâmetros dos modelos e melhorar seu desempenho.

### 7. Implantação do Modelo
- Adicionar módulos para implantar o modelo treinado como um serviço de predição, disponibilizando-o para acesso via API REST.

### 8. Automação e Execução de Pipelines
- Configurar pipelines para execução manual ou automática com base em triggers, como a chegada de novos dados.
- Agendar execuções regulares para re-treinamento de modelos ou implementação de novos dados.

### 9. Monitoramento e Gestão de Pipelines
- Monitorar o status da execução de pipelines, visualizar logs de execução e diagnosticar problemas em caso de falhas.
- Realizar versionamento dos pipelines, garantindo rastreabilidade e reutilização de versões anteriores.

---

## Conclusão

O **AutoML** e o **Pipeline Designer** são ferramentas poderosas no Azure ML que ajudam a automatizar e simplificar o processo de desenvolvimento de modelos de machine learning. O **AutoML** facilita a construção de modelos automaticamente, enquanto o **Pipeline Designer** oferece uma maneira visual e escalável de criar fluxos de trabalho completos de ML. Ambos são recursos essenciais para quem deseja otimizar a criação, treinamento e implantação de modelos no Azure ML.
