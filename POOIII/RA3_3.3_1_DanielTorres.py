#Programa fet per Daniel Torres
#Data: 28/01/2026
#Versio: 2.1
#Crea una classe Factura que tingui atributs per al client, l'import total i una impressora.
class ImpressoraPDF:
    def imprimir(self, contingut):
        print(f"Imprimit PDF: {contingut}")

class Factura:
    def __init__(self,client,import_total,impressora):
        self.client = client
        self.import_total = import_total
        self.impressora = impressora
        
    def imprimir_factura(self):
        contingut = f"Factura per {self.client}, Import Total: {self.import_total} EUR"
        self.impressora.imprimir(contingut)
        
imp = ImpressoraPDF()
factura = Factura("Daniel", 100, imp)
factura.imprimir_factura()