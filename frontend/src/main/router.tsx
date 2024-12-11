import EstudianteIcon from './assets/estudiante.svg';
import ProfesorIcon from './assets/profesor.svg';
import HomeIcon from './assets/home.svg';
import AulaIcon from './assets/aula.svg';
import AsignaturaIcon from './assets/asignatura.svg';
import MediosIcon from './assets/medios.svg';

import HomeScreen from "./home/HomeScreen.tsx";
import ProfesoresScreen from './profesores/ProfesoresScreen.tsx';
import EstudiantesScreen from "./estudiantes/EstudiantesScreen.tsx";
import AulasScreen from "./aulas/AulasScreen.tsx";
import AsignaturasScreen from "./asignaturas/AsignaturasScreen.tsx";
import MediosScreen from "./medios/MediosScreen.tsx";
import ScreenType from "./types.ts";
import MantenimientosScreen from "./mantenimientos/MantenimientosScreen.tsx";

export const Screens = {
    Inicio: new ScreenType('Inicio', HomeIcon, <HomeScreen />),
    Estudiantes: new ScreenType('Estudiantes', EstudianteIcon, <EstudiantesScreen />),
    Profesores: new ScreenType('Profesores', ProfesorIcon, <ProfesoresScreen/>),
    Aulas: new ScreenType('Aulas', AulaIcon, <AulasScreen/>),
    Asignaturas: new ScreenType('Asignaturas', AsignaturaIcon, <AsignaturasScreen/>),
    Medios: new ScreenType('Medios', MediosIcon, <MediosScreen/>),
    Mantenimientos: new ScreenType('Mantenimientos', MediosIcon, <MantenimientosScreen/>),
}
