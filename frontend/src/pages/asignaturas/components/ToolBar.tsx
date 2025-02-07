import SearchInput from "../../../components/SearchInput.tsx";
import AddButton from "../../../components/AddButton.tsx";
import {useContext} from "react";
import {AsignaturaContext} from "../AsignaturasScreen.tsx";
import ExportButton from "../../../components/ExportButton.tsx";
import {AsignaturaGetAdapter} from "../adapters/AsignaturaGetAdapter.ts";
import {AppContext} from "../../../App.tsx";
import {RolesEnum} from "../../../api/RolesEnum.ts";

export default function ToolBar() {
    const {
        searchText,
        setSearchText,
        setShowModal,
        dataTable
    } = useContext(AsignaturaContext)
    const {allowRoles} = useContext(AppContext)

    return (
            <div className={'self-end w-2/3 my-4 h-1/6 flex items-center justify-between px-5'}>
                {/*<ToggleButton/>*/}
                <SearchInput focus={true} searchText={searchText!} setSearchText={(text: string) => {
                    setSearchText!(text)
                }}/>

                <ExportButton title={'Asignaturas'} headers = {AsignaturaGetAdapter.Properties.slice(1)} data={dataTable}></ExportButton>
                {allowRoles!([RolesEnum.SECRETARY]) &&
                    <AddButton onClick={() => setShowModal!(true)}/>
                }
            </div>
    )
}