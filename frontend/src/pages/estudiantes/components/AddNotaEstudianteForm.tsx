import { useForm, SubmitHandler } from "react-hook-form";
import { EstudianteCreateAdapter } from "../adapters/EstudianteCreateAdapter.ts";
import { useContext} from "react";
import { EstudianteContext } from "../EstudiantesScreen.tsx";
import MySpinner from "../../../components/MySpinner.tsx";
import {useApiEstudiante} from "../hooks/useApiEstudiante.ts";

export default function AddEstudianteForm() {
    const { register, handleSubmit } = useForm<EstudianteCreateAdapter>();
    const { editting, onEditTableItem, onAddTableItem, setEditting, setShowModal } = useContext(EstudianteContext);

    const {isLoading} = useApiEstudiante()

    const onSubmit: SubmitHandler<EstudianteCreateAdapter> = (data) => {
        if (editting)
            onEditTableItem!(data);
        else
            onAddTableItem!(data);
        setShowModal!(false)
    };

    return (
        <div className={` fixed  z-20 inset-0 bg-black bg-opacity-50 flex justify-center items-center`}>
            <div className="min-h-[30%] bg-white w-1/2  py-6 px-8 rounded-lg">
                <h2 className="text-2xl text-indigo-600 text-center font-bold group mb-4">{`${editting ? 'Editar Registro' : 'Añadir Registro'}`}</h2>
                <form onSubmit={handleSubmit(onSubmit)}>
                    <div className={'grid grid-cols-2 gap-y-1 gap-x-10'}>
                        <div className="group mb-4">
                            <label
                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Nombre</label>
                            <input
                                type="text"
                                {...register("name", {
                                    required: "true"
                                })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                                defaultValue={editting?.body.name}
                            />
                        </div>
                        <div className="group mb-4">
                            <label
                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Edad</label>
                            <input
                                type="number" {...register("age", {
                                required: true
                            })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                                defaultValue={editting?.body.age}
                            />
                        </div>
                        <div className="group mb-4">
                            <label
                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Correo</label>
                            <input
                                type="email" {...register("email", {
                                required: true
                            })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                                defaultValue={editting?.body.email}
                            />
                        </div>
                        <div className="group mb-4">
                            <label
                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Actividades
                                Extras</label>
                            <input
                                type="checkbox" {...register("extraActivities")}
                                className={"rounded-lg mx-4 p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}
                                defaultChecked={editting?.body.extraActivities}
                            />
                        </div>
                        <div className="group mb-4">
                            <label
                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Usuario</label>
                            <input
                                type="text" {...register("username", {
                                required: true
                            })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                                defaultValue={editting?.body.username}
                            />
                        </div>
                        <div className="group mb-4">
                            <label
                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Contraseña</label>
                            <input
                                type="password" {...register("password", {
                                required: true
                            })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                                defaultValue={editting?.body.password}
                            />
                        </div>
                    </div>

                    <div className="flex space-x-3 justify-center">
                        <button type="button" onClick={() => {
                            setShowModal!(false);
                            setEditting!(undefined);
                        }}
                                hidden={isLoading}
                                className="hover:bg-gray-400 transition-colors w-full py-2 bg-gray-300 rounded-lg text-gray-900">Cancelar
                        </button>
                        <button type="submit"
                                className={`${isLoading ? 'hover:bg-indigo-300 bg-indigo-300 cursor-default' : 'bg-indigo-500 hover:bg-indigo-600 '} transition-colors w-full flex justify-center py-2  text-indigo-50 rounded-lg`}>
                            {isLoading ? <MySpinner className={'h-6 w-6'}/> : null}
                            <p className={`${isLoading ? 'invisible' : 'visible'}`}>
                                {editting ? 'Editar' : 'Guardar'}
                            </p>
                        </button>
                    </div>
                </form>
            </div>
        </div>
    )
        ;
}