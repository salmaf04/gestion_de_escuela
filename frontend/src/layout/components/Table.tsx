// @ts-ignore
import {Profesor} from './Types.tsx';

interface Props {
    header: string[],
    rows: string[][],
    setEdit: (index:number) => void,
    Data : Profesor[] ,
    className? : string
}


export default function Table({header,className, setEdit, Data}: Props) {




    return (

        <div className={`flex flex-col text-indigo-950 ${className}`}>
            <div className={'flex  justify-around py-2'}>
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
           <div className={'overflow-y-scroll'}>
               {Data.map((row, index) => {
                   return (
                       <div onClick={() => setEdit(index)} key={index}
                            className={'flex justify-around py-2 items-center hover:bg-indigo-100'}>
                           {Object.values(row).map((item, index) => {
                               return <div key={index} className={` w-full text-center py-1`}>{item}</div>
                           })}
                           <div className={'w-full flex justify-center items-center'}>
                               <div onClick={(e)=>{
                                   e.stopPropagation()

                               }} className={'h-[3px] w-4 bg-red-500 rounded-full'}/>
                           </div>
                       </div>)
               })}
           </div>

        </div>
    )
}