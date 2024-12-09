import {useState} from "react";
import  {Profesor} from "../../types.ts";

interface Props {
    onCancel: () => void
    onAccept: (formData: Profesor) => void
    formDataEdit?: Profesor
}

export default function AddProfesorForm({onCancel, onAccept, formDataEdit}: Props) {
    const [formData, setFormData] = useState(formDataEdit || {
        Id: '',
        Nombre: '',
        Apellidos: '',
        Contrato: '',
        Asignaturas: '',
        Valoracion: '',
        Especialidad: '',
        Experiencia: ''
    });
    return (
        <div className="fixed z-40 inset-0 bg-black bg-opacity-50 flex justify-center items-center">
            <div className="bg-white w-1/2  p-6 rounded-lg">
                <h2 className="text-xl   text-indigo-400 text-center font-bold mb-4">{`${formDataEdit ? 'Editar Registro' : 'Anadir Registro'}`}</h2>
                <form className={'justify-around flex flex-row  '}>
                    <div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Nombre</label>
                            <input type="text" name="nombre" value={formData.Nombre} onChange={(e) => {
                                setFormData(
                                    {
                                        ...formData,
                                        Nombre: e.target.value
                                    }
                                )
                            }}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Apellidos</label>
                            <input type="text" name="apellidos" value={formData.Apellidos} onChange={(e) => {
                                setFormData(
                                    {
                                        ...formData,
                                        Apellidos: e.target.value
                                    }
                                )
                            }}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Especialidad</label>
                            <input type="text" name="especialidad" value={formData.Especialidad} onChange={(e) => {
                                setFormData(
                                    {
                                        ...formData,
                                        Especialidad: e.target.value
                                    }
                                )
                            }}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Contrato</label>
                            <input type="text" name="contrato" value={formData.Contrato} onChange={(e) => {
                                setFormData(
                                    {
                                        ...formData,
                                        Contrato: e.target.value
                                    }
                                )
                            }}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                    </div>
                    <div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Asignaturas</label>
                            <input type="text" name="asignaturas" value={formData.Asignaturas} onChange={(e) => {
                                setFormData(
                                    {
                                        ...formData,
                                        Asignaturas: e.target.value
                                    }
                                )
                            }}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Experiencia</label>
                            <input type="text" name="experiencia" value={formData.Experiencia} onChange={(e) => {
                                setFormData(
                                    {
                                        ...formData,
                                        Experiencia: e.target.value
                                    }
                                )
                            }}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Valoracion</label>
                            <input type="text" name="valoracion" value={formData.Valoracion} onChange={(e) => {
                                setFormData(
                                    {
                                        ...formData,
                                        Valoracion: e.target.value
                                    }
                                )
                            }}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                    </div>
                </form>
                <div className="flex justify-end">
                    <button type="button" onClick={onCancel}
                            className="mr-4 px-4 py-2 bg-gray-300 rounded">Cancelar
                    </button>
                    <button onClick={()=>{
                        onAccept(formData)
                    }} type="submit"
                            className="px-4 py-2 bg-indigo-500 text-white rounded">{formDataEdit? 'Editar': 'Guardar'}
                    </button>
                </div>
            </div>
        </div>
    );
}