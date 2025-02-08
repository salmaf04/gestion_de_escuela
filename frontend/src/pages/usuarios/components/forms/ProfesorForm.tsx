import SelectProfesor from "../../../profesores/components/SelectProfesor.tsx";
import MySpinner from "../../../../components/MySpinner.tsx";
import {ProfesorCreateAdapter} from "../../../profesores/adapters/ProfesorCreateAdapter.ts";
import {SubmitHandler, useForm} from "react-hook-form";
import {ISelect} from "../../../../types/ISelect.ts";
import {useContext, useEffect, useState} from "react";
import {AppContext} from "../../../../App.tsx";
import {useApiAsignatura} from "../../../asignaturas/hooks/useApiAsignatura.ts";
import {useApiProfesor} from "../../../profesores/hooks/useApiProfesor.ts";
import {UsuariosContext} from "../../UsuariosScreen.tsx";

export default function ProfesorForm(){
    const {register, handleSubmit} = useForm<ProfesorCreateAdapter>()
    const {setShowModal} = useContext(UsuariosContext)
    const {isLoading} = useApiProfesor()
    const {getAsignaturas} = useApiAsignatura()
    const {asignaturas} = useContext(AppContext)
    const {
        createProfesor,
    } = useApiProfesor()
    useEffect(() => {
        getAsignaturas()
    }, []);
    const [arraySelect, setArraySelect] = useState<ISelect[]>([])
    const asignaturasSelect: ISelect[] = asignaturas?.map((item)=>{
        return {
            id: item.id,
            name: item?.name
        }
    }) ?? []

    const onSubmit: SubmitHandler<ProfesorCreateAdapter> = (data) => {
        const data1 = {
            ...data,
            asignaturas: arraySelect.map((i)=>i.name)
        }
        createProfesor!(data1)

        setShowModal!(false)
    }

    return (
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

                    />

                </div>

                {
                    arraySelect.map((item, index) => {
                        return (
                            <div className="group relative" key={index}>
                                <SelectProfesor
                                    {...register(`asignaturas.${index}`, {
                                        value: arraySelect[index]?.name
                                    })}
                                    label={`Asignatura ${index + 1}`}
                                    labelClassName={'text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold '}
                                    data={asignaturasSelect}
                                    selected={item}
                                    setSelected={(newItem) => {
                                        setArraySelect((prev) =>
                                            prev.map((item, idx) =>
                                                idx === index ? newItem : item
                                            )
                                        );
                                    }}
                                />

                            </div>
                        )
                    })
                }
                <button
                    type={'button'}
                    className={'self-center w-full translate-y-3 py-2 h-10 text-center text-indigo-500 rounded-lg border-2 border-indigo-500 text-sm font-semibold hover:bg-indigo-50 transition-colors'}
                    onClick={() => {
                        setArraySelect((prev) => [...prev, asignaturasSelect[0]])
                    }}
                >
                    Insertar asignatura
                </button>
            </div>

            <div className="flex space-x-3 justify-center mt-10">
                <button type="button" onClick={() => {
                    setShowModal!(false);
                }}
                        hidden={isLoading}
                        className="hover:bg-gray-400 transition-colors w-full py-2 bg-gray-300 rounded-lg text-gray-900">Cancelar
                </button>
                <button type="submit"
                        className={`${isLoading ? 'hover:bg-indigo-300 bg-indigo-300 cursor-default' : 'bg-indigo-500 hover:bg-indigo-600 '} transition-colors w-full flex justify-center py-2  text-indigo-50 rounded-lg`}>
                    {isLoading ? <MySpinner className={'h-6 w-6'}/> : null}
                    <p className={`${isLoading ? 'invisible' : 'visible'}`}>
                        Guardar
                    </p>
                </button>
            </div>
        </form>
    )
}