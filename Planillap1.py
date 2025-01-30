from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Toplevel
from tkinter import ttk
import tkinter as tk
import sqlite3

# Crear la base de datos y la tabla
def crear_base_datos():
    conn = sqlite3.connect('planilla.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            razon_social TEXT,
            actividad_economica TEXT,
            dia TEXT,
            mes TEXT,
            año TEXT,
            tipo_evaluacion TEXT,
            nombre_apellido TEXT,
            cedula TEXT,
            edad INTEGER,
            genero TEXT,
            estado_civil TEXT,
            lugar_nacimiento TEXT,
            fecha_nacimiento TEXT,
            nivel_escolar TEXT,
            telefono TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Guardar los datos en la base de datos
def guardar_datos():
    razon_social = razonsocial_entry.get()
    actividad_economica = actividadeconomica_entry.get()
    dia = combobox_dia.get()
    mes = combobox_mes.get()
    año = combobox_año.get()
    tipo_evaluacion = opcionesevaluacion.get()
    nombre_apellido_val = apellidosnombres_entry.get()
    cedula_val = cedula_entry.get()
    edad_val = edad_entry.get()
    genero_val = combobox_genero.get()
    estado_civil_val = combobox_estado_civil.get()
    lugar_nacimiento_val = lugar_nacimiento_entry.get()
    fecha_nacimiento_val = f"{combobox_dia_nacimiento.get()}/{combobox_mes_nacimiento.get()}/{combobox_año_nacimiento.get()}"
    nivel_escolar_val = nivelescolar_entry.get()
    telefono_val = telefono_entry.get()

    conn = sqlite3.connect('planilla.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO registros (razon_social, actividad_economica, dia, mes, año, tipo_evaluacion, nombre_apellido, cedula, edad, genero, estado_civil, lugar_nacimiento, fecha_nacimiento, nivel_escolar, telefono)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (razon_social, actividad_economica, dia, mes, año, tipo_evaluacion, nombre_apellido_val, cedula_val, edad_val, genero_val, estado_civil_val, lugar_nacimiento_val, fecha_nacimiento_val, nivel_escolar_val, telefono_val))
    conn.commit()
    conn.close()
    messagebox.showinfo("Información", "Datos guardados exitosamente")


def crear_tabla_con_encabezados_verticales(cuadrotiempo, encabezados, ancho_columna=30, altura_columna=170):
    """
    Crea una tabla con encabezados verticales en una ventana de Tkinter.

    Args:
        cuadrotiempo: El frame donde se colocarán los encabezados.
        encabezados: Una lista con los nombres de las columnas.
        ancho_columna: El ancho deseado de cada columna en píxeles.
        altura_columna: La altura deseada de cada columna en píxeles.
    """

    # Crear un LabelFrame para cada encabezado
    for i, encabezado in enumerate(encabezados):
        labelframe = tk.LabelFrame(cuadrotiempo, width=ancho_columna, height=altura_columna)
        labelframe.grid(row=0, column=i+1, padx=1, pady=1)  # Ajustar la columna para que empiece desde 1
        labelframe.pack_propagate(False)  # Evitar que el LabelFrame cambie de tamaño

        # Crear un canvas dentro del LabelFrame para el texto rotado
        canvas = tk.Canvas(labelframe, width=ancho_columna, height=altura_columna)
        canvas.create_text(ancho_columna // 2, altura_columna // 2, text=encabezado, anchor="center", angle=90)
        canvas.pack()

def crear_rows_revision_por_sistema(parent, text, variable, entry_variable, row):
    """
    Crea una fila en un grid layout con una etiqueta, dos radiobuttons y un campo de entrada.

    Args:
        parent (tk.Widget): El widget padre donde se colocarán los elementos.
        text (str): El texto de la etiqueta.
        variable (tk.IntVar): La variable asociada a los radiobuttons.
        entry_variable (tk.StringVar): La variable asociada al campo de entrada.
        row (int): La fila en la que se colocarán los elementos en el grid layout.

    Ejemplo:
        frameRevisionPorSistema = tk.LabelFrame(frame_contenido, text="REVISION POR SISTEMA", font=(bool))
        frameRevisionPorSistema.grid(row=0, column=0, padx=10, pady=10)
        
        opcpielfaneras = tk.IntVar()
        hipertencionarterial = tk.StringVar()
        
        crear_rows_revision_por_sistema(frameRevisionPorSistema, "PIEL Y FANERAS", opcpielfaneras, hipertencionarterial, 1)

    Esta función crea una etiqueta, dos radiobuttons y un campo de entrada en la fila especificada del grid layout del widget padre.
    """

    label = Label(parent, text=text)
    label.grid(row=row, column=0, sticky="w", padx=5, pady=2)
    
    radio1 = tk.Radiobutton(parent, text="", width=4, anchor="n", variable=variable, value=1)
    radio1.grid(row=row, column=1, padx=5, pady=1)
    
    radio2 = tk.Radiobutton(parent, text="", width=4, anchor="n", variable=variable, value=2)
    radio2.grid(row=row, column=2, padx=5, pady=1)
    
    entry = Entry(parent, textvariable=entry_variable, width=93)
    entry.grid(row=row, column=3, padx=5, pady=2)

ventana = tk.Tk()
ventana.title("Planilla de registro MO")
ventana.geometry("920x700")

# Crear la base de datos y la tabla al iniciar la aplicación
crear_base_datos()

# Crear un Frame contenedor
contenedor = tk.Frame(ventana)
contenedor.pack(fill=BOTH, expand=True)

# Crear un Canvas
canvas = tk.Canvas(contenedor)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Crear una barra de desplazamiento vertical
scrollbar = ttk.Scrollbar(contenedor, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configurar el Canvas para usar la barra de desplazamiento
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", on_mouse_wheel)

# Crear un Frame dentro del Canvas
frame_contenido = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame_contenido, anchor="nw")

# Ahora puedes agregar widgets al frame_contenido en lugar de ventana
frame1 = tk.Frame(frame_contenido)
frame1.pack(anchor="w")

# Cargar la imagen
#imagen = PhotoImage(file="imagen1.png")
# Crear un Label con la imagen
#imagenlabel = Label(frame1, image=imagen)
#imagenlabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

cuadroRIF = Label(frame1, text="GERENCIA MEDICA MATURIN, C.A.\nRIF. J-31209675-6", fg="blue", font=(16))
cuadroRIF.grid(row=0, column=1, sticky="w", padx=10, pady=10)
#cuadroRIF = Label(frame1, text="RIF. J-31209675-6", fg="blue")
#cuadroRIF.grid(row=1, column=1, sticky="w", padx=10, pady=10)

cuadronombrepla = Label(frame1, text="", width=20)
cuadronombrepla.grid(row=0, column=2, sticky="e", padx=10, pady=10)
cuadronombrepla = Label(frame1, text="HISTOROAL MEDICO OCUPACIONAL", font=(26))
cuadronombrepla.grid(row=0, column=3, sticky="e", padx=10, pady=10)

frame2 = tk.Frame(frame_contenido)
frame2.pack(anchor="w")

cuadrofechaevaluacion = tk.LabelFrame(frame2)
cuadrofechaevaluacion.grid(row=1, column=0, padx=10, pady=10)

# Crear combobox para la fecha
dias = [str(i) for i in range(1, 32)]
meses = [str(i) for i in range(1, 13)]
años = [str(i) for i in range(2000, 2031)]

framefecha = tk.Frame(cuadrofechaevaluacion)
framefecha.grid(row=0, column=0, padx=10, pady=10)

combobox_dia = ttk.Combobox(framefecha, values=dias, width=5)
combobox_dia.grid(row=1, column=0, padx=10, pady=10)
combobox_dia.set("Día")

combobox_mes = ttk.Combobox(framefecha, values=meses, width=5)
combobox_mes.grid(row=1, column=1, padx=10, pady=10)
combobox_mes.set("Mes")

combobox_año = ttk.Combobox(framefecha, values=años, width=7)
combobox_año.grid(row=1, column=2, padx=10, pady=10)
combobox_año.set("Año")

cuadroevaluacion = tk.LabelFrame(frame2)
cuadroevaluacion.grid(row=1, column=1, padx=10, pady=10)
opcionesevaluacion = tk.IntVar()

# Crear frames para organizar los radiobuttons
frame_izquierda = tk.Frame(cuadroevaluacion)
frame_izquierda.grid(row=0, column=0, padx=10, pady=10)

frame_centro = tk.Frame(cuadroevaluacion)
frame_centro.grid(row=0, column=1, padx=10, pady=10)

frame_derecha = tk.Frame(cuadroevaluacion)
frame_derecha.grid(row=0, column=2, padx=10, pady=10)

fechaevaluacion = Label(frame2, text="FECHA DE EVALUACION", font=bool)
fechaevaluacion.grid(row=0, column=0, sticky="w", padx=10, pady=10)

tipoevaluacion = Label(frame2, text="TIPO DE EVALUACION", font=bool)
tipoevaluacion.grid(row=0, column=1, sticky="w", padx=10, pady=10)



# Añadir radiobuttons a los frames correspondientes
opcion1 = tk.Radiobutton(frame_izquierda, text="PRE EMPLEO", width=22, anchor="w", variable=opcionesevaluacion, value=1)
opcion1.pack()
opcion2 = tk.Radiobutton(frame_izquierda, text="EGRESO", width=22, anchor="w", variable=opcionesevaluacion, value=2)
opcion2.pack()
opcion3 = tk.Radiobutton(frame_centro, text="PRE VACACIONAL",  width=22, anchor="w", variable=opcionesevaluacion, value=3)
opcion3.pack()
opcion4 = tk.Radiobutton(frame_centro, text="POST VACACIONAL", width=22, anchor="w", variable=opcionesevaluacion, value=4)
opcion4.pack()
opcion5 = tk.Radiobutton(frame_derecha, text="PERIODICOS", width=22, anchor="w", variable=opcionesevaluacion, value=5)
opcion5.pack()
opcion6 = tk.Radiobutton(frame_derecha, text="OTROS", width=22, anchor="w", variable=opcionesevaluacion, value=6)
opcion6.pack()

frame3 = tk.Frame(frame_contenido)
frame3.pack(anchor="w")

razonsocial = StringVar()
actividadeconomica = StringVar()

cuadrorazonsocial = tk.LabelFrame(frame3, text="RAZON SOCIAL", width=67)
cuadrorazonsocial.grid(row=1, column=0, padx=10, pady=10)

razonsocial_entry = Entry(cuadrorazonsocial, textvariable=razonsocial, width=67)
razonsocial_entry.grid(row=1, column=0, padx=10, pady=10)

cuadroactividadeconomica = tk.LabelFrame(frame3, text="ACTIVIDAD ECONOMICA", width=67)
cuadroactividadeconomica.grid(row=1, column=1, padx=10, pady=10)

actividadeconomica_entry = Entry(cuadroactividadeconomica, textvariable=actividadeconomica, width=67)
actividadeconomica_entry.grid(row=1, column=1, padx=10, pady=10)

Idempresa = Label(frame3, text="IDENTIFICACION DE LA EMPRESA", font=bool)
Idempresa.grid(row=0, column=0, sticky="w", padx=10, pady=10)

frame4 = tk.Frame(frame_contenido)
frame4.pack(anchor="w")

apellidosnombres = StringVar()
cedula = IntVar()
edad = IntVar()
genero = StringVar()
stadocivil = StringVar()
lugardenacimiento = StringVar()
fechanacimiento = StringVar()
nivelescolar = StringVar()
telefono = IntVar()

cuadroapellidosnombres = tk.LabelFrame(frame4, text="APELLIDOS Y NOMBRES", width=71)
cuadroapellidosnombres.grid(row=1, column=0, padx=5, pady=10)
apellidosnombres_entry = Entry(cuadroapellidosnombres, textvariable=apellidosnombres, width=71)
apellidosnombres_entry.grid(row=1, column=0, padx=5, pady=10)

cuadrocedula = tk.LabelFrame(frame4, text="CEDULA", width=25)
cuadrocedula.grid(row=1, column=1, padx=5, pady=10)
cedula_entry = Entry(cuadrocedula, textvariable=cedula, width=25)
cedula_entry.grid(row=1, column=1, padx=5, pady=10)


miniframedatospostulados = Frame(frame4)
miniframedatospostulados.grid(row=2, column=0, padx=10, pady=10)

cuadroedad = tk.LabelFrame(miniframedatospostulados, text="Edad", width=10)
cuadroedad.grid(row=1, column=2, padx=5, pady=10)
edad_entry = Entry(cuadroedad, textvariable=edad, width=10)
edad_entry.grid(row=1, column=2, padx=5, pady=10)

cuadrogenero = tk.LabelFrame(miniframedatospostulados, text="Genero", width=30)
cuadrogenero.grid(row=1, column=3, padx=5, pady=10)
combobox_genero = ttk.Combobox(cuadrogenero, values=["Hombre", "Mujer", "Otros"], width=5)
combobox_genero.grid(row=1, column=3, padx=5, pady=10)
combobox_genero.set("Sexo")

cuadroestadocivil = tk.LabelFrame(miniframedatospostulados, text="Estado Civil", width=30)
cuadroestadocivil.grid(row=1, column=4, padx=5, pady=10)
combobox_estado_civil = ttk.Combobox(cuadroestadocivil, values=["Soltero", "Casado", "Divorciado", "Viudo"], width=5)
combobox_estado_civil.grid(row=1, column=4, padx=5, pady=10)
combobox_estado_civil.set("Estado")

cuadrolugarnacimiento = tk.LabelFrame(frame4, text="LUGAR DE NACIMIENTO", width=35)
cuadrolugarnacimiento.grid(row=1, column=2, padx=5, pady=10)
lugar_nacimiento_entry = Entry(cuadrolugarnacimiento, textvariable=lugardenacimiento, width=35)
lugar_nacimiento_entry.grid(row=1, column=2, padx=5, pady=10)

cuadrofechanacimiento = tk.LabelFrame(miniframedatospostulados, text="FECHA DE NACIMIENTO", width=30)
cuadrofechanacimiento.grid(row=1, column=5, padx=5, pady=10)

# Crear combobox para la fecha de nacimiento
combobox_dia_nacimiento = ttk.Combobox(cuadrofechanacimiento, values=dias, width=5)
combobox_dia_nacimiento.grid(row=2, column=1, padx=5, pady=10)
combobox_dia_nacimiento.set("Día")

combobox_mes_nacimiento = ttk.Combobox(cuadrofechanacimiento, values=meses, width=5)
combobox_mes_nacimiento.grid(row=2, column=2, padx=5, pady=10)
combobox_mes_nacimiento.set("Mes")

combobox_año_nacimiento = ttk.Combobox(cuadrofechanacimiento, values=años, width=7)
combobox_año_nacimiento.grid(row=2, column=3, padx=5, pady=10)
combobox_año_nacimiento.set("Año")

cuadrotelefono = tk.LabelFrame(frame4, text="TELEFONO", width=25)
cuadrotelefono.grid(row=2, column=1, padx=5, pady=10)
telefono_entry = Entry(cuadrotelefono, textvariable=telefono, width=25)
telefono_entry.grid(row=2, column=1, padx=5, pady=10)

cuadronivelescolar = tk.LabelFrame(frame4, text="NIVEL ESCOLAR", width=35)
cuadronivelescolar.grid(row=2, column=2, padx=5, pady=10)
nivelescolar_entry = Entry(cuadronivelescolar, textvariable=nivelescolar, width=35)
nivelescolar_entry.grid(row=2, column=2, padx=5, pady=10)


datostrabajadoropostulado = Label(frame4, text="DATOS DEL TRABAJADOR O POSTULADO", font=bool)
datostrabajadoropostulado.grid(row=0, column=0, sticky="w", padx=10, pady=10)


frame5 = tk.Frame(frame_contenido)
frame5.pack(anchor="w")

antiguedadenpresa = StringVar()
cargoactual = StringVar()
antiguedadencargo = StringVar()
descriccioncargo = Text()
jornadadetrabajo = tk.IntVar()

miniframeinformacionocupacinal = Frame(frame5)
miniframeinformacionocupacinal.grid(row=1, column=0, padx=5, pady=10)

cuadroantiguedadenpresa= tk.LabelFrame(miniframeinformacionocupacinal, text="ANTIGUEDAD EN LA EMPRESA", width=44)
cuadroantiguedadenpresa.grid(row=1, column=0, padx=5, pady=10)
cuadroantiguedadenpresa_entry = Entry(cuadroantiguedadenpresa, textvariable=antiguedadenpresa, width=44)
cuadroantiguedadenpresa_entry.grid(row=1, column=0, padx=5, pady=10)

cuadrocargoactual = tk.LabelFrame(miniframeinformacionocupacinal, text="CARGO ACTUAL O A DESEMPENAR", width=4)
cuadrocargoactual.grid(row=1, column=1, padx=5, pady=10)
cargoactual_entry = Entry(cuadrocargoactual, textvariable=cargoactual, width=44)
cargoactual_entry.grid(row=1, column=1, padx=5, pady=10)

cuadroantiguedadencargo = tk.LabelFrame(frame5, text="ANTIGUEDAD EN EL CARGO", width=44)
cuadroantiguedadencargo.grid(row=1, column=1, padx=5, pady=10)
antiguedadencargo_entry = Entry(cuadroantiguedadencargo, textvariable=antiguedadencargo, width=44)
antiguedadencargo_entry.grid(row=1, column=1, padx=5, pady=10)

cuadrodescriccioncargo = tk.LabelFrame(frame5, text="DESCRIPCION DEL CARGO", width=70)
cuadrodescriccioncargo.grid(row=2, column=0, padx=5, pady=10)
descriccioncargo_entry = Text(cuadrodescriccioncargo, height=2, width=70)
descriccioncargo_entry.grid(row=2, column=0, padx=5, pady=10)

cuadrojornadatrabajo = tk.LabelFrame(frame5, text="JORNADA DE TRABAJO")
cuadrojornadatrabajo.grid(row=2, column=1, padx=5, pady=10)
opcionejornadatrabajo = tk.IntVar()

# Crear frames para organizar los radiobuttons
frame_izquierda = tk.Frame(cuadrojornadatrabajo)
frame_izquierda.grid(row=0, column=0, padx=5, pady=10)

frame_derecha = tk.Frame(cuadrojornadatrabajo)
frame_derecha.grid(row=0, column=1, padx=5, pady=10)

# Añadir radiobuttons a los frames correspondientes
opcion1 = tk.Radiobutton(frame_izquierda, text="DIURNA", width=10, anchor="w", variable=opcionesevaluacion, value=1)
opcion1.pack()
opcion2 = tk.Radiobutton(frame_izquierda, text="ROTATIVA", width=10, anchor="w", variable=opcionesevaluacion, value=2)
opcion2.pack()
opcion3 = tk.Radiobutton(frame_derecha, text="NOCTURNA", width=10, anchor="w", variable=opcionesevaluacion, value=3)
opcion3.pack()
opcion4 = tk.Radiobutton(frame_derecha, text="OTROS MIXTO", width=10, anchor="w", variable=opcionesevaluacion, value=4)
opcion4.pack()



datospostulado = Label(frame5, text="INFORMACION OCUPACIONAL", font=bool)
datospostulado.grid(row=0, column=0, sticky="w", padx=5, pady=10)


frame6 = tk.Frame(frame_contenido)
frame6.pack(anchor="w")

cuadrotiempo = LabelFrame(frame6, text="", width=300, height=500)
cuadrotiempo.grid(row=1, column=0, padx=5, pady=10)

nombreempresa = Label(cuadrotiempo, text="NOMBRE DE LA EMPRESA")
nombreempresa.grid(row=0, column=0, padx=5, pady=5)

nombreempresa_entry1 = Entry(cuadrotiempo, width=33)
nombreempresa_entry1.grid(row=1, column=0, padx=5, pady=5)

encabezados = ["Tiempo de Exposicion", "Iluminacion", "Radiaciones Ionizantes", "Radiaciones no Ionizantes", "Ruido", "Bajas Temperaturas", "Altas Temperaturas", "Vibraciones", "Electricidad", "Gases", "Humos", "Vapores", "Polvos", "Liquidos", "Fibras", "Altas Presiones", "Levantamientos de Cargas", "Esfuerzo Fisico", "Disergonomicos", "Psicosociales", "Biologicos"]
crear_tabla_con_encabezados_verticales(cuadrotiempo, encabezados)

opciones = [IntVar() for _ in range(len(encabezados) * 2)]

# Crear los Checkbutton y colocarlos en forma horizontal
for i in range(len(encabezados)):
    Checkbutton(cuadrotiempo, text="", variable=opciones[i], onvalue=1, offvalue=0).grid(row=1, column=i+1, padx=1, pady=1)

nombreempresa_entry2 = Entry(cuadrotiempo, width=33)
nombreempresa_entry2.grid(row=2, column=0, padx=5, pady=5)

# Crear los Checkbutton para la segunda fila
for i in range(len(encabezados)):
    Checkbutton(cuadrotiempo, text="", variable=opciones[i + len(encabezados)], onvalue=1, offvalue=0).grid(row=2, column=i+1, padx=1, pady=1)

riesgosocupacionea = tk.Label(frame6, text="RIENGOS OCUPACIONALES EN LA EMPRESA ACTUAL Y/O ANTERIONES", font=bool)
riesgosocupacionea.grid(row=0, column=0, sticky="w", padx=5, pady=10)


frame7 = tk.Frame(frame_contenido)
frame7.pack(anchor="n")

opcionp1 = IntVar()
opcionp2 = IntVar()
opcionp3 = IntVar()
opcionp4 = IntVar()
opcionp5 = IntVar()
opcionp6 = IntVar()
opcionp7 = IntVar()
opcionp8 = IntVar()


cuadroproteccion = tk.LabelFrame(frame7, text="", width=30)
cuadroproteccion.grid(row=1, column=0, padx=10, pady=10)

Checkbutton(cuadroproteccion, text="GUANTES", variable=opcionp1, onvalue=1, offvalue=0,).grid(row=0, column=0, padx=10, pady=10)
Checkbutton(cuadroproteccion, text="BRAGAS", variable=opcionp2, onvalue=1, offvalue=0,).grid(row=0, column=1, padx=10, pady=10)
Checkbutton(cuadroproteccion, text="TAPABOCAS", variable=opcionp3, onvalue=1, offvalue=0,).grid(row=0, column=2, padx=10, pady=10)
Checkbutton(cuadroproteccion, text="LENTES", variable=opcionp4, onvalue=1, offvalue=0,).grid(row=0, column=3, padx=10, pady=10)
Checkbutton(cuadroproteccion, text="PRETECTORES AUDITIVOS", variable=opcionp5, onvalue=1, offvalue=0,).grid(row=0, column=4, padx=10, pady=10)
Checkbutton(cuadroproteccion, text="CASCO", variable=opcionp6, onvalue=1, offvalue=0,).grid(row=1, column=0, padx=10, pady=10)
Checkbutton(cuadroproteccion, text="BOTAS", variable=opcionp7, onvalue=1, offvalue=0,).grid(row=1, column=1, padx=10, pady=10)
Checkbutton(cuadroproteccion, text="RESPIRADORES", variable=opcionp8, onvalue=1, offvalue=0,).grid(row=1, column=2, padx=10, pady=10)

cuadroproteccionp = Label(cuadroproteccion, text= "OTROS")
cuadroproteccionp.grid(row=1, column=3, padx=10, pady=10)
cuadroproteccion_entry = Entry(cuadroproteccion, textvariable=razonsocial, width=30)
cuadroproteccion_entry.grid(row=1, column=4, padx=10, pady=10)

tituloelementosproteccion = Label(frame7, text="USO DE ELEMENTOS DE PROTECCION PERSONAL", font=bool)
tituloelementosproteccion.grid(row=0, column=0, sticky="w", padx=10, pady=10)


frame8 = tk.Frame(frame_contenido)
frame8.pack(anchor="w")

opcionaccidentetrabajo = tk.IntVar()
adfecha=StringVar()
adnombreempresa=StringVar()
adtipolecion=StringVar()
adparteafectada=StringVar()
addiasincapacidad=StringVar()
adsecuelas=StringVar()

cuadroaccidentetrabajo = tk.LabelFrame(frame8, text="")
cuadroaccidentetrabajo.grid(row=1, column=0, padx=10, pady=10)

accidentetrabajo = Label(cuadroaccidentetrabajo, text="ACCIDENTES DE \nTRABAJO", font=bool)
accidentetrabajo.grid(row=1, column=0, padx=1, pady=1)

frame_centro = tk.Frame(cuadroaccidentetrabajo)
frame_centro.grid(row=1, column=1, padx=1, pady=1)

opcion1 = tk.Radiobutton(frame_centro, text="SI", width=2, anchor="w", variable=opcionaccidentetrabajo, value=1).grid(row=0, column=0, padx=1, pady=1)
opcion2 = tk.Radiobutton(frame_centro, text="NO", width=2, anchor="w", variable=opcionaccidentetrabajo, value=2).grid(row=0, column=1, padx=1, pady=1)


fechalabel = Label(cuadroaccidentetrabajo, text="FECHA", width=15)
fechalabel.grid(row=2, column=0, padx=1, pady=1)
nombreempresalabel = Label(cuadroaccidentetrabajo, text="NOMBRE DE LA EMPRESA")
nombreempresalabel.grid(row=2, column=1, padx=1, pady=1)
tipolecionlabel = Label(cuadroaccidentetrabajo, text="TIPO DE LESION")
tipolecionlabel.grid(row=2, column=2, padx=0, pady=0)
parteafectadalabel = Label(cuadroaccidentetrabajo,text="PARTE DEL CUERPO \nAFECTADA")
parteafectadalabel.grid(row=2, column=3, padx=1, pady=1)
diasincapacidadlabel = Label(cuadroaccidentetrabajo, text="DIAS DE \nINCAPACIDAD")
diasincapacidadlabel.grid(row=2, column=4, padx=1, pady=1)
secuelalabel = Label(cuadroaccidentetrabajo, text="SECUELAS")
secuelalabel.grid(row=2, column=5, padx=5, pady=1)

fecha_entry = Entry(cuadroaccidentetrabajo, textvariable=adfecha, width=15)
fecha_entry.grid(row=3, column=0, padx=1, pady=1)
fecha_entry = Entry(cuadroaccidentetrabajo, textvariable=adfecha, width=15)
fecha_entry.grid(row=4, column=0, padx=1, pady=1)
fecha_entry = Entry(cuadroaccidentetrabajo, textvariable=adfecha, width=15)
fecha_entry.grid(row=5, column=0, padx=1, pady=1)

nombreempresa_entry = Entry(cuadroaccidentetrabajo, textvariable=adnombreempresa, width=30)
nombreempresa_entry.grid(row=3, column=1, padx=1, pady=1)
nombreempresa_entry = Entry(cuadroaccidentetrabajo, textvariable=adnombreempresa, width=30)
nombreempresa_entry.grid(row=4, column=1, padx=1, pady=1)
nombreempresa_entry = Entry(cuadroaccidentetrabajo, textvariable=adnombreempresa, width=30)
nombreempresa_entry.grid(row=5, column=1, padx=1, pady=1)

tipolecion_entry = Entry(cuadroaccidentetrabajo, textvariable=adtipolecion, width=25)
tipolecion_entry.grid(row=3, column=2, padx=0, pady=0)
tipolecion_entry = Entry(cuadroaccidentetrabajo, textvariable=adtipolecion, width=25)
tipolecion_entry.grid(row=4, column=2, padx=0, pady=0)
tipolecion_entry = Entry(cuadroaccidentetrabajo, textvariable=adtipolecion, width=25)
tipolecion_entry.grid(row=5, column=2, padx=0, pady=0)

adparteafectada_entry = Entry(cuadroaccidentetrabajo, textvariable=adparteafectada, width=25)
adparteafectada_entry.grid(row=3, column=3, padx=1, pady=1)
adparteafectada_entry = Entry(cuadroaccidentetrabajo, textvariable=adparteafectada, width=25)
adparteafectada_entry.grid(row=4, column=3, padx=1, pady=1)
adparteafectada_entry = Entry(cuadroaccidentetrabajo, textvariable=adparteafectada, width=25)
adparteafectada_entry.grid(row=5, column=3, padx=1, pady=1)

addiasincapacidad_entry = Entry(cuadroaccidentetrabajo, textvariable=addiasincapacidad, width=10)
addiasincapacidad_entry.grid(row=3, column=4, padx=1, pady=1)
addiasincapacidad_entry = Entry(cuadroaccidentetrabajo, textvariable=addiasincapacidad, width=10)
addiasincapacidad_entry.grid(row=4, column=4, padx=1, pady=1)
addiasincapacidad_entry = Entry(cuadroaccidentetrabajo, textvariable=addiasincapacidad, width=10)
addiasincapacidad_entry.grid(row=5, column=4, padx=1, pady=1)

adsecuelas_entry = Entry(cuadroaccidentetrabajo, textvariable=adsecuelas, width=25)
adsecuelas_entry.grid(row=3, column=5, padx=5, pady=1)
adsecuelas_entry = Entry(cuadroaccidentetrabajo, textvariable=adsecuelas, width=25)
adsecuelas_entry.grid(row=4, column=5, padx=5, pady=1)
adsecuelas_entry = Entry(cuadroaccidentetrabajo, textvariable=adsecuelas, width=25)
adsecuelas_entry.grid(row=5, column=5, padx=5, pady=1)


frame9 = tk.Frame(frame_contenido)
frame9.pack(anchor="w")

opcionenfermedadespro = tk.IntVar()
enfermedadesprofecionales=StringVar()
enfermedadesprofecionales2=StringVar()
diapro = IntVar()
mespro = IntVar()
añopro = IntVar()
diapro2 = IntVar()
mespro2 = IntVar()
añopro2 = IntVar()

cuadroenfermedadespro = tk.LabelFrame(frame9, text="")
cuadroenfermedadespro.grid(row=1, column=0, padx=10, pady=10)

frameenfermedadespro = tk.Frame(cuadroenfermedadespro)
frameenfermedadespro.grid(row=1, column=0)
enfermedadespro = Label(frameenfermedadespro, text="ENFERMEDADES PROFECIONALES", font=bool)
enfermedadespro.grid(row=1, column=0, padx=10, pady=10)

frame_centro = tk.Frame(frameenfermedadespro)
frame_centro.grid(row=1, column=1, padx=10, pady=10)

opcion1 = tk.Radiobutton(frame_centro, text="SI", width=2, anchor="w", variable=opcionenfermedadespro, value=1).grid(row=0, column=0, padx=5, pady=1)
opcion2 = tk.Radiobutton(frame_centro, text="NO", width=2, anchor="w", variable=opcionenfermedadespro, value=2).grid(row=0, column=1, padx=5, pady=1)

enfermedadespro_entry = Entry(cuadroenfermedadespro, textvariable=enfermedadesprofecionales, width=100)
enfermedadespro_entry.grid(row=2, column=0, padx=10, pady=10)

enfermedadespro_entry = Entry(cuadroenfermedadespro, textvariable=enfermedadesprofecionales2, width=100)
enfermedadespro_entry.grid(row=3, column=0, padx=10, pady=10)

cuadrofechaentry = tk.Frame(cuadroenfermedadespro)
cuadrofechaentry.grid(row=2, column=2, padx=5, pady=1)

dia_entry = Entry(cuadrofechaentry, textvariable=diapro, width=5)
dia_entry.grid(row=0, column=1, padx=5, pady=1)
mes_entry = Entry(cuadrofechaentry, textvariable=mespro, width=5)
mes_entry.grid(row=0, column=3, padx=5, pady=1)
año_entry = Entry(cuadrofechaentry, textvariable=añopro, width=5)
año_entry.grid(row=0, column=5, padx=5, pady=1)

diaprolabel = Label(cuadrofechaentry, text="DIA")
diaprolabel.grid(row=0, column=0, padx=5, pady=1)
mesprolabel = Label(cuadrofechaentry, text="MES")
mesprolabel.grid(row=0, column=2, padx=5, pady=1)
añoprolabel = Label(cuadrofechaentry, text="AÑO")
añoprolabel.grid(row=0, column=4, padx=5, pady=1)

cuadrofechaentry2 = tk.Frame(cuadroenfermedadespro)
cuadrofechaentry2.grid(row=3, column=2, padx=1, pady=1)

dia_entry = Entry(cuadrofechaentry2, textvariable=diapro2, width=5)
dia_entry.grid(row=0, column=1, padx=5, pady=1)
mes_entry = Entry(cuadrofechaentry2, textvariable=mespro2, width=5)
mes_entry.grid(row=0, column=3, padx=5, pady=1)
año_entry = Entry(cuadrofechaentry2, textvariable=añopro2, width=5)
año_entry.grid(row=0, column=5, padx=5, pady=1)

diaprolabel = Label(cuadrofechaentry2, text="DIA")
diaprolabel.grid(row=0, column=0, padx=5, pady=1)
mesprolabel = Label(cuadrofechaentry2, text="MES")
mesprolabel.grid(row=0, column=2, padx=5, pady=1)
añoprolabel = Label(cuadrofechaentry2, text="AÑO")
añoprolabel.grid(row=0, column=4, padx=5, pady=1)


frame10 = tk.Frame(frame_contenido)
frame10.pack(anchor="w")

actividadfisica = StringVar()
patologicos = StringVar()
quirurgico = StringVar()
traumaticos = StringVar()
alergicos = StringVar()
farmacologicos = StringVar()
ginecobstericos = StringVar()
metodosacticonceptivos = StringVar()
menarquia = StringVar()
ciclos = StringVar()

cuadroractividadfisica = tk.LabelFrame(frame10, text="")
cuadroractividadfisica.grid(row=0, column=0, padx=10, pady=10)

actividadfisicalabel = Label(cuadroractividadfisica,text="ACTIVIDAD FISICA", font=bool)
actividadfisicalabel.grid(row=0, column=0, sticky="w", padx=5, pady=2)
actividadfisicalabel_entry = tk.Text(cuadroractividadfisica, height=2)  # Ajusta los valores de width y height
actividadfisicalabel_entry.grid(row=0, column=1, padx=5, pady=2)

antecedentespersonaleslabel = Label(cuadroractividadfisica,text="ANTECEDENTES\nPERSONALES DE SALUD", font=bool)
antecedentespersonaleslabel.grid(row=2, column=0, sticky="w", padx=5, pady=1)

patologicoslabel = Label(cuadroractividadfisica,text="PATOLOGICOS")
patologicoslabel.grid(row=3, column=0, sticky="w", padx=5, pady=2)
patologicoslabel_entry = tk.Text(cuadroractividadfisica, height=2)  # Ajusta los valores de width y height
patologicoslabel_entry.grid(row=3, column=1, padx=5, pady=2)

quirurgicolabel = Label(cuadroractividadfisica,text="QUIRURGICOS")
quirurgicolabel.grid(row=4, column=0, sticky="w", padx=5, pady=2)
quirurgicolabel_entry = tk.Text(cuadroractividadfisica, height=2)  # Ajusta los valores de width y height
quirurgicolabel_entry.grid(row=4, column=1, padx=5, pady=2)

traumaticoslabel = Label(cuadroractividadfisica,text="TRAUMATICOS")
traumaticoslabel.grid(row=5, column=0, sticky="w", padx=5, pady=2)
traumaticoslabel_entry = tk.Text(cuadroractividadfisica, height=2)  # Ajusta los valores de width y height
traumaticoslabel_entry.grid(row=5, column=1, padx=5, pady=2)

alergicoslabel = Label(cuadroractividadfisica,text="ALERGICOS")
alergicoslabel.grid(row=6, column=0, sticky="w", padx=5, pady=2)
alergicoslabel_entry = tk.Text(cuadroractividadfisica, height=2)  # Ajusta los valores de width y height
alergicoslabel_entry.grid(row=6, column=1, padx=5, pady=2)

farmacologicoslabel = Label(cuadroractividadfisica,text="FARMACOLOGICOS")
farmacologicoslabel.grid(row=7, column=0, sticky="w", padx=5, pady=2)
farmacologicos_entry = tk.Text(cuadroractividadfisica, height=2)  # Ajusta los valores de width y height
farmacologicos_entry.grid(row=7, column=1, padx=5, pady=2)

ginecobstericoslabel = Label(cuadroractividadfisica, text="GINECOBSTETRICOS")
ginecobstericoslabel.grid(row=8, column=0, sticky="w", padx=5, pady=2)


frameextra = tk.Frame(cuadroractividadfisica)
frameextra.grid(row=8,column=1)

ginecobstericos_entry = tk.Text(frameextra, width=32, height=2)  # Ajusta los valores de width y height
ginecobstericos_entry.grid(row=1, column=1, padx=10, pady=2)

menarquialabel = Label(frameextra, text="MENARQUIA")
menarquialabel.grid(row=1, column=2, sticky="w", padx=2, pady=2)
menarquia_entry = Entry(frameextra, textvariable=menarquia)
menarquia_entry.grid(row=1, column=3, sticky="w", padx=2, pady=2)

cicloslabel = Label(frameextra, text="CICLOS")
cicloslabel.grid(row=1, column=4, sticky="e", padx=2, pady=2)
ciclos_entry = Entry(frameextra, textvariable=ciclos)
ciclos_entry.grid(row=1, column=5, sticky="w", padx=2, pady=2)


frame11 = tk.Frame(frame_contenido)
frame11.pack(anchor="w")

metodosanticonceptivos = StringVar()
niparidad = IntVar()
gestas = IntVar()
partos = IntVar()
cesarias = IntVar()
abortos = IntVar()
embarazoectopicos = IntVar()


cuadrorazoncuadrometodoanticonceptivosocial = tk.LabelFrame(frame11, text="", width=30)
cuadrorazoncuadrometodoanticonceptivosocial.grid(row=1, column=0, padx=10, pady=10)

metodoanticonceptivolabel = Label(cuadrorazoncuadrometodoanticonceptivosocial, text="METODOS ANTICONCEPTIVOS")
metodoanticonceptivolabel.grid(row=0, column=0, sticky="w", padx=5, pady=2)

cuadrometodoanticonceptivo_entry = tk.Text(cuadrorazoncuadrometodoanticonceptivosocial, width=40, height=2)  # Ajusta los valores de width y height
cuadrometodoanticonceptivo_entry.grid(row=1, column=0, padx=5, pady=2)

cuadrofechaultimaregla = Label(cuadrorazoncuadrometodoanticonceptivosocial, text="FECHA ULTIMA REGLA")
cuadrofechaultimaregla.grid(row=0, column=1, padx=5, pady=2)

frameextra2 = tk.Frame(cuadrorazoncuadrometodoanticonceptivosocial)
frameextra2.grid(row=1,column=1)

dia_entry = Entry(frameextra2, textvariable=diapro, width=5)
dia_entry.grid(row=2, column=1, padx=5, pady=1)
mes_entry = Entry(frameextra2, textvariable=mespro, width=5)
mes_entry.grid(row=2, column=2, padx=5, pady=1)
año_entry = Entry(frameextra2, textvariable=añopro, width=5)
año_entry.grid(row=2, column=3, padx=5, pady=1)

diaprolabel = Label(frameextra2, text="DIA")
diaprolabel.grid(row=3, column=1, padx=5, pady=1)
mesprolabel = Label(frameextra2, text="MES")
mesprolabel.grid(row=3, column=2, padx=5, pady=1)
añoprolabel = Label(frameextra2, text="AÑO")
añoprolabel.grid(row=3, column=3, padx=5, pady=1)

cuadroparidad = tk.LabelFrame(frame11, text="PARIDAD", width=60)
cuadroparidad.grid(row=1, column=1, padx=10, pady=10)

nuliparalabel = Label(cuadroparidad, text="NULIPARIDAD")
nuliparalabel.grid(row=0, column=0, padx=5, pady=2)
nuliparalabel_entry = Entry(cuadroparidad, textvariable=niparidad, width=5)
nuliparalabel_entry.grid(row=0, column=1, padx=5, pady=2)

nuliparalabel = Label(cuadroparidad, text="GESTAS")
nuliparalabel.grid(row=0, column=2, padx=5, pady=2)
nuliparalabel_entry = Entry(cuadroparidad, textvariable=gestas, width=5)
nuliparalabel_entry.grid(row=0, column=3, padx=5, pady=2)

nuliparalabel = Label(cuadroparidad, text="PARTOS")
nuliparalabel.grid(row=0, column=4, padx=5, pady=2)
nuliparalabel_entry = Entry(cuadroparidad, textvariable=partos, width=5)
nuliparalabel_entry.grid(row=0, column=5, padx=5, pady=2)

nuliparalabel = Label(cuadroparidad, text="CESARIAS")
nuliparalabel.grid(row=1, column=0, padx=5, pady=2)
nuliparalabel_entry = Entry(cuadroparidad, textvariable=cesarias, width=5)
nuliparalabel_entry.grid(row=1, column=1, padx=5, pady=2)

nuliparalabel = Label(cuadroparidad, text="ABORTOS")
nuliparalabel.grid(row=1, column=2, padx=5, pady=2)
nuliparalabel_entry = Entry(cuadroparidad, textvariable=abortos, width=5)
nuliparalabel_entry.grid(row=1, column=3, padx=5, pady=2)

nuliparalabel = Label(cuadroparidad, text="EMBARASOS\nECTOPICOS")
nuliparalabel.grid(row=1, column=4, padx=5, pady=2)
nuliparalabel_entry = Entry(cuadroparidad, textvariable=embarazoectopicos, width=5)
nuliparalabel_entry.grid(row=1, column=5, padx=5, pady=2)



frame12 = tk.Frame(frame_contenido)
frame12.pack(anchor="w")

neurologico = StringVar()
ocular = StringVar()
orl = StringVar()
respiratorio = StringVar()
cardiovascular = StringVar()
digestivo = StringVar()
genitourinario = StringVar()
musculoesqueletico = StringVar()
dermatologico = StringVar()
#aqui va a ser el proximo cambio se implementara para mayor eficiencia

cuadrorevisionsistema = tk.LabelFrame(frame12, text="REVISION POR SISTEMA", font=(bool)) #esto es para modificar el texto, aumento, negrita, ect
cuadrorevisionsistema.grid(row=0, column=0, padx=10, pady=10)

neurologicolabel = Label(cuadrorevisionsistema,text="NEUROLOGICO")
neurologicolabel.grid(row=0, column=0, sticky="w", padx=2, pady=2)
neurologico_entry = Entry(cuadrorevisionsistema, textvariable=neurologico, width=118)
neurologico_entry.grid(row=0, column=1, padx=10, pady=10)

ocularlabel = Label(cuadrorevisionsistema,text="OCULAR")
ocularlabel.grid(row=1, column=0, sticky="w", padx=2, pady=2)
ocular_entry = Entry(cuadrorevisionsistema, textvariable=ocular, width=118)
ocular_entry.grid(row=1, column=1, padx=10, pady=10)

orllabel = Label(cuadrorevisionsistema,text="ORL")
orllabel.grid(row=2, column=0, sticky="w", padx=2, pady=2)
orl_entry = Entry(cuadrorevisionsistema, textvariable=orl, width=118)
orl_entry.grid(row=2, column=1, padx=10, pady=10)

respiratoriolabel = Label(cuadrorevisionsistema,text="RESPIRATORIO")
respiratoriolabel.grid(row=3, column=0, sticky="w", padx=2, pady=2)
respiratorio_entry = Entry(cuadrorevisionsistema, textvariable=respiratorio, width=118)
respiratorio_entry.grid(row=3, column=1, padx=10, pady=10)

cardiovascularlabel = Label(cuadrorevisionsistema,text="CARDIOVASCULAR")
cardiovascularlabel.grid(row=4, column=0, sticky="w", padx=2, pady=2)
cardiovascular_entry = Entry(cuadrorevisionsistema, textvariable=cardiovascular, width=118)
cardiovascular_entry.grid(row=4, column=1, padx=10, pady=10)

digestivolabel = Label(cuadrorevisionsistema,text="DIGESTIVOS")
digestivolabel.grid(row=5, column=0, sticky="w", padx=2, pady=2)
digestivo_entry = Entry(cuadrorevisionsistema, textvariable=digestivo, width=118)
digestivo_entry.grid(row=5, column=1, padx=10, pady=10)

genitourinariolabel = Label(cuadrorevisionsistema,text="GENITOURUNARIO")
genitourinariolabel.grid(row=6, column=0, sticky="w", padx=2, pady=2)
genitourinario_entry = Entry(cuadrorevisionsistema, textvariable=genitourinario, width=118)
genitourinario_entry.grid(row=6, column=1, padx=10, pady=10)

musculoesqueleticolabel = Label(cuadrorevisionsistema,text="MUSCULO ESQUELETICO")
musculoesqueleticolabel.grid(row=7, column=0, sticky="w", padx=2, pady=2)
musculoesqueletico_entry = Entry(cuadrorevisionsistema, textvariable=musculoesqueletico, width=118)
musculoesqueletico_entry.grid(row=7, column=1, padx=10, pady=10)

dermatologicolabel = Label(cuadrorevisionsistema,text="DERMATOLOGICO")
dermatologicolabel.grid(row=8, column=0, sticky="w", padx=2, pady=2)
dermatologico_entry = Entry(cuadrorevisionsistema, textvariable=dermatologico, width=118)
dermatologico_entry.grid(row=8, column=1, padx=10, pady=10)


frame13= tk.Frame(frame_contenido)
frame13.pack(anchor="w")

opchipertencionarterial = IntVar()
opcinfarto = IntVar()
opcnfcerebrovarcular = IntVar()
opcdiabetes = IntVar()
opccancer = IntVar()
opcasma = IntVar()
opcenfrenales = IntVar()
opcenfermedadescolageno = IntVar()
opcenfreumaticas = IntVar()
opcenfmentales = IntVar()
otros = StringVar()
hipertencionarterial = StringVar()
infarto = StringVar()
nfcerebrovarcular = StringVar()
diabetes = StringVar()
cancer = StringVar()
asma = StringVar()
enfrenales = StringVar()
enfermedadescolageno = StringVar()
enfreumaticas = StringVar()
enfmentales = StringVar()

cuadroantecedentesfamiliares = tk.LabelFrame(frame13, text="ANTECEDENTES FAMILIARES", font=(bool)) #esto es para modificar el texto, aumento, negrita, ect
cuadroantecedentesfamiliares.grid(row=0, column=0, padx=10, pady=10)

patologiaslabe = Label(cuadroantecedentesfamiliares, text="PATOLOGIAS", font=bool)
patologiaslabe.grid(row=0, column=0, padx=5, pady=2)
silabel = Label(cuadroantecedentesfamiliares, text="SI", font=bool)
silabel.grid(row=0, column=1, padx=5, pady=2)
silabel = Label(cuadroantecedentesfamiliares, text="NO", font=bool)
silabel.grid(row=0, column=2, padx=5, pady=2)
parentescolabel = Label(cuadroantecedentesfamiliares, text="PARENTESCO", font=bool)
parentescolabel.grid(row=0, column=3, padx=5, pady=2)

opchipertencionarteriallabe = Label(cuadroantecedentesfamiliares, text="HIPERTENSION ARTERIAL")
opchipertencionarteriallabe.grid(row=1, column=0, sticky="w", padx=5, pady=2)
opchipertencionarterial1 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opchipertencionarterial, value=1).grid(row=1, column=1, padx=5, pady=1)
opchipertencionarterial2 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opchipertencionarterial, value=2).grid(row=1, column=2, padx=5, pady=1)
opchipertencionarterial_entry = Entry(cuadroantecedentesfamiliares, textvariable=hipertencionarterial, width=88)
opchipertencionarterial_entry.grid(row=1, column=3, padx=5, pady=2)

opcinfartolabe = Label(cuadroantecedentesfamiliares, text="INFARTOS")
opcinfartolabe.grid(row=2, column=0, sticky="w", padx=5, pady=2)
opcinfarto1 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opcinfarto, value=1).grid(row=2, column=1, padx=5, pady=1)
opcinfarto2 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opcinfarto, value=2).grid(row=2, column=2, padx=5, pady=1)
opcinfarto_entry = Entry(cuadroantecedentesfamiliares, textvariable=hipertencionarterial, width=88)
opcinfarto_entry.grid(row=2, column=3, padx=5, pady=2)

