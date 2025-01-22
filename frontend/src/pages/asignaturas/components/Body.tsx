import {AsignaturaGetAdapter} from "../adapters/AsignaturaGetAdapter.ts";
import Table from "../../../components/Table.tsx";
import {useContext} from "react";
import {AsignaturaContext} from "../AsignaturasScreen.tsx";

export default function Body(){
    const {dataTable, setEditting, onDeleteTableItem, isGetLoading} = useContext(AsignaturaContext)
    return(
            <Table
                className={'h-5/6'}
                isLoading={isGetLoading!}
                Data={dataTable ?? []} header={AsignaturaGetAdapter.Properties.slice(1)}
                   onRemoveRow={(index) => {
                       onDeleteTableItem!(index)
                   }}
                   onEditRow={(index) => {
                       const item = dataTable!.find((item) => item.id === index)
                       console.log(item)
                       setEditting!(item!)
                   }}
            />
    )
}