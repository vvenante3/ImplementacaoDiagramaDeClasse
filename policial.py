class Policial:
    def __init__(self, idPolicial, dataCadastro, DataNascimento, sexo, ImgPolicial):
        self.idPolicial     = idPolicial                                                     ##2º ETAPA (incluir id do Db)
        self.dataCadastro   = dataCadastro
        self.DataNascimento = ' ' ##2º ETAPA (incluir data do sistema)
        self.sexo           = ' '
        self.ImgPolicial    = ' ' #arquivo da imagem do indivíduo

def cadastrarPolicial(idPolicial, dataCadastro, DataNascimento, sexo, ImgPolicial):
    Policial(idPolicial, dataCadastro, DataNascimento, sexo, ImgPolicial)
    # futuramente, construir logica que realize salvar em Db...
    return Policial

def editarPolicial(self, idPolicial=None, dataCadastro=None, sexo='none', ImgPolicial=None):
    if idPolicial is not None:
        self.idPolicial = idPolicial
    if dataCadastro is not None:
        self.dataCadastro = dataCadastro
    if sexo is not None:
        self.sexo = sexo
    if ImgPolicial is not None:
        self.ImgPolicial = ImgPolicial

def excluirPolicial(lista_policiais, idPolicial):
    for i, policial in enumerate(lista_policiais):  # O enumerate(função) atribui um índice e saiba as posições de cada item
        if policial.idPolicial == idPolicial:
            del lista_policiais[i]
            print(f"Policial com o ID {idPolicial} excluído."),
            return
        print(f"Policial com ID {idPolicial} não encontrado.")