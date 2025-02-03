import Table from "../../../components/Table.tsx";
import {useContext} from "react";
import {MedioGetAdapter} from "../adapters/MedioGetAdapter.ts";
import {MedioContext} from "../MediosScreen.tsx";
import SolicitarIcon from "../../../assets/solicitar.svg";
import {useApiMedio} from "../hooks/useApiMedios.ts";
import AlertIcon from "../../../assets/alert.svg";
import {AppContext} from "../../../App.tsx";
import {RolesEnum} from "../../../api/RolesEnum.ts";
import {DBObject} from "../../../types.ts";

export default function Body(){
    const {dataTable, setEditting, onDeleteTableItem, isLoading} = useContext(MedioContext)
    const {solicitarMedio} = useApiMedio()
    const {setError, medios, allowRoles, typeRole} = useContext(AppContext)
    const actions = []
    if (allowRoles!([RolesEnum.TEACHER])){
        actions.push({
            action: (row: DBObject) => {
                solicitarMedio!({mean_id: row.id})
            },
            lineColor: 'bg-green-500',
            hoverColor: 'bg-green-100',
            title: "Solicitar",
            icon: <img src={SolicitarIcon} alt={'Solicitar'}/>,
            isVisible: ()=>true
        })
    }
    if (typeRole === 'dean'){
        actions.push({
            action: (row: DBObject) => {
                solicitarMedio!({mean_id: row.id})
            },
            lineColor: 'bg-green-500',
            hoverColor: 'bg-green-100',
            title: "Solicitar",
            icon: <img src={SolicitarIcon} alt={'Solicitar'}/>,
            isVisible: ()=>true
        })
    }
    return(
            <Table
                className={'h-5/6 accentgree'}
                isLoading={isLoading!}
                Data={dataTable ?? []} header={MedioGetAdapter.Properties.slice(1)}
                   onRemoveRow={(index) => {
                       onDeleteTableItem!(index)
                   }}
                   onEditRow={(index) => {
                       const item = dataTable!.find((item) => item.id === index)
                       console.log(item)
                       setEditting!(item!)
                   }}
                actions={actions}
            />
    )
}