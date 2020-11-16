Para iniciar o projeto navegue até a pasta app, dentro da mesma digite "flask run", o terminal lhe informara o localhost e sua porta, para navegar entre páginas sigua o endpoint em cada função.

Dentro do arquivo config.py, localizado na pasta raiz do projeto, é necessário alterar as credências do banco dedados.
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://loginbanco:senhaBanco@localhost/medion'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    SECRET_KEY = "secret"



para que o software funcione de forma correta, é necessário que as tabelas estejam de acordo com as tabelas abaixo listadas.

ALTERAÇÕES NAS TABELAS :

CREATE TABLE `adminlogin` (
  `idAdmin` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `cpf` varchar(11) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `rg` varchar(9) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `password` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`idAdmin`),
  UNIQUE KEY `cpf` (`cpf`),
  UNIQUE KEY `rg` (`rg`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci

CREATE TABLE `consulta` (
  `fk_Receita_idReceita` int DEFAULT NULL,
  `fk_Farmacia_idFarmacia` int DEFAULT NULL,
  `fk_Farmacia_cnpj` varchar(14) DEFAULT NULL,
  KEY `fkreceita` (`fk_Receita_idReceita`),
  KEY `fkfarmacia` (`fk_Farmacia_idFarmacia`),
  CONSTRAINT `fkfarmacia` FOREIGN KEY (`fk_Farmacia_idFarmacia`) REFERENCES `farmacia` (`idFarmacia`),
  CONSTRAINT `fkreceita` FOREIGN KEY (`fk_Receita_idReceita`) REFERENCES `receita` (`idReceita`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `farmacia` (
  `idFarmacia` int NOT NULL AUTO_INCREMENT,
  `cnpj` varchar(14) NOT NULL,
  `nomeFantasia` varchar(100) DEFAULT NULL,
  `senha` varchar(200) NOT NULL,
  `telefone` varchar(11) DEFAULT NULL,
  `cep` varchar(8) DEFAULT NULL,
  `numero` varchar(6) DEFAULT NULL,
  `complemento` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idFarmacia`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `medico` (
  `idMedico` int NOT NULL AUTO_INCREMENT,
  `crm` varchar(6) NOT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `rg` varchar(9) DEFAULT NULL,
  `cpf` varchar(11) DEFAULT NULL,
  `especialidade` varchar(50) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `senha` varchar(200) NOT NULL,
  `telefone` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`idMedico`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


CREATE TABLE `paciente` (
  `idPaciente` int NOT NULL AUTO_INCREMENT,
  `cpf` varchar(11) NOT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `rg` varchar(9) DEFAULT NULL,
  `dataNascimento` date DEFAULT NULL,
  `genero` char(1) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `senha` varchar(200) NOT NULL,
  `telefone` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`idPaciente`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


CREATE TABLE `possui` (
  `fk_Receita_idReceita` int DEFAULT NULL,
  `fk_Medico_idMedico` int DEFAULT NULL,
  `fk_Medico_crm` varchar(6) NOT NULL,
  `fk_Paciente_idPaciente` int DEFAULT NULL,
  `fk_Paciente_cpf` varchar(11) NOT NULL,
  KEY `fkreceitapossui` (`fk_Receita_idReceita`),
  KEY `fkmedicopossui` (`fk_Medico_idMedico`),
  KEY `fkcrm` (`fk_Paciente_idPaciente`),
  CONSTRAINT `fkcrm` FOREIGN KEY (`fk_Paciente_idPaciente`) REFERENCES `paciente` (`idPaciente`),
  CONSTRAINT `fkmedicopossui` FOREIGN KEY (`fk_Medico_idMedico`) REFERENCES `medico` (`idMedico`),
  CONSTRAINT `fkreceitapossui` FOREIGN KEY (`fk_Receita_idReceita`) REFERENCES `receita` (`idReceita`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `receita` (
  `idReceita` int NOT NULL AUTO_INCREMENT,
  `prescricao` varchar(500) DEFAULT NULL,
  `dataReceita` date DEFAULT NULL,
  `statusReceita` varchar(1) DEFAULT (_utf8mb4'd'),
  PRIMARY KEY (`idReceita`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
