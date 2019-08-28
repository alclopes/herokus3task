# Deploy de Aplicação Django no Heroku - TestHeroku V4

Conheça a aplicação no [Heroku](https://alclopes-S3.herokuapp.com/).

## Características básicas desta aplicação
##### 01. Projeto de duas páginas 
##### 03. Uso de Imagem Estática
##### 04. Biblioteca DeCouple para proteger as variáveis de configuração
##### 05. Uso de S3 AWS para armazenar arquivos estaticos e medias
##### 06. Gestão dos Settings de produção e desenvolvimento separados
##### 07. Gestão dos Requirements de produção e desenvolvimento separados
##### 08. Uso de signals para excluir arquivos de media no servidor quando ultrapasa o limite de três imagens
##### 09. Serviços disponíveis:
###### Página 01 - My Images 
   01. Upload de Imagem
   02. Listagem e exibição das ultimas 3 imagens oriundas de upload
   03. Limpar todas as imagens oriundas de upload do servidor
###### Página 02 - My Files
   01. Upload de Arquivo
   02. Exibição de link para download do ultimo arquivo oriundo de upload.
   03. Limpar todas os arquivos oriundos de upload do servidor

Proximos desenvolvimentos
V4-alclopes-Celery
   04. Limpar todas as imagens oriundas de upload do servidor apos 15 minutos da inserção
           
## Lembretes e cuidados importantes ao utilizar o Heroku
##### 01. Importante para não ter retrabalho é saber que a base de dados utilizada pelo Heroku é o Postgres
* O Heroku utiliza o Postgres como base de dados padrão, portanto, se estiver utilizando db.sqlite3 para desenvolvimento em sua maquina local, você dever apagar e recriar suas migrações para postgres antes de fazer o deploy no servidor.
##### 02. Lembre-se na opção grátis o Heroku não armazena seus uploads
* Imagens de origem de upload (pasta MEDIA da aplicação) não são mantidas pelo HEROKU (uma solução é usar amazon S3 para armazená-las)
* Motivos do Heroku apagar os arquivos media: o Servidor de imagens não exige complexidade podendo até ser um servidor apache e também para evitar sobrecarga de arquivos no servidor gratis e portanto a queda de sua performance a longo prazo.
* Não estou utilizando um servidor de arquivos estáticos externos neste projeto e o heroku apaga os arquivos físicos, portanto, criei uma condição para apagar os registros na base de dados referentes a estes arquivos deletados (não há regra de negócio envolvida aos registros). Em breve irei incluir outro projeto utilizando o S3.
##### 03. Importante tentar controlar o armazenamento por upload de sua aplicação 
* Como não vou controlar o conteúdo dos uploads limitei a apenas 3 imagens (media) disponíveis no servidor, 
* Também coloquei as imagens em um percentual de tamanho de 2% o que não permite a visibilidade clara da imagem na própria página.

## Algumas dicas para rodar a aplicação
 Além das dicas usuais de instalação utilizando o GIT,  seguir as dicas abaixo:
 
#### Valorizar em arquivo .env as variáveis de configuração abaixo:
 
##### 1. Para rodar a aplicação setar no arquivo .env ou .ini criado para o pacote decouple as variáveis:
            SECRET_KEY=... 
            DEBUG=True
            SETTINGS_MODULE_PATH=testheroku.settings.development
            DEBUG_DESENV=True 
            ALLOWED_HOSTS_DEV =.localhost,127.0.0.1
            
##### 2. Valorizar no servidor Heroku as variáveis de configuração abaixo:
            SECRET_KEY=... 
            DEBUG=False
            ALLOWED_HOSTS=.herokuapp.com 
            SETTINGS_MODULE_PATH=testheroku.settings.production
            DISABLE_COLLECTSTATIC=1
            DATABASE_URL=...   #Será incluida e configurada automaticamente pelo Heroku na inclusão do Resource/addon do Postgres
              
## Teste Heroku - Situação Atual do projeto
##### 1. Deploy de aplicação Django no Heroku 
=> Situação: Feito/Sucesso
##### 2. Gestão de arquivos estáticos 
=> Situação: Feito/Sucesso (mais detalhes abaixo) 
##### 3. Gestão de arquivos média 
=> Situação: Feito/Sucesso (mais detalhes abaixo)

## Branch04 - V4-Heroku-S3
##### Deploy  de aplicação em Servidor Heroku + S3 AWS
* Gerenciamento de arquivos estáticos disponibilizados em servidor remoto S3 AWS 

#### Detalhes da Situação do Projeto Teste

##### 1. Arquivos estáticos -  - Situação: OK
* Envolveu: Files/Images e CSS
* Sem pendências

##### 2. Upload de Arquivos de Mídia (media) - Situação: OK
* Envolveu imagens por upload do usuário
* Sem pendências

##### 3. Asynchronous task delete - Situação: Pendente
* Em construção

## Branch03 - V3-Heroku-S3
##### Deploy  de aplicação em Servidor Heroku + S3 AWS
* Gerenciamento de arquivos estáticos disponibilizados em servidor remoto S3 AWS 

#### Detalhes da Situação do Projeto Teste

##### 1. Arquivos estáticos -  - Situação: OK
* Envolveu: Files/Images e CSS
* Sem pendências

##### 2. Upload de Arquivos de Mídia (media) - Situação: OK
* Envolveu imagens por upload do usuário
* Sem pendências

## Branch02 - V2-Heroku-Dj-static
##### Deploy  de aplicação em Servidor Heroku
* Gerenciamento de arquivos estáticos em servidor Heroku usando biblioteca dj-static

##### Pacote: dj-static
* Promete a gerencia de arquivos estáticos no servidor Heroku
* Configuração simples

#### Detalhes da Situação do Projeto Teste

##### 1. Arquivos estáticos - Situação: Aguardando Solução
* Envolveu: Imagens e CSS
* Se Debug = False não esta servindo arquivos estáticos 
* Se Debug = True - OK

##### 2. Upload de Arquivos de Mídia (media) - Situação: OK
* Envolveu imagens por upload do usuário
* Sem pendências

## Branch01 - V1-Heroku-Whitenoise
##### Deploy  de aplicação em Servidor Heroku
* Gerenciamento de arquivos estáticos em servidor Heroku usando biblioteca Whitenose

##### Pacotes: Whitenose 4.1.2 + django_heroku 0.3.1
* Promete a gerencia de arquivos estáticos no servidor
* "WhiteNoise is not suitable for serving user-uploaded “media” files." Source:WhiteNoise

#### Detalhes da Situação do Projeto Teste

##### 1. Arquivos estáticos - Situação: Aguardando Solução
* Envolveu: Imagens e CSS
* Se Debug = False dá erro 500
* Se Debug = True - OK

##### 2. Upload de Arquivos de Mídia (media) - Situação: Aguardando Solução
* Envolveu imagens por upload do usuário
* Sem pendências
  
####  Lembretes e cuidados importantes ao utilizar o Django com WhiteNoise
* As part of deploying your application you’ll need to run ./manage.py collectstatic to put all your static files into STATIC_ROOT. (If you’re running on Heroku then this is done automatically for you.)
* You might find other third-party middleware that suggests it should be given highest priority at the top of the middleware list. Unless you understand exactly what is happening you should ignore this advice and always place WhiteNoiseMiddleware above other middleware. If you plan to have other middleware run before WhiteNoise you should be aware of the request_finished bug in Django.
