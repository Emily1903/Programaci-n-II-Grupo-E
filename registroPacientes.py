#importación de libreria
import tkinter as tk 
from tkinter import ttk, messagebox
from datetime import datetime
#función para enmascarar fecha
def enmascarar_fecha(texto): #texto=recibe la fecha
    limpio=''.join(filter(str.isdigit,texto))
    formato_final=""
    
    if len(limpio)>8:
        limpio=limpio[:8]
    if len(limpio)>4:
        formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"#ordena los digitos de 2 en 2, luego l resto queda separado por guión
    elif len(limpio)>2:
        formato_final=f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final=limpio
    
    if fechaN.get() !=formato_final:
        fechaN.delete(0,tk.END)
        fechaN.insert(0,formato_final)
    if len(fechaN.get())==10:
        fecha_actual=datetime.now().date()
        fecha_nacimiento=datetime.strptime(fechaN.get(),"%d-%m-%Y").date()
        edad=fecha_actual.year-fecha_nacimiento.year 
        edadVar.set(edad)
    else:
        edadVar.set("")
    return True

#Guardar archivo de texto
def guardar_en_archivo():
    with open("pacientePeso.txt","w",encoding="utf-8") as archivo2:
        for paciente in paciente_data:
            archivo2.write(
            f"{paciente['Nombre']}|"
            f"{paciente['Fecha de Nacimiento']}|"
            f"{paciente['Edad']}|"
            f"{paciente['Género']}|{paciente['Grupo Sanguíneo']}|"
            f"{paciente['Tipo de Seguro']}|{paciente['Centro Médico']}|"
            f"{paciente['Peso']}\n")
            
#Para cargar los datos al archivo
def cargar_desde_archivo_pacientes():
    try:
        with open("pacientePeso.txt", "r", encoding="utf-8") as archivo:
            paciente_data.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 8:
                    paciente = {
                        "Nombre": datos[0],
                        "Fecha de Nacimiento": datos[1],
                        "Edad": datos[2],
                        "Género": datos[3],
                        "Grupo Sanguíneo": datos[4],
                        "Tipo de Seguro": datos[5],
                        "Centro Médico": datos[6],
                        "Peso": datos[7]
                    }
                    paciente_data.append(paciente)
        cargar_treeview()
    except FileNotFoundError:
        open("pacientePeso.txt", "w", encoding="utf-8").close()
            
#Lista de pacientes(inicialmente vacía)
paciente_data=[]

#Función para registrar paciente
def registrarPaciente():
    #Craer un diccionario con los datos ingresados
    paciente={
        "Nombre":nombreP.get(),
        "Fecha de Nacimiento":fechaN.get(),
        "Edad":edadVar.get(),
        "Género":genero.get(),
        "Grupo Sanguíneo":grupoSanguineo.get(),
        "Tipo de Seguro":tipo_seguro.get(),
        "Centro Médico":centro_medico.get(),
        "Peso":entry_peso.get()
    }
    #Agregar paciente a la lista
    paciente_data.append(paciente)
    guardar_en_archivo()
    cargar_treeview()
    #Cargar Treeview
def cargar_treeview():
    #Limpiar el Treeview
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    #Insertar cada paciente
    for i, item in enumerate(paciente_data):
        treeview.insert(
            "","end",iid=str(i),
            values=(
                item["Nombre"],
                item["Fecha de Nacimiento"],
                item["Edad"],
                item["Género"],
                item["Grupo Sanguíneo"],
                item["Tipo de Seguro"],
                item["Centro Médico"],
                item["Peso"]
            )
        )

#Crear una ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Registro de Pacientes")
ventana_principal.geometry("850x600")

#Nombre
labelNombre=tk.Label(ventana_principal,text="Nombre Completo: ")
labelNombre.grid(row=0,column=0,sticky="w",padx=5,pady=5)
nombreP=tk.Entry(ventana_principal)
nombreP.grid(row=0,column=1,sticky="w",padx=5,pady=5)

#Fecha de nacimiento
labelFechaN=tk.Label(ventana_principal,text="Fecha de Nacimiento: ")
labelFechaN.grid(row=1,column=0,sticky="w",padx=5,pady=5)

validacion_fecha=ventana_principal.register(enmascarar_fecha)
fechaN=ttk.Entry(ventana_principal,validate="key",validatecommand=(validacion_fecha,'%P'))
fechaN.grid(row=1,column=1,sticky="w",padx=5,pady=5)

