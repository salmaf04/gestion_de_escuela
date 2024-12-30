import LoadingIcon from "../assets/loading.svg";

export default function Spinner(){
    return (
        <img src={LoadingIcon} alt="loading" className="absolute w-6 h-6 animate-spin"/>
    )
}