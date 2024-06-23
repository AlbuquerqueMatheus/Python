class Passaro:
    def voa(self):
        print("voando")

class papagaio(Passaro):
    def voa(self):
        print("papagaio voando")

class pinguim(Passaro):
    def voa(self):
        print("pinguim não voa")

def plano_voar(pa):
    pa.voa()

plano_voar(papagaio())
plano_voar(pinguim())
