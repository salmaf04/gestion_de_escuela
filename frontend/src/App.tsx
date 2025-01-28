import LoginScreen from "./pages/login/LoginScreen.tsx";
import {BrowserRouter, Navigate, Route, Routes} from "react-router-dom";
import Sidebar from "./components/Sidebar.tsx";
import HomeScreen from "./pages/home/HomeScreen.tsx";
import Notification from "./components/Notification.tsx";
import {createContext, useCallback, useEffect, useState} from "react";
import {ProfesorGetAdapter} from "./pages/profesores/adapters/ProfesorGetAdapter.ts";
import EstudiantesScreen from "./pages/estudiantes/EstudiantesScreen.tsx";
import ProfesoresScreen from "./pages/profesores/ProfesoresScreen.tsx";
import AulasScreen from "./pages/aulas/AulasScreen.tsx";
import AsignaturasScreen from "./pages/asignaturas/AsignaturasScreen.tsx";
import MediosScreen from "./pages/medios/MediosScreen.tsx";
import MantenimientosScreen from "./pages/mantenimientos/MantenimientosScreen.tsx";
import {AulaGetAdapter} from "./pages/aulas/adapters/AulaGetAdapter.ts";
import {MedioGetAdapter} from "./pages/medios/adapters/MedioGetAdapter.ts";
import UsuariosScreen from "./pages/usuarios/UsuariosScreen.tsx";
import {AsignaturaGetAdapter} from "./pages/asignaturas/adapters/AsignaturaGetAdapter.ts";
import {RolesEnum} from "./api/RolesEnum.ts";
import {EstudianteGetAdapter} from "./pages/estudiantes/adapters/EstudianteGetAdapter.ts";
import NotasScreen from "./pages/notas/NotasScreen.tsx";
import {INotaLocal} from "./pages/notas/models/INotaLocal.ts";
import {ICursoGetLocal} from "./pages/cursos/models/ICursoGetLocal.ts";
import CursosScreen from "./pages/cursos/CursosScreen.tsx";


interface AppContextInterface {
    setError?: (error: Error) => void;
    token?: string;
    setToken?: (token: string) => void;
    profesores?: ProfesorGetAdapter[];
    setProfesores?: (profesor: ProfesorGetAdapter[]) => void;
    aulas?: AulaGetAdapter[];
    setAulas?: (aulas: AulaGetAdapter[]) => void;
    estudiantes?: EstudianteGetAdapter[];
    setEstudiantes?: (estudiante: EstudianteGetAdapter[]) => void;
    medios?: MedioGetAdapter[];
    setMedios?: (medios: MedioGetAdapter[]) => void;
    asignaturas?: AsignaturaGetAdapter[];
    setAsignaturas?: (asignaturas: AsignaturaGetAdapter[]) => void;
    notas?: INotaLocal[];
    setNotas?: (notas: INotaLocal[]) => void;
    cursos?: ICursoGetLocal[];
    setCursos?: (cursos: ICursoGetLocal[]) => void;

    setRole?: (role: RolesEnum) => void,
    role?: RolesEnum,
    allowRoles?: (roles: RolesEnum[]) => boolean
}

export const AppContext = createContext<AppContextInterface>({})

