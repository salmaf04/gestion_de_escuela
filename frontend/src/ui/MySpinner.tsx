import LoadingIcon from "../assets/loading.svg";

export default function MySpinner({className}: {className?: string}) {
    return <img src={LoadingIcon} alt="loading" className={`absolute animate-spin ${className}`}/>
}