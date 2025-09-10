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
    with open("paciente.txt","w",encoding="utf-8") as archivo2:
        for paciente in paciente_data:
            archivo2.write(
            f"{paciente['Nombre']}|"
            f"{paciente['Fecha de Nacimiento']}|"
            f"{paciente['Edad']}|"
            f"{paciente['Género']}|{paciente['Grupo Sanguíneo']}|"
            f"{paciente['Tipo de Seguro']}|{paciente['Centro Médico']}\n")
            
def cargar_desde_archivo_pacientes():
    try:
        with open("paciente.txt","r",encoding="utf-8")as archivo:
            paciente_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==7:
                    paciente={
                        "Nombre":datos[0],
                        "Fecha de Nacimiento":datos[1],
                        "Edad":datos[2],
                        "Género":datos[3],
                        "Tipo de Seguro":datos[3],
                        "Grupo Sanguíneo":datos[5],
                        "Centro Médico":datos[6]
                    }
                    paciente_data.append(paciente)
        cargar_treeview()
    except FileNotFoundError:
        open("paciente.txt","w",encoding="uft-8").close()
            
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
        "Centro Médico":centro_medico.get()
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
                item["Centro Médico"]
            )
        )
#Función para eliminar paciente
def eliminarPaciente():
    seleccionado=treeview.selection()
    if seleccionado:
        indice=int(seleccionado[0])
        id_item=seleccionado[0]
        if messagebox.askyesno("Eliminar Paciente",f"¿Está seguro de eliminar el paciente{treeview.item(id_item,'values')[0]}'?"):
            del paciente_data[indice]
            guardar_en_archivo() #Guardar los cambios en el archivo
            cargar_treeview()
            messagebox.showinfo("Eliminar Paciente","Paciente eliminado exitosamente.")
        else: #este else es del if seleccionado
            messagebox.showwarning("Eliminar Paciente","No se ha seleccionado ningún paciente.")
            return

#DOCTORES 
#PARA CARGAR A UN ARCHIVO
def guardar_en_archivo_doctores():
    with open("doctor.txt","w",encoding="utf-8") as archivo:
        for doctor in doctores_data:
            archivo.write(
            f"{doctor['Nombre']}|"
            f"{doctor['Especialidad']}|"
            f"{doctor['Edad']}|"
            f"{doctor['Teléfono']}\n")
            
def cargar_desde_archivo_doctores():
    try:
        with open("doctor.txt", "r", encoding="utf-8") as archivo1:
            doctores_data.clear()
            for linea in archivo1:
                datos_doctor = linea.strip().split("|")
                if len(datos_doctor) == 4:
                    doctor = {
                        "Nombre": datos_doctor[0],
                        "Especialidad": datos_doctor[1],
                        "Edad": datos_doctor[2],
                        "Telefono": datos_doctor[3],
                    }
                    doctores_data.append(doctor)
        Cargar_treeview()
    except FileNotFoundError:
        open("doctor.txt", "w", encoding="utf-8").close()
        
#Evento Cambiar pesteña
def al_cambiar_pestaña(event):
    pestaña_activa=pestañas.index(pestañas.select())
    if pestaña_activa==0: #Pacientes
        cargar_desde_archivo_pacientes()
    elif pestaña_activa==1: #Doctores
        cargar_desde_archivo_doctores() 
        

#LISTA DE DPCTORES (INICIALMENTE VACIA)
doctores_data=[]
#FUNCION PARA REGITRAR PACIENTE
def registrar_doctor():
    Doctores={  #Crear un diccionario con los datos registrados
        "Nombre": nombreD.get(),
        "Especialidad": especialidad.get(),
        "Edad": spin.get(),
        "Teléfono": telefonoD.get(),
    }
    #AGREGAR DOCTOR A LA LISTA
    doctores_data.append(Doctores)
    guardar_en_archivo_doctores()
    Cargar_treeview()
#CARGAR EL TREEVIEW
def Cargar_treeview():
    #limpiar el treeview
    for doctor in treeview2.get_children():
        treeview2.delete(doctor)
    #Insertar cada paciente
    for a, item in enumerate(doctores_data):
        treeview2.insert(
            "", "end", iid=str(a),
            values=(
                item["Nombre"],
                item["Especialidad"],
                item["Edad"],
                item["Teléfono"],
            )
        )
