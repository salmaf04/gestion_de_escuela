import {useState} from "react";
import {rolesDisplayParser} from "../../../utils/utils.ts";
import {RolesEnum} from "../../../api/RolesEnum.ts";
import ProfesorForm from "./forms/ProfesorForm.tsx";
import SecretariaForm from "./forms/SecretariaForm.tsx";
import EstudianteForm from "./forms/EstudianteForm.tsx";
import DecanoForm from "./forms/DecanoForm.tsx";
import AdminForm from "./forms/AdminForm.tsx";

export default function AddAulaForm() {
    const [userType, setUserType] = useState(rolesDisplayParser[RolesEnum.SECRETARY])

    return (
        <div className={`fixed z-20 inset-0 bg-black bg-opacity-50 flex justify-center items-center`}>
            <div className="min-h-[30%] bg-white w-1/2 py-6 px-8 rounded-lg space-y-3">
                <h2 className="text-2xl text-indigo-600 text-center font-bold group mb-4">Añadir Registro</h2>
                <div className={'flex w-full justify-around space-x-4'}>
                    <button className={`rounded-md font-semibold  w-full py-1 ${userType === rolesDisplayParser[RolesEnum.SECRETARY] ? 'bg-indigo-600 text-indigo-50 border-none' : 'hover:bg-indigo-100 border-2 border-indigo-400 bg-indigo-50 text-indigo-500'}`}
                            onClick={() => setUserType(rolesDisplayParser[RolesEnum.SECRETARY])}
                    >
                        {rolesDisplayParser[RolesEnum.SECRETARY]}
                    </button>
                    <button
                        className={`rounded-md font-semibold  w-full py-1  ${userType === rolesDisplayParser[RolesEnum.TEACHER] ? 'bg-indigo-600 text-indigo-50 border-none' : 'hover:bg-indigo-100 border-2 border-indigo-400 bg-indigo-50 text-indigo-500'}`}
                        onClick={() => setUserType(rolesDisplayParser[RolesEnum.TEACHER])}
                    >
                        {rolesDisplayParser[RolesEnum.TEACHER]}
                    </button>
                    <button
                        className={`rounded-md font-semibold  w-full py-1 ${userType === rolesDisplayParser[RolesEnum.STUDENT] ? 'bg-indigo-600 text-indigo-50 border-none' : 'hover:bg-indigo-100 border-2 border-indigo-400 bg-indigo-50 text-indigo-500'}`}
                        onClick={() => setUserType(rolesDisplayParser[RolesEnum.STUDENT])}
                    >
                        {rolesDisplayParser[RolesEnum.STUDENT]}
                    </button>
                    <button
                        className={`rounded-md font-semibold  w-full py-1 ${userType === rolesDisplayParser[RolesEnum.DEAN] ? 'bg-indigo-600 text-indigo-50 border-none' : 'hover:bg-indigo-100 border-2 border-indigo-400 bg-indigo-50 text-indigo-500'}`}
                        onClick={() => setUserType(rolesDisplayParser[RolesEnum.DEAN])}
                    >
                        {rolesDisplayParser[RolesEnum.DEAN]}
                    </button>
                    <button
                        className={`rounded-md font-semibold  w-full py-1 ${userType === rolesDisplayParser[RolesEnum.ADMIN] ? 'bg-indigo-600 text-indigo-50 border-none' : 'hover:bg-indigo-100 border-2 border-indigo-400 bg-indigo-50 text-indigo-500'}`}
                        onClick={() => setUserType(rolesDisplayParser[RolesEnum.ADMIN])}
                    >
                        {rolesDisplayParser[RolesEnum.ADMIN]}
                    </button>
                </div>
                {userType === rolesDisplayParser[RolesEnum.SECRETARY] &&
                    <SecretariaForm />
                }
                {userType === rolesDisplayParser[RolesEnum.TEACHER] &&
                    <ProfesorForm />
                }
                {userType === rolesDisplayParser[RolesEnum.STUDENT] &&
                    <EstudianteForm />
                }
                {userType === rolesDisplayParser[RolesEnum.DEAN] &&
                    <DecanoForm />
                }
                {userType === rolesDisplayParser[RolesEnum.ADMIN] &&
                    <AdminForm />
                }
            </div>
        </div>
    );
}