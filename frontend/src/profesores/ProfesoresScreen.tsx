import {createContext, useEffect, useState} from "react";
import {ProfesorGetAdapter} from "./adapters/ProfesorGetAdapter.ts";
import ToolBar from "./components/ToolBar.tsx";
import Body from "./components/Body.tsx";
import {useGetProfesores} from "./api/useGetProfesores.ts";
import {ProfesorCreateAdapter} from "./adapters/ProfesorCreateAdapter.ts";

interface profesorContextProps{
    searchText?: string;
    dataTable?: ProfesorGetAdapter[];
    isEditting?: boolean;
    isAdding?: boolean;
    setIsAdding?: (text: boolean) => void;
    setIsEditting?: (text: boolean) => void;
    isGetLoading?: boolean;
    setSearchText?: (text: string) => void;
    onDeleteTableItem?: (index: string) => void;
    onEditTableItem?: (profesorEdit: ProfesorCreateAdapter) => void;
}

export const ProfesorContext = createContext<profesorContextProps>(
    {}
);

export default function ProfesoresScreen() {
    const [searchText, setSearchText] = useState('');
    const [isEditting, setIsEditting] = useState(false)
    const [isAdding, setIsAdding] = useState(false)
    const {
        isGetLoading,
        profesores,
        getProfesores,
        getError
    } = useGetProfesores()

    useEffect(() => {
        getProfesores()
    }, []);

    const onDeleteTableItem = (index: string) => {
        //todo DELETE request Profesor
    }

    const onEditTableItem = (profesorEdit: ProfesorCreateAdapter) => {
        //todo PUT request Profesor
    }
    return (
        <>
            <ProfesorContext.Provider value={{
                isGetLoading: isGetLoading,
                dataTable: profesores,
                searchText: searchText,
                isEditting: isEditting,
                isAdding: false,
                setIsAdding: setIsAdding,
                setIsEditting: setIsEditting,
                setSearchText: setSearchText,
                onDeleteTableItem: onDeleteTableItem,
                onEditTableItem: onEditTableItem
            }
            }>
                <ToolBar />
                <Body />
                {/*getError &&
                    <Alert title={'Error:'} message={error} className={'bg-red-200'} onClick={() => {
                        setError('')
                    }}/>*/
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