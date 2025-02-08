import SearchInput from "../../../components/SearchInput.tsx";
import AddButton from "../../../components/AddButton.tsx";
import {useContext} from "react";
import {ProfesorContext} from "../ProfesoresScreen.tsx";
import ExportButton from "../../../components/ExportButton.tsx";
import {ProfesorGetAdapter} from "../adapters/ProfesorGetAdapter.ts";
import {AppContext} from "../../../App.tsx";
import {RolesEnum} from "../../../api/RolesEnum.ts";

export default function ToolBar() {
    const {
        searchText,
        setSearchText,
        setShowModal,
        dataTable
    } = useContext(ProfesorContext)
    const {allowRoles} = useContext(AppContext)

    return (
            <div className={'self-end w-2/3 my-4 h-1/6 flex items-center justify-between px-5'}>
                {/*<ToggleButton/>*/}
                <SearchInput focus={true} searchText={searchText!} setSearchText={(text: string) => {
                    setSearchText!(text)
                }}/>
                <ExportButton title={'Profesores'} headers = {ProfesorGetAdapter.Properties.slice(1)} data={dataTable}></ExportButton>
                {allowRoles!([RolesEnum.SECRETARY]) &&
                    <AddButton onClick={() => setShowModal!(true)}/>
                }
            </div>
    )
}