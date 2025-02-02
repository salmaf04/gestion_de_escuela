import React, { useState } from 'react';

interface FunctionalitiesFormProps {
    options: string[];
    onAccept: (selectedOptions: string[]) => void;
    onCancel: () => void;
}

const FunctionalitiesForm: React.FC<FunctionalitiesFormProps> = ({ options, onAccept, onCancel }) => {
    const [selectedOptions, setSelectedOptions] = useState<string[]>([]);

    const handleOptionChange = (option: string) => {
        setSelectedOptions(prevSelectedOptions =>
            prevSelectedOptions.includes(option)
                ? prevSelectedOptions.filter(opt => opt !== option)
                : [...prevSelectedOptions, option]
        );
    };

    const handleAccept = () => {
        onAccept(selectedOptions);
    };

    return (
        <div className="absolute top-0 left-0 w-full h-full bg-gray-900 bg-opacity-50 flex justify-center items-center">
            <div className="bg-white p-4 rounded-lg shadow-lg">
                <h2 className="text-lg font-semibold mb-4">Select Options</h2>
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
                <div className="flex justify-end gap-2">
                    <button onClick={handleAccept} className="bg-blue-500 text-white py-1 px-3 rounded-lg">Accept</button>
                    <button onClick={onCancel} className="bg-gray-500 text-white py-1 px-3 rounded-lg">Cancel</button>
                </div>
            </div>
        </div>
    );
};

export default FunctionalitiesForm;