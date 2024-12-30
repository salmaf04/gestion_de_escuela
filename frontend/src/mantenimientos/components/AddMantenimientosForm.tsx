import {useState} from "react";
import {MantenimientoDeMedio} from "../../types.ts";

interface Props {
    onCancel: () => void
    onAccept: (formData: MantenimientoDeMedio) => void
    formDataEdit?: MantenimientoDeMedio
}

export default function AddMantenimientoForm({onCancel, onAccept, formDataEdit}: Props) {
    const [formData, setFormData] = useState(formDataEdit || {
        Id: '',
        Medio: '',
        Fecha: '',
        Costo: '',
    });

    return (
        <div className="fixed z-40 inset-0 bg-black bg-opacity-50 flex justify-center items-center">
            <div className="bg-white w-1/2 p-6 rounded-lg">
                <h2 className="text-xl text-indigo-400 text-center font-bold mb-4">{`${formDataEdit ? 'Editar Registro' : 'Anadir Registro'}`}</h2>
                <form className={'justify-around flex flex-row'}>
                    <div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Medio</label>
                            <input type="text" name="medio" value={formData.Medio} onChange={(e) => {
                                setFormData(
                                    {
                                        ...formData,
                                        Medio: e.target.value
                                    }
                                )
                            }}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Fecha</label>
                            <input type="date" name="fecha" value={formData.Fecha} onChange={(e) => {
                                setFormData(
                                    {
                                        ...formData,
                                        Fecha: e.target.value
                                    }
                                )
                            }}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                    </div>
                    <div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Costo</label>
                            <input type="text" name="costo" value={formData.Costo} onChange={(e) => {
                                setFormData(
                                    {
                                        ...formData,
                                        Costo: e.target.value
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