import {DBObject} from "../types.ts";
import MySpinner from "./MySpinner.tsx";
import {getTextEllipsis} from "../pages/profesores/utils/utils.ts";

interface Props {
    header: string[],
    Data: DBObject[],
    className?: string
    onEditRow: (index: string) => void
    onRemoveRow: (index: string) => void
    isLoading: boolean
    actions?: {
        title: string,
        icon: JSX.Element,
        action: (row: DBObject) => void,
        color: string,
        isVisible: (id: string) => boolean
    }[]
}

export default function Table({header, className, Data, onRemoveRow, onEditRow, isLoading, actions}: Props) {

    return (
        <>
            {
                isLoading ?
                    (<div className={'flex justify-center items-center h-full'}>
                        <MySpinner className={'size-10'}/>
                    </div>)

                    :
                    (<div className={` flex flex-col text-indigo-950 scrollbar-hide overflow-y-scroll  ${className}`}>
                        <div className={'flex justify-around me-2 text-sm mb-1'}>
                            {header.map((item, index) => {
                                return (
                                    <div key={index} className={'w-full flex justify-center'}>
                                        <div className={'w-fit'}>
                                            <div className={`font-bold w-full`}>{item}</div>
                                            <div className={'h-[3px] w-full bg-indigo-500 rounded-full'}/>
                                        </div>
                                    </div>)
                            })}
                            {
                                actions?.map((action, index) => {
                                    return (
                                        <div key={index} className={'w-full flex justify-center'}>
                                            <div className={'w-fit'}>
                                                <div className={`font-bold w-full`}>{action.title}</div>
                                                <div className={`h-[3px] w-full rounded-full ${action.color}`}/>
                                            </div>
                                        </div>
                                    )
                                })
                            }
                            <div className={'w-full flex justify-center'}>
                                <div className={'w-fit'}>
                                    <div className={`font-bold w-full`}>Eliminar</div>
                                    <div className={'h-[3px] w-full bg-red-500 rounded-full'}/>
                                </div>
                            </div>
                        </div>
                        <div className={'scrollbar-hide text-sm'}>
                            {(Data).map((row) => {
                                return (
                                    <div key={row.id} onClick={() => onEditRow(row.id)}
                                         className={'flex w-full py-2 items-center hover:bg-indigo-100 cursor-pointer '}>
                                        {Object.values(row).slice(1).map((item, index) => {
                                            if (typeof item === "string" || typeof item === "number")
                                                return (
                                                    <div key={index}
                                                         className={`w-full text-center py-1`}>{getTextEllipsis(item.toString(), 10)}
                                                        <div
                                                            className={'absolute rounded-lg invisible group-hover:visible transition-all opacity-0 group-hover:opacity-100 text-xs z-20 text-slate-600 grid grid-cols-2 gap-3 size-fit p-2 bg-white'}>
                                                            <p>{item}</p>
                                                        </div>
                                                    </div>
                                                )

                                            else if (typeof item === "boolean") {
                                                return (
                                                    <div key={index}
                                                         className={'w-full text-center py-1 flex items-center justify-center'}>
                                                        <div
                                                            className={`${item ? 'bg-green-200 text-green-950' : 'bg-red-200 text-red-950'} rounded-full py-2 w-16 font-bold text-xs`}>
                                                            {item ? "Sí" : "No"}
                                                        </div>
                                                    </div>

                                                )
                                            } else
                                                return (
                                                    <div key={index}
                                                         className={'w-full group flex justify-center items-center text-center py-1'}>
                                                        {getTextEllipsis(item?.toString(), 10) ?? ""}
                                                        <div
                                                            className={'absolute rounded-lg invisible group-hover:visible transition-all opacity-0 group-hover:opacity-100 text-xs z-20 text-slate-600 grid grid-cols-2 gap-3 size-fit p-2 bg-white'}>
                                                            {
                                                                (item as Array<string>)?.map((value, indx) => {
                                                                    return <p key={indx}>{value}</p>
                                                                })
                                                            }
                                                        </div>
                                                    </div>
                                                )
                                        })}
                                        {
                                            actions?.map((action, index) => {
                                                return (
                                                    <div key={index} className={'w-full flex justify-center'}>
                                                        {action.isVisible(row.id) &&
                                                            <div
                                                                onClick={(e) => {
                                                                    action.action(row)
                                                                    e.stopPropagation()
                                                                }}
                                                                className={`size-9 flex items-center justify-center rounded-full hover:bg-${action.color}-200 cursor-pointer`}>

                                                                {action.icon}
                                                            </div>
                                                        }


                                                    </div>
                                                )
                                            })
                                        }
                                        <div className={'w-full flex justify-center'}>
                                            <div
                                                onClick={(e) => {
                                                    onRemoveRow(row.id)
                                                    e.stopPropagation()
                                                }}
                                                className={'size-9 flex items-center justify-center rounded-full hover:bg-indigo-200 cursor-pointer'}>

                                                <div className={'h-[3px] w-4 bg-red-500 rounded-full'}/>
                                            </div>

                                        </div>
                                    </div>
                                )
                            })}
                        </div>
                    </div>)
            }
        </>

    )
}