opcenfcerebrovasculareslabe = Label(cuadroantecedentesfamiliares, text="ENF. CEREBRO VASCULARES")
opcenfcerebrovasculareslabe.grid(row=3, column=0, sticky="w", padx=5, pady=2)
opcenfcerebrovasculares1 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opcnfcerebrovarcular, value=1).grid(row=3, column=1, padx=5, pady=1)
opcenfcerebrovasculares2 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opcnfcerebrovarcular, value=2).grid(row=3, column=2, padx=5, pady=1)
opcenfcerebrovasculareslabe_entry = Entry(cuadroantecedentesfamiliares, textvariable=hipertencionarterial, width=88)
opcenfcerebrovasculareslabe_entry.grid(row=3, column=3, padx=5, pady=2)

opcdiabeteslabe = Label(cuadroantecedentesfamiliares, text="DIABETES")
opcdiabeteslabe.grid(row=4, column=0, sticky="w", padx=5, pady=2)
opcdiabetes1 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opcdiabetes, value=1).grid(row=4, column=1, padx=5, pady=1)
opcdiabetes2 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opcdiabetes, value=2).grid(row=4, column=2, padx=5, pady=1)
opcdiabetes_entry = Entry(cuadroantecedentesfamiliares, textvariable=hipertencionarterial, width=88)
opcdiabetes_entry.grid(row=4, column=3, padx=5, pady=2)

