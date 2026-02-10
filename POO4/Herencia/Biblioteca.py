#Fet per Daniel
#10/02/2026
#Crea llibres en paper i digitals que mostren la seva informació amb herència
class Llibre:
    def __init__(self, titol, autor):
        self.titol = titol
        self.autor = autor

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}")

class LlibrePaper(Llibre):
    def __init__(self, titol, autor, n_pagines):
        super().__init__(titol, autor)
        self.n_pagines = n_pagines

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}, Pàgines: {self.n_pagines}")

class LlibreDigital(Llibre):
    def __init__(self, titol, autor, format):
        super().__init__(titol, autor)
        self.format = format

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}, Format: {self.format}")
        
paper = LlibrePaper("1984", "George Orwell", 328)
digital = LlibreDigital("Python Avançat", "Dani", "PDF")
paper.mostrar_info()   
digital.mostrar_info()   