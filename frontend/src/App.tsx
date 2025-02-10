import LoginScreen from "./pages/login/LoginScreen.tsx";
import {BrowserRouter, Navigate, Route, Routes} from "react-router-dom";
import Sidebar from "./components/Sidebar.tsx";
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
import {AsignaturaGetAdapter} from "./pages/asignaturas/adapters/AsignaturaGetAdapter.ts";
import {RolesEnum} from "./api/RolesEnum.ts";
import {EstudianteGetAdapter} from "./pages/estudiantes/adapters/EstudianteGetAdapter.ts";
import NotasScreen from "./pages/notas/NotasScreen.tsx";
import {INotaLocal} from "./pages/notas/models/INotaLocal.ts";
import {ICursoGetLocal} from "./pages/cursos/models/ICursoGetLocal.ts";
import CursosScreen from "./pages/cursos/CursosScreen.tsx";
import {Screens} from "./utils/router.ts";
import {IMantenimientoLocal} from "./pages/mantenimientos/models/IMantenimientoLocal.ts";
import FuncionalidadesScreen from "./pages/funcionalidades/FuncionalidadesScreen.tsx";
import InfoScreen from "./pages/info/InfoScreen.tsx";
import {ISecretariaDB} from "./pages/info/models/ISecretariaDB.ts";
import {IAdministradorDB} from "./pages/info/models/IAdministradorDB.ts";
import {IAusenciaLocal} from "./pages/ausencias/models/IAusenciaLocal.ts";
import AusenciasScreen from "./pages/ausencias/AusenciasScreen.tsx";
import {IUsuarioLocal} from "./pages/usuarios/models/IUsuarioLocal.ts";
import UsuariosScreen from "./pages/usuarios/UsuariosScreen.tsx";
import {IValorationPeriod} from "./pages/info/models/IValorationPeriod.ts";
import ValoracionesScreen from "./pages/valoraciones/ValoracionesScreen.tsx";


interface AppContextInterface {
    setError?: (error: Error) => void;
    token?: string;
    setToken?: (token: string) => void;
    profesores?: ProfesorGetAdapter[];
    setProfesores?: (profesor: ProfesorGetAdapter[]) => void;
    decanos?: ProfesorGetAdapter[];
    setDecanos?: (decano: ProfesorGetAdapter[]) => void;
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
    mantenimientos?: IMantenimientoLocal[],
    setMantenimientos?: (mantenimiento: IMantenimientoLocal[]) => void,
    ausencias?: IAusenciaLocal[],
    setAusencias?: (ausencia: IAusenciaLocal[]) => void,
    secretarias?: ISecretariaDB[],
    setSecretarias?: (secretaria: ISecretariaDB[]) => void,
    administradores?: IAdministradorDB[],
    setAdministradores?: (administradores: IAdministradorDB[]) => void,
    usuarios?: IUsuarioLocal[],
    setUsuarios?: (usuarios: IUsuarioLocal[]) => void,
    valorationPeriod?: IValorationPeriod,
    setvalorationPeriod?: (usuarios: IValorationPeriod) => void,

    setRoles?: (role: RolesEnum[]) => void,
    roles?: RolesEnum[],
    allowRoles?: (roles: RolesEnum[]) => boolean
    personalId?: string,
    setPersonalId?: (personalId: string) => void
    typeRole?: string,
    setTypeRole?: (typeRole: string) => void,

    username?: string,
    setUsername?: (username: string) => void

    message?: string,
    setMessage?: (message: string) => void
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
    const [mantenimientos, setMantenimientos] = useState<IMantenimientoLocal[]>()
    const [ausencias, setAusencias] = useState<IAusenciaLocal[]>()
    const [secretarias, setSecretarias] = useState<ISecretariaDB[]>()
    const [administradores, setAdministradores] = useState<IAdministradorDB[]>()
    const [decanos, setDecanos] = useState<ProfesorGetAdapter[]>()
    const [valorationPeriod, setvalorationPeriod] = useState<IValorationPeriod>()
    const [roles, setRoles] = useState<RolesEnum[]>()
    const [personalId, setPersonalId] = useState<string>()
    const [message, setMessage] = useState<string | undefined>()
    const [username, setUsername] = useState<string>()
    const [usuarios, setUsuarios] = useState<IUsuarioLocal[]>()
    const [typeRole, setTypeRole] = useState<string>()