opccancerlabe = Label(cuadroantecedentesfamiliares, text="CANCER")
opccancerlabe.grid(row=5, column=0, sticky="w", padx=5, pady=2)
opccancer1 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opccancer, value=1).grid(row=5, column=1, padx=5, pady=1)
opccancer2 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opccancer, value=2).grid(row=5, column=2, padx=5, pady=1)
opccancer_entry = Entry(cuadroantecedentesfamiliares, textvariable=hipertencionarterial, width=88)
opccancer_entry.grid(row=5, column=3, padx=5, pady=2)

opcasmalabe = Label(cuadroantecedentesfamiliares, text="ASMA")
opcasmalabe.grid(row=6, column=0, sticky="w", padx=5, pady=2)
opcasma1 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opcasma, value=1).grid(row=6, column=1, padx=5, pady=1)
opcasma2 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opcasma, value=2).grid(row=6, column=2, padx=5, pady=1)
opcasma_entry = Entry(cuadroantecedentesfamiliares, textvariable=hipertencionarterial, width=88)
opcasma_entry.grid(row=6, column=3, padx=5, pady=2)

opcenfrenaleslabe = Label(cuadroantecedentesfamiliares, text="ENF. RENALES")
opcenfrenaleslabe.grid(row=7, column=0, sticky="w", padx=5, pady=2)
opcenfrenales1 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opcenfrenales, value=1).grid(row=7, column=1, padx=5, pady=1)
opcenfrenales2 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opcenfrenales, value=2).grid(row=7, column=2, padx=5, pady=1)
opcenfrenales_entry = Entry(cuadroantecedentesfamiliares, textvariable=hipertencionarterial, width=88)
opcenfrenales_entry.grid(row=7, column=3, padx=5, pady=2)

