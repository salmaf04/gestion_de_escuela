import React from 'react';
import {ProfesorEspGetAdapter} from "../adapters/ProfesorEspGetAdapter.ts";
import {FiltrodeMantenimientoGetAdapter} from "../adapters/FiltrodeMantenimientoGetAdapter.ts";
import {CostoPromedioGetAdapter} from "../adapters/CostoPromedioGetAdapter.ts";
import {ValoracionPromediodeProfesorGetAdapter} from "../adapters/ValoracionPromediodeProfesorGetAdapter.ts";
import {ValoracionPromediodeEstudianteGetAdapter} from "../adapters/ValoracionPromediodeEstudianteGetAdapter.ts";
import {SalariosdeProfesoresGetAdapter} from "../adapters/SalariosdeProfesorGetAdapter.ts";

interface ProfesoresTableProps {
    items: ProfesorEspGetAdapter[] | CostoPromedioGetAdapter[]| FiltrodeMantenimientoGetAdapter[] | ValoracionPromediodeProfesorGetAdapter[] | ValoracionPromediodeEstudianteGetAdapter[] | SalariosdeProfesoresGetAdapter[]
    headers: string[]
    showHeaders: string[]
}

const Table: React.FC<ProfesoresTableProps> = ({items,headers,showHeaders} : ProfesoresTableProps) => {
    if (items.length === 0) {
        return <div>No data available</div>;
    }


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
            {items.map((profesor, index) => (
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

export default Table;