import {useForm, SubmitHandler} from "react-hook-form"
import {ProfesorCreateAdapter} from "../adapters/ProfesorCreateAdapter.ts";
import {useContext, useState} from "react";
import {ProfesorContext} from "../ProfesoresScreen.tsx";
import MySpinner from "../../../components/MySpinner.tsx";
import {useApiProfesor} from "../hooks/useApiProfesor.ts";
import Select from "../../../components/Select.tsx";
import {ISelect} from "../../../types/ISelect.ts";

export default function AddProfesorForm() {
    const {register, handleSubmit} = useForm<ProfesorCreateAdapter>()
    const {editting, onEditTableItem, onAddTableItem, setEditting, setShowModal} = useContext(ProfesorContext)
    const {isLoading} = useApiProfesor()
    const [asignaturas, setAsignaturas] = useState(editting ? editting.asignaturas ?? [] : [])
    const data = [
        { id: 1, name: 'Wade Cooper' },
        { id: 2, name: 'Arlene Mccoy' },
        { id: 3, name: 'Devon Webb' },
        { id: 4, name: 'Tom Cook' },
        { id: 5, name: 'Tanya Fox' },
        { id: 6, name: 'Hellen Schmidt' },
        { id: 7, name: 'Caroline Schultz' },
        { id: 8, name: 'Mason Heaney' },
        { id: 9, name: 'Claudie Smitham' },
        { id: 10, name: 'Emil Schaefer' },
    ]
    const [selected, setSelected] = useState<ISelect>(data[0])


    const onSubmit: SubmitHandler<ProfesorCreateAdapter> = (data) => {
        console.log(data.asignaturas)
        if (editting)
            onEditTableItem!(data)
        else
            onAddTableItem!(data)

        setEditting!(undefined)
        setShowModal!(false)
    }
    return (
        <div className={` fixed  z-20 inset-0 bg-black bg-opacity-50 flex justify-center items-center`}
        >
            <div className="min-h-[30%] bg-white w-1/2  py-6 px-8 rounded-lg">
                <h2 className="text-2xl text-indigo-600 text-center font-bold group mb-6">{`${editting ? 'Editar Registro' : 'Añadir Registro'}`}</h2>
                <form onSubmit={handleSubmit(onSubmit)}>
                    <div className={'grid grid-cols-2 gap-y-5 gap-x-10'}>
                        <div className="group ">
                            <label
                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Nombre</label>
                            <input
                                type="text"
                                {...register("name", {
                                    required: "true"
                                })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                                defaultValue={editting?.name}

                            />
                        </div>
                        <div className="group ">
                            <label
                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Apellidos</label>
                            <input
                                type="text" {...register("lastname", {
                                required: true
                            })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                                defaultValue={editting?.lastname}
                            />
                        </div>
                        <div className="group group ">
                            <label
                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Usuario</label>
                            <input
                                type="text" {...register("username", {
                                required: true
                            })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                                defaultValue={editting?.username}
                            />
                        </div>
                        <div className="group ">
                            <label
                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Especialidad</label>
                            <input
                                type="text" {...register("specialty", {
                                required: true
                            })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}

                                defaultValue={editting?.specialty}
                            />
                        </div>
                        <div className="group ">
                            <label
                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Contrato</label>
                            <input
                                type="text" {...register("contractType", {
                                required: true
                            })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}

                                defaultValue={editting?.contractType}
                            />
                        </div>
                        <div className="group ">
                            <label
                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Experiencia</label>
                            <input
                                type="number" {...register("experience", {
                                required: true
                            })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}

                                defaultValue={editting?.experience}
                            />
                        </div>
                        <div className="group ">
                            <label
                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Salario</label>
                            <input
                                type="number" {...register("salary", {
                                required: true
                            })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}

                                defaultValue={editting?.salary}
                            />
                        </div>
                        <div className="group ">
                            <label
                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Correo</label>
                            <input
                                type="text" {...register("email", {
                                required: true
                            })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}

                                defaultValue={editting?.email}
                            />

                        </div>

                        {
                            asignaturas.map((_, index) => {
                                return (
                                    <div className="group relative" key={index}>
                                        <Select
                                            {...register(`asignaturas.${index}`, {
                                                value: selected.name
                                            })}
                                            label={`Asignatura ${index+1}`}
                                            labelClassName={'text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold '}
                                            data={data}
                                            selected={selected}
                                            setSelected={setSelected}
                                        />

                                    </div>
                                )
                            })
                        }
                        <button
                            type={'button'}
                            className={'self-center w-full translate-y-3 py-2 h-10 text-center text-indigo-500 rounded-lg border-2 border-indigo-500 text-sm font-semibold hover:bg-indigo-50 transition-colors'}
                            onClick={() => {
                                setAsignaturas((prev) => [...prev, ""])
                            }}
                        >
                            Insertar asignatura
                        </button>
                    </div>

                    <div className="flex space-x-3 justify-center mt-10">
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
    );
}