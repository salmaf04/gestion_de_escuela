import jsPDF from 'jspdf';
import 'jspdf-autotable';
import {MedioGetAdapter} from "../pages/medios/adapters/MedioGetAdapter.ts";
import {AsignaturaGetAdapter} from "../pages/asignaturas/adapters/AsignaturaGetAdapter.ts";

interface ExportButtonProps {
    data : Adapter;
}

type Adapter = MedioGetAdapter[] | AsignaturaGetAdapter[] | undefined

function exportDataToPDF(data : Adapter){
    const doc = new jsPDF();
    const tableColumn = Object.keys(data[0]).filter(key => key !== 'id');
    const tableRows = [];

    data.forEach(item => {
        const itemData = tableColumn.map(key => {
            const value = item[key];
            if( key === 'id' ) return "";
            if (typeof value === 'object' && value !== null) {
                return Object.values(value).join(', ');
            }
            return value;
        });
        tableRows.push(itemData);
    });

    (doc as any).autoTable(tableColumn, tableRows, { startY: 20 });
    doc.text("Exported Data", 14, 15);
    doc.save('exported_data.pdf');
}



export default function ExportButton({data} : ExportButtonProps) {


    const handleExport = () => {
        exportDataToPDF(data);
    };

    return (
        <button onClick={handleExport} className="flex justify-around items-center gap-2 cursor-pointer transition-all hover:from-indigo-600 hover:to-indigo-600 hover:scale-105 text-indigo-50 font-semibold py-2 px-5 bg-gradient-to-br from-indigo-500 to-indigo-600 rounded-lg ">
            Exportar
        </button>
    );
}