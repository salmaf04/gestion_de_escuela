import {useState} from "react";
import {Estudiante} from "../../types.ts";

interface Props {
    onCancel: () => void
    onAccept: (formData: Estudiante) => void
    formDataEdit?: Estudiante
}

export default function AddEstudianteForm({onCancel, onAccept, formDataEdit}: Props) {
    const [formData, setFormData] = useState(formDataEdit || {
        Id : '',
        Nombre: '',
        Edad: '',
        ActividadesExtras: false
    });

    return (
        <div className="fixed z-40 inset-0 bg-black bg-opacity-50 flex justify-center items-center">
            <div className="bg-white w-1/2 p-6 rounded-lg">
                <h2 className="text-xl text-indigo-400 text-center font-bold mb-4">{`${formDataEdit ? 'Editar Registro' : 'Anadir Registro'}`}</h2>
                <form className={'justify-around flex flex-row'}>
                    <div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Nombre</label>
                            <input type="text" name="nombre" value={formData.Nombre} onChange={(e) => {
                                setFormData({
                                    ...formData,
                                    Nombre: e.target.value
                                });
                            }}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Edad</label>
                            <input type="text" name="edad" value={formData.Edad} onChange={(e) => {
                                setFormData({
                                    ...formData,
                                    Edad: e.target.value
                                });
                            }}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                        <div className="mb-4 flex flex-row">
                            <label className="block text-gray-700">Actividades Extras</label>
                            <input type="checkbox" name="actividadesExtras"  checked={formData.ActividadesExtras} onChange={(e) => {
                                setFormData({
                                    ...formData,
                                    ActividadesExtras: e.target.checked
                                });
                            }}
                                   className={"rounded-lg mx-4 p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                    </div>
                </form>
                <div className="flex justify-end">
                    <button type="button" onClick={onCancel}
                            className="mr-4 px-4 py-2 bg-gray-300 rounded">Cancelar
                    </button>
                    <button onClick={() => {
                        onAccept(formData)
                    }} type="submit"
                            className="px-4 py-2 bg-indigo-500 text-white rounded">{formDataEdit ? 'Editar' : 'Guardar'}
                    </button>
                </div>
            </div>
        </div>
    );
}