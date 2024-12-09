interface Props {
    title: string
    message: string
    className?: string
    onClick: () => void
}

export default function Alert({title, message, className, onClick}: Props) {
    return (
        <div id={'alert'} className={'fixed z-30 flex inset-0 -translate-y-20 justify-center p-4 text-white transition-all'} onClick={
            ()=>{onClick()}
        }>
            <div className={`bg-indigo-300 flex flex-col w-1/5 rounded-lg py-1 px-4 h-fit ${className}`}>
                <h1 className={'text-xl font-semibold text-indigo-950'}>{title}</h1>
                <p className={'text-indigo-950'}>{message}</p>
            </div>
        </div>)
}