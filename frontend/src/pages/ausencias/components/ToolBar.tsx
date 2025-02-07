import SearchInput from "../../../components/SearchInput.tsx";
import AddButton from "../../../components/AddButton.tsx";
import {useContext} from "react";
import {AusenciasContext} from "../AusenciasScreen.tsx";
import ExportButton from "../../../components/ExportButton.tsx";
import {AusenciaAdapter} from "../adapters/AusenciaAdapter.ts";
import {RolesEnum} from "../../../api/RolesEnum.ts";
import {AppContext} from "../../../App.tsx";

export default function ToolBar() {
    const {
        searchText,
        setSearchText,
        setShowModal,
        dataTable
    } = useContext(AusenciasContext)
    const {allowRoles} = useContext(AppContext)

    return (
            <div className={'self-end w-2/3 my-4 h-1/6 flex items-center justify-between px-5'}>
                {/*<ToggleButton/>*/}
                <SearchInput focus={true} searchText={searchText!} setSearchText={(text: string) => {
                    setSearchText!(text)
                }}/>
                <ExportButton title={'Ausencias'} headers = {AusenciaAdapter.Properties.slice(1)} data={dataTable}></ExportButton>
                {allowRoles!([RolesEnum.TEACHER]) &&
                    <AddButton onClick={() => setShowModal!(true)}/>
                }
            </div>
    )
}