opcenfermedadescolagenolabe = Label(cuadroantecedentesfamiliares, text="ENFERMEDADES DEL COLAGENO")
opcenfermedadescolagenolabe.grid(row=8, column=0, sticky="w", padx=5, pady=2)
opcenfermedadescolageno1 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opcenfermedadescolageno, value=1).grid(row=8, column=1, padx=5, pady=1)
opcenfermedadescolageno2 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opcenfermedadescolageno, value=2).grid(row=8, column=2, padx=5, pady=1)
opcenfermedadescolageno_entry = Entry(cuadroantecedentesfamiliares, textvariable=hipertencionarterial, width=88)
opcenfermedadescolageno_entry.grid(row=8, column=3, padx=5, pady=2)

opcenfreumaticaslabe = Label(cuadroantecedentesfamiliares, text="ENF. REUMATICAS")
opcenfreumaticaslabe.grid(row=9, column=0, sticky="w", padx=5, pady=2)
opcenfreumaticas1 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opcenfreumaticas, value=1).grid(row=9, column=1, padx=5, pady=1)
opcenfreumaticas2 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opcenfreumaticas, value=2).grid(row=9, column=2, padx=5, pady=1)
opcenfreumaticas_entry = Entry(cuadroantecedentesfamiliares, textvariable=hipertencionarterial, width=88)
opcenfreumaticas_entry.grid(row=9, column=3, padx=5, pady=2)

