def validar_projeto_disruptivo(empresa, projeto, caracteristicas):
    elementos_obrigatorios = ["IoT", "Big Data", "AI"]
    
    if all(elemento in caracteristicas for elemento in elementos_obrigatorios):
        return f"O projeto {projeto} da empresa {empresa} atende os requisitos"
    else:
        return f"O projeto {projeto} da empresa {empresa} NÃO atende os requisitos"

# Exemplo de uso
empresa = "Tech Innovations"
projeto = "Smart City"
caracteristicas = ["IoT", "Big Data", "AI"]

resultado = validar_projeto_disruptivo(empresa, projeto, caracteristicas)
print(resultado)