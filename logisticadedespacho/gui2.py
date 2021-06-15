# ---------------------- Importaciones -------------------------------------------

from listado import *
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from despacho import *
from datetime import date
from datetime import datetime
from transportista import *


# ----------------------------- Variables Globales --------------------------------------

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   creando a los transportistas   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
t1 = Transportista("Juan Perez","111","moto",0)
t2 = Transportista("Jose Rozas","222","moto",0)
t3 = Transportista("Federico Henriquez","333","camioneta",0)
t4 = Transportista("Sandra Soto","444","camioneta",0)
t5 = Transportista("Vicente Ceron","555","camion",0)
t6 = Transportista("Cristobal Reynoso","666","camion",0)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    creando despachos   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
d1 = Despacho( Cliente( "Mauro Hernandez","20426307-8","Exposicion #1478"), Producto(3,"Televisor Smart tv"), Destinatario("Juan Diaz","45742367","Gorbea #1245"), "5 de enero del 2021" )
d1.asignaBodega()
d1.asignaTransporte()

d2 = Despacho( Cliente( "Pedro Fontena","2354323-6","martinas #1421"), Producto(6,"3 Refrigeradores sony"), Destinatario("herneesto jorkera","98484567","Maquinon#1245"), "6 de marzo del 2021" )
d2.asignaBodega()
d2.asignaTransporte()

d3 = Despacho( Cliente( "Maria Luengo","2012323-6","Av kito #3321"), Producto(1,"Iphone X"), Destinatario("pepito","10484567","plantas #3335"), "6 de marzo del 2021" )
d3.asignaBodega()
d3.asignaTransporte()

d4 = Despacho( Cliente( "Manuel Astorga","1245321-6","Tazas #1111"), Producto(3,"Sillon azul"), Destinatario("joakin efe","60484567","Catalan #1225"), "6 de marzo del 2021" )
d4.asignaBodega()
d4.asignaTransporte()

d5 = Despacho( Cliente( "Evelin Tobar", "1111111-1","Melipilla #1131"), Producto(6,"100 Cajas de cigarros"), Destinatario("Benja","60484767","la Pac#3335"), "8 de junio del 2021" )
d5.asignaBodega()
d5.asignaTransporte()

d6 = Despacho( Cliente( "Francisco Tompson","aaaaaaa-a","Maitecinos #1313"), Producto(1,"3 Poleras Nike"), Destinatario("Luis Gorm","55584567","maipuci #1222"), "6 de marzo del 2021" )
d6.asignaBodega()
d6.asignaTransporte()

d7 = Despacho( Cliente( "Vicente ceron","2011111-2", "Exposi #1111"), Producto(1,"5 Libros de fisica"), Destinatario("Seba rodri", "666666666","quevola #1225"), "9 de marzo del 2021" )
d7.asignaBodega()
d7.asignaTransporte()
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

listaTransportistas = [t1,t2,t3,t4,t5,t6]
listadoDespachos= Listado()
listadoDespachos.agregarDespacho(d1)
listadoDespachos.agregarDespacho(d2)
listadoDespachos.agregarDespacho(d3)
listadoDespachos.agregarDespacho(d4)
listadoDespachos.agregarDespacho(d5)
listadoDespachos.agregarDespacho(d6)
listadoDespachos.agregarDespacho(d7)





def current_date_format(date): # Me entrega la fecha actual
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)

    return messsage

