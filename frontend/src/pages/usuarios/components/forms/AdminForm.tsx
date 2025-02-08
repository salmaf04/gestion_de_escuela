import MySpinner from "../../../../components/MySpinner.tsx";
import {SubmitHandler, useForm} from "react-hook-form";
import {IAdministradorCreateDB} from "../../../info/models/IAdministradorCreateDB.ts";
import {useContext} from "react";
import {UsuariosContext} from "../../UsuariosScreen.tsx";
import {useApiAdministrador} from "../../../info/hooks/useApiAdministrador.ts";
import {useApiUsuarios} from "../../hooks/useApiUsuarios.ts";

export default function AdminForm(){

    const { register, handleSubmit } = useForm<IAdministradorCreateDB>();
    const { setShowModal } = useContext(UsuariosContext);
    const {createAdministrador} = useApiAdministrador()
    const {getUsuarios} = useApiUsuarios()
    const isLoading = false;

    const onSubmit: SubmitHandler<IAdministradorCreateDB> = (data) => {
        createAdministrador(data)
        setShowModal!(false)
        getUsuarios()
    };
    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <div className={'grid grid-cols-2 gap-y-1 gap-x-10'}>
                <div className="group mb-4">
                    <label
                        className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold">Nombre</label>
                    <input
                        type="text"
                        {...register("name", {required: true})}
                        className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                    />
                </div>
                <div className="group mb-4">
                    <label
                        className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold">Apellidos</label>
                    <input
                        type="text"
                        {...register("lastname", {required: true})}
                        className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                    />
                </div>
                <div className="group mb-4">
                    <label
                        className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold">Usuario</label>
                    <input
                        type="text"
                        {...register("username", {required: true})}
                        className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                    />
                </div>
                <div className="group mb-4">
                    <label
                        className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold">Correo</label>
                    <input
                        type="text"
                        {...register("email", {required: true})}
                        className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                    />
                </div>
            </div>

            <div className="flex space-x-3 justify-center mt-10">
                <button type="button" onClick={() => {
                    setShowModal!(false);
                }}
                        hidden={isLoading}
                        className="hover:bg-gray-400 transition-colors w-full py-2 bg-gray-300 rounded-lg text-gray-900">Cancelar
                </button>
                <button type="submit"
                        className={`${isLoading ? 'hover:bg-indigo-300 bg-indigo-300 cursor-default' : 'bg-indigo-500 hover:bg-indigo-600 '} transition-colors w-full flex justify-center py-2 text-indigo-50 rounded-lg`}>
                    {isLoading ? <MySpinner className={'h-6 w-6'}/> : null}
                    <p className={`${isLoading ? 'invisible' : 'visible'}`}>
                        Guardar
                    </p>
                </button>
            </div>
        </form>
    )
}