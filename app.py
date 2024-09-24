from flask import Flask, redirect, url_for, session, request, render_template
from authlib.integrations.flask_client import OAuth
from decouple import config


app = Flask(__name__)
app.debug = True
app.secret_key = config("SECRET_KEY")
oauth = OAuth(app)

oauth.register(
    name='suap',
    client_id=config("CLIENT_ID"),
    client_secret=config("CLIENT_SECRET"),
    api_base_url='https://suap.ifrn.edu.br/api/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://suap.ifrn.edu.br/o/token/',
    authorize_url='https://suap.ifrn.edu.br/o/authorize/',
    fetch_token=lambda: session.get('suap_token')
)


class User:
    def __init__(self, oauth):
        self.oauth = oauth

    def get_user_data(self):
        return self.oauth.suap.get('v2/minhas-informacoes/meus-dados').json()

    def get_boletim(self, ano_letivo, periodo_letivo):
        return self.oauth.suap.get(f"v2/minhas-informacoes/boletim/{ano_letivo}/{periodo_letivo}/").json()

    def get_periodos(self):
        return self.oauth.suap.get("v2/minhas-informacoes/meus-periodos-letivos/").json()


@app.route('/')
def index():
    if 'suap_token' in session:
        suap_user = User(oauth)
        user = suap_user.get_user_data()
        return render_template('user.html', user=user)
    else:
        return render_template('index.html')


@app.route("/boletim/", methods=["GET", "POST"])
def boletim():
    suap_user = User(oauth)

    if request.method == "POST":
        periodo = request.form["periodo"]
        return redirect(url_for("boletim", periodo=periodo))

    if request.method == "GET":
        periodo = request.args.get("periodo", "2024.1")

    ano_letivo, periodo_letivo = periodo.split(".")

    user = suap_user.get_user_data()
    boletim = suap_user.get_boletim(ano_letivo, periodo_letivo)
    periodos = suap_user.get_periodos()

    context = {
        "user": user,
        "boletim": boletim,
        "periodos": periodos,
        "selected_periodo": periodo
    }

    return render_template("boletim.html", context=context)


@app.route('/login/')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.suap.authorize_redirect(redirect_uri)


@app.route('/logout/')
def logout():
    session.pop('suap_token', None)
    return redirect(url_for('index'))


@app.route('/login/authorized/')
def auth():
    token = oauth.suap.authorize_access_token()
    session['suap_token'] = token
    return redirect(url_for('index'))