function App() {
    const [error, setError] = useState<Error | undefined>()
    const [token, setToken] = useState<string>()
    const [profesores, setProfesores] = useState<ProfesorGetAdapter[]>()
    const [aulas, setAulas] = useState<AulaGetAdapter[]>()
    const [medios, setMedios] = useState<MedioGetAdapter[]>()
    const [asignaturas, setAsignaturas] = useState<AsignaturaGetAdapter[]>()
    const [notas, setNotas] = useState<INotaLocal[]>()
    const [estudiantes, setEstudiantes] = useState<EstudianteGetAdapter[]>()
    const [cursos, setCursos] = useState<ICursoGetLocal[]>()
    const [role, setRole] = useState<RolesEnum>()
    useEffect(() => {
        const t = sessionStorage.getItem('token')
        if (t) {
            setToken(t)
            setRole(JSON.parse(atob(t!.split(".")[1])).type)
        }

    }, []);
    const allowRoles = useCallback((roles: RolesEnum[]) => {

            return roles?.some((item) => item === role)
    }, [role])

    return (
        <AppContext.Provider value={{
            setError: setError,
            token: token,
            setToken: setToken,
            profesores: profesores,
            setProfesores: setProfesores,
            aulas: aulas,
            setAulas: setAulas,
            medios: medios,
            setMedios: setMedios,
            asignaturas: asignaturas,
            setAsignaturas: setAsignaturas,
            role: role,
            setRole: setRole,
            allowRoles: allowRoles,
            estudiantes: estudiantes,
            setEstudiantes: setEstudiantes,
            notas: notas,
            setNotas: setNotas,
            cursos: cursos,
            setCursos: setCursos,
        }}>
            <BrowserRouter>
                {error &&
                    <Notification title={'Error:'} message={error.message}
                                  className={'bg-red-100 text-sm rounded-md py-1'} onClick={() => {
                        setError(undefined)
                    }}/>
                }
                {token ?
                    (
                        <div className={'h-dvh bg-indigo-50 flex w-full'}>
                            <div className={'w-1/12'}>
                                <Sidebar/>
                            </div>
                            <div className={'w-11/12'}>
                                <Routes>
                                    <Route path={'/'} element={<Navigate to={'/inicio'}/>}/>
                                    <Route path={'/inicio'} element={<HomeScreen/>}/>
                                    {allowRoles([RolesEnum.TEACHER, RolesEnum.SECRETARY, RolesEnum.DEAN]) &&
                                        <Route path={'/estudiantes'} element={<EstudiantesScreen/>}/>
                                    }
                                    {allowRoles([RolesEnum.STUDENT, RolesEnum.SECRETARY, RolesEnum.DEAN]) &&
                                        <Route path={'/profesores'} element={<ProfesoresScreen/>}/>
                                    }
                                    {allowRoles([RolesEnum.TEACHER, RolesEnum.SECRETARY, RolesEnum.DEAN, RolesEnum.STUDENT]) &&
                                        <Route path={'/aulas'} element={<AulasScreen/>}/>
                                    }
                                    {allowRoles([RolesEnum.TEACHER, RolesEnum.SECRETARY, RolesEnum.DEAN, RolesEnum.STUDENT]) &&
                                        <Route path={'/asignaturas'} element={<AsignaturasScreen/>}/>
                                    }
                                    {allowRoles([RolesEnum.ADMIN, RolesEnum.TEACHER, RolesEnum.DEAN]) &&
                                        <Route path={'/medios'} element={<MediosScreen/>}/>
                                    }
                                    {allowRoles([RolesEnum.ADMIN, RolesEnum.SECRETARY, RolesEnum.DEAN]) &&
                                        <Route path={'/mantenimientos'} element={<MantenimientosScreen/>}/>
                                    }
                                    {allowRoles([RolesEnum.SECRETARY, RolesEnum.DEAN]) &&
                                        <Route path={'/usuarios'} element={<UsuariosScreen/>}/>
                                    }
                                    {allowRoles([RolesEnum.SECRETARY, RolesEnum.DEAN, RolesEnum.TEACHER]) &&
                                        <Route path={'/nota'} element={<NotasScreen/>}/>
                                    }
                                    {allowRoles([RolesEnum.SECRETARY, RolesEnum.DEAN, RolesEnum.TEACHER, RolesEnum.STUDENT]) &&
                                        <Route path={'/curso'} element={<CursosScreen/>}/>
                                    }
                                </Routes>
                            </div>
                        </div>
                    ) :
                    (
                        <Routes>
                            <Route path={'/'} element={<LoginScreen/>}/>
                            <Route path={'*'} element={<Navigate to={'/'}/>}/>
                        </Routes>
                    )


                }
            </BrowserRouter>
        </AppContext.Provider>

    )
}

export default App
