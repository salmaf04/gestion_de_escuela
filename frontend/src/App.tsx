import LoginScreen from "./login/LoginScreen.tsx";
import {BrowserRouter, Navigate, Route, Routes} from "react-router-dom";
import {useEffect, useState} from "react";
import Sidebar from "./components/Sidebar.tsx";
import HomeScreen from "./home/HomeScreen.tsx";
import EstudiantesScreen from "./estudiantes/EstudiantesScreen.tsx";
import ProfesoresScreen from "./profesores/ProfesoresScreen.tsx";
import AsignaturasScreen from "./asignaturas/AsignaturasScreen.tsx";
import MediosScreen from "./medios/MediosScreen.tsx";
import MantenimientosScreen from "./mantenimientos/MantenimientosScreen.tsx";
import AulasScreen from "./aulas/AulasScreen.tsx";

function App() {
    const [isLogged, setIsLogged] = useState(false)
    useEffect(() => {
        if (sessionStorage.getItem('token'))
            setIsLogged(true)
        else
            setIsLogged(false)
    }, []);
    return (
        <BrowserRouter>
            {isLogged ?
                (
                    <div className={'h-dvh bg-indigo-50 flex'}>
                        <Sidebar/>
                        <Routes>
                            <Route path={'/'} element={<Navigate to={'/inicio'}/>}/>
                            <Route path={'/inicio'} element={<HomeScreen/>}/>
                            <Route path={'/estudiantes'} element={<EstudiantesScreen/>}/>
                            <Route path={'/profesores'} element={<ProfesoresScreen/>}/>
                            <Route path={'/aulas'} element={<AulasScreen/>}/>
                            <Route path={'/asignaturas'} element={<AsignaturasScreen/>}/>
                            <Route path={'/medios'} element={<MediosScreen/>}/>
                            <Route path={'/mantenimientos'} element={<MantenimientosScreen/>}/>
                        </Routes>
                    </div>
                ) :
                (
                    <Routes>
                        <Route path={'/'} element={<LoginScreen setIsLogged={setIsLogged}/>}/>
                        <Route path={'*'} element={<Navigate to={'/'}/>}/>
                    </Routes>
                )


            }
        </BrowserRouter>
    )
}

export default App
