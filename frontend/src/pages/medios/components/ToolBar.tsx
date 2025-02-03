import SearchInput from "../../../components/SearchInput.tsx";
import AddButton from "../../../components/AddButton.tsx";
import {useContext} from "react";
import {MedioContext} from "../MediosScreen.tsx";
import ExportButton from "../../../components/ExportButton.tsx";
import UserIcon from "../../../assets/user.svg";
import {AppContext} from "../../../App.tsx";
import {MedioGetAdapter} from "../adapters/MedioGetAdapter.ts";

export default function ToolBar() {
    const {
        searchText,
        setSearchText,
        setShowModal,
        dataTable
    } = useContext(MedioContext)
    const {setToken, username} = useContext(AppContext)
    return (
        <div className={'self-end w-full my-4 h-1/6 flex items-center justify-between px-5'}>
            <div className={'flex space-x-4'}>
                <div className={'flex flex-col items-center space-y-2'}>
                    <img src={UserIcon} alt={'usuario'}/>
                    <p className={'text-xs underline font-semibold text-slate-600 cursor-pointer'}
                       onClick={() => {
                           setToken!("")
                           sessionStorage.removeItem('token')
                       }}
                    >
                        Cerrar Sesión
                    </p>
                </div>
                <div className={'flex flex-col '}>
                    <h1 className={'text-3xl text-indigo-600 accent-i font-bold'}>
                        Bienvenido/a
                    </h1>
                    <p className={'text-slate-800 text-sm italic'}>
                        {username}
                    </p>

                </div>
            </div>

            <SearchInput focus={true} searchText={searchText!} setSearchText={(text: string) => {
                setSearchText!(text)
            }}/>
            <ExportButton title={'Medios'} headers = {MedioGetAdapter.Properties.slice(1)} data={dataTable}></ExportButton>
            <AddButton onClick={() => setShowModal!(true)}/>
        </div>
    )
}