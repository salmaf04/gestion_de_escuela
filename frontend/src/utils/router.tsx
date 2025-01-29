import EstudianteIcon from '../assets/estudiante.svg';
import ProfesorIcon from '../assets/profesor.svg';
import HomeIcon from '../assets/home.svg';
import AulaIcon from '../assets/aula.svg';
import AsignaturaIcon from '../assets/asignatura.svg';
import MediosIcon from '../assets/medios.svg';
import ScreenType from "../types.ts";
import {RolesEnum} from "../api/RolesEnum.ts";
import NotaIcon from '../assets/nota.svg'

export const Screens = {
    Inicio: new ScreenType('Inicio', HomeIcon, '/inicio', [RolesEnum.TEACHER, RolesEnum.SECRETARY, RolesEnum.DEAN,RolesEnum.ADMIN, RolesEnum.STUDENT]),
    Estudiantes: new ScreenType('Estudiantes', EstudianteIcon, '/estudiantes', [RolesEnum.TEACHER, RolesEnum.SECRETARY, RolesEnum.DEAN]),
    Profesores: new ScreenType('Profesores', ProfesorIcon, '/profesores', [RolesEnum.TEACHER, RolesEnum.SECRETARY, RolesEnum.DEAN, RolesEnum.STUDENT]),
    Aulas: new ScreenType('Aulas', AulaIcon, '/aulas', [RolesEnum.TEACHER, RolesEnum.SECRETARY, RolesEnum.DEAN, RolesEnum.STUDENT]),
    Asignaturas: new ScreenType('Asignaturas', AsignaturaIcon, '/asignaturas', [RolesEnum.TEACHER, RolesEnum.SECRETARY, RolesEnum.DEAN, RolesEnum.STUDENT]),
    Medios: new ScreenType('Medios', MediosIcon, '/medios', [RolesEnum.TEACHER, RolesEnum.DEAN,RolesEnum.ADMIN, RolesEnum.SECRETARY]),
    Mantenimientos: new ScreenType('Mantenimientos', MediosIcon, '/mantenimientos', [RolesEnum.DEAN,RolesEnum.ADMIN, RolesEnum.SECRETARY]),
    Usuarios : new ScreenType('Usuarios' ,  MediosIcon , '/usuarios', [RolesEnum.SECRETARY, RolesEnum.DEAN]),
    Notas: new ScreenType('Notas', NotaIcon, '/nota', [RolesEnum.TEACHER, RolesEnum.SECRETARY, RolesEnum.DEAN]),
    Cursos: new ScreenType('Cursos', NotaIcon, '/curso', [RolesEnum.TEACHER, RolesEnum.SECRETARY, RolesEnum.DEAN, RolesEnum.STUDENT]),
    Ausencias: new ScreenType('Ausencias', NotaIcon, '/ausencias', [RolesEnum.TEACHER, RolesEnum.SECRETARY, RolesEnum.DEAN, RolesEnum.STUDENT]),
}
