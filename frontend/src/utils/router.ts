import EstudianteIcon from '../assets/estudiante.svg';
import ProfesorIcon from '../assets/profesor.svg';
import AulaIcon from '../assets/aula.svg';
import AsignaturaIcon from '../assets/asignatura.svg';
import MediosIcon from '../assets/medios.svg';
import ScreenType from "../types.ts";
import {RolesEnum} from "../api/RolesEnum.ts";
import NotaIcon from '../assets/nota.svg'
import UserIcon from '../assets/user-sidebar.svg'
import CursoIcon from '../assets/curso.svg'
import AusenciaIcon from '../assets/ausencia.svg'
import UsersIcon from '../assets/users.svg'
import FunctIcon from '../assets/charts.svg'

export const Screens = {
    Info: new ScreenType('Sobre mí', UserIcon, '/info', [RolesEnum.TEACHER, RolesEnum.STUDENT,RolesEnum.SECRETARY, RolesEnum.ADMIN, RolesEnum.DEAN]),
    Estudiantes: new ScreenType('Estudiantes', EstudianteIcon, '/estudiantes', [RolesEnum.TEACHER, RolesEnum.SECRETARY, RolesEnum.DEAN]),
    Profesores: new ScreenType('Profesores', ProfesorIcon, '/profesores', [RolesEnum.SECRETARY, RolesEnum.DEAN, RolesEnum.STUDENT]),
    Aulas: new ScreenType('Aulas', AulaIcon, '/aulas', [RolesEnum.TEACHER, RolesEnum.SECRETARY, RolesEnum.DEAN, RolesEnum.STUDENT]),
    Asignaturas: new ScreenType('Asignaturas', AsignaturaIcon, '/asignaturas', [RolesEnum.TEACHER, RolesEnum.SECRETARY, RolesEnum.DEAN, RolesEnum.STUDENT]),
    Medios: new ScreenType('Medios', MediosIcon, '/medios', [RolesEnum.TEACHER, RolesEnum.DEAN,RolesEnum.ADMIN]),
    Mantenimientos: new ScreenType('Mantenimientos', MediosIcon, '/mantenimientos', [RolesEnum.DEAN,RolesEnum.ADMIN]),
    Notas: new ScreenType('Notas', NotaIcon, '/nota', [RolesEnum.TEACHER, RolesEnum.SECRETARY, RolesEnum.DEAN, RolesEnum.STUDENT]),
    Cursos: new ScreenType('Cursos', CursoIcon, '/curso', [RolesEnum.SECRETARY, RolesEnum.DEAN]),
    Ausencias: new ScreenType('Ausencias', AusenciaIcon, '/ausencias', [RolesEnum.TEACHER, RolesEnum.SECRETARY, RolesEnum.DEAN, RolesEnum.STUDENT]),
    Usuarios: new ScreenType('Usuarios', UsersIcon, '/usuarios', [RolesEnum.SECRETARY]),
    Funcionalidades: new ScreenType('Funcionalidades', FunctIcon, '/funcionalidades', [ RolesEnum.SECRETARY, RolesEnum.DEAN, RolesEnum.ADMIN]),
}