opcenfmentaleslabe = Label(cuadroantecedentesfamiliares, text="ENF. MENTALES")
opcenfmentaleslabe.grid(row=10, column=0, sticky="w", padx=5, pady=2)
opcenfmentales1 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opchipertencionarterial, value=1).grid(row=10, column=1, padx=5, pady=1)
opcenfmentales2 = tk.Radiobutton(cuadroantecedentesfamiliares, text="", width=4, anchor="n", variable=opchipertencionarterial, value=2).grid(row=10, column=2, padx=5, pady=1)
opcenfmentales_entry = Entry(cuadroantecedentesfamiliares, textvariable=hipertencionarterial, width=88)
opcenfmentales_entry.grid(row=10, column=3, padx=5, pady=2)

otroslabel = Label(cuadroantecedentesfamiliares,text="OTROS")
otroslabel.grid(row=11, column=0, sticky="w", padx=5, pady=2)
otros_entry = Entry(cuadroantecedentesfamiliares, textvariable=otros, width=88)
otros_entry.grid(row=11, column=3, padx=10, pady=10)



frame14 = tk.Frame(frame_contenido)
frame14.pack(anchor="w")

inmunizaciones = StringVar()
docishepatitisb = StringVar()
fechahepatitisb = StringVar()
docishepatitisa = StringVar()
fechahepatitisa = StringVar()
docisantiamarilla = StringVar()
fechaantiamarilla = StringVar()
docisdobleviral = StringVar()
fechadobleviral = StringVar()
docistetanos = StringVar()
fechatetanos = StringVar()
docisotrasinmuniza = StringVar()
fechaotrasinmuniza = StringVar()

