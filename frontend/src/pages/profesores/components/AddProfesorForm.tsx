import {useForm, SubmitHandler} from "react-hook-form"
import {ProfesorCreateAdapter} from "../adapters/ProfesorCreateAdapter.ts";
import {useContext, useEffect, useState} from "react";
import {ProfesorContext} from "../ProfesoresScreen.tsx";
import MySpinner from "../../../components/MySpinner.tsx";
import {useApiProfesor} from "../hooks/useApiProfesor.ts";
import {ISelect} from "../../../types/ISelect.ts";
import {useApiAsignatura} from "../../asignaturas/hooks/useApiAsignatura.ts";
import {AppContext} from "../../../App.tsx";
import SelectProfesor from "./SelectProfesor.tsx";

export default function AddProfesorForm() {
    const {register, handleSubmit} = useForm<ProfesorCreateAdapter>()
    const {editting, onEditTableItem, onAddTableItem, setShowModal, setEditting} = useContext(ProfesorContext)
    const {isLoading} = useApiProfesor()
    const {getAsignaturas} = useApiAsignatura()
    const {asignaturas} = useContext(AppContext)
    console.log(editting)
    useEffect(() => {
        getAsignaturas()
    }, []);
    const edittingAsignaturasArray: ISelect[] = editting?.body.asignaturas.map((item)=>{
        return {
            id: asignaturas!.find((i)=>i.name === item)!.id!,
            name: item
        }
    }) ?? []
    const [arraySelect, setArraySelect] = useState<ISelect[]>(edittingAsignaturasArray)
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
        if (editting)
            onEditTableItem!(data1)
        else
            onAddTableItem!(data1)

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
                                defaultValue={editting?.body?.name}

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
                                defaultValue={editting?.body.lastname}
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
                                defaultValue={editting?.body.username}
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

                                defaultValue={editting?.body.specialty}
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

                                defaultValue={editting?.body.contractType}
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

                                defaultValue={editting?.body.experience}
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

                                defaultValue={editting?.body.salary}
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

                                defaultValue={editting?.body.email}
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
                                            label={`Asignatura ${index+1}`}
                                            labelClassName={'text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold '}
                                            data={asignaturasSelect}
                                            selected={item}
                                            setSelected={(newItem)=>{setArraySelect((prev) =>
                                                prev.map((item, idx) =>
                                                    idx === index ? newItem : item
                                                )
                                            );}}
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
                            setEditting!(undefined)
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