import sqlite3

class Crud:

    def __init__(self):
        self.conexao = sqlite3.connect("alunos.sqlite")
        self.cursor  = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()
        print("fechou")

    def criar(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            disciplina TEXT NOT NULL,
            idade INTEGER NOT NULL
            );
        '''
        self.cursor.execute(sql)
        print("tabela criada")

    def ler(self):
        sql = '''
            SELECT * FROM alunos
        '''
        resultado = self.cursor.execute(sql)
        return resultado.fetchall()
    
    def inserir(self, tabela, campos, dados):
        valores = '('
        resultado = '('
        for campo in campos:
            resultado += f"{campo}, "
            valores += f"?, "
        resultado = resultado[:-2]+ ")"
        valores = valores[:-2] + ")"
        sql = f'''
            INSERT INTO {tabela}{resultado}
            VALUES{valores}
        '''
        self.cursor.execute(sql, (dados))
        self.conexao.commit()
        return "Salvo com Sucesso!"
    
    def alterar(self, dados, id):
        nome = dados[0]
        disciplina = dados[1]
        idade = dados[2]

        sql = '''
            INSERT INTO alunos
            SET nome = ?, disciplina = ?, idade = ?,
            WHERE id = ?;
        '''

        self.cursor.execute(sql, [nome, disciplina, idade, id])
        self.conexao.commit()


tabela = 'alunos'
campos = ("nome", "disciplina", "idade")
#dados = ["Eduardo", "prog1", 18]

dados = [input("Entre com seu nome: "), input("Entre com a Disciplina: "), int(input("Entre com sua idade: "))]
#print(dados1)
a = Crud()
#a.criar()
#a.inserir(tabela, campos, dados)
#print(a.ler())
a.alterar(dados, int(input("entre com o ID: ")))

a.fechar()