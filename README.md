# TranslateSpeakers
Uma ferramenta de tradução de textos entre vários idiomas, desenvolvida em Python com o framework `Flask` e `MongoDB` para o  banco de dados. Esta aplicação Server Side utiliza uma arquitetura em camadas *MVC* para fornecer uma experiência de tradução intuitiva e eficiente.

## ⚙️ Funcionalidades
* Tradução de textos para mais de 130 idiomas diferentes.
* Implementação de uma API RESTful para integração com outras aplicações.
* Integração com um banco de dados não relacional MongoDB para armazenamento de configurações e histórico de traduções.
* Desenvolvimento de páginas web Server Side para interação com o usuário.

## 💻 Tecnologias Utilizadas
* Python
* Flask
* MongoDB
* Docker
* Pymongo
* Waitress

### Como Executar
1️⃣ Crie o ambiente virtual:
```
python3 -m venv .venv && source .venv/bin/activate
```
2️⃣ Instale as dependências:
```
python3 -m pip install -r dev-requirements.txt
```
3️⃣ Inicializando com docker:
```
docker compose up translate
```
🎲 Popule o banco de dados:
```
docker compose exec -it translate python3 src/run_seeds.py
```
