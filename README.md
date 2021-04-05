

![Badge](https://img.shields.io/static/v1?label=DjangoRestFramework&message=v3.1.1.1&color=blue&style=<STYLE>&logo=ghost) 


# CurrencyBotAPI
API simples para consumo de dados com angular 9


## Pré-Requisitos📃
   * Python3
## Instalação💻
   
   * Primeiramente baixe o arquivo ou clone com o comando git clone
   
~~~
 git clone https://github.com/lowliet64/CurrencyBotApi.git
~~~

  * Em seguida entre no diretório da aplicação
  
  ~~~
    cd CurrencyBotApi
  ~~~

   * Crie um ambiente virtual para instalacao das dependencias:
 ~~~
    pip3 -m venv .venv
 ~~~~
   
  * Em seguida ative o ambiente virtual com :

 ~~~
    source .venv/bin/activate
 ~~~~
   * Dentro da pasta instale as dependencias executando :
   
  ~~~
    pip3 install -r requirements.txt
  ~~~~
 * rode as migrations com 
   
  ~~~
    python3 manage.py migrate
  ~~~~

  * Por último inicie o serviço com o comando :
  ~~~
   python3 manage.py runserver
  ~~~

O Serviço estará disponivel em http://127.0.0.1:8080

## Utilizando com Docker 🐳

Para executar o container com o docker execute o comando:
~~~
   docker-compose up
~~~
Em seguida , abra outro terminal e aplique as migrations com o comando:
~~~
   docker-compose run web python manage.py migrate
~~~

O Serviço estará disponivel em http://127.0.0.1:8080
