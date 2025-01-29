import Table from "../../../components/Table.tsx";
import {useContext} from "react";
import {AusenciasContext} from "../AusenciasScreen.tsx";
import {AusenciaAdapter} from "../adapters/AusenciaAdapter.ts";

export default function Body(){
    const {dataTable, setEditting, onDeleteTableItem, isGetLoading} = useContext(AusenciasContext)
    return(
            <Table
                className={'h-5/6'}
                isLoading={isGetLoading!}
                Data={dataTable ?? []} header={AusenciaAdapter.Properties.slice(1)}
                   onRemoveRow={(index) => {
                       onDeleteTableItem!(index)
                   }}
                   onEditRow={(index) => {
                       const item = dataTable!.find((item) => item.id === index)
                       setEditting!(item!)
                   }}
            />
    )
}