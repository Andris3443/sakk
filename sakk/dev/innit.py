def sakktabla():    
    tabla = []


    for sor in range(8): 
        for oszlop in range(8):  
            if (sor + oszlop) % 2 == 0:
                tabla.append('⬜')  
            else:
                tabla.append('⬛')  


    for i in range(8): 
        print(" ".join(tabla[i * 8:(i + 1) * 8]))  