#Edad(readonly)
labelEdad=tk.Label(ventana_principal,text="Edad: ")
labelEdad.grid(row=2,column=0,sticky="w",padx=5,pady=5)
edadVar=tk.StringVar()
edadP=tk.Entry(ventana_principal,textvariable=edadVar,state="readonly") 
edadP.grid(row=2,column=1,sticky="w",padx=5,pady=5)

#Género
labelGenero=tk.Label(ventana_principal,text="Género: ")
labelGenero.grid(row=3,column=0,sticky="w",padx=5,pady=5)
genero=tk.StringVar()
genero.set("Masculino") #Valor por defecto
radioMasculino=ttk.Radiobutton(ventana_principal,text="Masculino",variable=genero,value="Masculino")
radioMasculino.grid(row=3,column=1,sticky="w",padx=5)
radioFemenino=ttk.Radiobutton(ventana_principal,text="Femenino",variable=genero,value="Femenino")
radioFemenino.grid(row=4,column=1,sticky="w",padx=5)

#Grupo Sanguíneo
labelGrupoSanguineo=tk.Label(ventana_principal,text="Grupo Sanguíneo: ")
labelGrupoSanguineo.grid(row=5,column=0,sticky="w",padx=5,pady=5)
grupoSanguineo=tk.Entry(ventana_principal,text="Grupo Sanguíneo")
grupoSanguineo.grid(row=5,column=1,padx=5,pady=5,sticky="w")

#Tipo de Seguro
labelTipoSeguro=tk.Label(ventana_principal,text="Tipo de seguro: ")
labelTipoSeguro.grid(row=6,column=0,sticky="w",padx=5,pady=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Público")#Valor por defecto
comboTipoSeguro=ttk.Combobox(ventana_principal,values=["Público","Privado","Ninguno"],textvariable=tipo_seguro)
comboTipoSeguro.grid(row=6,column=1,sticky="w",padx=5,pady=5)

#Centro Médico
labelCentroMedico=tk.Label(ventana_principal,text="Centro de salud: ")
labelCentroMedico.grid(row=7,column=0,sticky="w",padx=5,pady=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central") #ValoR por defecto
comboCentroMedico=ttk.Combobox(ventana_principal,values=["Hospital Central","Clínica Norte","Centro Sur"],textvariable=centro_medico)
comboCentroMedico.grid(row=7,column=1,sticky="w",padx=5,pady=5)

#Peso del Paciente
tk.Label(ventana_principal, text="Peso (kg):").grid(row=8, column=0, sticky="w")
entry_peso = tk.Entry(ventana_principal)
entry_peso.grid(row=8, column=1,sticky="w",padx=5,pady=5)

#Frame para los botones
btn_frame=tk.Frame(ventana_principal)
btn_frame.grid(row=9,column=0,columnspan=2,pady=5,sticky="w")

#Botón Registrar
btn_registrar=tk.Button(btn_frame,text="Registrar",command=registrarPaciente)
btn_registrar.grid(row=0,column=0,padx=5)
btn_registrar.configure(bg="Green")

#Botón eliminar
btn_eliminar=tk.Button(btn_frame,text="Eliminar",command="")
btn_eliminar.grid(row=0,column=1,padx=5)
btn_eliminar.configure(bg="Red")

#Crear TreeView para mostrar pacientes
treeview=ttk.Treeview(ventana_principal,columns=("Nombre","FechaN","Edad","Genero","GrupoS","TipoS","CentroM","Peso"),show="headings")

#Definir encabezados
treeview.heading("Nombre",text="Nombre Completo")
treeview.heading("FechaN",text="Fecha Nacimiento")
treeview.heading("Edad",text="Edad")
treeview.heading("Genero",text="Género")
treeview.heading("GrupoS",text="Grupo Sanguíneo")
treeview.heading("TipoS",text="Tipo de Seguro")
treeview.heading("CentroM",text="Centro Médico")
treeview.heading("Peso",text="Peso(kg) del Paciente")

#Definir ancho de columnas
treeview.column("Nombre",width=120)
treeview.column("FechaN",width=120)
treeview.column("Edad",width=50,anchor="center")
treeview.column("Genero",width=70,anchor="center")
treeview.column("GrupoS",width=100,anchor="center")
treeview.column("TipoS",width=100,anchor="center")
treeview.column("CentroM",width=120,anchor="center")
treeview.column("Peso",width=120)

#Indicar el TreeView en la cuadrícula
treeview.grid(row=10,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)

#Scrolibar vertical
scroll_y=ttk.Scrollbar(ventana_principal,orient="vertical",command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=11,column=2,sticky="w")

cargar_desde_archivo_pacientes() #Cargar datos desde el archivo al inciar la palicación
cargar_treeview()#Cargar los datos del treeview

ventana_principal.mainloop()