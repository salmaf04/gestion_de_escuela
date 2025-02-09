// frontend/src/pages/ausencias/components/AddAusenciaForm.tsx
import {useContext} from "react";
import {AusenciasContext} from "../AusenciasScreen.tsx";
import {useForm} from "react-hook-form";
import {reverseDate} from "../../../utils/utils.ts";
import {IAusenciaCreateDB} from "../models/IAusenciaCreateDB.ts";

interface Props {
    setShowModal: (value: string | undefined) => void,
    estudianteId: string,
    asignaturaId: string,
    ausenciaId: string
}

export default function EditAusencia({setShowModal, estudianteId, asignaturaId, ausenciaId}: Props) {
    const {onEditTableItem, setEditting} = useContext(AusenciasContext);
    const {register, control, handleSubmit} = useForm()

    const onSubmit = (data) => {
        const dataParse: IAusenciaCreateDB = {
            student_id: asignaturaId,
            subject_id: estudianteId,
            date: data[`date`],
        }
        console.log(dataParse)
        console.log(asignaturaId)
        onEditTableItem!(dataParse, ausenciaId)
        setShowModal!(undefined)
    }

    return (
        <div className={` fixed  z-20 inset-0 bg-black bg-opacity-50 flex justify-center items-center`}
        >
            <div className="min-h-[30%] bg-white w-1/2  py-6 px-8 rounded-lg">
                <h2 className="text-2xl text-indigo-600 text-center font-bold group mb-6">Editar Registro</h2>
                <form onSubmit={handleSubmit(onSubmit)}>
                    <div className="group w-full">
                        <label
                            className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Fecha</label>
                        <input
                            type="date" {...register(`date`, {
                            required: true
                        })}
                            className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}

                        />

                    </div>

                    <div className="flex space-x-3 justify-center mt-10">
                        <button type="button" onClick={() => {
                            setShowModal!(undefined);
                        }}
                                className="hover:bg-gray-400 transition-colors w-full py-2 bg-gray-300 rounded-lg text-gray-900">Cancelar
                        </button>
                        <button type="submit"
                                className={`bg-indigo-500 hover:bg-indigo-600 transition-colors w-full flex justify-center py-2  text-indigo-50 rounded-lg`}>
                            <p>
                                Editar
                            </p>
                        </button>
                    </div>
                </form>
            </div>

        </div>
    )
        ;
}