def name(nombre_usuario):

        long = len(nombre_usuario) 
        y = nombre_usuario.isalnum() 
        
        if y== False: # La cadena contiene valores no alfanuméricos
            print("El nombre de usuario puede contener solo letras y números")
            
        if long < 10: 
            print("El nombre de usuario debe contener al menos 10 caracteres")
            
        if long > 12: 
            print("El nombre de usuario no puede contener más de 12 caracteres")
            
        if long >5 and long <13 and y ==True:
            return True 