# Projeto Final da Segunda Unidade de POS

## Grupo
- Anael
- Thaisy

## Instalação

- Crie um ambiente virtual

```bash
python -m venv .venv
```

- Ative o ambiente virtual

*powershell*
```powershell
.venv/Scripts/activate
```

*bash*
```bash
source .venv/Scripts/active
```

- Instale as dependências do projeto

```bash
pip install -r requirements.txt
```

- Crie um arquivo `.env` e adicione as informações
```
SECRET_KEY='development'
CLIENT_ID=
CLIENT_SECRET=
```

- Rode o servidor

```bash
flask --app app.py --debug run
```
