import LoginScreen from "./login/LoginScreen.tsx";
import {BrowserRouter, Navigate, Route, Routes} from "react-router-dom";
import {createContext, useEffect, useState} from "react";
import Sidebar from "./components/Sidebar.tsx";
import HomeScreen from "./home/HomeScreen.tsx";
import EstudiantesScreen from "./estudiantes/EstudiantesScreen.tsx";
import ProfesoresScreen from "./profesores/ProfesoresScreen.tsx";
import AsignaturasScreen from "./asignaturas/AsignaturasScreen.tsx";
import MediosScreen from "./medios/MediosScreen.tsx";
import MantenimientosScreen from "./mantenimientos/MantenimientosScreen.tsx";
import AulasScreen from "./aulas/AulasScreen.tsx";
import Alert from "./components/Alert.tsx";


interface AppContextInterface {
    setError?: (error: Error) => void;
}

export const AppContext = createContext<AppContextInterface>({})

function App() {
    const [isLogged, setIsLogged] = useState(false)
    const [error, setError] = useState<Error | undefined>()

    useEffect(() => {
        if (sessionStorage.getItem('token'))
            setIsLogged(true)
        else
            setIsLogged(false)
    }, []);

    return (
        <AppContext.Provider value={{
            setError: setError
        }}>
            <BrowserRouter>
                {isLogged ?
                    (
                        <div className={'h-dvh bg-indigo-50 flex'}>
                            {error &&
                                <Alert title={'Error:'} message={error.message} className={'bg-red-200'} onClick={() => {
                                    setError(undefined)
                                }}/>
                            }
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
        </AppContext.Provider>

    )
}

export default App
