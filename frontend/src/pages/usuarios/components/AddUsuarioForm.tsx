// frontend/src/pages/notas/components/AddAusenciaForm.tsx
import {useContext, useEffect} from "react";
import {UsuariosContext} from "../UsuariosScreen.tsx";
import {useApiEstudiante} from "../../estudiantes/hooks/useApiEstudiante.ts";
import {useApiAsignatura} from "../../asignaturas/hooks/useApiAsignatura.ts";
import {AppContext} from "../../../App.tsx";
import Select from "../../../components/Select.tsx";
import MySpinner from "../../../components/MySpinner.tsx";
import { useFieldArray, useForm} from "react-hook-form";
import {ISelect} from "../../../types/ISelect.ts";
import {useApiProfesor} from "../../profesores/hooks/useApiProfesor.ts";
import {IUsuarioDB} from "../models/IUsuarioDB.ts";

export default function AddUsuarioForm() {
    const { onAddTableItem, setShowModal, editting, onEditTableItem, setEditting } = useContext(UsuariosContext);
    const {getEstudiantes, isLoading} = useApiEstudiante()
    const {getAsignaturas} = useApiAsignatura()
    const {getProfesores} = useApiProfesor()
    const {asignaturas, estudiantes, profesores} = useContext(AppContext)
    useEffect(() => {
        getAsignaturas()
        getEstudiantes()
        getProfesores()
    }, []);

    const {register, control, handleSubmit}=useForm()
    const {fields, append, remove} = useFieldArray({
        control,
        name: "notas",
    });

    const onSubmit = (data) => {

        if (editting){
            const dataParse: Partial<IUsuarioDB> = {
                teacher_id: data[`profesor${0}`],
                student_id: data[`estudiante${0}`],
                subject_id: data[`asignatura${0}`],
                note_value: data[`note_value${0}`],
            }
            onEditTableItem!(dataParse)
        }
        else{
            console.log(data)
            const dataParse: Partial<IUsuarioDB>[] = []
            for (let i = 0; i < fields.length; i++) {
                dataParse.push({
                    teacher_id: data[`profesor${i}`],
                    student_id: data[`estudiante${i}`],
                    subject_id: data[`asignatura${i}`],
                    note_value: data[`note_value${i}`],
                })
            }
            console.log(dataParse)
            onAddTableItem!(dataParse)
        }
        setShowModal!(false)
    }


    const estudiantesSelect: ISelect[] = estudiantes?.map((item)=>{
        return {
            id: item.id,
            name: item?.name
        }
    }) ?? []

    useEffect(() => {

    }, []);
    const asignaturasSelect: ISelect[] = asignaturas?.map((item)=>{
        return {
            id: item.id,
            name: item?.name
        }
    }) ?? []

    const profesoresSelect: ISelect[] = profesores?.map((item)=>{
        return {
            id: item.id,
            name: item?.name
        }
    }) ?? []



    return (
        <div className={` fixed  z-20 inset-0 bg-black bg-opacity-50 flex justify-center items-center`}
        >
            <div className="min-h-[30%] bg-white w-1/2  py-6 px-8 rounded-lg">
                <h2 className="text-2xl text-indigo-600 text-center font-bold group mb-6">{`${editting ? 'Editar Registro' : 'Añadir Registro'}`}</h2>
                <form onSubmit={handleSubmit(onSubmit)}>
                    <div className={''}>
                        {
                            fields.map((item, index) => {
                                return (
                                    <div className="relative flex w-full items-center space-x-4" key={item.id}>
                                        <div className={'w-full'}>
                                            <Select
                                                {...register(`profesor${index}`, {
                                                    required: true,
                                                })}
                                                labelClassName={'text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold '}
                                                label={'Profesor: '}
                                                data={profesoresSelect}
                                                control={control}
                                            />
                                        </div>
                                        <div className={'w-full'}>
                                            <Select
                                                {...register(`estudiante${index}`, {
                                                    required: true,
                                                })}
                                                labelClassName={'text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold '}
                                                label={'Estudiante'}
                                                data={estudiantesSelect}
                                                control={control}
                                            />
                                        </div>
                                        <div className={'w-full'}>
                                            <Select
                                                {...register(`asignatura${index}`, {
                                                    required: true,
                                                })}
                                                label={'Asignatura'}
                                                labelClassName={'text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold '}
                                                data={asignaturasSelect}
                                                control={control}
                                            />
                                        </div>

                                        <div className="group w-full">
                                            <label
                                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Nota</label>
                                            <input
                                                type="number" {...register(`note_value${index}`, {
                                                required: true
                                            })}
                                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}

                                                defaultValue={editting?.note_value}
                                            />

                                        </div>

                                    </div>

                                )
                            })
                        }
                        {!editting &&
                            <button
                                type={'button'}
                                className={'self-center w-full translate-y-3 py-2 h-10 text-center text-indigo-500 rounded-lg border-2 border-indigo-500 text-sm font-semibold hover:bg-indigo-50 transition-colors'}
                                onClick={() => append({})}
                            >
                                Nueva Nota
                            </button>
                        }

                    </div>

                    <div className="flex space-x-3 justify-center mt-10">
                        <button type="button" onClick={() => {
                            setShowModal!(false);
                            setEditting!(undefined)
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