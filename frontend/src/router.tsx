import EstudianteIcon from './assets/estudiante.svg';
import ProfesorIcon from './assets/profesor.svg';
import HomeIcon from './assets/home.svg';
import AulaIcon from './assets/aula.svg';
import AsignaturaIcon from './assets/asignatura.svg';
import MediosIcon from './assets/medios.svg';
import ScreenType from "./types.ts";

export const Screens = {
    Inicio: new ScreenType('Inicio', HomeIcon, '/inicio'),
    Estudiantes: new ScreenType('Estudiantes', EstudianteIcon, '/estudiantes'),
    Profesores: new ScreenType('Profesores', ProfesorIcon, '/profesores'),
    Aulas: new ScreenType('Aulas', AulaIcon, '/aulas'),
    Asignaturas: new ScreenType('Asignaturas', AsignaturaIcon, '/asignaturas'),
    Medios: new ScreenType('Medios', MediosIcon, '/medios'),
    Mantenimientos: new ScreenType('Mantenimientos', MediosIcon, '/mantenimientos'),
    Usuarios : new ScreenType('Usuarios' ,  MediosIcon , '/usuarios')
}