#FUNCION PARA ELIMINAR DOCTORES      
def eliminarDoctor():
    doctor_seleccionado=treeview2.selection()
    if doctor_seleccionado:
        indice2=int(doctor_seleccionado[0])
        id_itemD=doctor_seleccionado[0]
        if messagebox.askyesno("Eliminar Doctor",f"¿Está seguro de eliminar el doctor {treeview2.item(id_itemD,'values')[0]}'?"):
            del doctores_data[indice2]
            guardar_en_archivo_doctores() #Guardar los cambios en el archivo
            cargar_treeview()
            messagebox.showinfo("Eliminar Doctor","Doctor eliminado exitosamente.")
        else: #este else es del if seleccionado
            messagebox.showwarning("Eliminar Doctor","No se ha seleccionado ningún doctor.")
            return
        

#Crear una ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("700x700")

#Crear contenedor Notebook(pestañas)
pestañas=ttk.Notebook(ventana_principal)
#Crear frames(uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)
#Agregar pestañas al Notebook(para organizar el contenido)
pestañas.add(frame_pacientes,text="Pacientes")

#Mostrar las pestañas en la ventana
pestañas.pack(expand=True,fill="both") #fill=relleno, both para que se muestre en todo el espacio

#Nombre
labelNombre=tk.Label(frame_pacientes,text="Nombre Completo: ")
labelNombre.grid(row=0,column=0,sticky="w",padx=5,pady=5)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0,column=1,sticky="w",padx=5,pady=5)

#Fecha de nacimiento
labelFechaN=tk.Label(frame_pacientes,text="Fecha de Nacimiento: ")
labelFechaN.grid(row=1,column=0,sticky="w",padx=5,pady=5)

validacion_fecha=ventana_principal.register(enmascarar_fecha)
fechaN=ttk.Entry(frame_pacientes,validate="key",validatecommand=(validacion_fecha,'%P'))
fechaN.grid(row=1,column=1,sticky="w",padx=5,pady=5)

#Edad(readonly)
labelEdad=tk.Label(frame_pacientes,text="Edad: ")
labelEdad.grid(row=2,column=0,sticky="w",padx=5,pady=5)
edadVar=tk.StringVar()
edadP=tk.Entry(frame_pacientes,textvariable=edadVar,state="readonly") 
edadP.grid(row=2,column=1,sticky="w",padx=5,pady=5)

#Género
labelGenero=tk.Label(frame_pacientes,text="Género: ")
labelGenero.grid(row=3,column=0,sticky="w",padx=5,pady=5)
genero=tk.StringVar()
genero.set("Masculino") #Valor por defecto
radioMasculino=ttk.Radiobutton(frame_pacientes,text="Masculino",variable=genero,value="Masculino")
radioMasculino.grid(row=3,column=1,sticky="w",padx=5)
radioFemenino=ttk.Radiobutton(frame_pacientes,text="Femenino",variable=genero,value="Femenino")
radioFemenino.grid(row=4,column=1,sticky="w",padx=5)

#Grupo Sanguíneo
labelGrupoSanguineo=tk.Label(frame_pacientes,text="Grupo Sanguíneo: ")
labelGrupoSanguineo.grid(row=5,column=0,sticky="w",padx=5,pady=5)
grupoSanguineo=tk.Entry(frame_pacientes,text="Grupo Sanguíneo")
grupoSanguineo.grid(row=5,column=1,padx=5,pady=5,sticky="w")

