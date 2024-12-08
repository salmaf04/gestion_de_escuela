import {Profesor} from "../types.ts";

interface Props {
    header: string[],
    Data: Profesor[],
    className?: string
}

export default function Table({header, className, Data}: Props) {
    return (
        <div className={`flex flex-col text-indigo-950 ${className}`}>
            <div className={'flex justify-around me-2 text-sm mb-1'}>
                {header.map((item, index) => {
                    return (
                        <div key={index} className={'w-full flex justify-center'}>
                            <div className={'w-fit'}>
                                <div  className={`font-bold w-full`}>{item}</div>
                                <div className={'h-[3px] w-full bg-indigo-500 rounded-full'}/>
                            </div>
                        </div>)
                })}
                <div className={'w-full flex justify-center'}>
                    <div className={'w-fit'}>
                        <div className={`font-bold w-full`}>Eliminar</div>
                        <div className={'h-[3px] w-full bg-red-500 rounded-full'}/>
                    </div>
                </div>
            </div>
            <div className={'overflow-y-scroll scrollbar-hide text-sm'}>
                {Data.map((row, index) => {
                    return (
                        <div key={index} onClick={() => {
                            //todo setEdit
                        }}
                             className={'flex justify-around py-2 items-center hover:bg-indigo-100 cursor-pointer'}>
                            {Object.values(row).map((item, index) => {
                                return <div key={index} className={` w-full text-center py-1`}>{item}</div>
                            })}
                            <div className={'w-full flex justify-center'}>
                                <div
                                    className={'size-9 flex items-center justify-center rounded-full hover:bg-indigo-200 cursor-pointer'}>
                                    <div onClick={(e) => {
                                        e.stopPropagation()
                                    }} className={'h-[3px] w-4 bg-red-500 rounded-full'}/>
                                </div>

                            </div>
                        </div>
                    )
                })}
            </div>
        </div>
    )
}