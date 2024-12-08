import {useState} from 'react';

interface Props {
    Materials: String[]
}

export default function MaterialForm({Materials}: Props) {
    const [formData, setFormData] = useState({
        option: '',
        date: '',
        time: ''
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
        const {name, value} = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    return (
        <div className="fixed z-40 inset-0 bg-black bg-opacity-50 flex justify-center items-center">
            <div className="bg-white w-1/5 p-6 rounded-lg">
                <h2 className="text-xl text-indigo-400 text-center font-bold mb-4">Solicitar Medio</h2>
                <form className="justify-around flex flex-col ">
                    <div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Material</label>
                            <select name="option" value={formData.option} onChange={handleChange}
                                    className="rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50">
                                <option value="" disabled>Selecciona un material</option>
                                {Materials.map((material, index) => {
                                    return <option key={index} value={index}>{material}</option>
                                })}
                            </select>
                        </div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Fecha</label>
                            <input type="date" name="date" value={formData.date} onChange={handleChange}
                                   className="rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"/>
                        </div>
                        <div className="mb-4">
                            <label className="block text-gray-700">Hora</label>
                            <input type="time" name="time" value={formData.time} onChange={handleChange}
                                   className="rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"/>
                        </div>
                    </div>
                    <div className="flex my-2 items-center justify-center">
                        <button type="button" onClick={() => {
                            //TODO: Handle cancel action
                        }}
                                className="mr-4 px-4 py-2 bg-gray-300 rounded">Cancelar
                        </button>
                        <button onClick={() => {
                            //TODO: Handle submit action
                        }} type="submit"
                                className="px-4 py-2 bg-indigo-500 text-white rounded">Solicitar
                        </button>
                    </div>

                </form>

            </div>
        </div>
    );
}