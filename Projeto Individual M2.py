#função para buscar candidatos com base nos critérios
def buscar_candidatos(candidato, nota_entre, nota_teo, nota_prat, nota_soft):
    candidatos_encontrados = [] #lista para armazenar os candidatos encontrados

    for candidato in candidatos_encontrados: # percorre cada candidato na lista de candidatos
        nome = candidato['candidato']
        entre = candidato['entre']
        teo = candidato ['teo']
        prat = candidato ['prat']
        soft = candidato ['soft']

        # verifica se as notas do candidato são maiores ou iguais às notas mínimas
        if entre >= nota_entre and teo >= nota_teo and prat >= nota_prat and soft >= nota_soft:
            candidatos_encontrados.append(candidato)
    
    return candidatos_encontrados

candidatos_encontrados = [
    {'candidato': 'Douglas', 'entre': 5, 'teo': 5, 'prat': 8, 'soft': 7},
    {'candidato': 'Ana', 'entre': 3, 'teo': 6, 'prat': 8, 'soft': 3},
    {'candidato': 'Gabriel', 'entre': 4, 'teo': 3, 'prat': 7, 'soft': 8}]

print (buscar_candidatos(candidato, nota_entre, nota_teo, nota_prat, nota_soft)) 