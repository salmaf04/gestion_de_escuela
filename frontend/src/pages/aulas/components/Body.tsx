import Table from "../../../components/Table.tsx";
import {useContext} from "react";
import {AulasContext} from "../AulasScreen.tsx";
import {AulaGetAdapter} from "../adapters/AulaGetAdapter.ts";
import SolicitarIcon from "../../../assets/solicitar.svg";
import {useApiAulas} from "../hooks/useApiAulas.ts";
import {AppContext} from "../../../App.tsx";
import {RolesEnum} from "../../../api/RolesEnum.ts";
import DevolverIcon from "../../../assets/devolver.svg";

export default function Body(){
    const {dataTable,  setEditting, onDeleteTableItem, isLoading} = useContext(AulasContext)
    const {solicitarAula, devolverAula} = useApiAulas()
    const {allowRoles, aulas, personalId} = useContext(AppContext)

    return(
            <Table
                className={'h-5/6 accre5'}
                isLoading={isLoading!}
                Data={dataTable ?? []} header={AulaGetAdapter.Properties.slice(1)}
                   onRemoveRow={(index) => {
                       onDeleteTableItem!(index)
                   }}
                   onEditRow={(index) => {
                       if (allowRoles!([RolesEnum.SECRETARY])) {
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
                        hoverColor: 'hover:bg-green-100',
                        title: "Solicitar",
                        icon: <img src={SolicitarIcon} alt={'Solicitar'}/>,
                        isVisible: (id)=> !aulas!.find((aula)=>aula.id === id)!.requested_by
                    },
                    {
                        action: (row) => {
                            devolverAula(row.id)
                        },
                        lineColor: 'bg-red-500',
                        hoverColor: 'hover:bg-red-100',
                        title: "Devolver",
                        icon: <img src={DevolverIcon} alt={'Devolver'}/>,
                        isVisible: (id)=> aulas!.find((aula)=>aula.id === id)!.requested_by === personalId
                    }
                ]: []}
                isRemoveActive={allowRoles!([RolesEnum.SECRETARY])}
            />
    )
}