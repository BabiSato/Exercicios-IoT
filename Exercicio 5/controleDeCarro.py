class CarroAutonomo:
    def __init__(self):
        self.velocidade = 0  # Velocidade atual do carro em km/h
        self.sensor_distancia = 100  # Distância em metros para o objeto à frente
        self.acelerando = False  # Estado do carro, se está acelerando ou parando
    
    def verificar_distancia(self):
        if self.sensor_distancia < 10:
            self.velocidade = 0
            self.acelerando = False
            print(f"Distância muito curta! O carro está parando. Velocidade: {self.velocidade} km/h")
        else:
            self.velocidade += 10
            self.acelerando = True
            print(f"O carro está acelerando. Velocidade: {self.velocidade} km/h")
    
    def atualizar_distancia(self, nova_distancia):
        self.sensor_distancia = nova_distancia
    
    def mostrar_status(self):
        estado = "acelerando" if self.acelerando else "parando"
        print(f"Status do carro: Velocidade {self.velocidade} km/h, Estado: {estado}")

# Exemplo de uso
carro = CarroAutonomo()
carro.mostrar_status()
carro.verificar_distancia()
carro.mostrar_status()

# Simulando diferentes cenários alterando a distância do sensor
carro.atualizar_distancia(5)
carro.verificar_distancia()
carro.mostrar_status()

carro.atualizar_distancia(20)
carro.verificar_distancia()
carro.mostrar_status()