    useEffect(() => {
        const t = sessionStorage.getItem('token')
        if (t) {
            setToken(t)
            setRoles(JSON.parse(atob(t!.split(".")[1])).roles)
            setPersonalId(JSON.parse(atob(t!.split(".")[1])).user_id)
            setUsername(JSON.parse(atob(t!.split(".")[1])).sub)
            setTypeRole(JSON.parse(atob(t!.split(".")[1])).type)
        }

    }, []);
    const allowRoles = useCallback((rolesParam: RolesEnum[]) => {
            return rolesParam.some(r => roles?.includes(r))
    }, [roles])

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
            roles: roles,
            setRoles: setRoles,
            allowRoles: allowRoles,
            estudiantes: estudiantes,
            setEstudiantes: setEstudiantes,
            notas: notas,
            setNotas: setNotas,
            cursos: cursos,
            setCursos: setCursos,
            mantenimientos: mantenimientos,
            setMantenimientos: setMantenimientos,
            personalId,
            setPersonalId: setPersonalId,
            message,
            setMessage,
            ausencias: ausencias,
            setAusencias: setAusencias,
            username: username,
            setUsername: setUsername,
            secretarias: secretarias,
            setSecretarias: setSecretarias,
            administradores: administradores,
            setAdministradores: setAdministradores,
            usuarios: usuarios,
            setUsuarios: setUsuarios,
            typeRole: typeRole,
            setTypeRole: setTypeRole,
            decanos: decanos,
            setDecanos: setDecanos,
            setvalorationPeriod: setvalorationPeriod,
            valorationPeriod: valorationPeriod
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
                        <div className={'h-dvh bg-indigo-50 flex w-full overscroll-none'}>
                            <div className={'w-1/12'}>
                                <Sidebar/>
                            </div>
                            <div className={'w-11/12'}>
                                <Routes>
                                    <Route path={'/info'} element={<InfoScreen/>}/>
                                    <Route path={'/'} element={<Navigate to={'/info'}/>}/>
                                    {allowRoles(Screens.Estudiantes.allowedRoles) &&
                                        <Route path={'/estudiantes'} element={<EstudiantesScreen/>}/>
                                    }
                                    {allowRoles(Screens.Profesores.allowedRoles) &&
                                        <Route path={'/profesores'} element={<ProfesoresScreen/>}/>
                                    }
                                    {allowRoles(Screens.Aulas.allowedRoles) &&
                                        <Route path={'/aulas'} element={<AulasScreen/>}/>
                                    }
                                    {allowRoles(Screens.Asignaturas.allowedRoles) &&
                                        <Route path={'/asignaturas'} element={<AsignaturasScreen/>}/>
                                    }
                                    {allowRoles(Screens.Medios.allowedRoles) &&
                                        <Route path={'/medios'} element={<MediosScreen/>}/>
                                    }
                                    {allowRoles(Screens.Notas.allowedRoles) &&
                                        <Route path={'/nota'} element={<NotasScreen/>}/>
                                    }
                                    {allowRoles(Screens.Cursos.allowedRoles) &&
                                        <Route path={'/curso'} element={<CursosScreen/>}/>
                                    }
                                    {allowRoles(Screens.Mantenimientos.allowedRoles) &&
                                        <Route path={'/mantenimientos'} element={<MantenimientosScreen/>}/>
                                    }
                                    {allowRoles(Screens.Funcionalidades.allowedRoles) &&
                                        <Route path={'/funcionalidades'} element={<FuncionalidadesScreen/>}/>
                                    }
                                    {allowRoles(Screens.Ausencias.allowedRoles) &&
                                        <Route path={'/ausencias'} element={<AusenciasScreen/>}/>
                                    }
                                    {allowRoles(Screens.Usuarios.allowedRoles) &&
                                        <Route path={'/usuarios'} element={<UsuariosScreen/>}/>
                                    }

                                    <Route path={'/funcionalidades'} element={<FuncionalidadesScreen/>}/>

                                    <Route path={'/valoraciones'} element={<ValoracionesScreen/>}/>

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
