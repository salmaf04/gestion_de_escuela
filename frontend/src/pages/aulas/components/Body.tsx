import Table from "../../../components/Table.tsx";
import {useContext} from "react";
import {AulasContext} from "../AulasScreen.tsx";
import {AulaGetAdapter} from "../adapters/AulaGetAdapter.ts";
import SolicitarIcon from "../../../assets/solicitar.svg";
import {useApiAulas} from "../hooks/useApiAulas.ts";
import {AppContext} from "../../../App.tsx";
import {RolesEnum} from "../../../api/RolesEnum.ts";

export default function Body(){
    const {dataTable,  setEditting, onDeleteTableItem, isLoading} = useContext(AulasContext)
    const {solicitarAula} = useApiAulas()
    const {allowRoles} = useContext(AppContext)

    return(
            <Table
                className={'h-5/6'}
                isLoading={isLoading!}
                Data={dataTable ?? []} header={AulaGetAdapter.Properties.slice(1)}
                   onRemoveRow={(index) => {
                       onDeleteTableItem!(index)
                   }}
                   onEditRow={(index) => {
                       if (allowRoles([RolesEnum.SECRETARY])) {
                           const item = dataTable!.find((item) => item.id === index)
                           setEditting!({id: item!.id, body: item!})
                       }
                   }}
                actions={allowRoles!([RolesEnum.TEACHER]) ? [
                    {
                        action: (row) => {
                            solicitarAula({classroom_id: row.id})
                        },
                        lineColor: 'bg-green-500',
                        hoverColor: 'bg-green-100',
                        title: "Solicitar",
                        icon: <img src={SolicitarIcon} alt={'Solicitar'}/>,
                        isVisible: ()=>true
                    }
                ]: []}
                isRemoveActive={allowRoles!([RolesEnum.SECRETARY])}
            />
    )
}