#---------------------------------------------------------------------------------------------------------- Inicio de la Vista del Administrador --------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def creaVistaAd(): # Crea la vista del administrador, contiene sus propias Funciones
    vAd = Toplevel(root)
    vAd.geometry("1152x700")
    vAd.resizable(0,0)


    def buscarElemento(): #Busca un elemento determinado y lo muestra en la tabla
        registros = tree.get_children()
        for elemento in registros:
            tree.delete(elemento)

        for despacho in listadoDespachos.getLista():
            if despacho.getCliente().getRut()==buscadorRut.get():
                tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))


    def mostrarTodo(): # Muestra los valores de cada despacho en una tabla
        registros = tree.get_children()
        for elemnto in registros:
            tree.delete(elemnto)
        for despacho in listadoDespachos.getLista():
                tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))
                

        

    def seleccionarElemento(): # Me permite Registrar una Seleccion en la tabla
        item = tree.item(tree.selection())['values'][1]
        return item


    def eliminarElemento(): # Elimina el elemnto que seleccione el usuario en la Tabla
        for despacho in listadoDespachos.getLista():
            data = seleccionarElemento()
            if despacho.getCliente().getRut()==data:
                listadoDespachos.eliminarDespacho(despacho)
                mostrarTodo()




    #------------------------------------------------------------------------------------- Inicio de la Vista del Formulario --------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    
    def abrirVistaDespacho(): # Abre el formulario para agregar un nuevo despacho
       
        def capturarValores(): # Captura los valores de los entry y crea un despacho para agregarlo a la lista de despachos
            now= datetime.now()
            fechaActual = current_date_format(now)
            despacho = Despacho(Cliente(eNombreCliente.get(),eRut.get(),eDireccion.get()), Producto(int(eTamaño.get()), eDescripcion.get()), Destinatario(eNumeroDes.get(),eNumeroDes.get(),eDireccionDes.get()), fechaActual)
            
            despacho.asignaBodega()
            despacho.asignaTransporte()
            listadoDespachos.agregarDespacho(despacho)
            mostrarTodo()
            print(listadoDespachos.mostrarDespachos())
            vistaformulario.destroy() 

        vistaformulario = Toplevel(vAd) # Crea la Sub ventana "Registro de Despacho"
        vistaformulario.title('Registro de Despacho')
        vistaformulario.geometry('330x460')
        vistaformulario.config(bg="#649FB1")
        vistaformulario.resizable(0,0)
        
        # REGISTRO DE CLIENTE 

        labelframe1 = ttk.LabelFrame(vistaformulario, text="Registro de Cliente")
        labelframe1.grid(column=0,row=0,padx=5,pady=5)
        label1 = ttk.Label(labelframe1, text="Nombre Cliente:") 
        label1.grid(column=0,row=0,padx=4,pady=4)
        eNombreCliente = Entry(labelframe1) # Entry de Nombre Cliente
        eNombreCliente.grid(column=1,row=0,padx=4,pady=4)

        label2 = ttk.Label(labelframe1, text="Rut:")
        label2.grid(column=0,row=1,padx=4,pady=4)
        eRut= Entry(labelframe1)
        eRut.grid(column=1,row=1,padx=4,pady=4)

        label3 = ttk.Label(labelframe1, text="Direccion:")
        label3.grid(column=0,row=2,padx=4,pady=4)
        eDireccion = Entry(labelframe1)  # Entry de Direccion Cliente 
        eDireccion.grid(column=1,row=2,padx=4,pady=4)

        label4 = ttk.Label(labelframe1, text="Mail:")
        label4.grid(column=0,row=3,padx=4,pady=4)
        eMail = Entry(labelframe1)
        eMail.grid(column=1,row=3,padx=4,pady=4)

        label5 = ttk.Label(labelframe1, text="Numero:")
        label5.grid(column=0,row=4,padx=4,pady=4)
        eNumero = Entry(labelframe1)
        eNumero.grid(column=1,row=4,padx=4,pady=4)


        # REGISTRO DE PRODUCTO
        labelframe2 = ttk.LabelFrame(vistaformulario, text="Registro de Producto")
        labelframe2.grid(column=0,row=1,padx=5,pady=7)

        label6 = ttk.Label(labelframe2, text="Descripcion:")
        label6.grid(column=0,row=0,padx=4,pady=4)
        eDescripcion= Entry(labelframe2)
        eDescripcion.grid(column=1,row=0,padx=4,pady=4)

        label7 = ttk.Label(labelframe2, text="Tamaño(mt2):")
        label7.grid(column=0,row=1,padx=4,pady=4)
        eTamaño= Entry(labelframe2)
        eTamaño.grid(column=1,row=1,padx=4,pady=4)

        # REGISTRO DE DESTINATARIO
        labelframe3 = ttk.LabelFrame(vistaformulario, text="Registro de Destinatario")
        labelframe3.grid(column=0,row=2,padx=5,pady=7)

        label8 = ttk.Label(labelframe3, text="Nombre Cliente:")
        label8.grid(column=0,row=0,padx=4,pady=4)
        eNombreDes = Entry(labelframe3)
        eNombreDes.grid(column=1,row=0,padx=4,pady=4)

        label9 = ttk.Label(labelframe3, text="Direccion:")
        label9.grid(column=0,row=1,padx=4,pady=4)
        eDireccionDes= Entry(labelframe3)
        eDireccionDes.grid(column=1,row=1,padx=4,pady=4)

        label10 = ttk.Label(labelframe3, text="Numero:")
        label10.grid(column=0,row=2,padx=4,pady=4)
        eNumeroDes = Entry(labelframe3)
        eNumeroDes.grid(column=1,row=2,padx=4,pady=4)

        btnAgregar = ttk.Button(vistaformulario, text="Agregar",command=capturarValores)
        btnAgregar.grid(column=1,row=3)
        #--------------------------------------------------------------------------- Fin de la Vista de Formulario ---------------------------------------------------------------------------------------------




    #  ------------------------- Frame titulo ----------------------------
    ft = Frame(vAd)
    ft.config(bg="black",width=1152,height=78)
    ft.pack()
    ft.pack_propagate(False)

    imgTitulo = PhotoImage(file='imagenes/adpeque.png', master=ft)
    lbltit = Label(ft,image=imgTitulo, bg="black")
    lbltit.image = imgTitulo
    lbltit.pack()
    
    # --------------------- Frame contenido ------------------------------
    fc = Frame(vAd)
    fc.config(bg="#649FB1",width=1152,height=622)
    fc.pack()
    fc.pack_propagate(False)
    imgFondo = PhotoImage(file='imagenes/fondocielo.png', master = fc)
    lblFondo = Label(fc, image= imgFondo)
    lblFondo.image = imgFondo
    lblFondo.place(x = 0, y = 0, relwidth = 1, relheight = 1)



    

    # Boton Agregar
    imgBtnAdd = PhotoImage(file='imagenes/btnagregar.png', master=fc) # Para que se muetre una imagen dentro de una subventana debo poner el parametro "master=lugar donde ira la imagen" dentro del metodo PhotoImage 
    labelAdd = Button(fc, image=imgBtnAdd,bd=0,command=abrirVistaDespacho)
    labelAdd.image = imgBtnAdd # Luego de cargar el label con una imagen debo volver a referenciarlo como imagen y listo
    labelAdd.place(x=85,y=15)

    # Boton Buscar
    imgBtnSearch = PhotoImage(file='imagenes/btnbuscar.png',master=fc)
    labelSearch = Button(fc, image=imgBtnSearch,bd=0,command=buscarElemento)
    labelSearch.image = imgBtnSearch
    labelSearch.place(x=240,y=15)

    buscadorRut = Entry(fc) # Entry para que ingresen un rut buscador
    buscadorRut.place(x=240 , y=100)
    Font_tuple3 = ("Dungeon", 13, "normal")
    lbBuscar = Label(fc,text="Ingrese un rut ej: 20734727-2",font= Font_tuple3, bg="white")
    lbBuscar.place( x =240, y =115 )
    
    # Boton Eliminar
    imgBtnElimina = PhotoImage(file='imagenes/btneliminar.png',master=fc)
    labelElimina = Button(fc, image=imgBtnElimina,bd=0,command=eliminarElemento)
    labelElimina.image = imgBtnElimina
    labelElimina.place(x=395,y=15)
    
    # Boton Mostrar Todo
    imgBtnMostrar = PhotoImage(file='imagenes/btnmostrar.png',master=fc)
    labelMostrar = Button(fc, image=imgBtnMostrar,bd=0,command=mostrarTodo)
    labelMostrar.image = imgBtnMostrar
    labelMostrar.place(x=550,y=15)

   

    """
    # Label Estadisticas de Despachos
    fuenteEstadistica = ("Dungeon", 17, "normal")
    lblEst = Label(fc,text="Estadisticas de Los Despachos",font= fuenteEstadistica, bg="#19E9EE")
    lblEst.place( x =395, y =380)

     # Boton Estadisticas Cantidad de Despachos VS Tipo
    imgGTorta = PhotoImage(file='imagenes/gtorta.png',master=fc)
    btnGTorta= Button(fc, image=imgGTorta,bd=0)
    btnGTorta.image = imgGTorta
    btnGTorta.place(x=85,y=450)
    lblDvT = Label(fc,text="Canridad de Despachos VS Tipo",font=("Dungeon", 11, "normal"),bg="#19E9EE")
    lblDvT.place(x=20,y=550 )

    # Boton Estadisticas Cantidad de Despachos VS Mes
    imgGbarras = PhotoImage(file='imagenes/gbarras.png',master=fc)
    btnGbarras= Button(fc, image=imgGbarras,bd=0)
    btnGbarras.image = imgGbarras
    btnGbarras.place(x=385,y=450)
    lblDvT = Label(fc,text="Cantidad de Despachos VS Mes",font=("Dungeon", 11, "normal"),bg="#19E9EE")
    lblDvT.place(x=320,y=550 ) """
    

    


    # ---------------------- Frame tabla -------------------------------

    ftabla = Frame(fc)
    ftabla.config(bg="white",width=1000,height=220,relief="groove",bd=3)
    ftabla.place(x=85,y=150,width=1000, height=220)


    tree=ttk.Treeview(ftabla,height=10,columns=('#0','#1','#2','#3','#4','#5','#6','#7','#8')) # Creacion de una Tabla
    horscrlbar = ttk.Scrollbar(ftabla, orient="horizontal", command=tree.xview) # Scrollbar X
    horscrlbar.pack(side='bottom', fill='x')
    verscrlbar = ttk.Scrollbar(ftabla, orient="vertical", command=tree.yview) #Scrollbar Y
    verscrlbar.pack(side='right', fill='y')
    tree.configure(yscrollcommand=verscrlbar.set)
    tree.configure(xscrollcommand=horscrlbar.set)
    tree.pack(side='left')

    tree.column('#0', width=150)     # Configuraciones de la Tabla
    tree.column('#1', width=150)
    tree.column('#2', width=150)
    tree.column('#3', width=150)
    tree.column('#4', width=150)
    tree.column('#5', width=150)
    tree.column('#6', width=150)
    tree.column('#7', width=150)
    tree.column('#8', width=150)

    tree.heading('#0',text='Nombre Cliente', anchor='c')
    tree.heading('#1',text='Direccion Cliente', anchor='c')
    tree.heading('#2',text='Rut Cliente', anchor='c')
    tree.heading('#3',text='Producto', anchor='c')
    tree.heading('#4',text='Transporte', anchor='c')
    tree.heading('#5',text='Nombre Destinatario', anchor='c')
    tree.heading('#6',text='Direccion Destinatario', anchor='c')
    tree.heading('#7',text='Fecha de Registro', anchor='c')
    tree.heading('#8',text='Estado del Despacho', anchor='c')


