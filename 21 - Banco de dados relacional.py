import sqlite3

def manipulaDados(bancoDados, comando):
    conexao = sqlite3.connect(bancoDados)
    cursor = conecao.cursor
    cursor.execute(comando)
    conexao.commit()
    conexao.close()

def selecionaDados(bancoDados, comando):
    conexao = sqlite3.connect(bancoDados)
    cursor = conecao.cursor
    cursor.execute(comando)
    linhas = cursor.fetchall()

    for linha in linhas:
        print(linhas)

def ManipulacaoDados():
    comandoInsert = "INSERT INTO estados (nome_estaco, sigl_estado, nome_capital) VALUES ('Estado Teste', 'XX', 'Teste Inclusão')"
    pathBD = "insira endereço de rede onde esta o banco"
    comandoSELECT = "SELECT nome_estaco, sigl_estado, nome_capital FROM estados"

    manipulaDados(pathBD, comandoInsert)
    selecionaDados(pathBD, comandoSELECT)
ManipulacaoDados()