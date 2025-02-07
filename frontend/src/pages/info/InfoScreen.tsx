// frontend/src/pages/medios/CursosScreen.tsx
import {AppContext} from "../../App.tsx";
import {useContext} from "react";
import {RolesEnum} from "../../api/RolesEnum.ts";
import ProfesorInfo from "./components/ProfesorInfo.tsx";
import EstudianteInfo from "./components/EstudianteInfo.tsx";
import SecretariaInfo from "./components/SecretariaInfo.tsx";
import AdministradorInfo from "./components/AdministradorInfo.tsx";
import {rolesDisplayParser} from "../../utils/utils.ts";

export default function InfoScreen() {
    const {roles, setToken, username} = useContext(AppContext)
    const displayRoles = roles?.map((item) => rolesDisplayParser[item]).join(', ')

    return (
        <div className={'w-full h-dvh flex flex-col py-10 px-20'}>
            <div className={'flex space-x-4 w-full justify-between'}>
                <div className={'flex flex-col'}>
                    <h1 className={'text-3xl text-indigo-600 accent-i font-bold'}>
                        Bienvenido/a
                    </h1>
                    <p className={'text-slate-800 text-sm italic'}>
                        {`${username}: ${displayRoles}`}
                    </p>

                </div>
                <button className={'bg-gray-50 size-fit py-2 px-5 shadow rounded-md font-semibold text-gray-900 hover:bg-gray-200 transition-colors'}
                        onClick={() => {
                            setToken!("")
                            sessionStorage.removeItem('token')
                        }}
                >
                    Cerrar Sesión
                </button>
            </div>
            <div className={'h-full flex items-center ps-20'}>
                {roles?.some((item) => item === RolesEnum.TEACHER) &&
                    <ProfesorInfo/>
                }
                {roles?.some((item) => item === RolesEnum.STUDENT) &&
                    <EstudianteInfo/>
                }
                {roles?.some((item) => item === RolesEnum.SECRETARY) &&
                    <SecretariaInfo/>
                }
                {roles?.some((item) => item === RolesEnum.ADMIN) &&
                    <AdministradorInfo/>
                }
            </div>
        </div>
    );
}