cuadroinmunizaciones = tk.LabelFrame(frame14, text="")
cuadroinmunizaciones.grid(row=0, column=0, padx=10, pady=10)
 
inmunizacioneslabel = Label(cuadroinmunizaciones, text="INMUNIZACIONES", font=bool)
inmunizacioneslabel.grid(row=0, column=0, padx=1, pady=1)
inmunizaciones_entry = Entry(cuadroinmunizaciones, textvariable=inmunizacioneslabel, width=20)
inmunizaciones_entry.grid(row=1, column=0, padx=1, pady=1)

hepatitisblabel = Label(cuadroinmunizaciones, text="HEPATITIS B")
hepatitisblabel.grid(row=2, column=0, padx=0, pady=10)
hepatitisbfechalabel = Label(cuadroinmunizaciones, text="FECHA")
hepatitisbfechalabel.grid(row=2, column=1, padx=1, pady=1)
hepatitisdocislabel = Label(cuadroinmunizaciones, text="DOCIS")
hepatitisdocislabel.grid(row=3, column=1, padx=1, pady=1)
hepatitisfechaentry_entry = Entry(cuadroinmunizaciones, textvariable=fechahepatitisb)
hepatitisfechaentry_entry.grid(row=2, column=2, padx=1, pady=1)
hepatitisdocisentry_entry = Entry(cuadroinmunizaciones, textvariable=docishepatitisb)
hepatitisdocisentry_entry.grid(row=3, column=2, padx=1, pady=1)

hepatitisalabel = Label(cuadroinmunizaciones, text="HEPATITIS A")
hepatitisalabel.grid(row=4, column=0, padx=0, pady=10)
hepatitisafechalabel = Label(cuadroinmunizaciones, text="FECHA")
hepatitisafechalabel.grid(row=4, column=1, padx=1, pady=1)
hepatitisadocislabel = Label(cuadroinmunizaciones, text="DOCIS")
hepatitisadocislabel.grid(row=5, column=1, padx=1, pady=1)
hepatitisafechaentry_entry = Entry(cuadroinmunizaciones, textvariable=fechahepatitisa)
hepatitisafechaentry_entry.grid(row=4, column=2, padx=1, pady=1)
hepatitisadocisentry_entry = Entry(cuadroinmunizaciones, textvariable=docishepatitisa)
hepatitisadocisentry_entry.grid(row=5, column=2, padx=1, pady=1)

antiamarillalabel = Label(cuadroinmunizaciones, text="ANTIAMARILLA", width=15)
antiamarillalabel.grid(row=2, column=3, padx=0, pady=10)
antiamarillafechalabel = Label(cuadroinmunizaciones, text="FECHA")
antiamarillafechalabel.grid(row=2, column=4, padx=1, pady=1)
hepatitisdicislabel = Label(cuadroinmunizaciones, text="DOCIS")
hepatitisdicislabel.grid(row=3, column=4, padx=1, pady=1)
hepatitisfechaentry_entry = Entry(cuadroinmunizaciones, textvariable=fechaantiamarilla)
hepatitisfechaentry_entry.grid(row=2, column=5, padx=1, pady=1)
hepatitisdocisentry_entry = Entry(cuadroinmunizaciones, textvariable=docisantiamarilla)
hepatitisdocisentry_entry.grid(row=3, column=5, padx=1, pady=1)

doblevirallabel = Label(cuadroinmunizaciones, text="DOBLEVIRAL")
doblevirallabel.grid(row=4, column=3, padx=0, pady=10)
dobleviralfechalabel = Label(cuadroinmunizaciones, text="FECHA")
dobleviralfechalabel.grid(row=4, column=4, padx=1, pady=1)
dobleviraldocislabel = Label(cuadroinmunizaciones, text="DOCIS")
dobleviraldocislabel.grid(row=5, column=4, padx=1, pady=1)
dobleviralfechaentry_entry = Entry(cuadroinmunizaciones, textvariable=fechadobleviral)
dobleviralfechaentry_entry.grid(row=4, column=5, padx=1, pady=1)
dobleviraldocisentry_entry = Entry(cuadroinmunizaciones, textvariable=docisdobleviral)
dobleviraldocisentry_entry.grid(row=5, column=5, padx=1, pady=1)

tetanosblabel = Label(cuadroinmunizaciones, text="TETANOS", width=15)
tetanosblabel.grid(row=2, column=6, padx=0, pady=10)
tetanosfechalabel = Label(cuadroinmunizaciones, text="FECHA")
tetanosfechalabel.grid(row=2, column=7, padx=1, pady=1)
tetanosdocislabel = Label(cuadroinmunizaciones, text="DOCIS")
tetanosdocislabel.grid(row=3, column=7, padx=1, pady=1)
tetanosfechaentry_entry = Entry(cuadroinmunizaciones, textvariable=fechatetanos)
tetanosfechaentry_entry.grid(row=2, column=8, padx=1, pady=1)
tetanosdocisentry_entry = Entry(cuadroinmunizaciones, textvariable=docistetanos)
tetanosdocisentry_entry.grid(row=3, column=8, padx=1, pady=1)

otrasinmunizalabel = Label(cuadroinmunizaciones, text="OTRAS")
otrasinmunizalabel.grid(row=4, column=6, padx=0, pady=10)
otrasinmunizafechalabel = Label(cuadroinmunizaciones, text="FECHAS")
otrasinmunizafechalabel.grid(row=4, column=7, padx=1, pady=1)
otrasinmunizadocislabel = Label(cuadroinmunizaciones, text="DOCIS")
otrasinmunizadocislabel.grid(row=5, column=7, padx=1, pady=1)
otrasinmunizafechaentry_entry = Entry(cuadroinmunizaciones, textvariable=fechaotrasinmuniza)
otrasinmunizafechaentry_entry.grid(row=4, column=8, padx=1, pady=1)
otrasinmunizadocisentry_entry = Entry(cuadroinmunizaciones, textvariable=docisotrasinmuniza)
otrasinmunizadocisentry_entry.grid(row=5, column=8, padx=1, pady=1)


frame15 = tk.Frame(frame_contenido)
frame15.pack(anchor="w")

alcohol = StringVar()
cigarrillo = StringVar()
otrassustanciaspsicoactivas = StringVar()


cuadrohabitostoxicos = tk.LabelFrame(frame15, text="HABITOS TOXICOS", font=bool)
cuadrohabitostoxicos.grid(row=0, column=0, padx=10, pady=10)

alcohollabel = Label(cuadrohabitostoxicos, text="ALCOHOL")
alcohollabel.grid(row=0, column=0, padx=10, pady=5)
alcohol_entry = Entry(cuadrohabitostoxicos, textvariable=alcohol, width=45)
alcohol_entry.grid(row=1, column=0, padx=10, pady=5)

