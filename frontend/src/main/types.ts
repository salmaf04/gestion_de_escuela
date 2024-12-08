import EstudianteIcon from './assets/estudiante.svg';
import ProfesorIcon from './assets/profesor.svg';
import HomeIcon from './assets/home.svg';
import HomeScreen from "./home/HomeScreen.tsx";
import ProfesoresScreen from './profesores/ProfesoresScreen.tsx';
import EstudiantesScreen from "./estudiantes/EstudiantesScreen.tsx";


export default class ScreenType {
    title: string;
    icon: string;
    screen: JSX.Element;
    constructor(title: string, icon: string, screen: JSX.Element) {
        this.title = title;
        this.icon = icon;
        this.screen = screen;
    }

}
export const Screens = {
    Inicio: new ScreenType('Inicio', HomeIcon, HomeScreen()),
    Estudiantes: new ScreenType('Estudiantes', EstudianteIcon, EstudiantesScreen()),
    Profesores: new ScreenType('Profesores', ProfesorIcon, ProfesoresScreen()),
}

