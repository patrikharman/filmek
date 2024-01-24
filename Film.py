class Film:
    def __init__(self,cim:str,rendezo:str,foszereplo:str,ev:str,perc:int):
        self.cim = cim
        self.rendezo = rendezo
        self.foszereplo = foszereplo
        self.ev = int(ev)
        self.perc = int(perc)
    def __str__(self):
        return  f"Cím:{self.cim},Rendező:{self.rendezo},Főszereplő:{self.foszereplo},Cím:{self.cim},Perc:{self.perc}"



