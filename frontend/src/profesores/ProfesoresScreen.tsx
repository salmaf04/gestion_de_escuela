import {createContext, useContext, useEffect, useState} from "react";
import {ProfesorGetAdapter} from "./adapters/ProfesorGetAdapter.ts";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import {useGetProfesores} from "./hooks/useGetProfesores.ts";
import {ProfesorCreateAdapter} from "./adapters/ProfesorCreateAdapter.ts";
import {AppContext} from "../App.tsx";

interface profesorContextInterface{
    searchText?: string;
    dataTable?: ProfesorGetAdapter[];
    editting?: ProfesorCreateAdapter;
    isAdding?: boolean;
    setIsAdding?: (text: boolean) => void;
    setEditting?: (profesor: ProfesorCreateAdapter) => void;
    isGetLoading?: boolean;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (profesorEdit: ProfesorCreateAdapter) => void;
    onAddTableItem?: (profesorEdit: ProfesorCreateAdapter) => void;
}

export const ProfesorContext = createContext<profesorContextInterface>(
    {}
);

export default function ProfesoresScreen() {
    const [searchText, setSearchText] = useState('');
    const [editting, setEditting] = useState<ProfesorCreateAdapter | undefined>()
    const [isAdding, setIsAdding] = useState(false)
    const {setError} = useContext(AppContext)
    const {
        isGetLoading,
        profesores,
        getProfesores,
    } = useGetProfesores(setError!)

    useEffect(() => {
        getProfesores()
    }, []);

    const onDeleteTableItem = (index: string) => {
        //todo DELETE request Profesor
    }

    const onEditTableItem = (profesorEdit: ProfesorCreateAdapter) => {
        //todo PUT request Profesor
    }

    const onAddTableItem = (profesor: ProfesorCreateAdapter) => {
        //todo Add request Profesor
    }
    return (
        <>
            <ProfesorContext.Provider value={{
                isGetLoading: isGetLoading,
                dataTable: profesores,
                searchText: searchText,
                editting: editting,
                isAdding: isAdding,
                setIsAdding: setIsAdding,
                setEditting: setEditting,
                setSearchText: setSearchText,
                onDeleteTableItem: onDeleteTableItem,
                onEditTableItem: onEditTableItem,
                onAddTableItem: onAddTableItem
            }
            }>
                <ToolBar />
                <Body />
                {/*getError &&
                    */
                }

                {/*{isAdding && <AddProfesorForm
                    onAccept={(formData) => {
                        setisLoading(true)
                        postProfesor(formData).then(res => {
                            if (res.ok) {
                                res.json().then((data: ProfesorGetAdapter) => {
                                    setDataTable([...dataTable, data])
                                    setIsAdding(false)
                                })
                            } else {
                                setError(res.statusText)
                            }
                        }).finally(() => {
                            setisLoading(false)
                        })


                    }}
                    isLoading={isLoading}
                    onCancel={() => setIsAdding(false)}
                />}

                {isEditing && <AddProfesorForm
                    isLoading={isLoading}
                    onAccept={(formData) => {
                        //todo PUT request Profesor
                        setIsEditing(null)
                    }}
                    formDataEdit={isEditing}
                    onCancel={() => setIsEditing(null)}
                    <div className={"mx-4 w-11/12 h-dvh flex flex-col"}>


                {
                    isTableLoading && <Spinner/>
                }

            </div>
                />}*/}
            </ProfesorContext.Provider>

        </>

    )
}