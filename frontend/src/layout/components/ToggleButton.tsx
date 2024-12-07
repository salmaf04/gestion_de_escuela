import { useState } from 'react';

export default function ToggleButton() {
    const [selected, setSelected] = useState('Profesores');

    const handleToggle = () => {
        setSelected(selected === 'Profesores' ? 'Estudiante' : 'Profesores');
    };

    return (
        <div className=" font-medium flex items-center justify-center ">
            <div className="  relative flex w-64 h-9 bg-gray-200 rounded-full p-1">
                <div
                    className={`absolute top-0 left-0 w-36 h-full bg-gradient-to-r from-indigo-400 to-indigo-500 rounded-full transition-transform duration-300 ease-in-out ${selected === 'Estudiante' ? 'translate-x-28' : ''}`}
                ></div>
                <button
                    className={`w-1/2 h-full z-10 focus:outline-none ${selected === 'Profesores' ? 'text-white' : 'text-gray-700'}`}
                    onClick={handleToggle}
                >
                    Profesores
                </button>
                <button
                    className={`  w-1/2 h-full  z-10 focus:outline-none ${selected === 'Estudiante' ? 'text-white' : 'text-gray-700'}`}
                    onClick={handleToggle}
                >
                    Estudiante
                </button>
            </div>
        </div>
    );
}