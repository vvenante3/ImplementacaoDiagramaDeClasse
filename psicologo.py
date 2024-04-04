from policial import Policial

class Psicologo:
    def __init__(self, idPsicologo, nomePsicologo, CRP):
        self.idPsicologo    = idPsicologo
        self.nomePiscologo  = nomePsicologo
        self.CRP            = CRP

def cadastrarPsicologo(idPsicologo, nomePsicologo, CRP):
    Psicologo(idPsicologo, nomePsicologo, CRP)
    ## futuramente, construir logica que realize salvar em Db... PS: Igual ao Policial
    return Psicologo

def editarPsicologo(self, idPsicologo=None, nomePsicologo=None, CRP=None):
    if idPsicologo is not None:
        self.idPsicologo    = idPsicologo
    if nomePsicologo is not None:
        self.nomePsicologo  = nomePsicologo
    if CRP is not None:
        self.CRP            = CRP

def excluirPsicologo(lista_psicologo, idPosicologo):
    for i, psicologo in enumerate(lista_psicologo): #mesma função dos policiais
        if psicologo.idPsicologo == idPosicologo:
            del lista_psicologo[i]
            print(f"Psicologo como ID {idPosicologo} excluído")
            return
        print(f"Psicologo com ID {idPosicologo} não encontrado")

def entrevistar():                              ##2ºETAPA: RELACIONAR COM O POLICIAL
    # DESCREVER FUNÇÃO

def diagnosticar():                             ##2ºETAPA: RELACIONAR COM O RESULTADO
    # DESCREVER FUNÇÃO