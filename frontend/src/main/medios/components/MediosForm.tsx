import {useState} from 'react';

interface Props {
    Materials: String[]
}

export default function MediosForm({Materials}: Props) {

    return (
        <div className="fixed z-40 inset-0 bg-black bg-opacity-50 flex justify-center items-center">
            <div className="bg-white w-1/2 p-6 rounded-lg">
                <h2 className="text-xl text-indigo-400 text-center font-bold mb-4">Solicitar Medio</h2>
                <form className="justify-around flex flex-row">

                </form>
                <div className="flex justify-end">
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
            </div>
        </div>
    );
}