import Table from "../../../components/Table.tsx";
import {useContext} from "react";
import {MantenimientoGetAdapter} from "../adapters/MantenimientoGetAdapter.ts";
import {MantenimientoContext} from "../MantenimientosScreen.tsx";

export default function Body(){
    const {dataTable, setEditting, onDeleteTableItem, isGetLoading} = useContext(MantenimientoContext)
    return(
            <Table
                className={'h-5/6'}
                isLoading={isGetLoading!}
                Data={dataTable ?? []} header={MantenimientoGetAdapter.Properties.slice(1)}
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