# ---------------------------------------------------------------------------- Inicia la Vista de los Transportistas ---------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def creaVistaTrans():
    vTrans = Toplevel(root)
    vTrans.geometry("1152x700")
    vTrans.resizable(0,0)
    

    def seleccionarElemento(): # Me permite Registrar una Seleccion en la tabla
        item = tree.item(tree.selection())['values'][1]
        return item
    
   
    def despachaElemento(): # Cambia el estado del despacho a entregado y descuenta la carga del transportista
        data = seleccionarElemento()
        for despacho in listadoDespachos.getLista():
            if despacho.getCliente().getRut()==data:
                despacho.setEntregado(True)
                muestraTrans()
                print(listadoDespachos.mostrarDespachos())

        for trans in listaTransportistas:
            if trans.getClave() == eClave.get():
                newCantidad = trans.getCantidadDespachos() - 1
                trans.setCantidadDespachos(newCantidad)    
        

    def muestraTrans(): # Muestra los despachos exclusivos segun una clave
        registros = tree.get_children()
        for elemnto in registros:
            tree.delete(elemnto)
        for trans in listaTransportistas:
            if trans.getClave() == eClave.get():
                for despacho in trans.getDespachos():
                    tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))


                    
    # -------- Frame Titulo -------------
    ft = Frame(vTrans)
    ft.config(bg="black",width=1152,height=78)
    ft.pack()
    ft.pack_propagate(False)

    imgTitulo = PhotoImage(file='imagenes/transpeque.png', master=ft)
    lbltit = Label(ft,image=imgTitulo, bg="black")
    lbltit.image = imgTitulo
    lbltit.pack()

    # ---------------------------------------- Frame contenido -----------------------------------------
    fc = Frame(vTrans)
    fc.config(bg="#649FB1",width=1152,height=622)
    fc.pack()
    fc.pack_propagate(False)
    imgFondo = PhotoImage(file='imagenes/fondocielo.png', master = fc)
    lblFondo = Label(fc, image= imgFondo)
    lblFondo.image = imgFondo
    lblFondo.place(x = 0, y = 0, relwidth = 1, relheight = 1)


    Font_tuple = ("Dungeon", 13, "normal")
    Label(fc,text="Ingrese su Clave: ",font=Font_tuple,bg="white").place(x = 86, y = 112)
    eClave = Entry(fc)
    eClave.place(x =265,y=118)

    Label(fc,text="Seleccione un Despacho: ",font=Font_tuple,bg="white").place(x = 500, y = 150)
    # ----------------------------------------- Botones ---------------------------------------------------

    # Boton OK
    Button(fc,text="OK",command = muestraTrans).place(x = 400,y = 113)    



    # Boton Para Despachar un Producto
    imgEnviado = PhotoImage(file='imagenes/enviado.png',master=fc)
    btnEnviado = Button(fc, image=imgEnviado,bg="#1E92DA", command = despachaElemento)
    btnEnviado.image = imgEnviado
    btnEnviado.place( x = 960 , y = 440)
    Font_tuple1 = ("Dungeon", 13, "normal")
    lbBuscar = Label(fc,text="Despachado",font= Font_tuple1, bg="#1E92DA")
    lbBuscar.place( x =960, y =550 )



    
    # ------------------------ Tabla -------------------------------
    ftabla = Frame(fc)
    ftabla.config(bg="white",width=1000,height=220,relief="groove",bd=3)
    ftabla.place(x=85,y=200,width=1000, height=220)
   
    

    tree=ttk.Treeview(ftabla,height=10,columns=('#0','#1','#2','#3','#4','#5','#6','#7','#8')) # Creacion de una Tabla
    horscrlbar = ttk.Scrollbar(ftabla, orient="horizontal", command=tree.xview) # Scrollbar X
    horscrlbar.pack(side='bottom', fill='x')
    verscrlbar = ttk.Scrollbar(ftabla, orient="vertical", command=tree.yview) #Scrollbar Y
    verscrlbar.pack(side='right', fill='y')
    tree.configure(yscrollcommand=verscrlbar.set)
    tree.configure(xscrollcommand=horscrlbar.set)
    tree.pack(side='left')

    tree.column('#0', width=150)     # Configuraciones de la Tabla
    tree.column('#1', width=150)
    tree.column('#2', width=150)
    tree.column('#3', width=150)
    tree.column('#4', width=150)
    tree.column('#5', width=150)
    tree.column('#6', width=150)
    tree.column('#7', width=150)
    tree.column('#8', width=150)

    tree.heading('#0',text='Nombre Cliente', anchor='c')
    tree.heading('#1',text='Direccion Cliente', anchor='c')
    tree.heading('#2',text='Rut Cliente', anchor='c')
    tree.heading('#3',text='Producto', anchor='c')
    tree.heading('#4',text='Transporte', anchor='c')
    tree.heading('#5',text='Nombre Destinatario', anchor='c')
    tree.heading('#6',text='Direccion Destinatario', anchor='c')
    tree.heading('#7',text='Fecha de Registro', anchor='c')
    tree.heading('#8',text='Estado del Despacho', anchor='c')



