import Table from "../../../components/Table.tsx";
import {useContext} from "react";
import {AulasContext} from "../AulasScreen.tsx";
import {AulaGetAdapter} from "../adapters/AulaGetAdapter.ts";
import SolicitarIcon from "../../../assets/solicitar.svg";
import {useApiAulas} from "../hooks/useApiAulas.ts";

export default function Body(){
    const {dataTable,  setEditting, onDeleteTableItem, isLoading} = useContext(AulasContext)
    const {solicitarAula} = useApiAulas()

    return(
            <Table
                className={'h-5/6'}
                isLoading={isLoading!}
                Data={dataTable ?? []} header={AulaGetAdapter.Properties.slice(1)}
                   onRemoveRow={(index) => {
                       onDeleteTableItem!(index)
                   }}
                   onEditRow={(index) => {
                       const item = dataTable!.find((item) => item.id === index)
                       setEditting!({id: item!.id, body: item!})
                   }}
                actions={[
                    {
                        action: (row) => {
                            solicitarAula({classroom_id: row.id})
                        },
                        color: 'green',
                        title: "Solicitar",
                        icon: <img src={SolicitarIcon} alt={'Solicitar'}/>,
                        isVisible: ()=>true
                    }
                ]}
            />
    )
}