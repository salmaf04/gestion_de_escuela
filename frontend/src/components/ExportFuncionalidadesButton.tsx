import jsPDF from 'jspdf';
import 'jspdf-autotable';
import {DBObject} from "../types.ts";
import {jsPDFDocument} from "jspdf-autotable";
import {useState} from "react";
import FunctionalitiesForm from "./FunctionalitiesForm.tsx";



interface ExportButtonProps {
    data?: DBObject[]  ;
    headers: string[];
    title : string
    options : string[]

}


function exportDataToPDF( options : string[] ,  data : DBObject[] | undefined ){
    const doc = new jsPDF();
    const tableColumn = headers;
    const tableRows : unknown = [];


    if(data)
        data.forEach(row =>
        { const itemData  = Object.values(row).slice(1).map(key =>
        { return key; }); tableRows.push(itemData); });

    (doc as jsPDFDocument).autoTable(tableColumn, tableRows, { startY: 20 });
    doc.text(title, 14, 15);
    doc.save(`${title}_report_pdf`);
}




export default function ExportFuncionalidadesButton({data , options }  : ExportButtonProps ) {

    const[select , setSelect] = useState(false)

    const handleExport = (options : string[]) => {
        exportDataToPDF(options , data );
        setSelect(false);
    };


    return (

        <>
            {select && <FunctionalitiesForm onAccept={() =>handleExport(options)} onCancel={() => setSelect(false)} options={options}></FunctionalitiesForm>}
            <button onClick={() => setSelect(true)} className="flex justify-around items-center gap-2 cursor-pointer transition-all hover:from-indigo-600 hover:to-indigo-600 hover:scale-105 text-indigo-50 font-semibold py-2 px-5 bg-gradient-to-br from-indigo-500 to-indigo-600 rounded-lg ">
                Exportar
            </button>
        </>
    );
}