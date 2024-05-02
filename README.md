
# Back-End C317

Back-End da aplicação da disciplina C317. Feita com Django, Django REST e MongoDB


## Stack utilizada

**Framework:** Django

**Banco de Dados:** Mongo DB

**Biblioteca API:** Django Rest

**DB Driver:** Djongo


## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/C317-2024-1/C317-back.git
```

Entre no diretório do projeto

```bash
  cd C317-back/
```

Instale as dependências

Para executar o projeto é necessário o Python versão 3.x.x

As dependências do projeto estão no arquivo 

```
dependencies.txt
```

Podemos instalar todas de uma vez com os seguintes comandos:

```bash
  pip install -r dependencies.txt
```

Inicie o servidor

```bash
  python manage.py runserver 8080
```

O banco de dados da aplicação é hospedado no MongoDB Atlas então não é necessário inicia-lo localmente.

## Documentação da API

#### Registro de Usuario

```http
  POST /api/register
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `name` | `string` | **Obrigatório**. O nome do usuario no sistema |
| `email` | `string` | **Obrigatório**. O email do ususario, usado para fazer login |
| `password` | `string` | **Obrigatório**. A senha de acesso do usuario. |

Tipos de Retorno

| Data   | Status |Descrição    |
| :---------- | :--------- | :----|
| `Dados do Usuario`  | 201 | Usuario criado com sucesso! |
| `Detalhes do Erro`  | 400 | Falha ao criar o usuario |

#### Login de usuario.

```http
  POST /api/login/
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `email` | `string` | **Obrigatório**. O email do ususario, usado para fazer login |
| `password` | `string` | **Obrigatório**. A senha de acesso do usuario. |

Tipos de Retorno

| Data   | Status |Descrição    |
| :---------- | :--------- | :----|
| `Token JWT`  | 201 | Usuario Logado |
| `Detalhes do Erro`  | 401 | Usuario não autorizado |

#### Logout


```http
  POST /api/logout/
```

Não recebe nenhum parametro, apenas deleta o token JWT dos cookies.

#### Retornar informações de usuario

```http
  GET /api/user/
```

Não recebe nenhum parametro, captura o usuario via informações contidas no token JWT

Tipos de Retorno

| Data   | Tipo |Descrição    |
| :---------- | :--------- | :----|
| `HTTP Response`  | 401 | Usuario não autorizado |
| `Id`  | `integer` | Id do Usuario no banco de dados|
| `Nome`  | `string` | Nome do Usuario |
| `Email`  | `string` | Email do Usuario |

#### Enviar Menssagens

```http
  POST /api/messages/
```

Envia a mensagem para o chat e recebe uma resposta da IA.

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `message` | `string` | **Obrigatório**. Mensagem a ser respondida pela IA |

Tipos de Retorno

| Data   | Status |Descrição    |
| :---------- | :--------- | :----|
| `JSON`  | 201 | Mensagem Enviada e Salva no Banco de Dados |
| `Detalhes do Erro`  | 401 | Usuario não autorizado |
|`Detalhes do Erro`|400| Não foi possivel conectar ao banco de dados |

Formato da mensagem recebida
```JSON
{
	"message": "Hello, I am an AI",
	"date": "2024-05-02T01:03:30.818319",
	"isUserMessage": false
}
```

### Retornar todas as mensagens de um usuario

```http
  POST /api/user/messages/
```

Não recebe nenhum parametro, captura o usuario via informações contidas no token JWT

Tipos de Retorno

| Tipo | Descrição    |
|  :--------- | :----|
| `Array de mensagens`  | Um array com todas as mensagens do enviadas e recebidas pelo usuario | 

Formato das Menssagens

```JSON
[
	{
		"message": "teste message sdkndsk",
		"date": "2024-05-02T01:03:30.783000",
		"isUserMessage": true
	},
	{
		"message": "Hello, I am an AI",
		"date": "2024-05-02T01:03:30.818000",
		"isUserMessage": false
	}
]

```

## Autores

- [@Edras Simões](https://github.com/edrassimoes)
- [@Gustavo Luz](https://github.com/GustavoFLuz)
- [@Rafael Moreira](https://github.com/vonot16)
