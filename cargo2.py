clase  Carga :
    secuencia = 0
    def  __init__ ( self , des = "sin cargo" ):
        Carga . secuencia = Cargo . secuencia + 1
        yo . codigo = Carga . secuencia 
        yo . descripcion = des
if  __name__  ==  "__main__" :

    cargo1 = Cargo ()
    print ( "cargo1" , cargo1 . codigo , cargo1 . descripcion )

    cargo2 = Cargo ( "docente" )
    print ( "cargo2" , cargo2 . codigo , cargo2 . descripcion )

    cargo3  =  Cargo ()
    print ( "cargo3" , cargo3 . codigo , cargo3 . descripcion )
    imprimir ( Cargo . secuencia )