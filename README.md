Inicialização do projeto:

O projeto consiste no desenvolvimento de uma aplicação que pudesse armazenar informações de um arquivo CNAB, um tipo de arquivo comum em bancos.

Após o fazer o clone dos dois repositorios na sua maquina, faça os seguinte comandos nesse repositorio
    Instalando as techs
    pip install requirements.txt

    Para iniciar seu ambiente virtual
    .\venv\Scripts\activate

    Para iniciar a api localmente:
    python manage.py runserver


Techs usadas no front:

    Djnago RestFramework;
    Python:
    Pandas;
    Django-cors-headers;

Porta: 
    A api por padrão roda na http://127.0.0.1:8000/

Estrutura de pastas:

Cada tabela esta estrutura em uma pasta diferente, sendo a project a pasta inicial do projeto e a dados a tabela que de fato armazena os valores, dentro das pastas temos os arquivos de views, serializer, urls e models.

