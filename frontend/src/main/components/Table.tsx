interface Props {
    header: string[],
    rows: string[][]
    className?: string
}

export default function Table({header, rows, className}: Props) {
    return (
        <div className={`flex flex-col text-indigo-950 ${className}`}>
            <div className={'flex justify-around py-2'}>
                {header.map((item, index) => {
                    return (
                        <div className={'w-full flex justify-center'}>
                            <div className={'w-fit'}>
                                <div key={index} className={`font-bold w-full`}>{item}</div>
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
            {rows.map((row, index) => {
                return (
                    <div key={index} className={'flex justify-around py-2 hover:bg-indigo-100'}>
                        {row.map((item, index) => {
                            return <div key={index} className={` w-full text-center py-1`}>{item}</div>
                        })}
                        <div className={'w-full flex justify-center items-center'}>
                            <div className={'h-[3px] w-4 bg-red-500 rounded-full'} />
                        </div>
                    </div>)
            })}

        </div>
    )
}