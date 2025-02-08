import Select from "../../../../components/Select.tsx";
import MySpinner from "../../../../components/MySpinner.tsx";
import {SubmitHandler, useForm} from "react-hook-form";
import {IEstudianteDB} from "../../../estudiantes/models/IEstudianteDB.ts";
import {useContext, useEffect} from "react";
import {AppContext} from "../../../../App.tsx";
import {useApiEstudiante} from "../../../estudiantes/hooks/useApiEstudiante.ts";
import {IEstudianteCreateDB} from "../../../estudiantes/models/IEstudianteCreateDB.ts";
import {ISelect} from "../../../../types/ISelect.ts";
import {ICursoGetLocal} from "../../../cursos/models/ICursoGetLocal.ts";
import {CursoContext} from "../../../cursos/CursosScreen.tsx";
import {useApiCurso} from "../../../cursos/hooks/useApiCurso.ts";

export default function EstudianteForm(){

    const { register, handleSubmit, control } = useForm<Partial<IEstudianteDB>>();
    const { setShowModal } = useContext(CursoContext);
    const {createEstudiante} = useApiEstudiante()
    const {cursos} = useContext(AppContext)
    const {getCursos} = useApiCurso()

    useEffect(() => {
        getCursos!()
    }, []);

    const {isLoading} = useApiEstudiante()

    const onSubmit: SubmitHandler<Partial<IEstudianteCreateDB>> = (data) => {
        createEstudiante(data)
        setShowModal!(false)
    };

    const cursosSelect: ISelect[] = cursos?.map((item: ICursoGetLocal)=>{
        return {
            id: item.id,
            name: item.year.toString()
        }
    }) ?? []

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <div className={'grid grid-cols-2 gap-y-1 gap-x-10'}>
                <div className="group mb-4">
                    <label
                        className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Nombre</label>
                    <input
                        type="text"
                        {...register("name", {
                            required: "true"
                        })}
                        className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                    />
                </div>
                <div className="group mb-4">
                    <label
                        className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Apellidos</label>
                    <input
                        type="text"
                        {...register("lastname", {
                            required: "true"
                        })}
                        className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                    />
                </div>
                <div className="group mb-4">
                    <label
                        className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Edad</label>
                    <input
                        type="number" {...register("age", {
                        required: true
                    })}
                        className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                    />
                </div>
                <div className="group mb-4">
                    <label
                        className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Correo</label>
                    <input
                        type="email" {...register("email", {
                        required: true
                    })}
                        className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                    />
                </div>

                <div className="group mb-4">
                    <label
                        className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Usuario</label>
                    <input
                        type="text" {...register("username", {
                        required: true
                    })}
                        className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}
                    />
                </div>

                <div className={'w-full mb-4'}>
                    <Select
                        {...register(`course_id`, {
                            required: true,
                        })}
                        label={'Curso'}
                        labelClassName={'text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold '}
                        data={cursosSelect}
                        control={control}
                    />
                </div>
            </div>
            <div className="group mb-4">
                <label
                    className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Actividades
                    Extras</label>
                <input
                    type="checkbox" {...register("extra_activities")}
                    className={"rounded-lg mx-4 p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50"}
                />
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
                        Guardar
                    </p>
                </button>
            </div>
        </form>
    )
}