import SearchInput from "../../../components/SearchInput.tsx";
import AddButton from "../../../components/AddButton.tsx";
import {useContext} from "react";
import {MantenimientoContext} from "../MantenimientosScreen.tsx";
import ExportButton from "../../../components/ExportButton.tsx";
import {MantenimientoGetAdapter} from "../adapters/MantenimientoGetAdapter.ts";
import {RolesEnum} from "../../../api/RolesEnum.ts";
import {AppContext} from "../../../App.tsx";

export default function ToolBar() {
    const {
        searchText,
        setSearchText,
        setShowModal,
        dataTable,
    } = useContext(MantenimientoContext)
    const {allowRoles} = useContext(AppContext)

    return (
            <div className={'self-end w-2/3 my-4 h-1/6 flex items-center justify-between px-5'}>
                {/*<ToggleButton/>*/}
                <SearchInput focus={true} searchText={searchText!} setSearchText={(text: string) => {
                    setSearchText!(text)
                }}/>
                <ExportButton title={'Mantenimientos'} headers = {MantenimientoGetAdapter.Properties.slice(1)} data={dataTable}></ExportButton>
                {allowRoles!([RolesEnum.ADMIN]) &&
                    <AddButton onClick={() => setShowModal!(true)}/>
                }
            </div>
    )
}