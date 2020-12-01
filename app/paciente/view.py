from flask import Blueprint, redirect, render_template, url_for,request
from werkzeug.security import generate_password_hash,check_password_hash
from app.receita.view import receita
from app.app import db


paciente = Blueprint('paciente',__name__)

@paciente.route('/loginpaciente',methods=['GET','POST'])
def loginpaciente():
    Erro = None
    if request.method == 'POST':
        try:
            login = request.form['login']
            senha = request.form['senha']
            senhaInBd = [i for i in db.engine.execute(f"select senha from paciente where cpf ='{login}'")]
            if check_password_hash(senhaInBd[0][0],senha):
                return render_template('paciente.html',cpf=login)
            Erro = "Verifique suas credenciais"
        except:
            Erro = "Verifique suas credenciais"
            pass
    return render_template('loginpaciente.html',Erro =Erro)

@paciente.route('/paciente')
def paciente_():
    try:
        return render_template('paciente.html')
    except:
       return redirect('loginpaciente.html')

@paciente.route('/receitapaciente/<doc>',methods=['POST','GET'])
def receitaPaciente(doc):
    try:
        if len(doc) == 11 and doc != None:
            dados = receita.consultaReceitaPac(doc)
            return render_template('consultaReceitaPaciente.html',dados=dados)
        else:
            return render_template('loginpaciente.html')            
    except:
        return render_template('loginpaciente.html')
'''
@paciente.route('/AlterardadosPaciente')
def AlterardadosPaciente():
    return render_template('AlterardadosPaciente.html')
    '''

