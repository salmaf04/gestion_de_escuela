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
import DevolverIcon from "../../../assets/devolver.svg";

export default function Body() {
    const {dataTable, setEditting, onDeleteTableItem, isLoading} = useContext(MedioContext)
    const {solicitarMedio, devolverMedio} = useApiMedio()
    const {medios, allowRoles, personalId, setError} = useContext(AppContext)
    let actions = []
    if (allowRoles!([RolesEnum.TEACHER])) {
        actions.push({
            action: (row: DBObject) => {
                solicitarMedio!({mean_id: row.id})
            },
            lineColor: 'bg-green-500',
            hoverColor: 'hover:bg-green-100',
            title: "Solicitar",
            icon: <img src={SolicitarIcon} alt={'Solicitar'}/>,
            isVisible: (id) => !(medios?.find((aula) => aula.id === id)?.requested_by ?? false)
        }, {
            action: (row) => {
                devolverMedio(row.id)
            },
            lineColor: 'bg-red-500',
            hoverColor: 'hover:bg-red-100',
            title: "Devolver",
            icon: <img src={DevolverIcon} alt={'Devolver'}/>,
            isVisible: (id) => (medios?.find((aula) => aula.id === id)?.requested_by ?? "") === personalId
        })
    }
    if (allowRoles!([RolesEnum.ADMIN])){
        actions.push(
            {
                action: () => {
                    setError!(new Error("Este medio necesita ser reemplazado"))
                },
                lineColor: 'bg-amber-500',
                hoverColor: 'hover:bg-amber-100',
                title: "Alerta",
                icon: <img src={AlertIcon} alt={'Alerta'}/>,
                isVisible: (row: string) => medios?.find((medio) => medio.id === row)?.to_be_replaced ?? false
            }
        )
    }

    return (
        <Table
            className={'h-5/6'}
            isLoading={isLoading!}
            Data={dataTable ?? []} header={MedioGetAdapter.Properties.slice(1)}
            onRemoveRow={(index) => {
                onDeleteTableItem!(index)
            }}
            onEditRow={(index) => {
                if (allowRoles!([RolesEnum.ADMIN])) {
                    const item = dataTable!.find((item) => item.id === index)
                    setEditting!(item!)
                }
            }}
            actions={actions}
            isRemoveActive={allowRoles!([RolesEnum.ADMIN])}
        />
    )
}