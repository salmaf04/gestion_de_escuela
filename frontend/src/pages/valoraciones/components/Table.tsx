import React, { useState } from 'react';
import {ChevronDownIcon, ChevronRightIcon} from '@heroicons/react/20/solid';
import {ValoracionPorAsignaturadeProfesorGetAdapter} from "../adapters/ValoracionPromediodeProfesorGetAdapter.ts";

interface ProfesoresTableProps {
    items: ValoracionPorAsignaturadeProfesorGetAdapter [];
    headers: string[];
    showHeaders: string[];
    title: string;
}

const Table: React.FC<ProfesoresTableProps> = ({ title, items, headers, showHeaders }: ProfesoresTableProps) => {



    return (
        <>
            <h1 className={' font-semibold text-lg'}>{title} </h1>
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
                                        <span
                                            className={`${item[header] ? 'bg-green-200 text-green-950' : 'bg-red-200 text-red-950'} rounded-full py-2 w-16 font-bold text-xs`}>
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

        </>
    );
};

export default Table;