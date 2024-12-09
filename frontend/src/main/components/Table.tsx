import {DBObject} from "../types.ts";

interface Props {
    header: string[],
    Data: DBObject[],
    className?: string
    onEditRow: (index: string) => void
    onRemoveRow: (index: string) => void
}

export default function Table({header, className, Data, onRemoveRow, onEditRow}: Props) {
    return (
        <div className={`flex flex-col text-indigo-950 ${className}`}>
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
                <div className={'w-full flex justify-center'}>
                    <div className={'w-fit'}>
                        <div className={`font-bold w-full`}>Eliminar</div>
                        <div className={'h-[3px] w-full bg-red-500 rounded-full'}/>
                    </div>
                </div>
            </div>
            <div className={'overflow-y-scroll scrollbar-hide text-sm'}>
                {Data.map((row) => {
                    return (
                        <div key={row.Id} onClick={() => onEditRow(row.Id)}
                             className={'flex justify-around py-2 items-center hover:bg-indigo-100 cursor-pointer'}>
                            {Object.values(row).slice(1).map((item, index) => {
                                return (
                                    <div key={index} className={`w-full text-center py-1`}>
                                        {typeof item === 'boolean' ? (item ? 'Participa' : 'No participa') : item}
                                    </div>
                                );
                            })}
                            <div className={'w-full flex justify-center'}>
                                <div
                                    onClick={(e) => {
                                        onRemoveRow(row.Id)
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
        </div>
    )
}