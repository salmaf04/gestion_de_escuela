import React, {useState} from 'react';

interface FunctionalitiesFormProps {
    options: string[];
    onAccept: (selectedOptions: string[]) => void;
    onCancel: () => void;
}

const FunctionalitiesForm: React.FC<FunctionalitiesFormProps> = ({options, onAccept, onCancel}) => {
    const [selectedOptions, setSelectedOptions] = useState<string[]>([]);

    const handleOptionChange = (option: string) => {
        if (option === 'All') {
            if (selectedOptions.includes('All')) {
                setSelectedOptions([]);
            } else {
                setSelectedOptions(['All', ...options]);
            }
        } else {
            setSelectedOptions(prevSelectedOptions =>
                prevSelectedOptions.includes(option)
                    ? prevSelectedOptions.filter(opt => opt !== option && opt !== 'All')
                    : [...prevSelectedOptions, option]
            );
        }
    };

    const handleAccept = () => {
        onAccept(selectedOptions.includes('All') ? options : selectedOptions);
    };

    return (
        <div className="absolute top-0 left-0 w-full h-full bg-gray-900 bg-opacity-50 flex justify-center items-center">
            <div className="bg-white p-8  rounded-lg shadow-lg">
                <h2 className="text-2xl text-indigo-600 text-center font-bold group mb-4">Selecciona las Tablas </h2>
                <div className="mb-4">

                    {options.map(option => (
                        <div key={option} className="flex items-center mb-2">
                            <input
                                type="checkbox"
                                id={option}
                                value={option}
                                checked={selectedOptions.includes(option)}
                                onChange={() => handleOptionChange(option)}
                                className="mr-2"
                            />
                            <label htmlFor={option}>{option}</label>
                        </div>
                    ))}
                </div>
                <div className="flex text-sm font-light text-indigo-600 text-center  group   items-center mb-4">
                    <input
                        type="checkbox"
                        id="Marcar todas"
                        value="Marcar todas"
                        checked={selectedOptions.includes('All')}
                        onChange={() => handleOptionChange('All')}
                        className="mr-2"
                    />
                    <label className={'  font-bold'} htmlFor="Marcar todas">Marcar todas</label>
                </div>
                <div className="flex justify-center  gap-2">
                    <button onClick={handleAccept} className=" bg-indigo-500 hover:bg-indigo-600 transition-colors w-full flex justify-center py-2 text-indigo-50 rounded-lg">Exportar
                    </button>
                    <button onClick={onCancel} className="hover:bg-gray-400 transition-colors w-full py-2 bg-gray-300 rounded-lg text-gray-900">Cancelar</button>
                </div>
            </div>
        </div>
    );
};



export default FunctionalitiesForm;