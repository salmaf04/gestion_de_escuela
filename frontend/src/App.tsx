import LoginScreen from "./pages/login/LoginScreen.tsx";
import {BrowserRouter, Navigate, Route, Routes} from "react-router-dom";
import Sidebar from "./components/Sidebar.tsx";
import HomeScreen from "./pages/home/HomeScreen.tsx";
import Notification from "./components/Notification.tsx";
import {createContext, useEffect, useState} from "react";
import {ProfesorGetAdapter} from "./pages/profesores/adapters/ProfesorGetAdapter.ts";
import EstudiantesScreen from "./pages/estudiantes/EstudiantesScreen.tsx";
import ProfesoresScreen from "./pages/profesores/ProfesoresScreen.tsx";
import AulasScreen from "./pages/aulas/AulasScreen.tsx";
import AsignaturasScreen from "./pages/asignaturas/AsignaturasScreen.tsx";
import MediosScreen from "./pages/medios/MediosScreen.tsx";
import MantenimientosScreen from "./pages/mantenimientos/MantenimientosScreen.tsx";


interface AppContextInterface {
    setError?: (error: Error) => void;
    token?: string;
    setToken?: (token: string) => void;
    profesores?: ProfesorGetAdapter[];
    setProfesores?: (profesor: ProfesorGetAdapter[]) => void;

}

export const AppContext = createContext<AppContextInterface>({})

function App() {
    const [error, setError] = useState<Error | undefined>()
    const [token, setToken] = useState<string>()
    const [profesores, setProfesores] = useState<ProfesorGetAdapter[]>()
    useEffect(() => {
        const t = sessionStorage.getItem('token')
        if (t)
            setToken(t)
    }, []);

    return (
        <AppContext.Provider value={{
            setError: setError,
            token: token,
            setToken: setToken,
            profesores: profesores,
            setProfesores: setProfesores,
        }}>
            <BrowserRouter>
                {error &&
                    <Notification title={'Error:'} message={error.message} className={'bg-red-100 text-sm rounded-md py-1'} onClick={() => {
                        setError(undefined)
                        console.log('Error dismissed')
                    }}/>
                }
                {token ?
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
                            <Route path={'/'} element={<LoginScreen />}/>
                            <Route path={'*'} element={<Navigate to={'/'}/>}/>
                        </Routes>
                    )


                }
            </BrowserRouter>
        </AppContext.Provider>

    )
}

export default App
