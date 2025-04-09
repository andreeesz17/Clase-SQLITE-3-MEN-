from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine(f'sqlite:///notas_estudiantesAndres.db')

#Crear la sesion
Sesion = sessionmaker(bind=engine)
sesion = Sesion()

class Base(DeclarativeBase):
    pass

class Estudiante(Base):
    __tablename__ = 'estudiante'
    
    id = Column(Integer, primary_key=True)
    nombre=Column(String, nullable=False)
    apellido = Column(String)
    
    def __repr__(self):
        return f'{self.nombre} {self.apellido}'
    


class Notas(Base):
    __tablename__ = 'nota'
    
    id = Column(Integer, primary_key=True)
    nota = Column(Float, nullable=False)
    materia = Column(String, nullable=False)
    estudiante_id = Column(Integer, ForeignKey('estudiante.id'))
        
    def __repr__(self):
        return f'nota: {self.nota}'
    
Base.metadata.create_all(engine)


def crearusuario():
    estudiante1 = Estudiante(nombre='Andres', apellido='Zambrano')
    sesion.add(estudiante1)
    sesion.commit()
    nota1 = Notas(nota=10, materia='Programacion', estudiante_id=estudiante1.id)
    sesion.add(nota1)
    sesion.commit()
    
    
def crearnotas():
    estudiante1 = sesion.query(Estudiante).filter_by(nombre='Andres').first()
    nota1 = Notas(nota=7, materia='Base de Datos', estudiante_id=estudiante1.id)
    sesion.add(nota1)
    sesion.commit()
    nota1 = Notas(nota=5, materia='Estadística I', estudiante_id=estudiante1.id)
    sesion.add(nota1)
    sesion.commit()
    
#crearnotas()
#crearusuario()


def consultar():
    estudiante1 = sesion.query(Estudiante).filter_by(nombre='Andres').first()
    
    nota1 = sesion.query(Notas).filter_by(estudiante_id = estudiante1.id).first()
    print(f'La nota del estudiante {estudiante1.nombre} {estudiante1.apellido} es {nota1.nota} en la materia {nota1.materia}')
    
#consultar()


def crear_usuario():
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    estudiante = Estudiante(nombre=nombre, apellido=apellido)
    sesion.add(estudiante)
    sesion.commit()
    print("Estudiante REGISTRADO")

def crear_notas():
    nombre = input("Ingrese el nombre del estudiante para agregar notas: ")
    estudiante = sesion.query(Estudiante).filter_by(nombre=nombre).first()
    if estudiante:
        materia = input("Ingrese la materia: ")
        nota = float(input("Ingrese la nota: "))
        nueva_nota = Notas(nota=nota, materia=materia, estudiante_id=estudiante.id)
        sesion.add(nueva_nota)
        sesion.commit()
        print("Nota AGREGADA")
    else:
        print("Estudiante no encontrado")

def consultar_notas():
    nombre = input("Ingrese solamente el nombre del estudiante a consultar: ")
    estudiante = sesion.query(Estudiante).filter_by(nombre=nombre).first()
    if estudiante:
        notas = sesion.query(Notas).filter_by(estudiante_id=estudiante.id).all()
        if notas:
            print(f"📚 Notas del estudiante {estudiante.nombre} {estudiante.apellido}:")
            for nota in notas:
                print(f" - ID: {nota.id} | {nota.materia}: {nota.nota}")
        else:
            print("No hay notas registradas para este estudiante")
    else:
        print("Estudiante no encontrado")

def editar_nota():
    id_nota = input("Ingrese el ID de la nota que desea editar: ")
    nota = sesion.query(Notas).filter_by(id=id_nota).first()
    if nota:
        nueva_nota = float(input("Ingrese la nueva nota: "))
        nota.nota = nueva_nota
        sesion.commit()
        print("Se ACTUALIZO su nota")
    else:
        print("Nota no encontrada")

def eliminar_nota():
    id_nota = input("Ingrese el ID de la nota que desea eliminar: ")
    nota = sesion.query(Notas).filter_by(id=id_nota).first()
    if nota:
        sesion.delete(nota)
        sesion.commit()
        print("Nota eliminada correctamente.")
    else:
        print("Nota no encontrada")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Crear estudiante")
        print("2. Agregar nota")
        print("3. Consultar notas")
        print("4. Editar nota")
        print("5. Eliminar nota")
        print("6. Salir")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == '1':
            crear_usuario()
        elif opcion == '2':
            crear_notas()
        elif opcion == '3':
            consultar_notas()
        elif opcion == '4':
            editar_nota()
        elif opcion == '5':
            eliminar_nota()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción incorrecta, intentelo de nuevo")

menu()