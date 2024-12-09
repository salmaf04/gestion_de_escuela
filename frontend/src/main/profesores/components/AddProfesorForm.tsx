import {useState} from "react";
import  {Profesor} from "../../types.ts";
import LoadingIcon from "../../assets/loading.svg"

interface Props {
    onCancel: () => void
    onAccept: (formData: Profesor) => void
    formDataEdit?: Profesor
    isLoading: boolean
    className?: string
}

export default function AddProfesorForm({onCancel, onAccept, formDataEdit, isLoading, className}: Props) {
    const [formData, setFormData] = useState(formDataEdit || {
        Id: '',
        Nombre: '',
        Apellidos: '',
        Usuario: '',
        Password: '',
        Contrato: '',
        Asignaturas: '',
        Valoracion: '',
        Especialidad: '',
        Experiencia: ''
    });
    return (
        <div className={`fixed z-20 inset-0 bg-black bg-opacity-50 flex justify-center items-center ${className}`}>
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
                            <label className="block text-gray-700">Usuario</label>
                            <input type="text" name="usuario" value={formData.Usuario} onChange={(e) => {
                                setFormData(
                                    {
                                        ...formData,
                                        Usuario: e.target.value
                                    }
                                )
                            }}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                        {!formDataEdit &&
                            <div className="mb-4">
                                <label className="block text-gray-700">Contraseña</label>
                                <input type="text" name="password" value={formData.Password} onChange={(e) => {
                                    setFormData(
                                        {
                                            ...formData,
                                            Password: e.target.value
                                        }
                                    )
                                }}
                                       className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                            </div>

                        }

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

                    </div>
                    <div>
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
                            hidden={isLoading}
                            className="mr-4 px-4 py-2 bg-gray-300 rounded">Cancelar
                    </button>
                    <button onClick={() => {
                        onAccept(formData)
                    }} type="submit"
                            className={`${isLoading? ' bg-indigo-300 cursor-default': 'bg-indigo-500'} px-4 flex justify-center py-2  text-white rounded`}>
                        {isLoading? <img src={LoadingIcon} alt="loading" className="absolute w-6 h-6 animate-spin"/>: null}
                        <p className={`${isLoading? 'invisible': 'visible'}`}>
                            {formDataEdit ? 'Editar' : 'Guardar'}
                        </p>


                    </button>
                </div>
            </div>
        </div>
    );
}