# ---------------------------------------------------------------------------------wwwwwwwwwwwwwww---------------------------------------------------------

def creaVistaGe():
    vGe = Toplevel(root) 
    vGe.geometry("1414x801")

    ft = Frame(vGe) #Frame titulo
    ft.config(width=1414,height=80,bg="black")
    ft.pack()

    fc = Frame(vGe) # Frame contenido
    fc.config(width=1414,height=721)
    fc.pack()
    fc.pack_propagate(False)
    imgGalaxia = PhotoImage(file='imagenes/galaxia.png',master=fc)
    lblFondo = Label(fc, image=imgGalaxia)
    lblFondo.image = imgGalaxia
    lblFondo.place(x=0,y=0)

    fdes = Frame(fc) # Frame sector de despachos
    fdes.config(width=669,height=610,bg="#1A3649")
    fdes.place(x=10,y=20)

    ftra = Frame(fc) # Frame sector de transportistas
    ftra.config(width=700,height=610, bg="#171F50")
    ftra.place(x=700,y=20)


    # ---------------------------- Funciones ----------------------------------------


    def eliminarElemento(): # Elimina el elemnto que seleccione el usuario en la Tabla
        for despacho in listadoDespachos.getLista():
            data = seleccionarElemento()
            if despacho.getCliente().getRut()==data:
                listadoDespachos.eliminarDespacho(despacho)
                mostrarTodo()

    def buscarElemento(): #Busca un elemento determinado y lo muestra en la tabla
        registros = tree.get_children()
        for elemento in registros:
            tree.delete(elemento)

        for despacho in listadoDespachos.getLista():
            if despacho.getCliente().getRut()==buscadorRut.get():
                tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo()))

    def mostrarTodo(): # Muestra los valores de cada despacho en una tabla
        registros = tree.get_children()
        for elemnto in registros:
            tree.delete(elemnto)
        for despacho in listadoDespachos.getLista():
            tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getRut(),despacho.verificarAsignado(),despacho.getTransporte().getTipo(),despacho.verificarEntrega()))

    def seleccionarElemento(): # Me permite Registrar una Seleccion en la tabla
        item = tree.item(tree.selection())['values'][0]
        return item

    def seleccionarElemento2(): # Me permite Registrar una Seleccion en la tabla
        item = tree2.item(tree2.selection())['values'][0]
        return item


    def mostrarTrans(): # Muestra los valores de cada Transportista en una tabla
        registros = tree2.get_children()
        for elemento in registros:
            tree2.delete(elemento)
        for trans in listaTransportistas:
            tree2.insert("",END,text=trans.getTipoTrans(),values=(trans.getNombre(), trans.getCantidadDespachos()))
    
    def asignaDespacho(): # Asigna un despacho a un Transportista
        despacho = seleccionarElemento()
        transportista = seleccionarElemento2()
        
        for trans in listaTransportistas:
            if trans.getNombre() == transportista:
                for des in listadoDespachos.getLista():
                    if des.getCliente().getRut() == despacho:
                        trans.addDespacho(des)
                        des.setAsignado(True)  
                        newCantidad = trans.getCantidadDespachos() + 1
                        trans.setCantidadDespachos(newCantidad)
 
        mostrarTrans()
        mostrarTodo()

    def soloMoto(): # Mustra solo los despachos en moto
        registros = tree2.get_children()
        for elemnto in registros:
            tree2.delete(elemnto)
        for trans in listaTransportistas:
            if trans.getTipoTrans() =="moto":
                tree2.insert("",END,text= trans.getTipoTrans(),values=(trans.getNombre(),trans.getCantidadDespachos()))

    def soloCamioneta(): # Muestra solo los despachos en Camioneta
        registros = tree2.get_children()
        for elemnto in registros:
            tree2.delete(elemnto)
        for trans in listaTransportistas:
            if trans.getTipoTrans() =="camioneta":
                tree2.insert("",END,text= trans.getTipoTrans(),values=(trans.getNombre(),trans.getCantidadDespachos()))
    def soloCamion(): # Muestra solo los despachos en camion
        registros = tree2.get_children()
        for elemnto in registros:
            tree2.delete(elemnto)
        for trans in listaTransportistas:
            if trans.getTipoTrans() =="camion":
                tree2.insert("",END,text= trans.getTipoTrans(),values=(trans.getNombre(),trans.getCantidadDespachos()))

    def noAsignados(): #muestra solo lo no asignados
        registros = tree.get_children()
        for elemnto in registros:
            tree.delete(elemnto)
        for despacho in listadoDespachos.getLista():
            if despacho.getAsignado() == False:
                tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getRut(),despacho.verificarAsignado(),despacho.getTransporte().getTipo()))




    # -------------------------------------- Botones -------------------------------------
    Font_tuple3 = ("Dungeon", 13, "normal")
    Label(fdes, text="Seleccione una operacion",font = Font_tuple3,bg="white").place(x=10,y=20)

    # Boton Buscar
    imgBtnSearch = PhotoImage(file='imagenes/btnbuscar.png',master=fdes)
    labelSearch = Button(fdes, image=imgBtnSearch,bd=0, command = buscarElemento)
    labelSearch.image = imgBtnSearch
    labelSearch.place(x=10,y=60)

    buscadorRut = Entry(fdes) # Entry para que ingresen un rut buscador
    buscadorRut.place(x=10 , y=145)
    
    lbBuscar = Label(fdes,text="Ingrese un rut ej: 20734727-2",font= ("Dungeon", 10, "normal"), bg="white")
    lbBuscar.place( x =140, y =145 )
    
    # Boton Eliminar
    imgBtnElimina = PhotoImage(file='imagenes/btneliminar.png',master=fdes)
    labelElimina = Button(fdes, image=imgBtnElimina,bd=0,command = eliminarElemento)
    labelElimina.image = imgBtnElimina
    labelElimina.place(x=165,y=60)
    
    # Boton Mostrar Todo
    imgBtnMostrar = PhotoImage(file='imagenes/btnmostrar.png',master=fdes)
    labelMostrar = Button(fdes, image=imgBtnMostrar,bd=0, command = mostrarTodo)
    labelMostrar.image = imgBtnMostrar
    labelMostrar.place(x=320,y=60)
    
    # Boton Muestra solo no Asignados
    imgNoAsign = PhotoImage(file='imagenes/noasginados.png',master=fdes)
    btnNoAsign = Button(fdes,image=imgNoAsign,command = noAsignados)
    btnNoAsign.image = imgNoAsign
    btnNoAsign.place(x=475,y=60)

    # Boton Asigna despacho a transportista
    imgAsigna = PhotoImage(file='imagenes/asigna.png',master=ftra)
    btnAsigna = Button(ftra, image=imgAsigna, command= asignaDespacho)
    btnAsigna.image = imgAsigna
    btnAsigna.place(x=350, y = 400) 
    Label(ftra, text="Seleccione un Despacho y un Transportista para Asignar entrega",font = Font_tuple3,bg="white").place(x=10,y=20)

    # Boton solo Moto
    imgMoto = PhotoImage(file='imagenes/solomoto.png', master = ftra)
    btnMoto = Button(ftra, image=imgMoto,bg="white", command=soloMoto)
    btnMoto.image = imgMoto
    btnMoto.place(x=10,y = 60)    

    # Boton solo Camioneta
    imgCamioneta = PhotoImage(file='imagenes/solocamioneta.png', master = ftra)
    btnCamioneta = Button(ftra, image=imgCamioneta,bg="white",command=soloCamioneta)
    btnCamioneta.image = imgCamioneta
    btnCamioneta.place(x =165, y = 60 )

    # Boton solo Camion
    imgCamion = PhotoImage(file='imagenes/solocamion.png',master=ftra)
    btnCamion = Button(ftra, image=imgCamion,bg="white",command=soloCamion)
    btnCamion.image = imgCamion
    btnCamion.place(x =320,y=60)

    # Boton Mostrar Todos los Transportistas
    imgBtnMostrarT = PhotoImage(file='imagenes/btnmostrar.png',master=ftra)
    btnMostrarT = Button(ftra, image=imgBtnMostrarT,command=mostrarTrans)
    btnMostrarT.image = imgBtnMostrarT
    btnMostrarT.place(x=475,y=60)
    
    # -------------------------- Tabla Despachos ----------------------------------------------
        
    ftabla = Frame(fdes)
    ftabla.config(bg="white",width=640,height=220,relief="groove",bd=3)
    ftabla.place(x=10,y=170,width=640, height=220)

    tree=ttk.Treeview(ftabla,height=10,columns=('#0','#1','#2','#3','#4')) # Creacion de una Tabla
    horscrlbar = ttk.Scrollbar(ftabla, orient="horizontal", command=tree.xview) # Scrollbar X
    horscrlbar.pack(side='bottom', fill='x')
    verscrlbar = ttk.Scrollbar(ftabla, orient="vertical", command=tree.yview) #Scrollbar Y
    verscrlbar.pack(side='right', fill='y')
    tree.configure(yscrollcommand=verscrlbar.set)
    tree.configure(xscrollcommand=horscrlbar.set)
    tree.pack(side='left')

    tree.column('#0', width=150)     # Configuraciones de la Tabla
    tree.column('#1', width=150)
    tree.column('#2', width=150)
    tree.column('#3', width=150)
    tree.column('#4', width=150)
    

    tree.heading('#0',text='Nombre Cliente', anchor='c')
    tree.heading('#1',text='Rut Cliente', anchor='c')
    tree.heading('#2',text='Estado del Despacho', anchor='c')
    tree.heading('#3',text='Transporte', anchor='c')
    tree.heading('#4',text='Estado de la Entrega', anchor='c')

    mostrarTodo()

     # -------------------------- Tabla Transportistas ----------------------------------------------
        
    ftabla2 = Frame(ftra)
    ftabla2.config(bg="white",width=461,height=220,relief="groove",bd=3)
    ftabla2.place(x=10,y=170,width=461, height=220)

    tree2=ttk.Treeview(ftabla2,height=10,columns=('#0','#1','#2')) # Creacion de una Tabla
    horscrlbar2 = ttk.Scrollbar(ftabla2, orient="horizontal", command=tree2.xview) # Scrollbar X
    horscrlbar2.pack(side='bottom', fill='x')
    verscrlbar2 = ttk.Scrollbar(ftabla2, orient="vertical", command=tree2.yview) #Scrollbar Y
    verscrlbar2.pack(side='right', fill='y')
    tree2.configure(yscrollcommand=verscrlbar2.set)
    tree2.configure(xscrollcommand=horscrlbar2.set)
    tree2.pack(side='left')

    tree2.column('#0', width=150)     # Configuraciones de la Tabla
    tree2.column('#1', width=150)
    tree2.column('#2', width=150)
   
    tree2.heading('#0',text='Tipo de Transporte', anchor='c')
    tree2.heading('#1',text='Nombre Transportista', anchor='c')
    tree2.heading('#2',text='Cantidad de despachos Asignada', anchor='c')

    mostrarTrans()
    


