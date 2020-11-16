from flask import Blueprint, redirect, render_template, url_for,request
from werkzeug.security import generate_password_hash,check_password_hash
from app.receita.view import receita
from datetime import datetime
from app.app import db


medico = Blueprint('medico',__name__)

@medico.route('/loginmedico',methods=['GET','POST'])
def loginmedico():
    if request.method == 'POST':
        try:
            login = request.form['login']
            senha = request.form['senha']
            senhaInBd = [i for i in db.engine.execute(f"select senha from medico where cpf ='{login}'")]
            if check_password_hash(senhaInBd[0][0],senha):
                return render_template('medico.html')
        except:
            pass
    return render_template('loginmedico.html')

@medico.route('/medico',methods=['GET','POST'])
def medico_():
    return render_template('medico.html')

#Consultar os dados de um paciente
@medico.route('/consultapacientemedico',methods=["GET","POST"])
def consultapacientemedico():
    if request.method == 'POST':
        try:
            cpf = request.form['buscar']
            if len(cpf) > 0:
                consulta = db.engine.execute(f"select nome,email,telefone,cpf,rg,dataNascimento,genero from paciente where cpf ='{cpf}'")
                dadosConsulta = [i for i in consulta]
                if len(dadosConsulta) > 0:
                    return render_template('consultapacientemedico.html',dados=dadosConsulta[0])
                else:
                    dadosConsulta = None
                    return render_template('consultapacientemedico.html',dados=dadosConsulta)
        except:
            return render_template('consultapacientemedico.html')
    return render_template('consultapacientemedico.html')


def editarREceita2(valor,prescricao):
    db.engine.execute(f"update receita set prescricao = '{prescricao}' where idReceita = '{id}' ")
    return render_template('medico.html')

@medico.route('/editarReceita/<int:id>',methods=['POST','GET'])
def editarREceita(id):
    try:
        if request.method =='POST':
            prescricao = request.form['prescricao']
            db.engine.execute(f"update receita set prescricao = '{prescricao}' where idReceita = '{id}' ")
            return redirect('/medico')
        else:
            dados = [i for i in db.engine.execute(f"select p.idReceita,po.fk_Paciente_cpf,p.prescricao from possui po inner join receita p on po.fk_Receita_idReceita = p.idReceita where p.idReceita={id}")]    
            return render_template('editarReceitamedico.html',dados=dados)
    except:
        return redirect('/medico')

@medico.route('/deletar/<int:id>')
def excluirReceita(id):
    try:
        db.engine.execute(f'delete from possui where fk_Receita_idReceita = {id}')
        db.engine.execute(f'delete from receita where idReceita = {id}')
        return redirect('/consultareceitamedico')
    except:
        return redirect('/consultareceitamedico')

@medico.route('/consultareceitamedico',methods=['GET','POST'])
def consultareceitamedico():
    if request.method =='POST':
        try:
            documento = request.form['buscar']
            dados = receita.consultaReceita(documento)
            return render_template('consultareceitamedico.html',dados=dados)
        except:
            pass
    return render_template('consultareceitamedico.html')


#@medico.route('/alterardadosmedico')
#def alterardadosmedico():
#    return render_template('alterardadosmedico.html')

#cadastrar um novo médico
@medico.route('/cadastrarmedico',methods=['GET','POST'])
def cadastrarMedico():
    if request.method == 'POST':
        nome = request.form['name']
        crm = request.form['CRM']
        especialidade = request.form['Especialidade']
        email = request.form['email']
        rg = request.form['rg']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        db.engine.execute(f'''
            insert into medico (crm,nome,rg,cpf,especialidade,email,senha,telefone)
            values('{crm}','{nome}','{rg}','{cpf}','{especialidade}','{email}','{generate_password_hash(cpf)}','{telefone}')''')
        return redirect('/medico')        
    return render_template('cadastromedico.html')

#cadastrar um novo paciente
@medico.route('/cadastropaciente',methods=["GET","POST"])
def cadastropaciente():
    if request.method == 'POST':
        nome = request.form['name']
        cpf=request.form['cpf']
        rg =request.form['rg']
        genero =request.form['sexo']
        if genero == '1':
            g = 'F'
        elif genero == '2':
            g = 'M'
        else:
            g = 'O'
        email = request.form['email']
        senha = generate_password_hash(request.form['cpf'])
        dataNascimento =request.form['dataNascimento']
        telefone = request.form['telefone']
        db.engine.execute(f'''
        insert into paciente(cpf,nome,rg,dataNascimento,genero,email,senha,telefone)
        values ('{cpf}','{nome}','{rg}','{dataNascimento}','{g}','{email}','{senha}','{telefone}')''')

        return redirect('/medico')
    return render_template('cadastropaciente.html')

@medico.route('/cadastrarreceita',methods=['GET','POST'])
def cadastrarreceita():
    if request.method == 'POST':
        try:
            cpf = request.form['cpf']
            crm = request.form['crm']
            dataReceita = datetime.now()
            prescricao = request.form['prescricao']
            db.engine.execute(f"insert into receita(prescricao,dataReceita) values('{prescricao}','{dataReceita}')")
            idreceita = [i for i in db.engine.execute(f"select idReceita from receita where prescricao = '{prescricao}' and dataReceita = CURDATE()")]
            db.engine.execute(f"insert into possui(fk_Receita_idReceita,fk_Medico_crm,fk_Paciente_cpf) values('{idreceita[0][0]}','{crm}','{cpf}')")
            return render_template('medico.html')
        except:
            pass
    return render_template('cadastrarreceita.html')