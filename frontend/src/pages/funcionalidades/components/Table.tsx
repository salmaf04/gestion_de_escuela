import React, { useState } from 'react';
import { ProfesorEspGetAdapter } from "../adapters/ProfesorEspGetAdapter.ts";
import { FiltrodeMantenimientoGetAdapter } from "../adapters/FiltrodeMantenimientoGetAdapter.ts";
import { CostoPromedioGetAdapter } from "../adapters/CostoPromedioGetAdapter.ts";
import { ValoracionPromediodeProfesorGetAdapter } from "../adapters/ValoracionPromediodeProfesorGetAdapter.ts";
import { ValoracionPromediodeEstudianteGetAdapter } from "../adapters/ValoracionPromediodeEstudianteGetAdapter.ts";
import { SalariosdeProfesoresGetAdapter } from "../adapters/SalariosdeProfesorGetAdapter.ts";
import {ChevronDownIcon, ChevronRightIcon} from '@heroicons/react/20/solid';

interface ProfesoresTableProps {
    items: ProfesorEspGetAdapter[] | CostoPromedioGetAdapter[] | FiltrodeMantenimientoGetAdapter[] | ValoracionPromediodeProfesorGetAdapter[] | ValoracionPromediodeEstudianteGetAdapter[] | SalariosdeProfesoresGetAdapter[];
    headers: string[];
    showHeaders: string[];
    title: string;
}

const Table: React.FC<ProfesoresTableProps> = ({ title, items, headers, showHeaders }: ProfesoresTableProps) => {
    const [isVisible, setIsVisible] = useState(false);



    const toggleVisibility = () => {
        setIsVisible(!isVisible);
    };

    return (
        <>
            <div className=" flex flex-row  py-4 mb-4">
                <div className={'w-[98%]'}>
                    <h1 className={' font-semibold text-lg'}>{title} </h1>
                    <div
                        className={`${isVisible ? 'w-[98%]' : 'w-[24%]'} h-[2px] bg-indigo-500 rounded-full transition-all duration-300`}/>
                </div>
                <button onClick={toggleVisibility} className="ml-2">
                    {isVisible ? <ChevronDownIcon className="h-5 w-5"/> : <ChevronRightIcon className="h-5 w-5"/>}
                </button>
            </div>
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