import {AsignaturaGetAdapter} from "../adapters/AsignaturaGetAdapter.ts";
import Table from "../../../components/Table.tsx";
import {useContext} from "react";
import {AsignaturaContext} from "../AsignaturasScreen.tsx";
import {AppContext} from "../../../App.tsx";
import {RolesEnum} from "../../../api/RolesEnum.ts";

export default function Body(){
    const {dataTable, setEditting, onDeleteTableItem, isLoading} = useContext(AsignaturaContext)
    const {allowRoles} = useContext(AppContext)
    const header = AsignaturaGetAdapter.Properties.slice(1)
    if (allowRoles!([RolesEnum.TEACHER]))
        header.push('Mi Valoración')
    return(

            <Table
                className={'h-5/6'}
                isLoading={isLoading!}
                Data={dataTable ?? []}
                header={header}
                   onRemoveRow={(index) => {
                       onDeleteTableItem!(index)
                   }}
                   onEditRow={(index) => {
                       if (allowRoles!([RolesEnum.SECRETARY])) {
                           const item = dataTable!.find((item) => item.id === index)
                           setEditting!(item!)
                       }
                   }}
                isRemoveActive={allowRoles!([RolesEnum.SECRETARY])}
            />
    )
}