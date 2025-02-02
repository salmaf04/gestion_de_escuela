import Table from "../../../components/Table.tsx";
import {useContext} from "react";
import {UsuariosContext} from "../UsuariosScreen.tsx";
import {UsuarioAdapter} from "../adapters/UsuarioAdapter.ts";

export default function Body(){
    const {dataTable, setEditting, onDeleteTableItem, isGetLoading} = useContext(UsuariosContext)
    return(
            <Table
                className={'h-5/6'}
                isLoading={isGetLoading!}
                Data={dataTable ?? []} header={UsuarioAdapter.Properties.slice(1)}
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