cigarrillolabel = Label(cuadrohabitostoxicos, text="CIGARRILLO")
cigarrillolabel.grid(row=0, column=1, padx=10, pady=5)
cigarrillo_entry = Entry(cuadrohabitostoxicos, textvariable=cigarrillo, width=45)
cigarrillo_entry.grid(row=1, column=1, padx=10, pady=5)

otrassustanciaspsicoactivaslabel = Label(cuadrohabitostoxicos, text="OTRAS SUSTANCIAS PSICOACTIVAS")
otrassustanciaspsicoactivaslabel.grid(row=0, column=2, padx=10, pady=5)
otrassustanciaspsicoactivas_entry = Entry(cuadrohabitostoxicos, textvariable=otrassustanciaspsicoactivas, width=45)
otrassustanciaspsicoactivas_entry.grid(row=1, column=2, padx=10, pady=5)


frame16 = tk.Frame(frame_contenido)
frame16.pack(anchor="w")

tencionarterial = StringVar()
frecuenciacardiaca = StringVar()
frecuenciarespiratoria = StringVar()
peso = StringVar()
talla = StringVar()
indicecorporal = StringVar()
opclateralidaddominate = IntVar ()

cuadroexamenfisico = tk.LabelFrame(frame16, text="EXAMEN FISICO", font=bool)
cuadroexamenfisico.grid(row=0, column=0, padx=10, pady=10)

tencionarteriallabel = Label(cuadroexamenfisico, text="TENCION ARTERIAL (mm Hg)")
tencionarteriallabel.grid(row=0, column=0, padx=10, pady=5)
tencionarterial_entry = Entry(cuadroexamenfisico, textvariable=tencionarterial, width=34)
tencionarterial_entry.grid(row=1, column=0, padx=10, pady=5)

frecuenciacardiacalabel = Label(cuadroexamenfisico, text="FRECUENCIA CARDIACA (lat x min)")
frecuenciacardiacalabel.grid(row=0, column=1, padx=10, pady=5)
frecuenciacardiaca_entry = Entry(cuadroexamenfisico, textvariable=frecuenciacardiaca, width=34)
frecuenciacardiaca_entry.grid(row=1, column=1, padx=10, pady=5)

frecuenciarespiratorialabel = Label(cuadroexamenfisico, text="FRECUENCIA RESPIRATORIA (resp x min)")
frecuenciarespiratorialabel.grid(row=0, column=2, padx=10, pady=5)
frecuenciarespiratoria_entry = Entry(cuadroexamenfisico, textvariable=frecuenciarespiratoria, width=34)
frecuenciarespiratoria_entry.grid(row=1, column=2, padx=10, pady=5)

pesolabel = Label(cuadroexamenfisico, text="PESO (KG)")
pesolabel.grid(row=2, column=0, padx=10, pady=5)
peso_entry = Entry(cuadroexamenfisico, textvariable=peso, width=34)
peso_entry.grid(row=3, column=0, padx=10, pady=5)

tallalabel = Label(cuadroexamenfisico, text="TALLA (mts)")
tallalabel.grid(row=2, column=1, padx=10, pady=5)
talla_entry = Entry(cuadroexamenfisico, textvariable=talla, width=34)
talla_entry.grid(row=3, column=1, padx=10, pady=5)

indicecorporallabel = Label(cuadroexamenfisico, text="INDICE DE MASA CORPORAL")
indicecorporallabel.grid(row=2, column=2, padx=10, pady=5)
indicecorporal_entry = Entry(cuadroexamenfisico, textvariable=indicecorporal, width=34)
indicecorporal_entry.grid(row=3, column=2, padx=10, pady=5)

lateralidaddominatelabel = Label(cuadroexamenfisico, text="LATERALIDAD DOMINANTE")
lateralidaddominatelabel.grid(row=0, column=3, padx=10, pady=5)

opcion1 = tk.Radiobutton(cuadroexamenfisico, text="DIESTRO", compound="right", width=20, anchor="n", variable=opcionesevaluacion, value=1).grid(row=1, column=3, padx=5, pady=5)

opcion2 = tk.Radiobutton(cuadroexamenfisico, text="ZURDO", width=20, anchor="n", variable=opcionesevaluacion, value=2).grid(row=2, column=3, padx=5, pady=5)

opcion3 = tk.Radiobutton(cuadroexamenfisico, text="AMBIDIESTRO", width=20, anchor="n", variable=opcionesevaluacion, value=3).grid(row=3, column=3, padx=5, pady=5)


frame17= tk.Frame(frame_contenido)
frame17.pack(anchor="w")

## Opciones de los organos
opcpielfaneras = IntVar()
opccabeza = IntVar()
opcojos= IntVar()
opcconjuntivasoculares = IntVar()
opcreflejopupilar= IntVar()
opcoidos = IntVar()
opcotoscopia = IntVar()
opcnariz = IntVar()
opcsenosparanasales = IntVar()
opcboca = IntVar()
opccuello = IntVar()
opctoraz = IntVar()
opcmamas= IntVar()
opcpulmones = IntVar()
opccardiovascular= IntVar()
opccirculatorio = IntVar()
opcabdomen = IntVar()
opcgenitalesexternos = IntVar()
opcmiembrossuperiores = IntVar()
opcmiembrosinferiores = IntVar()
opccolumnavertebral = IntVar()
opcneurologico = IntVar()
opcestadomental= IntVar()
opcreflejostendinosas = IntVar()
opcmotilidad= IntVar()
opcsensibilidad = IntVar()
opcfuerzatonomuscular = IntVar()
opcmarcha = IntVar()
pielfaneras = StringVar()
cabeza = StringVar()
ojos= StringVar()
conjuntivasoculares = StringVar()
reflejopupilar= StringVar()
oidos = StringVar()
otoscopia = StringVar()
nariz = StringVar()
senosparanasales = StringVar()
boca = StringVar()
cuello = StringVar()
toraz = StringVar()
mamas= StringVar()
pulmones = StringVar()
cardiovascular= StringVar()
circulatorio = StringVar()
abdomen = StringVar()
genitalesexternos = StringVar()
miembrossuperiores = StringVar()
miembrosinferiores = StringVar()
columnavertebral = StringVar()
neurologico = StringVar()
estadomental= StringVar()
reflejostendinosas = StringVar()
motilidad= StringVar()
oidos = StringVar()
sensibilidad = StringVar()
fuerzatonomuscular = StringVar()
marcha = StringVar()

# LabelFrame para la revisión por sistema.
frameRevisionPorSistema = tk.LabelFrame(frame17, text="REVISION POR SISTEMA", font=(bool)) #esto es para modificar el texto, aumento, negrita, ect
frameRevisionPorSistema.grid(row=0, column=0, padx=10, pady=10)

organolabe = Label(frameRevisionPorSistema, text="ORGANOS")
organolabe.grid(row=0, column=0, padx=2, pady=2)
normallabel = Label(frameRevisionPorSistema, text="NORMAL")
normallabel.grid(row=0, column=1, padx=2, pady=2)
anormallabel = Label(frameRevisionPorSistema, text="ANORMAL")
anormallabel.grid(row=0, column=2, padx=2, pady=2)
hallazgolabel = Label(frameRevisionPorSistema, text="HALLAZGO")
hallazgolabel.grid(row=0, column=3, padx=2, pady=2)

# Variables para la revisión por sistema.
revisionSistema = {
    "PIEL Y FANERAS": (tk.IntVar(), tk.StringVar()),
    "CABEZA": (tk.IntVar(), tk.StringVar()),
    "OJOS": (tk.IntVar(), tk.StringVar()),
    "CONJUNTIVAS OCULARES": (tk.IntVar(), tk.StringVar()),
    "REFLEJOS PUPILARES": (tk.IntVar(), tk.StringVar()),
    "OIDOS": (tk.IntVar(), tk.StringVar()),
    "OTOSCOPIA": (tk.IntVar(), tk.StringVar()),
    "NARIZ": (tk.IntVar(), tk.StringVar()),
    "SENOS PARANASALES": (tk.IntVar(), tk.StringVar()),
    "BOCA": (tk.IntVar(), tk.StringVar()),
    "CUELLO": (tk.IntVar(), tk.StringVar()),
    "TORAX": (tk.IntVar(), tk.StringVar()),
    "MAMAS": (tk.IntVar(), tk.StringVar()),
    "PULMONES": (tk.IntVar(), tk.StringVar()),
    "CARDIOVASCULARES": (tk.IntVar(), tk.StringVar()),
    "CIRCULATORIO": (tk.IntVar(), tk.StringVar()),
    "ABDOMEN": (tk.IntVar(), tk.StringVar()),
    "GENITALES EXTERNOS": (tk.IntVar(), tk.StringVar()),
    "MIEMBROS SUPERIORES": (tk.IntVar(), tk.StringVar()),
    "MIEMBROS INFERIORES": (tk.IntVar(), tk.StringVar()),
    "COLUMNA VERTEBRAL": (tk.IntVar(), tk.StringVar()),
    "NEUROLOGICO": (tk.IntVar(), tk.StringVar()),
    "ESTADO MENTAL": (tk.IntVar(), tk.StringVar()),
    "REFLEJOS TENDIOSOS": (tk.IntVar(), tk.StringVar()),
    "MOTILIDAD": (tk.IntVar(), tk.StringVar()),
    "SENSIBILIDAD": (tk.IntVar(), tk.StringVar()),
    "FUERZA Y TONO MUSCULAR": (tk.IntVar(), tk.StringVar()),
    "MARCHA": (tk.IntVar(), tk.StringVar()),
}

# Crear las filas usando la función crear_rows_revision_por_sistema
for i, (text, (var1, var2)) in enumerate(revisionSistema.items(), start=1):
    crear_rows_revision_por_sistema(frameRevisionPorSistema, text, var1, var2, i)

frame17 = tk.Frame(frame_contenido)
frame17.pack(anchor="w")

laboratorio = StringVar()
rxtoraz = StringVar()
rxcolumna = StringVar()
audiometria = StringVar()
espirometria = StringVar()
visiometria = StringVar()
ekg = StringVar()
otrosdeparaliticos = StringVar()


cuadroexamenespara = tk.LabelFrame(frame17, text="RESULTADOS DE EXMENES PARACLINICOS", font=(bool)) #esto es para modificar el texto, aumento, negrita, ect
cuadroexamenespara.grid(row=0, column=0, padx=10, pady=10)

