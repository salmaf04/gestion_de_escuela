import Table from "../../../components/Table.tsx";
import {useContext} from "react";
import {AusenciasContext} from "../AusenciasScreen.tsx";
import {AusenciaAdapter} from "../adapters/AusenciaAdapter.ts";
import {AppContext} from "../../../App.tsx";
import {RolesEnum} from "../../../api/RolesEnum.ts";

export default function Body(){
    const {dataTable, setEditting, onDeleteTableItem, isGetLoading} = useContext(AusenciasContext)
    const {allowRoles, ausencias} = useContext(AppContext)
    console.log(dataTable)
    return(
            <Table
                className={'h-5/6'}
                isLoading={isGetLoading!}
                Data={dataTable ?? []}
                header={AusenciaAdapter.Properties.slice(allowRoles!([RolesEnum.STUDENT]) ? 2 : 1)}
                onRemoveRow={(index) => {
                    onDeleteTableItem!(index)
                }}
                onEditRow={(index) => {
                    if (allowRoles!([RolesEnum.TEACHER])) {
                        const item = ausencias!.find((item) => item.id === index)
                        console.log({
                            index
                            ,...item
                        })
                        setEditting!(item)
                    }
                }}
                isRemoveActive={allowRoles!([RolesEnum.TEACHER])}
            />
    )
}