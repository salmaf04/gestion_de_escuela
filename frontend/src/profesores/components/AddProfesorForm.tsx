import {useState} from "react";
import LoadingIcon from "../../assets/loading.svg"
import {ProfesorCreateAdapter} from "../adapters/ProfesorCreateAdapter.ts";
import {ProfesorGetAdapter} from "../adapters/ProfesorGetAdapter.ts";

interface Props {
    onCancel: () => void
    onAccept: (formData: ProfesorGetAdapter) => void
    formDataEdit?: ProfesorGetAdapter
    isLoading: boolean
    className?: string
}

export default function AddProfesorForm({onCancel, onAccept, formDataEdit, isLoading, className}: Props) {
    const [formData, setFormData] = useState<ProfesorCreateAdapter>(formDataEdit || new ProfesorCreateAdapter({
        name: '',
        fullname: '',
        username: '',
        email: '',
        contract_type: '',
        experience: 0,
        specialty: '',
        list_of_subjects: []
    }));

    return (
        <div className={`fixed z-20 inset-0 bg-black bg-opacity-50 flex justify-center items-center ${className}`}>
            <div className="bg-white w-1/2  p-6 rounded-lg">
                <h2 className="text-xl   text-indigo-400 text-center font-bold mb-4">{`${formDataEdit ? 'Editar Registro' : 'Anadir Registro'}`}</h2>
                <form className={'justify-around flex flex-row  '}>
                    <div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Nombre</label>
                            <input type="text" name="nombre" value={formData.name} onChange={(e) => {
                                setFormData(
                                    {
                                        ...formData,
                                        name: e.target.value
                                    }
                                )
                            }}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Apellidos</label>
                            <input type="text" name="apellidos" value={formData.lastname} onChange={(e) => {
                                setFormData(
                                    {
                                        ...formData,
                                        lastname: e.target.value
                                    }
                                )
                            }}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Usuario</label>
                            <input type="text" name="usuario" value={formData.username} onChange={(e) => {
                                setFormData(
                                    {
                                        ...formData,
                                        username: e.target.value
                                    }
                                )
                            }}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Especialidad</label>
                            <input type="text" name="especialidad" value={formData.specialty} onChange={(e) => {
                                setFormData(
                                    {
                                        ...formData,
                                        specialty: e.target.value
                                    }
                                )
                            }}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>

                    </div>
                    <div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Contrato</label>
                            <input type="text" name="contrato" value={formData.contractType} onChange={(e) => {
                                setFormData(
                                    {
                                        ...formData,
                                        contractType: e.target.value
                                    }
                                )
                            }}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Experiencia</label>
                            <input type="number" name="experiencia" value={formData.experience} onChange={(e) => {
                                setFormData(
                                    {
                                        ...formData,
                                        experience: parseInt(e.target.value.toString())
                                    }
                                )
                            }}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Correo</label>
                            <input type="text" name="correo" value={formData.email} onChange={(e) => {
                                setFormData(
                                    {
                                        ...formData,
                                        email: e.target.value,
                                    }
                                )
                            }}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                    </div>
                </form>
                <div className="flex justify-end">
                    <button type="button" onClick={onCancel}
                            hidden={isLoading}
                            className="mr-4 px-4 py-2 bg-gray-300 rounded">Cancelar
                    </button>
                    <button onClick={() => {
                        onAccept(formData)
                    }} type="submit"
                            className={`${isLoading ? ' bg-indigo-300 cursor-default' : 'bg-indigo-500'} px-4 flex justify-center py-2  text-white rounded`}>
                        {isLoading ?
                            <img src={LoadingIcon} alt="loading" className="absolute w-6 h-6 animate-spin"/> : null}
                        <p className={`${isLoading? 'invisible': 'visible'}`}>
                            {formDataEdit ? 'Editar' : 'Guardar'}
                        </p>
                    </button>
                </div>
            </div>
        </div>
    );
}