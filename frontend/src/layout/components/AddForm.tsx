// src/layout/components/FormModal.tsx
import { useState } from "react";

interface Props {
    onClose: () => void;
}

export default function FormModal({ onClose }: Props) {
    const [formData, setFormData] = useState({
        nombre: "",
        apellidos: "",
        especialidad: "",
        contrato: "",
        asignaturas: "",
        experiencia: "",
        valoracion: ""
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        // Handle form submission logic here
        onClose();
    };

    return (
        <div className="fixed z-40 inset-0 bg-black bg-opacity-50 flex justify-center items-center">
            <div className="bg-white w-1/2  p-6 rounded-lg">
                <h2 className="text-xl text-center font-bold mb-4">Añadir Nuevo Registro</h2>
                <form className={'justify-around flex flex-row  '} onSubmit={handleSubmit}>
                    <div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Nombre</label>
                            <input type="text" name="nombre" value={formData.nombre} onChange={handleChange}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Apellidos</label>
                            <input type="text" name="apellidos" value={formData.apellidos} onChange={handleChange}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Especialidad</label>
                            <input type="text" name="especialidad" value={formData.especialidad} onChange={handleChange}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Contrato</label>
                            <input type="text" name="contrato" value={formData.contrato} onChange={handleChange}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                    </div>
                    <div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Asignaturas</label>
                            <input type="text" name="asignaturas" value={formData.asignaturas} onChange={handleChange}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Experiencia</label>
                            <input type="text" name="experiencia" value={formData.experiencia} onChange={handleChange}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Valoracion</label>
                            <input type="text" name="valoracion" value={formData.valoracion} onChange={handleChange}
                                   className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}/>
                        </div>
                    </div>
                </form>
                <div className="flex justify-end">
                    <button type="button" onClick={onClose}
                            className="mr-4 px-4 py-2 bg-gray-300 rounded">Cancelar
                    </button>
                    <button type="submit" className="px-4 py-2 bg-indigo-500 text-white rounded">Guardar</button>
                </div>
            </div>
        </div>
    );
}