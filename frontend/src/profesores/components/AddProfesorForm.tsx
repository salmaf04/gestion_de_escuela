import LoadingIcon from "../../assets/loading.svg"
import {useForm, SubmitHandler} from "react-hook-form"
import {ProfesorCreateAdapter} from "../adapters/ProfesorCreateAdapter.ts";
import {useCreateProfesor} from "../hooks/useCreateProfesor.ts";
import {useContext, useEffect, useState} from "react";
import {ProfesorContext} from "../ProfesoresScreen.tsx";
import {useEditProfesor} from "../hooks/useEditProfesor.ts";
import {AppContext} from "../../App.tsx";

export default function AddProfesorForm() {
    const {register, handleSubmit} = useForm<ProfesorCreateAdapter>()
    const {editting, setShowModal} = useContext(ProfesorContext)
    const {setError} = useContext(AppContext)
    const {
        editedProfesor,
        isLoading: isEditting,
        editProfesor
    } = useEditProfesor()
    const {
        newProfesor,
        isLoading: isCreatting,
        createProfesor
    } = useCreateProfesor()

    const [isLoading, setIsLoading] = useState<boolean>(isEditting || isCreatting)

    useEffect(() => {
        setIsLoading(isEditting || isCreatting)
    }, [isEditting, isCreatting]);

    const onSubmit: SubmitHandler<ProfesorCreateAdapter> = (data) => {
        if (editting)
            editProfesor(data, setError!)
        else
            createProfesor(data, setError!)
    }
    return (
        <div className={` fixed  z-20 inset-0 bg-black bg-opacity-50 flex justify-center items-center`}>
            <div className="min-h-[30%] bg-white w-1/2  py-6 px-8 rounded-lg">
                <h2 className="text-2xl text-indigo-600 text-center font-bold group mb-4">{`${editting ? 'Editar Registro' : 'Anadir Registro'}`}</h2>
                <form onSubmit={handleSubmit(onSubmit)}>
                    <div className={'grid grid-cols-2 gap-y-1 gap-x-10'}>
                        <div className="group mb-4">
                            <label className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Nombre</label>
                            <input
                                type="text"
                                {...register("name", {
                                    required: "true"
                                })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                                defaultValue={editting?.name}

                            />
                        </div>
                        <div className="group mb-4">
                            <label className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Apellidos</label>
                            <input
                                type="text" {...register("lastname", {
                                required: true
                            })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                                defaultValue={editting?.lastname}
                            />
                        </div>
                        <div className="group group mb-4">
                            <label className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Usuario</label>
                            <input
                                type="text" {...register("username", {
                                required: true
                            })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                                defaultValue={editting?.username}
                                placeholder={"Usuario"}
                            />
                        </div>
                        <div className="group mb-4">
                            <label className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Especialidad</label>
                            <input
                                type="text" {...register("specialty", {
                                required: true
                            })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}

                                defaultValue={editting?.specialty}
                            />
                        </div>
                        <div className="group mb-4">
                            <label className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Contrato</label>
                            <input
                                type="text" {...register("contractType", {
                                required: true
                            })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}

                                defaultValue={editting?.contractType}
                            />
                        </div>
                        <div className="group mb-4">
                            <label className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Experiencia</label>
                            <input
                                type="number" {...register("experience", {
                                required: true
                            })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}

                                defaultValue={editting?.experience}
                            />
                        </div>
                        <div className="group mb-4">
                            <label className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Correo</label>
                            <input
                                type="text" {...register("email", {
                                required: true
                            })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}

                                defaultValue={editting?.email}
                            />
                        </div>
                    </div>

                    <div className="flex space-x-3 justify-center">
                        <button type="button" onClick={() => {
                            setShowModal!(false)
                        }}
                                hidden={isLoading}
                                className="hover:bg-gray-400 transition-colors w-full py-2 bg-gray-300 rounded-lg text-gray-900">Cancelar
                        </button>
                        <button type="submit"
                                className={`${isLoading ? 'hover:bg-indigo-300 bg-indigo-300 cursor-default' : 'bg-indigo-500'} transition-colors w-full hover:bg-indigo-600 flex justify-center py-2  text-indigo-50 rounded-lg`}>
                            {isLoading ?
                                <img src={LoadingIcon} alt="loading" className="absolute w-6 h-6 animate-spin"/> : null}
                            <p className={`${isLoading ? 'invisible' : 'visible'}`}>
                                {editting ? 'Editar' : 'Guardar'}
                            </p>
                        </button>
                    </div>
                </form>
            </div>

        </div>
    );
}