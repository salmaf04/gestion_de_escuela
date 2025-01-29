// frontend/src/pages/medios/CursosScreen.tsx
import {AppContext} from "../../App.tsx";
import {useContext} from "react";
import {RolesEnum} from "../../api/RolesEnum.ts";
import ProfesorInfo from "./components/ProfesorInfo.tsx";

export default function InfoScreen() {
    const {role} = useContext(AppContext)

    return (
        <div className={'w-full h-dvh flex flex-col py-10 px-20'}>
            <h1 className={'text-2xl text-indigo-900 font-bold'}>
                Mi Información:
            </h1>
            {role === RolesEnum.TEACHER &&
                <ProfesorInfo/>
            }
        </div>
    );
}