#importación de libreria
import tkinter as tk 
from tkinter import ttk, messagebox
from datetime import datetime

#DOCTORES 
#PARA CARGAR A UN ARCHIVO
def guardar_en_archivo_doctores():
    with open("doctoresRegistro.txt","w",encoding="utf-8") as archivo:
        for doctor in doctores_data:
            archivo.write(
            f"{doctor['Nombre']}|"
            f"{doctor['Especialidad']}|"
            f"{doctor['Años de Experiencia']}|"
            f"{doctor['Género']}|"
            f"{doctor['Hospital']}\n")
            
def cargar_desde_archivo_doctores():
    try:
        with open("doctoresRegistro.txt", "r", encoding="utf-8") as archivo1:
            doctores_data.clear()
            for linea in archivo1:
                datos_doctor = linea.strip().split("|")
                if len(datos_doctor) == 5:
                    doctor = {
                        "Nombre": datos_doctor[0],
                        "Especialidad": datos_doctor[1],
                        "Años de Experiencia": datos_doctor[2],
                        "Género": datos_doctor[3],
                        "Hospital":datos_doctor[4]
                    }
                    doctores_data.append(doctor)
        Cargar_treeview()
    except FileNotFoundError:
        open("doctoresRegistro.txt", "w", encoding="utf-8").close()
        
#LISTA DE DPCTORES (INICIALMENTE VACIA)
doctores_data=[]
#FUNCION PARA REGITRAR PACIENTE
def registrar_doctor():
    Doctores={  #Crear un diccionario con los datos registrados
        "Nombre": nombreD.get(),
        "Especialidad": especialidad.get(),
        "Años de Experiencia": spin.get(),
        "Género":genero.get(),
        "Hospital":hospital.get()
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
                item["Años de Experiencia"],
                item["Género"],
                item["Hospital"]
            )
        )
        
#Crear una ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Registro de Doctores")
ventana_principal.geometry("600x600")


#Pestaña 
#DOCTORES
labelRegistro=tk.Label(ventana_principal,text="Registro de Doctores")
labelRegistro.grid(row=0,column=1,sticky="w",padx=5,pady=5)
labelRegistro.configure(bg="LightBlue")

#Nombre
labelNombre=tk.Label(ventana_principal,text="Nombre Completo: ")
labelNombre.grid(row=1,column=0,sticky="w",padx=5,pady=5)
labelNombre.configure(bg="LightBlue")
nombreD=tk.Entry(ventana_principal)
nombreD.grid(row=1,column=1,sticky="w",padx=5,pady=5)

#Especialidad
labelEspecialidad=tk.Label(ventana_principal,text="Especialidad: ")
labelEspecialidad.grid(row=2,column=0,sticky="w",padx=5,pady=5)
labelEspecialidad.configure(bg="LightBlue")
especialidad=tk.StringVar()
especialidad.set("Pediatria")#Valor por defecto
comboEspecialidad=ttk.Combobox(ventana_principal,values=["Pediatria","Neurología","Cardiología","Traumatología"],textvariable=especialidad)
comboEspecialidad.grid(row=2,column=1,sticky="w",padx=5,pady=5)

#Años de Experiencia
def mostrarAñosExperiencia():
    tk.messagebox.showinfo("Años de Experiencia",f"Los años de experiencia seleccionada son:{spin.get()}")
labelEdad=tk.Label(ventana_principal,text="Años de Experiencia: ")
labelEdad.grid(row=3,column=0,padx=5,pady=5,sticky="w")
labelEdad.configure(bg="LightBlue")
spin=tk.Spinbox(ventana_principal,from_=1,to=60)
spin.grid(row=3,column=1,padx=5,pady=5,sticky="w")

#Género
labelGenero=tk.Label(ventana_principal,text="Género: ")
labelGenero.grid(row=5,column=0,sticky="w",padx=5,pady=5)
labelGenero.configure(bg="LightBlue")
genero=tk.StringVar()
genero.set("Masculino") #Valor por defecto
radioMasculino=ttk.Radiobutton(ventana_principal,text="Masculino",variable=genero,value="Masculino")
radioMasculino.grid(row=5,column=1,sticky="w",padx=5)
radioFemenino=ttk.Radiobutton(ventana_principal,text="Femenino",variable=genero,value="Femenino")
radioFemenino.grid(row=6,column=1,sticky="w",padx=5)

#Hospital
labelHospital=tk.Label(ventana_principal,text="Hospital: ")
labelHospital.grid(row=7,column=0,sticky="w",padx=5,pady=5)
labelHospital.configure(bg="LightBlue")
hospital=tk.StringVar()
hospital.set("Hospital Central") #Valos por defecto
comboCentroMedico=ttk.Combobox(ventana_principal,values=["Hospital Central","Hospital Norte","Clinica Santa María","Clínica Vida"],textvariable=hospital)
comboCentroMedico.grid(row=7,column=1,sticky="w",padx=5,pady=5)



#Frame para los botones
btn_frame=tk.Frame(ventana_principal)
btn_frame.grid(row=8,column=0,columnspan=2,pady=5,sticky="w")

#Botón Registrar
btn_registrarD=tk.Button(btn_frame,text="Registrar",command=registrar_doctor)
btn_registrarD.grid(row=8,column=0,padx=5)
btn_registrarD.configure(bg="LightGreen")



treeview2=ttk.Treeview(ventana_principal,columns=("Nombre","Especialidad","Años de Experiencia","Género","Hospital"),show="headings")
#Definir encabezados
treeview2.heading("Nombre",text="Nombre Completo")
treeview2.heading("Especialidad",text="Especialidad")
treeview2.heading("Años de Experiencia",text="Años de Experiencia")
treeview2.heading("Género",text="Género")
treeview2.heading("Hospital",text="Hospital")

#Definir ancho de columnas
treeview2.column("Nombre",width=120)
treeview2.column("Especialidad",width=120)
treeview2.column("Años de Experiencia",width=120,anchor="center")
treeview2.column("Género",width=120)
treeview2.column("Hospital",width=120)


#Indicar el TreeView en la cuadrícula
treeview2.grid(row=9,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)

cargar_desde_archivo_doctores()
Cargar_treeview()

ventana_principal.mainloop()