import {ProfesorGetAdapter} from "../adapters/ProfesorGetAdapter.ts";
import Table from "../../components/Table.tsx";
import {useContext} from "react";
import {ProfesorContext} from "../ProfesoresScreen.tsx";

export default function Body(){
    const {dataTable, onEditTableItem, onDeleteTableItem} = useContext(ProfesorContext)
    return(
        <div>
            <Table className={'h-5/6'} Data={dataTable ?? []} header={ProfesorGetAdapter.Properties.slice(1)}
                   onRemoveRow={(index) => {
                       onDeleteTableItem!(index)
                   }}
                   onEditRow={(index) => {
                       const item = dataTable!.find((item) => item.id === index)
                       onEditTableItem!(item!)
                   }}
            />
        </div>
    )
}