# -------------------------------------------------- LOGIN ----------------------------------------------------------------------------
def logAd():

    def comprueba():
        if eUsuario.get() =="administrador" and eContraseña.get() == "1111":
            creaVistaAd()
            logAdV.destroy()


    logAdV = Toplevel(root)
    logAdV.geometry("300x200")
    logAdV.resizable(0,0)

    Label(logAdV,text="ADMINISTRADOR").place(x=90,y=10)

    Label(logAdV, text="Usuario: ").place(x=10,y=50)
    eUsuario = Entry(logAdV)
    eUsuario.place(x = 90, y=50)

    Label(logAdV, text="Contraseña: ").place(x=10,y=80)
    eContraseña = Entry(logAdV,show="*")
    eContraseña.place(x=90,y=80)

    Button(logAdV, text="Entrar",command = comprueba).place(x=170,y = 110)
    

def logTra():
    
    def comprueba():
        if eUsuario.get() =="transporte" and eContraseña.get() == "1111":
            creaVistaTrans()
            logAdV.destroy()

    logAdV = Toplevel(root)
    logAdV.geometry("300x200")
    logAdV.resizable(0,0)

    Label(logAdV,text="TRANSPORTISTA").place(x=90,y=10)
    Label(logAdV, text="Usuario: ").place(x=10,y=50)
    eUsuario = Entry(logAdV)
    eUsuario.place(x = 90, y=50)

    Label(logAdV, text="Contraseña: ").place(x=10,y=80)
    eContraseña = Entry(logAdV,show="*")
    eContraseña.place(x=90,y=80)

    Button(logAdV, text="Entrar",command = comprueba).place(x=170,y = 110)


