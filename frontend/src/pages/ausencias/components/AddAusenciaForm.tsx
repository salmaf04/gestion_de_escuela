// frontend/src/pages/ausencias/components/AddAusenciaForm.tsx
import {useContext, useEffect} from "react";
import { AusenciasContext } from "../AusenciasScreen.tsx";
import {useApiEstudiante} from "../../estudiantes/hooks/useApiEstudiante.ts";
import {useApiAsignatura} from "../../asignaturas/hooks/useApiAsignatura.ts";
import {AppContext} from "../../../App.tsx";
import Select from "../../../components/Select.tsx";
import MySpinner from "../../../components/MySpinner.tsx";
import { useFieldArray, useForm} from "react-hook-form";
import {ISelect} from "../../../types/ISelect.ts";
import {useApiProfesor} from "../../profesores/hooks/useApiProfesor.ts";
import {reverseDate} from "../../../utils/utils.ts";
import {IAusenciaCreateDB} from "../models/IAusenciaCreateDB.ts";

export default function AddAusenciaForm() {
    const { onAddTableItem, setShowModal, editting, onEditTableItem, setEditting } = useContext(AusenciasContext);
    const {getEstudiantes, isLoading} = useApiEstudiante()
    const {getAsignaturas} = useApiAsignatura()
    const {getProfesores} = useApiProfesor()
    const {asignaturas, estudiantes} = useContext(AppContext)
    useEffect(() => {
        getAsignaturas()
        getEstudiantes()
        getProfesores()
    }, []);

    const {register, control, handleSubmit}=useForm()
    const {fields, append, remove} = useFieldArray({
        control,
        name: "ausencias",
    });
    if (fields.length ===0){
        append({})
    }
    const onSubmit = (data) => {
        if (editting){
            const dataParse: IAusenciaCreateDB = {
                student_id: data[`estudiante0`],
                subject_id: data[`asignatura0`],
                date: reverseDate(data[`date0`]),
            }
            console.log(dataParse)

            onEditTableItem!(dataParse)
        }
        else{
            const dataParse: IAusenciaCreateDB[] = []
            for (let i = 0; i < fields.length; i++) {
                dataParse.push({
                    student_id: data[`estudiante${i}`],
                    subject_id: data[`asignatura${i}`],
                    date: reverseDate(data[`date${i}`]),
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
            name: `${item?.name} ${item?.lastname}`
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
                                                {...register(`estudiante${index}`, {
                                                    required: true,
                                                })}
                                                labelClassName={'text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold '}
                                                label={'Estudiante'}
                                                data={estudiantesSelect}
                                                control={control}
                                                defaultValue={editting && estudiantes?.find((item) => item.name === editting?.studentName)?.id}

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
                                                defaultValue={editting && asignaturas?.find((item) => item.name === editting?.subjectName)?.id}
                                            />
                                        </div>

                                        <div className="group w-full">
                                            <label
                                                className="text-indigo-950 text-xs group-focus-within:text-indigo-500 font-semibold ">Fecha</label>
                                            <input
                                                type="date" {...register(`date${index}`, {
                                                required: true
                                            })}
                                                className={"rounded-lg h-10 w-full p-3 text-indigo-950 focus:outline-indigo-600 bg-indigo-50 text-sm"}

                                                defaultValue={editting && reverseDate(editting.date)}
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
                                Nueva Ausencia
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