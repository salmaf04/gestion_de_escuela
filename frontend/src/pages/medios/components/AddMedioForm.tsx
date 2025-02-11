// frontend/src/pages/medios/components/AddMedioForm.tsx
import { useForm, SubmitHandler } from "react-hook-form";
import { useContext, useEffect, useState } from "react";
import MySpinner from "../../../components/MySpinner.tsx";
import { MedioCreateAdapter } from "../adapters/MedioCreateAdapter.ts";
import { MedioContext } from "../MediosScreen.tsx";
import {ISelect} from "../../../types/ISelect.ts";
import {AulaGetAdapter} from "../../aulas/adapters/AulaGetAdapter.ts";
import {AppContext} from "../../../App.tsx";
import Select from "../../../components/Select.tsx";

export const stateType: { [key: string]: string } = {
    good: "Bien",
    regular: "Regular",
    bad: "Mal"
};

export const meanType: { [key: string]: string } = {
    technological_mean: "Medio Tecnológico",
    teaching_material: "Material de clases",
    other: "Otro"
};
export default function AddMedioForm() {
    const { register, handleSubmit, control } = useForm<MedioCreateAdapter>();
    const { editting, isEditting, isCreatting, onEditTableItem, onAddTableItem, setEditting, setShowModal } = useContext(MedioContext);
    const { aulas } = useContext(AppContext);
    const [isLoading, setIsLoading] = useState<boolean>(isEditting! || isCreatting!);

    useEffect(() => {
        setIsLoading(isEditting! || isCreatting!);
    }, [isEditting, isCreatting]);

    const onSubmit: SubmitHandler<MedioCreateAdapter> = (data) => {
        if (editting)
            onEditTableItem!(data);
        else
            onAddTableItem!(data);
        setShowModal!(false)
    };
    console.log(aulas)

    const aulasSelect: ISelect[] = aulas?.map((item: AulaGetAdapter)=>{
        return {
            id: item.id,
            name: item.number
        }
    }) ?? []

    const statusSelect: ISelect[] = [
        {id: 'good', name: 'Bien'},
        {id: 'regular', name: 'Regular'},
        {id: 'bad', name: 'Mal'}
    ]
    const typeSelect: ISelect[] = [
        {id: 'technological_mean', name: 'Medio Tecnológico'},
        {id: 'teaching_material', name: 'Material de clases'},
        {id: 'other', name: 'Otro'}
    ]


    return (
        <div className={`fixed z-20 inset-0 bg-black bg-opacity-50 flex justify-center items-center`}>
            <div className="min-h-[30%] bg-white w-1/2 py-6 px-8 rounded-lg">
                <h2 className="text-2xl text-indigo-600 text-center font-bold group mb-4">{`${editting ? 'Editar Registro' : 'Añadir Registro'}`}</h2>
                <form onSubmit={handleSubmit(onSubmit)}>
                    <div className={'grid grid-cols-2 gap-y-1 gap-x-10'}>
                        <div className="group mb-4">
                            <label className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold">Nombre</label>
                            <input
                                type="text"
                                {...register("name", { required: true })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                                defaultValue={editting?.name}
                            />
                        </div>
                        <div className={'w-full mb-4'}>
                            <Select
                                {...register(`state`, {
                                    required: true,
                                })}
                                label={'Estado'}
                                labelClassName={'text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold '}
                                data={statusSelect}
                                control={control}
                                defaultValue={editting && statusSelect!.find((item) => item.name === editting.state)!.id}
                            />
                        </div>
                        <div className="group mb-4">
                            <label
                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold">Ubicación</label>
                            <input
                                type="text"
                                {...register("location", {required: true})}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                                defaultValue={editting?.location}
                            />
                        </div>
                        <div className={'w-full mb-4'}>
                            <Select
                                {...register(`classroom_id`, {
                                    required: true,
                                })}
                                label={'Aula'}
                                labelClassName={'text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold '}
                                data={aulasSelect}
                                control={control}
                                defaultValue={editting && aulas!.find((item) => item.number === editting.classroom_name)?.id}
                            />
                        </div>
                        {!editting &&
                            <div className={'w-full mb-4'}>
                                <Select
                                    {...register(`type`, {
                                        required: true,
                                    })}
                                    label={'Tipo'}
                                    labelClassName={'text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold '}
                                    data={typeSelect}
                                    control={control}
                                />
                            </div>
                        }

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
                                className={`${isLoading ? 'hover:bg-indigo-300 bg-indigo-300 cursor-default' : 'bg-indigo-500 hover:bg-indigo-600 '} transition-colors w-full flex justify-center py-2 text-indigo-50 rounded-lg`}>
                            {isLoading ? <MySpinner className={'h-6 w-6'} /> : null}
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