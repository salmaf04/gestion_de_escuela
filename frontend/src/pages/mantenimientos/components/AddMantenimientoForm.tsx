import {useForm, SubmitHandler} from "react-hook-form"
import {useContext, useEffect, useState} from "react";
import MySpinner from "../../../components/MySpinner.tsx";
import {MantenimientoContext} from "../MantenimientosScreen.tsx";
import Select from "../../../components/Select.tsx";
import {MedioGetAdapter} from "../../medios/adapters/MedioGetAdapter.ts";
import {ISelect} from "../../../types/ISelect.ts";
import {AppContext} from "../../../App.tsx";
import {IMantenimientoDB} from "../models/IMantenimientoDB.ts";

export default function AddMantenimientoForm() {
    const {register, handleSubmit, control} = useForm<Partial<IMantenimientoDB>>()
    const {editting, isEditting, isCreatting, onEditTableItem, onAddTableItem, setEditting, setShowModal} = useContext(MantenimientoContext)
    const {medios} = useContext(AppContext)
    const [isLoading, setIsLoading] = useState<boolean>(isEditting! || isCreatting!)

    useEffect(() => {
        setIsLoading(isEditting! || isCreatting!)
    }, [isEditting, isCreatting]);
    const reverseDate = (date?: string) => {
        if (date){
            const [day, month, year] = date.split('-');
            return `${year}-${month}-${day}`;
        }
        return ""
    }

    const onSubmit: SubmitHandler<IMantenimientoDB> = (data) => {
        if (data.date) {
            const [day, month, year] = data.date.split('-');
            data.date = `${year}-${month}-${day}`;
        }
        if (editting)
            onEditTableItem!(data)
        else
            onAddTableItem!(data)
        setShowModal!(false);
        setEditting!(undefined);
    }

    const mediosSelect: ISelect[] = medios?.map((item: MedioGetAdapter) => {
        return {
            id: item.id,
            name: item.name
        }
    }) ?? []
    return (
        <div className={` fixed  z-20 inset-0 bg-black bg-opacity-50 flex justify-center items-center`}
        >
            <div className="min-h-[30%] bg-white w-1/2  py-6 px-8 rounded-lg">
                <h2 className="text-2xl text-indigo-600 text-center font-bold group mb-4">{`${editting ? 'Editar Registro' : 'Añadir Registro'}`}</h2>
                <form onSubmit={handleSubmit(onSubmit)}>
                    <div className={'grid grid-cols-2 gap-y-1 gap-x-10'}>
                        {!editting &&
                            <>
                                <div className={'w-full mb-4'}>
                                    <Select
                                        {...register(`mean_id`, {
                                            required: true,
                                        })}
                                        label={'Mantenimiento'}
                                        labelClassName={'text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold '}
                                        data={mediosSelect}
                                        control={control}
                                    />
                                </div>
                                <div className="group mb-4">
                                    <label
                                        className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Fecha</label>
                                    <input
                                        type="date"
                                        {...register("date", {
                                            required: "true"
                                        })}
                                        className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                                    />
                                </div>
                            </>


                        }


                        <div className="group mb-4">
                            <label
                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Costo</label>
                            <input
                                type="number" {...register("cost", {
                                required: true
                            })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}

                                defaultValue={editting?.cost}
                            />
                        </div>
                        <div className="group mb-4">
                            <label
                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Finalizado</label>
                            <input
                                type="checkbox" {...register("finished",{

                            })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}

                                defaultChecked={editting?.finished ?? false}
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
    );
}