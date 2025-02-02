import jsPDF from 'jspdf';
import 'jspdf-autotable';
;import {jsPDFDocument} from "jspdf-autotable";
import {useState} from "react";
import FunctionalitiesForm from "./FunctionalitiesForm.tsx";
import { ProfesorEspGetDB, FiltrodeMantenimientoGetDB, CostoPromedioGetDB, ValoracionPromediodeProfesorGetDB, ValoracionPromediodeEstudianteGetDB, SalariosdeProfesoresGetDB } from "../../models/models.ts";
type Adapter = ProfesorEspGetDB | FiltrodeMantenimientoGetDB | CostoPromedioGetDB | ValoracionPromediodeProfesorGetDB | ValoracionPromediodeEstudianteGetDB | SalariosdeProfesoresGetDB;


type dataExport =  { title: string, headers: string[], showHeaders: string[], items: Adapter[]  }

interface ExportButtonProps {
    data?: dataExport    ;
    options : string[]

}


function exportDataToPDF(options: string[], data?: dataExport) {
    const doc = new jsPDF();

    if (data) {
        options.forEach(option => {
            const section = data.find(d => d.title === option);
            if (section) {
                const tableColumn = section.showHeaders;
                const tableRows: unknown[] = [];

                section.items.forEach(item => {
                    const itemData = section.headers.map(header => item[header]);
                    tableRows.push(itemData);
                });

                const startY = doc.lastAutoTable ? doc.lastAutoTable.finalY + 20 : 20;
                doc.text(section.title, 14, startY - 2 );
                (doc as jsPDFDocument).autoTable(tableColumn, tableRows, { startY });
            }
        });
    }

    doc.save('data_report.pdf');
}


export default function ExportFuncionalidadesButton({data , options }  : ExportButtonProps ) {

    const[select , setSelect] = useState(false)

    const handleExport = (options : string[]) => {
        exportDataToPDF(options , data );
        setSelect(false);
    };


    return (

        <>
            {select && <FunctionalitiesForm onAccept={handleExport} onCancel={() => setSelect(false)} options={options}></FunctionalitiesForm>}
            <button onClick={() => setSelect(true)} className="flex justify-around items-center gap-2 cursor-pointer transition-all hover:from-indigo-600 hover:to-indigo-600 hover:scale-105 text-indigo-50 font-semibold py-2 px-5 bg-gradient-to-br from-indigo-500 to-indigo-600 rounded-lg ">
                Exportar
            </button>
        </>
    );
}