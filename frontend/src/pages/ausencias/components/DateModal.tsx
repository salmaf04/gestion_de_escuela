import {useContext, useState} from "react";
import {AppContext} from "../../../App.tsx";
import {AusenciasContext} from "../AusenciasScreen.tsx";
import MySpinner from "../../../components/MySpinner.tsx";
import {useApiAusencias} from "../hooks/useApiAusencias.ts";
import {useFieldArray, useForm} from "react-hook-form";
import {Simulate} from "react-dom/test-utils";
import RemoveIcon from '../../../assets/remove.svg'
import {AusenciaAdapter} from "../adapters/AusenciaAdapter.ts";
import {RolesEnum} from "../../../api/RolesEnum.ts";
import Table from "../../../components/Table.tsx";
import EditAusencia from "./EditAusencia.tsx";

export default function DateModal() {
    const {ausencias} = useContext(AppContext)
    const {editting, setEditting} = useContext(AusenciasContext)
    const {updateAusencia, isLoading, deleteAusencia} = useApiAusencias()
    const dataTable = editting?.dates?.map((date) => {
        return {
            id: date.absence_id,
            date: date.date
        }
    })
    console.log(editting)
    const [showEditModal, setShowEditModal] = useState<string | undefined>()
    return (
        <div className={` fixed  z-20 inset-0 bg-black bg-opacity-50 flex justify-center items-center`}
        >
            <div className="min-h-[30%] bg-white w-1/3 flex-col flex py-6 px-8 rounded-lg">
                <h2 className="text-2xl text-indigo-600 text-center font-bold group mb-6">Fechas</h2>

                <Table
                    className={'h-full'}
                    isLoading={false}
                    Data={dataTable ?? []}
                    header={['Fecha']}
                    onRemoveRow={(index) => {
                        deleteAusencia(index)
                    }}
                    onEditRow={(index) => {
                        setShowEditModal(index)
                    }}
                    isRemoveActive={true}
                />
                <div className="flex space-x-3 justify-center mt-10">
                    <button type="button" onClick={() => {
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
            </div>
            {showEditModal &&
                <EditAusencia
                    setShowModal={setShowEditModal}
                    asignaturaId={editting!.subject.id}
                    estudianteId={editting!.student.id}
                    ausenciaId={showEditModal}
                />
            }

        </div>
    )
}
