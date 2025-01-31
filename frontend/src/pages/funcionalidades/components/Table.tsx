import React, { useState } from 'react';
import { ProfesorEspGetAdapter } from "../adapters/ProfesorEspGetAdapter.ts";
import { FiltrodeMantenimientoGetAdapter } from "../adapters/FiltrodeMantenimientoGetAdapter.ts";
import { CostoPromedioGetAdapter } from "../adapters/CostoPromedioGetAdapter.ts";
import { ValoracionPromediodeProfesorGetAdapter } from "../adapters/ValoracionPromediodeProfesorGetAdapter.ts";
import { ValoracionPromediodeEstudianteGetAdapter } from "../adapters/ValoracionPromediodeEstudianteGetAdapter.ts";
import { SalariosdeProfesoresGetAdapter } from "../adapters/SalariosdeProfesoresGetAdapter.ts";

interface ProfesoresTableProps {
    items: ProfesorEspGetAdapter[] | CostoPromedioGetAdapter[] | FiltrodeMantenimientoGetAdapter[] | ValoracionPromediodeProfesorGetAdapter[] | ValoracionPromediodeEstudianteGetAdapter[] | SalariosdeProfesoresGetAdapter[];
    headers: string[];
    showHeaders: string[];
    title: string;
}

const Table: React.FC<ProfesoresTableProps> = ({ title, items, headers, showHeaders }: ProfesoresTableProps) => {
    const [isVisible, setIsVisible] = useState(false);

    if (items.length === 0) {
        return <div>No data available</div>;
    }

    const toggleVisibility = () => {
        setIsVisible(!isVisible);
    };

    return (
        <>
            <div className="m-2 flex flex-row items-center justify-around gap-28">
                <h1>{title} </h1>
                <button onClick={toggleVisibility} className="ml-2">
                    {isVisible ? '▼' : '▶'}
                </button>
            </div>
            < hr className={'mb-8'}/>
            {isVisible && (
                <table className="mb-10 min-w-full divide-y">
                    <thead>
                        <tr>
                            {showHeaders.map(header => (
                                <th key={header} className=" w-20 px-6 py-3 text-left text-xs">
                                    {header}
                                </th>
                            ))}
                        </tr>
                    </thead>
                    <tbody className="divide-y">
                    {items.map((item, index) => (
                        <tr key={index}>
                            {headers.map(header => (
                                <td key={header} className="px-6 py-4 text-sm" style={{width: '150px'}}>
                                    {Array.isArray(item[header]) ? (
                                        item[header].join(', ')
                                    ) : typeof item[header] === "boolean" ? (
                                        <span className={`${item[header] ? 'bg-green-200 text-green-950' : 'bg-red-200 text-red-950'} rounded-full py-2 w-16 font-bold text-xs`}>
                        {item[header] ? "Sí" : "No"}
                    </span>
                                    ) : (
                                        item[header]
                                    )}
                                </td>
                            ))}
                        </tr>
                    ))}
                    </tbody>
                </table>
            )}
        </>
    );
};

export default Table;