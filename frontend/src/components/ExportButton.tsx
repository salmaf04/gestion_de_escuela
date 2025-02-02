import jsPDF from 'jspdf';
import 'jspdf-autotable';
import {DBObject} from "../types.ts";
import {jsPDFDocument} from "jspdf-autotable";



interface ExportButtonProps {
    data?: DBObject[]  ;
    headers: string[];
    title : string[]
}


function exportDataToPDF(  data : DBObject[] | undefined ,headers : string[] , title : string ){
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




export default function ExportButton({data, headers , title }  : ExportButtonProps ) {


    const handleExport = () => {
        exportDataToPDF(data , headers);
    };

    return (
        <button onClick={handleExport} className="flex justify-around items-center gap-2 cursor-pointer transition-all hover:from-indigo-600 hover:to-indigo-600 hover:scale-105 text-indigo-50 font-semibold py-2 px-5 bg-gradient-to-br from-indigo-500 to-indigo-600 rounded-lg ">
            Exportar
        </button>
    );
}