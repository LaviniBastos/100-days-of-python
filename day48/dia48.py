def comportamento_log(cls):
    class ClasseLogging(cls):
        def __getattribute__(self, nome):
            attr = super().__getattribute__(nome)
            if callable(attr):
                def metodo_novo(*args, **kwargs):
                    print(f"[LOG] chamando o seguinte método: {nome}")
                    return attr(*args, **kwargs)
                return metodo_novo
            return attr
    return ClasseLogging 


@comportamento_log
class Calculadora:
    def soma(self, a, b):
        return a + b
    
    def multiplica(self, a, b):
        return a * b
    
    def subtrai(self, a, b):
        return a - b
    
    
calc = Calculadora()
print(calc.soma(9, 8))
print(calc.subtrai(9, 8))
print(calc.multiplica(9, 8))