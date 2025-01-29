import React from 'react';
import { ProfesorEspGetAdapter } from "../adapters/ProfesorEspGetAdapter.ts";

interface ProfesoresTableProps {
    profesores: ProfesorEspGetAdapter[];
}

const ProfesoresTable: React.FC<ProfesoresTableProps> = ({ profesores }) => {
    if (profesores.length === 0) {
        return <div>No data available</div>;
    }

    const headers = ['name', 'specialty', 'mean', 'state'];
    const showHeaders = ['Nombre', 'Especialidad', 'Medio', 'Estado'];

    return (
        <table className="min-w-full divide-y ">
            <thead className="">
                <tr>
                    {showHeaders.map(header => (
                        <th key={header} className="px-6 py-3 text-left text-xs   ">
                            {header}
                        </th>
                    ))}
                </tr>
            </thead>
            <tbody className="divide-y">
                {profesores.map((profesor, index) => (
                    <tr key={index}>
                        {headers.map(header => (
                            <td key={header} className="px-6 py-4 whitespace-nowrap text-sm ">
                                {profesor[header]}
                            </td>
                        ))}
                    </tr>
                ))}
            </tbody>
        </table>
    );
};

export default ProfesoresTable;