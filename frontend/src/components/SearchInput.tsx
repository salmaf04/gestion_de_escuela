import SearchIcon from "../assets/search.svg";
import CancelIcon from "../assets/cancel.svg"

interface Props {
    className?: string,
    focus?: boolean
    searchText: string
    setSearchText: (text: string) => void
}

export default function SearchInput({className, focus, searchText, setSearchText}: Props) {
    return (
        <div className={`relative ${className}`}>
            <input className={'rounded-md py-1 ps-2 pe-9 outline-indigo-500 text-sm'}
                   placeholder="Buscar" autoFocus={focus}
                   value={searchText}
                   onChange={
                       (e) => {
                           setSearchText(e.target.value)
                       }
                   }/>

            <img src={searchText? CancelIcon : SearchIcon} alt={'buscar'} className={`transition-all rounded-full p-[1px]  ${searchText && 'hover:bg-red-100 cursor-pointer'}  absolute right-2 top-1/2 -translate-y-1/2`}
                onClick={()=> setSearchText('')}
            />
        </div>
    )
}