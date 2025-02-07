import {useForm, SubmitHandler} from "react-hook-form"
import {useContext, useEffect} from "react";
import MySpinner from "../../../components/MySpinner.tsx";
import {useApiProfesor} from "../hooks/useApiProfesor.ts";
import {ISelect} from "../../../types/ISelect.ts";
import {useApiAsignatura} from "../../asignaturas/hooks/useApiAsignatura.ts";
import {AppContext} from "../../../App.tsx";
import {IValorationCreate} from "../models/IValorationCreate.ts";
import Select from "../../../components/Select.tsx";
import {DBObject} from "../../../types.ts";
import {useApiEstudiante} from "../../estudiantes/hooks/useApiEstudiante.ts";

interface Props{
    profesor?: DBObject,
    setShowModal?: (text: boolean) => void;
}
export default function SancionModal({profesor, setShowModal}: Props) {
    const {register, handleSubmit, control} = useForm<IValorationCreate>()
    const {isLoading, valorarProfesor} = useApiProfesor()
    const {getAsignaturas} = useApiAsignatura()
    const {getEstudiante, estudiante} = useApiEstudiante()
    const {asignaturas, personalId, profesores} = useContext(AppContext)
    const editting = false
    useEffect(() => {
        getAsignaturas!()
        getEstudiante!(personalId!)
    }, []);
    const asignaturasSelect: ISelect[] = profesores!.find((i) => i.id === profesor?.id)!.asignaturas.map((ap)=>{
        return {
            id: asignaturas?.find((a) => a.name === ap)!.id ?? "",
            name: ap
        }
    }) ?? []

    const onSubmit: SubmitHandler<Partial<IValorationCreate>> = (data) => {
        valorarProfesor({
            subject_id: data.subject_id!,
            course_id: estudiante!.course.id,
            grade: data.grade!,
            student_id: personalId!,
            teacher_id: profesor?.id ?? "",
        })
        setShowModal!(false)
    }
    return (
        <div className={` fixed  z-20 inset-0 bg-black bg-opacity-50 flex justify-center items-center`}
        >
            <div className="min-h-[30%] bg-white w-1/2  py-6 px-8 rounded-lg">
                <h2 className="text-2xl text-indigo-600 text-center font-bold group mb-6">{`${editting ? 'Editar Registro' : 'Añadir Registro'}`}</h2>
                <form onSubmit={handleSubmit(onSubmit)}>
                    <div className={'grid grid-cols-2 gap-y-5 gap-x-10'}>

                        <div className={'w-full mb-4'}>
                            <Select
                                {...register(`subject_id`, {
                                    required: true,
                                })}
                                label={'Asignatura'}
                                labelClassName={'text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold '}
                                data={asignaturasSelect}
                                control={control}
                            />
                        </div>
                        <div className="group ">
                            <label
                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Valoracion</label>
                            <input
                                type="number"
                                {...register("grade", {
                                    required: "true"
                                })}
                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                            />
                        </div>
                    </div>


                    <div className="flex space-x-3 justify-center mt-10">
                        <button type="button" onClick={() => {
                            setShowModal!(false);
                        }}
                                hidden={isLoading}
                                className="hover:bg-gray-400 transition-colors w-full py-2 bg-gray-300 rounded-lg text-gray-900">Cancelar
                        </button>
                        <button type="submit"
                                className={`${isLoading ? 'hover:bg-indigo-300 bg-indigo-300 cursor-default' : 'bg-indigo-500 hover:bg-indigo-600 '} transition-colors w-full flex justify-center py-2  text-indigo-50 rounded-lg`}>
                            {isLoading ? <MySpinner className={'h-6 w-6'}/> : null}
                            <p className={`${isLoading ? 'invisible' : 'visible'}`}>
                                {editting ? 'Editar' : 'Guardar'}
                            </p>
                        </button>
                    </div>
                </form>
            </div>

        </div>
    );
}