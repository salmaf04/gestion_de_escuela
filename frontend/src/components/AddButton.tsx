import AddIcon from '../assets/add.svg';

interface Props {
    className?: string
    onClick: () => void
}

export default function AddButton({className, onClick}: Props) {
    return (
        <div className={`flex justify-around items-center gap-2 cursor-pointer transition-all hover:from-indigo-600 hover:to-indigo-600 hover:scale-105 text-indigo-50 font-semibold py-2 px-5 bg-gradient-to-r from-indigo-500 to-indigo-600 rounded-lg shadow-md shadow-indigo-300 ${className}`}
                onClick={onClick}>
            Añadir
        <img src={AddIcon} alt={''}/>
        </div>
    )
}