<h1 align="center"> Projeto Consultas MED API </h1>

<h2 align="center">📷 Prévia <h2>

![proj_MED-gif-maker](https://github.com/pedro-hnrq/Proj_Med_API/assets/74242717/dfa82085-b1a0-48b4-be34-e90dcabc4d23)


<h3>🎯 Objetivo</h3>

<h5 align="justify">Este projeto Projeto Consultas MED API, tem como objetivo atender ao um teste, utilizando o Django REST Framework - DRF. A API permite o gerenciamento do cadastro de médicos e das consultas agendadas para um determinado paciente.</h5>

<h4>Funcionalidade</h4>

<ul>
<h5 align="justify"><li>Autenticação de usuários: é possível realizar o criação de novo usuário ou gerar um token de autenticação.</li></h5>
<h5 align="justify"><li>CRUD (Criar, Editar, Listar e Excluir): os usuários autenticados têm permissão para realizar todas as operações de CRUD nos médicos e consultas.</li></h5>
<h5 align="justify"><li>Leitura de dados: usuários não autenticados têm permissão apenas para leitura de dados, sem a possibilidade de fazer alterações.</li></h5>
</ul>

<h4>Endpoints Disponíveis</h4>
<ul>
<h5><li>Versão 1 da API: http://localhost:8000/api/v1/</li></h5>
<h5><li>Versão 2 da API: http://localhost:8000/api/v2/</li></h5>
</ul>

<h4>Métodos HTTP suportados</h4>
<ul>
<h5><li>GET: Recuperar informações de medicos ou consultas e exibir.</li></h5>
<h5><li>POST: Criar um novo medico ou consulta.</li></h5>
<h5><li>PUT: Atualizar pelo ID, as informações de um medico ou de uma consulta existente .</li></h5>
<h5><li>PATCH: Atualizar pelo ID, só uma parte que deseja do cadastro informado.</li></h5>
<h5><li>DELETE: Excluir um medico ou consulta existente pelo o ID.</li></h5>
</ul>

<h4> 🚀 Como executar </h4>

#### 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Python (versão 3.10.X)
- Django (versão 4.1.X)
- Django REST Framework (versão 3.14.X)
- GIT (versão 2.X.X)

#### 🛠️ Instalação

  
<ol>
<h5><li>Essas configurações é para máquina com Sistema Operacional LINUX, já tendo o GIT e Python instalado. Ressaltabdo, tem que ter noções de django.</li></h5>
<h5><li>Clone este repositório em sua máquina utilizando o seguinte comando no terminal: 
 
```
git clone git@github.com:pedro-hnrq/Proj_Med_API.git
```  
</li></h5>   
 <h5><li>Acesse ao diretório, na pasta Proj_Med_API.
  
```
cd Proj_Med_API
``` 
 </li></h5>

<h5><li>execute os comandos abaixo para criar arquivo de variáveis de ambiente a partir de exemplos. (Lembre-se de modificá-los)

```bash
cp env .env
```
</li></h5>

 <h5 align="justify"><li>Verifique se na sua máquina tenha o Python instalado, se já estiver crie ambiente virtual e logo em seguida ative. </li></h5>
  
<h5><li>Instale as dependências do projeto através do arquivo requirements.txt: 
  
```
pip install -r requirements.txt
```
</li></h5>

<h5><li>Execute as makemigrations e as migrações do banco de dados:

```
python3 manage.py makemigrations
```

```
python3 manage.py migrate
```
</li></h5>  

<h5><li>Crie um superusuário para acessar a área administrativa:
  
```
python3 manage.py createsuperuser
```
</li></h5>  

<h5><li>Execute servidor:  
  
```
python3 manage.py runserver
```
</li></h5>  
<h5><li>Acesse o endereço http://localhost:8000/admin e faça login com as credenciais do superusuário criado anteriormente.</li></h5>

<h5><li>Para acessar a API, utilize o endereço http://localhost:8000/api/v1/ para a versão 1 da API e http://localhost:8000/api/v2/ para a versão 2 da API. As rotas disponíveis podem ser encontradas nos arquivos med_cons/urls.py e agendamento/urls.py.</li></h5> 
  
<h5><li>Observação: usei o IDE do Visual Studio Code, juntamente com a extensão que instalei na IDE, chamado Thunder Client para realiza as requisição HTTP (GET, POST, PUT, PATCH, DELETE e Token).</li></h5>
</ol>

