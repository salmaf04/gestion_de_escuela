
import { useContext } from "react";
import SearchInput from "./SearchInput.tsx";
import AddButton from "./AddButton.tsx";
import {AppContext} from "../App.tsx";
import UserIcon from "../assets/user.svg";
import ExportButton from "./ExportButton.tsx";
import {EstudianteGetAdapter} from "../pages/estudiantes/adapters/EstudianteGetAdapter.ts";

export interface IToolbarContext {
    searchText?: string;
    setSearchText?: (text: string) => void;
    setShowModal?: (show: boolean) => void;
    dataTable?: Array<any>
}

export default function ToolBar({context, allowAddButton = true} : {context: React.Context<IToolbarContext>, allowAddButton: boolean }) {
    const {
        searchText,
        setSearchText,
        setShowModal,
        dataTable,

    } = useContext(context);
    const {username, setToken, roles} = useContext(AppContext)
    return (
        <div className={'w-full my-4 h-1/6 flex items-center justify-between px-5'}>
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
                        {`${username}: ${roles}`}
                    </p>

                </div>
            </div>

            <SearchInput focus={true} searchText={searchText!} setSearchText={(text: string) => {
                setSearchText!(text);
            }}/>
            <ExportButton title={'Estudiantes'} headers = {EstudianteGetAdapter.Properties.slice(1)} data={dataTable}></ExportButton>
            {allowAddButton && <AddButton onClick={() => setShowModal!(true)}/>}
        </div>
    );
}