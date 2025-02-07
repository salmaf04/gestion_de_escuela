import Table from "../../../components/Table.tsx";
import {useContext} from "react";
import {MantenimientoGetAdapter} from "../adapters/MantenimientoGetAdapter.ts";
import {MantenimientoContext} from "../MantenimientosScreen.tsx";
import {AppContext} from "../../../App.tsx";
import {RolesEnum} from "../../../api/RolesEnum.ts";

export default function Body(){
    const {dataTable, setEditting, onDeleteTableItem, isLoading} = useContext(MantenimientoContext)
    const {allowRoles} = useContext(AppContext)

    return(
            <Table
                className={'h-5/6'}
                isLoading={isLoading!}
                Data={dataTable ?? []} header={MantenimientoGetAdapter.Properties.slice(1)}
                   onRemoveRow={(index) => {
                       onDeleteTableItem!(index)
                   }}
                   onEditRow={(index) => {
                       if (allowRoles!([RolesEnum.ADMIN])) {
                           const item = dataTable!.find((item) => item.id === index)
                           setEditting!(item!)
                       }
                   }}
                isRemoveActive={allowRoles!([RolesEnum.ADMIN])}
            />
    )
}