def logGe():
    
    def comprueba():
        if eUsuario.get() =="gerente" and eContraseña.get() == "1111":
            creaVistaGe()
            logAdV.destroy()

    logAdV = Toplevel(root)
    logAdV.geometry("300x200")
    logAdV.resizable(0,0)

    Label(logAdV,text="GERENTE").place(x=90,y=10)
    Label(logAdV, text="Usuario: ").place(x=10,y=50)
    eUsuario = Entry(logAdV)
    eUsuario.place(x = 90, y=50)

    Label(logAdV, text="Contraseña: ").place(x=10,y=80)
    eContraseña = Entry(logAdV,show="*")
    eContraseña.place(x=90,y=80)

    Button(logAdV, text="Entrar",command = comprueba).place(x=170,y = 110)


# --------------------------------------------------------------------------------------------- Vista Principal - root -----------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
root = Tk()
root.geometry("1152x700")
root.resizable(0,0)
imgCielo1 = PhotoImage(file='imagenes/fondito.png')
Label(root,image=imgCielo1).place(x=0,y=0)
Font_tuple1 = ("Dungeon", 20, "normal")

lblOperacion=Label(root, text = 'Seleccione una plataforma', font = Font_tuple1,bg="white")
lblOperacion.place(x=400,y=200)


ta = PhotoImage(file="imagenes/transporte.png")
ad = PhotoImage(file="imagenes/administrador.png")
ge = PhotoImage(file="imagenes/gerente.png")
btnTra = Button(root, image=ta, command=logTra ).place(x=200, y=270)
btnAd = Button(root, image=ad, command=logAd).place(x=500, y=270)
btnGe = Button(root, image=ge, command=logGe).place(x=800, y=270)


root.mainloop()