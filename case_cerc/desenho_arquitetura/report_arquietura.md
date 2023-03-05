
## - Ingestão

Dentro da camada de ingestão será usada, para os bancos de dados relacionais, o Debezium, que enviará as mudanças dos bancos para o Kafka. Para dados de logs e mensageria, será conectada diretamente ao Apache Kafka com as APIs.

## - Armazenamento

Para o armazenamento, será separado em 2 camadas: bronze (em Armazenamento) e silver (em Processamento). Aqui será utilizado o Google Cloud Storage.
Junto a isso, será utilizado também o Delta Lake para adicionar uma camada mais inteligente de metadados, para governança e manutenção da qualidade de dados, além de trazer o melhor do data lake e do data warehouse, unificando tudo em um único local, o que facilita o acesso de dados para projetos de Data Science.

* A camada bronze será alimentada pelo Kafka, sendo ela uma camada "raw", ou seja, sem processamento algum, essa camada é necessária para que não se perca nenhum dado no processo;
    * Com isso, os dados serão conectados ao Delta Lake com o Delta Lake API;

## - Processamento e Treinamento de Modelos

### - Processamento dos Dados

* A camada silver será o processamento dos dados, utilizando o Apache Spark, com o propósito de disponibilizar dados de alta qualidade para diversos tipos de aplicação, como modelos de machine learning e ter tabelas disponíveis para uso posterior do time de business intelligence;

### - Treinamento de modelos

A camada silver do Delta Lake permite uso de MLOps pelo time de Data Science, já que o Delta Lake foi desenhado para funcionar muito bem com frameworks de machine learning.

## - Data Governance e Data Quality

Governança - É importante frisar que com o Delta Lake Metadata API se torna mais fácil definir e categorizar as tabelas do framework, além de facilitar o acesso ao metadado que fica armazenado em tabelas do próprio Delta Lake.
Qualidade - Com o Delta Lake é possível automatizar a checagem de schema, e a própria limpeza do dado, como retirar duplicatas, campos vazios ou qualquer outro problema com a qualidade dos dados.
- Data Analytics e Aplicações
Trino para analytics e criações de relatórios para a empresa.

Aplicações da empresa utilizando Python e Java direto do Delta Lake, com o metadado e logs das aplicações sendo adicionadas a tabelas, utilizando, por exemplo, pods Kubernetes para execução.

## - Visualização
Grafana, recebendo novas tabelas de analytics e data science do Trino, conectando-as ao Grafana para visualização.

## - Monitoramento e Alertas
No Grafana, com o metadado das aplicações, é possível observar o uso de CPU e memória para possíveis melhorias, conseguindo um monitoramento eficiente.
Além disso, é possível configurar alertas baseados em condições dos dados, como isso pode notificar o time de Data Engineering quando esses eventos ou anomalias acontecem.

 

