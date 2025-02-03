// frontend/src/pages/medios/CursosScreen.tsx
import {AppContext} from "../../App.tsx";
import {useContext} from "react";
import {RolesEnum} from "../../api/RolesEnum.ts";
import ProfesorInfo from "./components/ProfesorInfo.tsx";
import EstudianteInfo from "./components/EstudianteInfo.tsx";
import SecretariaInfo from "./components/SecretariaInfo.tsx";
import AdministradorInfo from "./components/AdministradorInfo.tsx";

export default function InfoScreen() {
    const {roles} = useContext(AppContext)

    return (
        <div className={'w-full h-dvh flex flex-col py-10 px-20'}>
            <h1 className={'text-2xl text-indigo-900 font-bold'}>
                Mi Información:
            </h1>
            {roles?.some((item) => item === RolesEnum.TEACHER) &&
                <ProfesorInfo/>
            }
            {roles?.some((item) => item === RolesEnum.STUDENT)&&
                <EstudianteInfo />
            }
            {roles?.some((item) => item === RolesEnum.SECRETARY) &&
                <SecretariaInfo />
            }
            {roles?.some((item) => item === RolesEnum.ADMIN) &&
                <AdministradorInfo />
            }

        </div>
    );
}