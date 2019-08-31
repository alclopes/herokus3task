# Deploy de Aplicação Django no Heroku - Projeto Heroku 04 - S3Tasks
* Aplicação envolvendo arquivos estáticos e medias utilizando: armazenador S3 AWS, Celery e Redis. Aplicação rodando no Heroku.   

Conheça esta aplicação no [Heroku](https://herokus3task.herokuapp.com).

## Características básicas desta aplicação
##### 01. Projeto de duas páginas 
##### 02. Uso de Imagem Estática
##### 03. Opção de Upload de Mídia (media - POST de imagem)
##### 04. Biblioteca DeCouple para proteger as variáveis de configuração
##### 05. Uso de Celery, Redis no S3 AWS para gestão de arquivos medias
##### 06. Gestão dos Settings de produção e desenvolvimento separados
##### 07. Gestão dos Requirements de produção e desenvolvimento separados
##### 08. Uso de signals para excluir arquivos de media no servidor quando ultrapasa o limite de três imagens
##### 09. Validação da disponibilidade de arquivos de media no servidor e posterior exclusão da referência em BD na ausência do arquivo.
##### 10. Serviços disponíveis:
###### Página 01 - My Images 
   01. Upload e armazenamento no servidor de Imagens
   02. Listagem e exibição das ultimas 3 imagens oriundas de upload
   03. Exclusão de todas as imagens oriundas de upload no servidor
   04. Serviço assincrono de exclusão de imagens após algum tempo de sua inserção
###### Página 02 - My Files
   01. Upload e armazenamento no servidor de Arquivos
   02. Exibição de link para download do ultimo arquivo oriundo de upload.
   03. Exclusão de todas os arquivos oriundos de upload do servidor
   04. Serviço assincrono de exclusão de arquivos após algum tempo de sua inserção

## Proximos desenvolvimentos
#### P5-Docker
* Usando Docker criaremos um container e montaremos o ambiente de projeto completo para migrar para o S3.
           
## Lembretes e cuidados importantes ao utilizar o Heroku
##### 01. Importante para não ter retrabalho é saber que a base de dados padrão utilizada pelo Heroku é o Postgres
* O Heroku utiliza o Postgres como base de dados padrão, portanto, se estiver utilizando db.sqlite3 ou outro banco de dados para desenvolvimento em sua maquina local, você dever verificar a aderência e se necessário recriar suas migrações antes de fazer o deploy no servidor.
##### 02. Lembre-se na opção grátis o Heroku não armazena uploads feitos pelo usuário a longo prazo.
* Imagens de origem de upload (pasta MEDIA da aplicação) não são mantidas pelo HEROKU (uma solução é usar amazon S3 para armazená-las, se necessário veja também o projeto 3)
* Motivos do Heroku apagar os arquivos media: Um servidor de imagens não exige complexidade podendo até ser um servidor apache, e também para evitar sobrecarga de arquivos no servidor gratis e portanto a queda de sua performance a longo prazo.
* Não estou utilizando um servidor de arquivos estáticos externos neste projeto e o heroku apaga os arquivos físicos, portanto, criei uma condição para apagar os registros da base de dados referentes a estes arquivos deletados (não há regra de negócio envolvida aos registros).
##### 03. Importante tentar controlar o conteúdo do armazenamento por upload na aplicação 
* Como não vou controlar o conteúdo dos uploads pelos usuários limitei a visualização de apenas até 3 imagens (media) disponíveis no servidor, 
* Coloquei as imagens em percentual de tamanho pequeno para dificultar sua visibilidade imediata e a distância.

## Algumas dicas para rodar a aplicação
 Além das dicas usuais de instalação utilizando o GIT, você devee seguir as dicas abaixo:
 
#### Valorizar em arquivo .env as variáveis de configuração abaixo:
 
##### 1. Para rodar a aplicação criar um arquivo .env criado para o pacote decouple.
            Usar como base as variáveis presentes no arquivo .env.var
            
##### 2. Valorizar Config Vars no servidor Heroku as variáveis de configuração abaixo:
            DEBUG=False
            SECRET_KEY=''
            SETTINGS_MODULE_PATH=testheroku.settings.production
            ALLOWED_HOSTS=.herokuapp.com 
            DATABASE_URL="Automatic" #Será incluida e configurada automaticamente pelo Heroku na inclusão do Resource/addon do Postgres
            DISABLE_COLLECTSTATIC=1
            USE_S3=True
            AWS_ACCESS_KEY_ID=
            AWS_SECRET_ACCESS_KEY=
            AWS_STORAGE_BUCKET_NAME=
            REDIS_URL="Automatic" #Será incluida e configurada automaticamente pelo Heroku na inclusão do Resource/addon Redis Heroku
                          
## Situação Atual do projeto
##### 1. Deploy de aplicação Django no Heroku 
=> Situação: Feito/Sucesso
##### 2. Gestão de arquivos estáticos 
=> Situação: Feito/Sucesso (mais detalhes abaixo) 
##### 3. Gestão de arquivos média 
=> Situação: Feito/Sucesso (mais detalhes abaixo)

## Detalhes da Situação do Projeto

##### 1. Arquivos estáticos - Situação: OK
* Envolveu: Files/Images e CSS
* Sem pendências

##### 2. Upload de Arquivos de Mídia (media) - Situação: OK
* Envolveu imagens por upload do usuário
* Sem pendências

##### 3. Asynchronous task delete - Situação: OK
* Envolveu Celery e Redis para exclusão dos registros em base de dados e arquivos físicos.
* Sem pendências