laboratoriolabel = Label(cuadroexamenespara,text="LABORATORIO")
laboratoriolabel.grid(row=0, column=0, sticky="w", padx=5, pady=2)
laboratorio_entry = Entry(cuadroexamenespara, textvariable=laboratorio, width=124)
laboratorio_entry.grid(row=0, column=1, padx=10, pady=10)

rxtorazlabel = Label(cuadroexamenespara,text="RX DE TORAX")
rxtorazlabel.grid(row=1, column=0, sticky="w", padx=5, pady=2)
rxtoraz_entry = Entry(cuadroexamenespara, textvariable=rxtoraz, width=124)
rxtoraz_entry.grid(row=1, column=1, padx=10, pady=10)

rxcolumnalabel = Label(cuadroexamenespara,text="RX DE COLUMNA")
rxcolumnalabel.grid(row=2, column=0, sticky="w", padx=5, pady=2)
rxcolumna_entry = Entry(cuadroexamenespara, textvariable=rxcolumna, width=124)
rxcolumna_entry.grid(row=2, column=1, padx=10, pady=10)

audiometrialabel = Label(cuadroexamenespara,text="AUDIOMETRIA")
audiometrialabel.grid(row=3, column=0, sticky="w", padx=5, pady=2)
audiometria_entry = Entry(cuadroexamenespara, textvariable=audiometria, width=124)
audiometria_entry.grid(row=3, column=1, padx=10, pady=10)

espirometrialabel = Label(cuadroexamenespara,text="ESPIROMETRIA")
espirometrialabel.grid(row=4, column=0, sticky="w", padx=5, pady=2)
espirometria_entry = Entry(cuadroexamenespara, textvariable=espirometria, width=124)
espirometria_entry.grid(row=4, column=1, padx=10, pady=10)

visiometrialabel = Label(cuadroexamenespara,text="VISIOMETRIA")
visiometrialabel.grid(row=5, column=0, sticky="w", padx=5, pady=2)
visiometria_entry = Entry(cuadroexamenespara, textvariable=visiometria, width=124)
visiometria_entry.grid(row=5, column=1, padx=10, pady=10)

ekglabel = Label(cuadroexamenespara,text="EKG")
ekglabel.grid(row=6, column=0, sticky="w", padx=5, pady=2)
ekg_entry = Entry(cuadroexamenespara, textvariable=ekg, width=124)
ekg_entry.grid(row=6, column=1, padx=10, pady=10)

otrosdeparaliticoslabel = Label(cuadroexamenespara,text="OTROS")
otrosdeparaliticoslabel.grid(row=7, column=0, sticky="w", padx=5, pady=2)
otrosdeparaliticos_entry = Entry(cuadroexamenespara, textvariable=otrosdeparaliticos, width=124)
otrosdeparaliticos_entry.grid(row=7, column=1, padx=10, pady=10)

frame18 = tk.Frame(frame_contenido)
frame18.pack(anchor="w")

impresionmedica = Text()


cuadroimpresionmedica = tk.LabelFrame(frame18, text="IMPRESION DIAGNSTICA", font=(bool)) #esto es para modificar el texto, aumento, negrita, ect
cuadroimpresionmedica.grid(row=0, column=0, padx=10, pady=10)

impresionmedicatexto = Text(cuadroimpresionmedica, width=107, height=3)
impresionmedicatexto.grid(row=0, column=0, padx=10, pady=10)



frame19 = tk.Frame(frame_contenido)
frame19.pack(anchor="w")

opcparaelcumplimiento = IntVar()
opcparacontinuar = IntVar()
opcparaeldisfrute = IntVar()
opcparaserretirado = IntVar()

cuadrocondicionmedica = tk.LabelFrame(frame19, text="", font=(bool)) #esto es para modificar el texto, aumento, negrita, ect
cuadrocondicionmedica.grid(row=0, column=0, padx=10, pady=10)

cuadrocondicionmedicalabel = Label(cuadrocondicionmedica, text="CONDICION MEDICA", font=bool)
cuadrocondicionmedicalabel.grid(row=0, column=0, padx=10, pady=10)
limitacioneslabel = Label(cuadrocondicionmedica, text="LIMITES", width=15, anchor="e", font=bool)
limitacioneslabel.grid(row=0, column=1, padx=1, pady=5, sticky="e")
condicionmedica_silabel = Label(cuadrocondicionmedica, text="SI", font=bool)
condicionmedica_silabel.grid(row=0, column=2, padx=5, pady=10)
condicionmedica_nolabel = Label(cuadrocondicionmedica, text="NO", font=bool)
condicionmedica_nolabel.grid(row=0, column=3, padx=10, pady=10)

opcparaelcumplimientolabel = Label(cuadrocondicionmedica, text="PARA EL CUMPLIMIENTO DE LAS FUNCIONES EN EL CARGO POSTULADO EN AREAS CON RIESGOS DESCRITOS")
opcparaelcumplimientolabel.grid(row=1, column=0, padx=10, pady=10, sticky="w")
opcparaelcumplimiento1 = tk.Radiobutton(cuadrocondicionmedica, text="", width=4, anchor="e", variable=opcparaelcumplimiento, value=1).grid(row=1, column=2, padx=5, pady=1)
opcparaelcumplimiento2 = tk.Radiobutton(cuadrocondicionmedica, text="", width=4, anchor="e", variable=opcparaelcumplimiento, value=2).grid(row=1, column=3, padx=5, pady=1)

opcparacontinuarlabel = Label(cuadrocondicionmedica, text="PARA CONTINUAR REALIZANDO LAS LABORES EN AREAS DESCRITAS")
opcparacontinuarlabel.grid(row=2, column=0, padx=10, pady=10, sticky="w")
opcparacontinuar1 = tk.Radiobutton(cuadrocondicionmedica, text="", width=4, anchor="e", variable=opcparacontinuar, value=1).grid(row=2, column=2, padx=5, pady=1)
opcparacontinuar2 = tk.Radiobutton(cuadrocondicionmedica, text="", width=4, anchor="e", variable=opcparacontinuar, value=2).grid(row=2, column=3, padx=5, pady=1)

opcparaeldisfrutelabel = Label(cuadrocondicionmedica, text="PARA EL DISFRUTE DE SU PERIODO VACACIONAL")
opcparaeldisfrutelabel.grid(row=3, column=0, padx=10, pady=10, sticky="w")
opcparaeldisfrute1 = tk.Radiobutton(cuadrocondicionmedica, text="", width=4, anchor="e", variable=opcparaeldisfrute, value=1).grid(row=3, column=2, padx=5, pady=1)
opcparaeldisfrute2 = tk.Radiobutton(cuadrocondicionmedica, text="", width=4, anchor="e", variable=opcparaeldisfrute, value=2).grid(row=3, column=3, padx=5, pady=1)

opcparaserretiradolabel = Label(cuadrocondicionmedica, text="PARA SER RETIRADO DE LA EMPRESA")
opcparaserretiradolabel.grid(row=4, column=0, padx=10, pady=10, sticky="w")
opcparaserretirado1 = tk.Radiobutton(cuadrocondicionmedica, text="", width=4, anchor="e", variable=opcparaserretirado, value=1).grid(row=4, column=2, padx=5, pady=1)
opcparaserretirado2 = tk.Radiobutton(cuadrocondicionmedica, text="", width=4, anchor="e", variable=opcparaserretirado, value=2).grid(row=4, column=3, padx=5, pady=1)


frame20 = tk.Frame(frame_contenido)
frame20.pack(anchor="w")

recomendaciones = Text()

cuadrorecomendaciones = tk.LabelFrame(frame20, text="RECOMENDACIONES", font=(bool)) #esto es para modificar el texto, aumento, negrita, ect
cuadrorecomendaciones.grid(row=0, column=0, padx=10, pady=10)

recomendacionestexto = Text(cuadrorecomendaciones, width=107, height=3)
recomendacionestexto.grid(row=0, column=0, padx=10, pady=10)


frame21 = tk.Frame(frame_contenido)
frame21.pack(anchor="w")

calificacionperdida = StringVar()
tratamientomedico = StringVar()
reubicacion = StringVar()
remision = StringVar()

cuadromanejo = tk.LabelFrame(frame21, text="MANEJO (EVALUACION MEDICO LAVORAL)", font=(bool)) #esto es para modificar el texto, aumento, negrita, ect
cuadromanejo.grid(row=0, column=0, padx=10, pady=10)

calificacionperdidalabel = Label(cuadromanejo, text="CALIFICACION PERDIDA LABORAL")
calificacionperdidalabel.grid(row=0, column=0, padx=10, pady=10)
calificacionperdida_entry = Entry(cuadromanejo, textvariable="calificacionperdida", width=107)
calificacionperdida_entry.grid(row=0, column=1, padx=10, pady=10)

tratamientomedicolabel = Label(cuadromanejo, text="TRATAMIENTO MEDICO")
tratamientomedicolabel.grid(row=1, column=0, padx=10, pady=10, sticky="w")
tratamientomedico_entry = Entry(cuadromanejo, textvariable="tratamientomedico", width=107)
tratamientomedico_entry.grid(row=1, column=1, padx=10, pady=10)

reubicacionlabel = Label(cuadromanejo, text="REUBICACION")
reubicacionlabel.grid(row=2, column=0, padx=10, pady=10, sticky="w")
reubicacion_entry = Entry(cuadromanejo, textvariable="reubicacion", width=107)
reubicacion_entry.grid(row=2, column=1, padx=10, pady=10)

remisionlabel = Label(cuadromanejo, text="REMISION")
remisionlabel.grid(row=3, column=0, padx=10, pady=10, sticky="w")
remision_entry = Entry(cuadromanejo, textvariable="remision", width=107)
remision_entry.grid(row=3, column=1, padx=10, pady=10)


# Botón para guardar los datos
frame22 = tk.Frame(frame_contenido)
frame22.pack()


guardar_button = Button(frame22, text="GUARDAR", command=guardar_datos)
guardar_button.grid(row=0, column=0, padx=10, pady=10)

boton_regresar = Button(frame22, text="REGRESAR", command=ventana.destroy)
boton_regresar.grid(row=0, column=1, padx=10, pady=10)





ventana.mainloop()