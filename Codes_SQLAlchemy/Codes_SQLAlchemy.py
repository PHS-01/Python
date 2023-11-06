# pip install sqlalchemy  --Comando para instalar o sqlalchemy
# pip install mysqlconnector  --Comando para instalar o mysqlconnector

#--------------------------------------Conexão para o banco de dados--------------------------------------

# Importações necessárias
import sqlalchemy

# Função para criar uma conexão com o banco 
engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:@localhost:3306/db_SQLAlchemy', echo=True)
#("dialect+driver://username:password@host:port/database")

#--------------------------------------Criando uma Sessão--------------------------------------

# Importações
from sqlalchemy.orm import sessionmaker

# Criação da sessão que iremos usar
Session = sessionmaker(bind=engine)
session = Session()

#--------------------------------------Funções session--------------------------------------

#session.add(intancia) -- Função para adicionar a intância ao banco

#session.commit() -- Função para ver o processo

#session.dirty -- Função para ver o objt antes do update

#session.new -- Ver os objetos que ainda não foram para o banco de dados

#query_user = session.query(User).filter_by(name='Teste').first() -- Função de consulta

#--------------------------------------Declaração de mapeamento--------------------------------------

# Importações do modo de declaração que ira ser usada
import sqlalchemy.orm 
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import declarative_base, mapped_column
from sqlalchemy.orm import sessionmaker

# Função que declara qual modelo de Base vamos usar
Base = declarative_base()

# Criando uma class
class User (Base):
    
    __tablename__ = 'tb_users'# Declaração do nome da tabela
    
    # mapped_column('nome_coluna, Tipo, outros_atributos...')
    id = mapped_column('use_id',Integer, primary_key=True)
    name = mapped_column('use_name', Text, nullable=False)
    email = mapped_column('use_email', String(50), nullable=False)
    password = mapped_column('use_password', String(50), nullable=False)
    
    # Insert
    def __create__(self):
        session.add(self)
        return session.commit()
    
    # Select
    def __read__(self):
        query_user = session.query(User).filter_by(id=self.id)
        session.commit()
        return query_user
    
    # Update
    def __update__(self, name):
        self.name = name
        return session.commit()
    
    # Delete
    def __delete__(self):
        session.delete(self)
        return session.commit()
        
# Cria as tabelas no banco -- Seria como se vc apertace o botão de execução la no workbench
Base.metadata.create_all(engine)

#--------------------------------------Criar intâncias da class--------------------------------------

# Criando a intância
user = User(name='Teste', email='teste@teste', password='123')

# Criando o objeto
user.__create__()

# Mostra as informações
user.__read__()

# Faz modificações
user.__update__('Teste2')

# Deleta o objeto
user.__delete__()

# Função que mostra todos os User
for intancia in session.query(User).order_by(User.id):
    print(intancia.name, intancia.email)

#--------------------------------------Um para Um--------------------------------------
from sqlalchemy.orm import relationship

# Para 1:1 parent uselist=False
class Parent(Base):
    __tablename__ = "tb_parent"

    id = mapped_column(Integer, primary_key=True)
    child = relationship("Child", uselist=False, back_populates="parent")


class Child(Base):
    __tablename__ = "tb_child"

    id = mapped_column(Integer, primary_key=True)
    parent_id = mapped_column(sqlalchemy.ForeignKey("tb_parent.id"))
    parent = relationship("Parent", back_populates="child")

#--------------------------------------Um para Muitos--------------------------------------

# Para 1:N os dois precisan ser uselist=True
class Parent(Base):
    __tablename__ = "tb_parent"

    id = mapped_column(Integer, primary_key=True)
    children = relationship("Child", back_populates="parent")


class Child(Base):
    __tablename__ = "tb_child"

    id = mapped_column(Integer, primary_key=True)
    parent_id = mapped_column(sqlalchemy.ForeignKey("tb_parent.id"))
    parent = relationship("Parent", back_populates="child")

#--------------------------------------Muitos para Muitos--------------------------------------

# Para N:N precisamos cria uma tabela de associação
association_table = Table(
    "tb_association",
    Base.metadata,
    sqlalchemy.Column("parent_id", sqlalchemy.ForeignKey("tb_parent.id"), primary_key=True),
    sqlalchemy.Column("child_id", sqlalchemy.ForeignKey("tb_child.id"), primary_key=True),
)


class Parent(Base):
    __tablename__ = "tb_parent"

    id = mapped_column(Integer, primary_key=True)
    children = relationship(secondary=association_table, back_populates="parents")


class Child(Base):
    __tablename__ = "tb_child"

    id = mapped_column(Integer, primary_key=True)
    parents = relationship(secondary=association_table, back_populates="children")

Base.metadata.create_all(engine)
