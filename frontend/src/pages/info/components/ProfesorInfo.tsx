import {useApiProfesor} from "../../profesores/hooks/useApiProfesor.ts";
import {useContext, useEffect} from "react";
import {AppContext} from "../../../App.tsx";

export default function ProfesorInfo(){
    const {getProfesor, profesor} = useApiProfesor()
    const {personalId} = useContext(AppContext)
    useEffect(() => {
        getProfesor(personalId!)
    }, []);
    return(
        <>
            <h2>Nombre</h2>
            <p>{profesor?.name}</p>
        </>
    )
}