#Tipo de Seguro
labelTipoSeguro=tk.Label(frame_pacientes,text="Tipo de seguro: ")
labelTipoSeguro.grid(row=6,column=0,sticky="w",padx=5,pady=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Público")#Valor por defecto
comboTipoSeguro=ttk.Combobox(frame_pacientes,values=["Público","Privado","Ninguno"],textvariable=tipo_seguro)
comboTipoSeguro.grid(row=6,column=1,sticky="w",padx=5,pady=5)

#Centro Médico
labelCentroMedico=tk.Label(frame_pacientes,text="Centro de salud: ")
labelCentroMedico.grid(row=7,column=0,sticky="w",padx=5,pady=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central") #Valos por defecto
comboCentroMedico=ttk.Combobox(frame_pacientes,values=["Hospital Central","Clínica Norte","Centro Sur"],textvariable=centro_medico)
comboCentroMedico.grid(row=7,column=1,sticky="w",padx=5,pady=5)

#Frame para los botones
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=8,column=0,columnspan=2,pady=5,sticky="w")

#Botón Registrar
btn_registrar=tk.Button(btn_frame,text="Registrar",command=registrarPaciente)
btn_registrar.grid(row=0,column=0,padx=5)
btn_registrar.configure(bg="Green")

#Botoón eliminar
btn_eliminar=tk.Button(btn_frame,text="Eliminar",command=eliminarPaciente)
btn_eliminar.grid(row=0,column=1,padx=5)
btn_eliminar.configure(bg="Red")

#Crear TreeView para mostrar pacientes
treeview=ttk.Treeview(frame_pacientes,columns=("Nombre","FechaN","Edad","Genero","GrupoS","TipoS","CentroM"),show="headings")

#Definir encabezados
treeview.heading("Nombre",text="Nombre Completo")
treeview.heading("FechaN",text="Fecha Nacimiento")
treeview.heading("Edad",text="Edad")
treeview.heading("Genero",text="Género")
treeview.heading("GrupoS",text="Grupo Sanguíneo")
treeview.heading("TipoS",text="Tipo de Seguro")
treeview.heading("CentroM",text="Centro Médico")

#Definir ancho de columnas
treeview.column("Nombre",width=120)
treeview.column("FechaN",width=120)
treeview.column("Edad",width=50,anchor="center")
treeview.column("Genero",width=60,anchor="center")
treeview.column("GrupoS",width=100,anchor="center")
treeview.column("TipoS",width=100,anchor="center")
treeview.column("CentroM",width=120)

#Indicar el TreeView en la cuadrícula
treeview.grid(row=7,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)

#Scrolibar vertical
scroll_y=ttk.Scrollbar(frame_pacientes,orient="vertical",command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=9,column=2,sticky="w")


#Pestaña 
#DOCTORES
frame_doctores=ttk.Frame(pestañas)
pestañas.add(frame_doctores,text="Doctores")
pestañas.pack(expand=True,fill="both")

labelRegistro=tk.Label(frame_doctores,text="Registro de Doctores")
labelRegistro.grid(row=0,column=0,sticky="w",padx=5,pady=5)

#Nombre
labelNombre=tk.Label(frame_doctores,text="Nombre Completo: ")
labelNombre.grid(row=1,column=0,sticky="w",padx=5,pady=5)
nombreD=tk.Entry(frame_doctores)
nombreD.grid(row=1,column=1,sticky="w",padx=5,pady=5)

#Especialidad
labelEspecialidad=tk.Label(frame_doctores,text="Especialidad: ")
labelEspecialidad.grid(row=2,column=0,sticky="w",padx=5,pady=5)
especialidad=tk.StringVar()
especialidad.set("Pediatria")#Valor por defecto
comboEspecialidad=ttk.Combobox(frame_doctores,values=["Pediatria","Neurología","Cardiología","Traumatología"],textvariable=especialidad)
comboEspecialidad.grid(row=2,column=1,sticky="w",padx=5,pady=5)

#Edad
def mostrarEdad():
    tk.messagebox.showinfo("Edad",f"La edad seleccionada es:{spin.get()}")
labelEdad=tk.Label(frame_doctores,text="Edad: ")
labelEdad.grid(row=3,column=0,padx=5,pady=5,sticky="w")
spin=tk.Spinbox(frame_doctores,from_=1,to=80)
spin.grid(row=3,column=1,padx=5,pady=5,sticky="w")

#Teléfono
labelTelefono=tk.Label(frame_doctores,text="Teléfono: ")
labelTelefono.grid(row=4,column=0,sticky="w",padx=5,pady=5)
telefonoD=tk.Entry(frame_doctores)
telefonoD.grid(row=4,column=1,sticky="w",padx=5,pady=5)

#Frame para los botones
btn_frame=tk.Frame(frame_doctores)
btn_frame.grid(row=5,column=0,columnspan=2,pady=5,sticky="w")

#Botón Registrar
btn_registrarD=tk.Button(btn_frame,text="Registrar",command=registrar_doctor)
btn_registrarD.grid(row=1,column=0,padx=5)
btn_registrarD.configure(bg="LightGreen")

#Botoón eliminar
btn_eliminarD=tk.Button(btn_frame,text="Eliminar",command=eliminarDoctor)
btn_eliminarD.grid(row=1,column=1,padx=5)
btn_eliminarD.configure(bg="OrangeRed")

treeview2=ttk.Treeview(frame_doctores,columns=("Nombre","Especialidad","Edad","Teléfono"),show="headings")
#Definir encabezados
treeview2.heading("Nombre",text="Nombre Completo")
treeview2.heading("Especialidad",text="Especialidad")
treeview2.heading("Edad",text="Edad")
treeview2.heading("Teléfono",text="Teléfono")
#Definir ancho de columnas
treeview2.column("Nombre",width=120)
treeview2.column("Especialidad",width=120)
treeview2.column("Edad",width=60,anchor="center")
treeview2.column("Teléfono",width=120,anchor="center")
#Indicar el TreeView en la cuadrícula
treeview2.grid(row=7,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)

#Asociar evento de cambio de pestaña
#pestañas.bind("<<NoteboookTabChanged>>>",al_cambiar_pestaña)

cargar_desde_archivo_pacientes() #Cargar datos desde el archivo al inciar la palicación

ventana_principal.mainloop()