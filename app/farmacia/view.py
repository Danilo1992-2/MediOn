from flask import Blueprint, redirect, render_template, url_for,request
from werkzeug.security import generate_password_hash,check_password_hash
from app.receita.view import receita
from app.app import db

farmacia = Blueprint('farmacia',__name__)


@farmacia.route('/loginfarmacia',methods=['GET','POST'])
def loginfarmacia():
    if request.method == 'POST':
        try:
            login = request.form['login']
            senha = request.form['senha']
            senhaInBd = [i for i in db.engine.execute(f"select senha from farmacia where cnpj ='{login}'")]
            if check_password_hash(senhaInBd[0][0],senha):
                return render_template('farmacia.html')
        except:
            pass
    return render_template('loginfarmacia.html')

@farmacia.route('/farmacia')
def farmacia_():
    return render_template('farmacia.html')

@farmacia.route('/consultareceitafarmacia',methods=['GET','POST'])
def consultareceitafarmacia():
    try:
        if request.method == 'POST':
            busca = request.form['search']
            dados = receita.consultaReceitaFarm(busca)
            return render_template('consultareceitafarmacia.html',dados = dados)
    except:
        pass
    return render_template('/consultareceitafarmacia.html')

@farmacia.route('/consultarpacienefarmacia',methods=['GET','POST'])
def consultarpacientefarmacia():
    if request.method == 'POST':
        try:
            cpf = request.form['buscar']
            if len(cpf)>0:
                print(cpf)
                consulta = db.engine.execute(f"select nome,email,telefone,cpf,rg,dataNascimento,genero from paciente where cpf = {cpf}")
                dadosConsulta = [i for i in consulta]
                print(dadosConsulta)
                if len(dadosConsulta) > 0:
                    return render_template('consultarpacientefarmacia.html',dados=dadosConsulta[0])
                else:
                    dadosConsulta = None
                    return render_template('consultarpacientefarmacia.html',dados=dadosConsulta)
        except:
            pass
    return render_template('consultarpacientefarmacia.html')


@farmacia.route('/cadastrarFarmacia',methods=['GET','POST'])
def cadastrarFarmacia():
    if request.method == 'POST':
        nome = request.form['name']
        telefone = request.form['telefone']
        cnpj = request.form['cnpj']
        numero = request.form['numero']
        cep = request.form['cep']
        complemento = request.form['complemento']

        db.engine.execute(f'''
            insert into farmacia(nomeFantasia,cnpj,telefone,senha,cep,numero,complemento)
            valueS('{nome}','{cnpj}','{telefone}','{generate_password_hash(cnpj)}','{cep}','{numero}','{complemento}')
        ''')

    return render_template('cadastrarFarmacia.html')

@farmacia.route("/vender/<int:id>",methods=['POST'])
def venderReceita(id):
    try:
        if request.method == 'POST':
            receita.vender(id)
            return redirect('/farmacia')
    except:
        pass
    return redirect('/farmacia')
